import re
from agents.news_agent import fetch_top_news
from agents.story_agent import generate_comic_script
from utils.image_generator import generate_panel_image
from utils.assembler import create_comic_strip

def parse_single_panel(script_text):
    """Extracts the single prompt and caption from Gemini's response."""
    print("\nManager: Extracting the visual gag and the joke...")
    
    prompt_match = re.search(r"PROMPT:(.*?)(?=CAPTION:)", script_text, re.DOTALL)
    caption_match = re.search(r"CAPTION:(.*)", script_text, re.DOTALL)
    
    if prompt_match and caption_match:
        return {
            "prompt": prompt_match.group(1).strip(),
            "caption": caption_match.group(1).strip()
        }
    else:
        print("Warning: Couldn't parse the script properly!")
        return {"prompt": "A funny political cartoon.", "caption": "*technical difficulties*"}

def run_comic_factory():
    print("========================================")
    print("🚀 STARTING AI EDITORIAL CARTOON FACTORY 🚀")
    print("========================================\n")

    news_items = fetch_top_news(limit=5)
    if not news_items: return

    script = generate_comic_script(news_items)
    print("\n--- GEMINI'S CONCEPT ---")
    print(script)
    print("-----------------------\n")

    panel_data = parse_single_panel(script)

    # We only draw ONE image now!
    image_path = generate_panel_image(panel_data["prompt"], 1)
        
    if not image_path:
        print("\nManager: Halting assembly line.")
        return

    print("\nManager: Image drawn! Sending to Publisher to add text...")
    # Send the single image and caption to the publisher
    final_comic_path = create_comic_strip(image_path, panel_data["caption"], "todays_editorial_cartoon.png")

    if final_comic_path:
        print("\n========================================")
        print("🎉 FACTORY RUN COMPLETE! 🎉")
        print(f"Go check out your masterpiece at: {final_comic_path}")
        print("========================================")

if __name__ == "__main__":
    run_comic_factory()