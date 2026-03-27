import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# 1. Open the vault
load_dotenv()
hf_token = os.getenv("HUGGINGFACE_TOKEN")

# 2. Initialize the official Hugging Face Client
# We are upgrading to Stable Diffusion XL! It is supported, fast, and makes better art.
client = InferenceClient(
    model="stabilityai/stable-diffusion-xl-base-1.0",
    token=hf_token
)

def generate_panel_image(prompt, panel_number):
    """
    Sends the prompt to Hugging Face's supercomputers using the official client.
    """
    print(f"Illustrator: Asking Hugging Face to draw Panel {panel_number}...")
    
    # 3. Enforce the Ghibli style
    # 3. Enforce the Satirical Cartoon style
    full_prompt = f"Editorial political cartoon style, satirical comic strip, exaggerated caricatures, humorous, hand-drawn newspaper comic look, pen and ink with watercolor. {prompt}"
    
    try:
        # 4. Generate the image! 
        # The client automatically talks to the right servers and hands us back an image file
        image = client.text_to_image(full_prompt)
        
        # 5. Make sure the output folder exists
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        # 6. Save the image
        file_path = f"{output_folder}/panel_{panel_number}.png"
        image.save(file_path)
        
        print(f"Illustrator: Panel {panel_number} saved instantly as {file_path}")
        return file_path
        
    except Exception as e:
        print(f"Error: The Illustrator dropped their paintbrush! Details: {e}")
        return None

# --- TEST BLOCK ---
if __name__ == "__main__":
    sample_prompt = "A giant, friendly panda wearing a small red scarf, sitting in a modern downtown cafe eating a bowl of glowing bamboo noodles."
    generate_panel_image(sample_prompt, 1)