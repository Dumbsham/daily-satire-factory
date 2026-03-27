import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Open the vault and grab your key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Initialize the modern GenAI Client
client = genai.Client(api_key=api_key)

def generate_comic_script(news_items):
    """
    Takes a list of news items, asks Gemini to pick the best one,
    and generates a 4-panel comic script.
    """
    print("Editor Agent: Analyzing the news and writing a script...")

    # Format the news so Gemini can read it easily
    news_text = "\n".join([f"- {item['title']}" for item in news_items])

    # 3. The Master Instructions (System Prompt)
# 3. The Master Instructions (System Prompt)
# 3. The Master Instructions (System Prompt)
 # 3. The Master Instructions (System Prompt)
   # 3. The Master Instructions (System Prompt)
    system_instruction = """
    You are an expert, biting Indian political satirist. Your job is to create a SINGLE-PANEL editorial cartoon about a real-world Indian news event.
    
    Task:
    1. Pick the ONE most interesting or absurd headline from the list.
    2. Write a visual gag for a single-panel newspaper cartoon based EXACTLY on that specific headline.
    
    CRITICAL RULES:
    - BE SPECIFIC: Name the actual world leaders, countries, and topics.
    - ONE STRONG METAPHOR: Combine the politicians and the news topic into one funny, exaggerated visual situation.
    - NO TEXT IN PROMPTS: Do not ask the image generator to draw words, signs, or speech bubbles.
    - LANGUAGE SPLIT: The PROMPT must be in pure English so the drawing AI understands it. However, the CAPTION *MUST* be written in witty, authentic HINGLISH (a conversational mix of Hindi and English written in the English alphabet).
    
    Format your response EXACTLY like this:
    TITLE: [The specific news topic]
    PROMPT: [Highly detailed visual description of the single funny scene in ENGLISH, NO TEXT]
    CAPTION: [A sharp 5-10 word funny punchline in HINGLISH, e.g., "Bhai, yeh scheme toh out of syllabus nikli!"]
    """

    # 4. Call the new Gemini 2.5 Flash model
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=news_text,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.7 # A little bit of creativity!
        )
    )
    
    return response.text

# --- TEST BLOCK ---
if __name__ == "__main__":
    sample_news = [
        {"title": "Global summit reaches historic agreement on ocean conservation"},
        {"title": "Tech stocks plummet after new AI regulations announced"},
        {"title": "Giant panda escapes local zoo, found eating bamboo in downtown cafe"}
    ]
    
    script = generate_comic_script(sample_news)
    
    print("\n--- THE COMIC SCRIPT ---")
    print(script)