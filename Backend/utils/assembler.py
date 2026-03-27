import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def create_comic_strip(image_path, caption, output_filename="final_comic.png"):
    """
    Takes a single image and writes the caption directly onto the top of the image
    with a thick outline for readability.
    """
    print("Publisher: Writing the joke directly onto the cartoon...")

    try:
        # 1. Open the single image
        image = Image.open(image_path)
        img_width, img_height = image.size
        
        # We don't create a new canvas anymore! We just draw ON the image.
        draw = ImageDraw.Draw(image)

        # 2. Load a larger font
        try:
            font = ImageFont.truetype("arial.ttf", 60) 
        except IOError:
            try:
                font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 60) 
            except IOError:
                font = ImageFont.load_default() 

        # 3. Wrap the text so it doesn't go off the edges
        # This breaks long sentences into multiple lines (roughly 35 characters wide)
        wrapped_text = textwrap.fill(caption, width=35)

        # 4. Calculate where to put the text (Top Center)
        # We use a bounding box to find out exactly how wide/tall the text is
        bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
        text_width = bbox[2] - bbox[0]
        
        # Center X coordinate, and put it 40 pixels down from the top
        x = (img_width - text_width) / 2
        y = 40 

        # 5. Draw the text with a thick white outline!
        draw.multiline_text(
            (x, y), 
            wrapped_text, 
            fill="black",           # The inside color of the letters
            font=font, 
            align="center",
            stroke_width=6,         # How thick the outline is
            stroke_fill="white"     # The outline color
        )

        # 6. Save the masterpiece
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        final_path = f"{output_folder}/{output_filename}"
        image.save(final_path)

        return final_path

    except Exception as e:
        print(f"Error: The Publisher spilled ink! Details: {e}")
        return None