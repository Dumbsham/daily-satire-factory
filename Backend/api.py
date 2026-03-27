import os
from datetime import date
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv

# Load the MongoDB URI from your .env file
load_dotenv()

# Import your hardworking agents
from agents.news_agent import fetch_top_news
from agents.story_agent import generate_comic_script
from utils.image_generator import generate_panel_image
from utils.assembler import create_comic_strip
from main import parse_single_panel

app = FastAPI(title="AI Comic Factory API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MONGODB SETUP ---
MONGO_URI = os.getenv("MONGODB_URI")
if not MONGO_URI:
    print("WARNING: MONGODB_URI not found in .env file!")

# Connect to your Atlas Cluster and select the usage collection
client = MongoClient(MONGO_URI)
db = client.comic_app
usage_collection = db.usage_ledger

# Define what data we expect from Next.js
class ComicRequest(BaseModel):
    user_id: str

def check_and_update_limit(user_id: str) -> bool:
    """Checks MongoDB to see if the user has hit their 5-comic limit today."""
    today = str(date.today())
    
    # Look for this user's record for today
    record = usage_collection.find_one({"user_id": user_id, "date": today})
    
    if not record:
        # First comic of the day! Create the record.
        usage_collection.insert_one({"user_id": user_id, "date": today, "count": 1})
        return True
    else:
        count = record.get("count", 0)
        if count >= 5:
            return False # Limit reached!
        
        # Add 1 to their daily count
        usage_collection.update_one(
            {"_id": record["_id"]},
            {"$inc": {"count": 1}}
        )
        return True

@app.get("/")
def read_root():
    return {"message": "The AI Comic Factory is awake and ready!"}

@app.post("/generate-comic")
def generate_comic_endpoint(request: ComicRequest):
    print(f"API: Received request from User {request.user_id}...")
    
    # 1. Check MongoDB before doing any expensive AI work!
    if not check_and_update_limit(request.user_id):
        print(f"User {request.user_id} hit their daily limit.")
        raise HTTPException(status_code=429, detail="Daily limit reached.")

    try:
        # Step 1: Scout
        news_items = fetch_top_news(limit=5)
        if not news_items:
            raise HTTPException(status_code=500, detail="Failed to fetch news.")

        # Step 2: Editor
        script = generate_comic_script(news_items)
        panel_data = parse_single_panel(script)

        # Step 3: Illustrator
        image_path = generate_panel_image(panel_data["prompt"], 1)
        if not image_path:
            raise HTTPException(status_code=500, detail="Illustrator failed to draw.")

        # Step 4: Publisher
        final_comic_path = create_comic_strip(image_path, panel_data["caption"], f"comic_{request.user_id}.png")
        
        if not final_comic_path or not os.path.exists(final_comic_path):
            raise HTTPException(status_code=500, detail="Publisher failed to assemble.")

        return FileResponse(final_comic_path, media_type="image/png")

    except Exception as e:
        print(f"API Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))