from PIL import Image
import os
from pathlib import Path

def combine_images_to_pdf_pillow(image_folder, output_pdf, dpi=150):
    """
    Combines all JPG images from a folder into a single PDF using Pillow.

    Args:
        image_folder: Path to the folder containing JPG images (e.g., "./images")
        output_pdf: Path for the output PDF file (e.g., "output.pdf")
        dpi: Resolution for the PDF (default: 150)
    """
    # Get all JPG files from the specified folder
    image_paths = []
    for ext in ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG']:
        image_paths.extend(Path(image_folder).glob(ext))
    
    image_paths = sorted(image_paths)
    
    if not image_paths:
        print(f"❌ No JPG files found in folder: {image_folder}")
        print(f"   Please check the path and try again.")
        return

    print(f"✅ Found {len(image_paths)} images in '{image_folder}'")
    print(f"   Files: {[p.name for p in image_paths]}")

    # Convert images to RGB and create PDF
    images = []
    for img_path in image_paths:
        img = Image.open(img_path)
        if img.mode in ('RGBA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        images.append(img)

    if images:
        first_image = images[0]
        remaining_images = images[1:] if len(images) > 1 else []
        
        first_image.save(
            output_pdf,
            "PDF",
            resolution=dpi,
            save_all=True,
            append_images=remaining_images
        )
        print(f"✅ PDF successfully created: {output_pdf}")

# ------------------------------------------------------------
# 🎯 IMPORTANT: THIS IS WHERE YOU SPECIFY YOUR FOLDER PATH
# ------------------------------------------------------------
if __name__ == "__main__":
    # OPTION 1: Images in a subfolder called "images"
    combine_images_to_pdf_pillow("images", "output.pdf")
    
    # OPTION 2: Images in the same folder as this script
    # combine_images_to_pdf_pillow(".", "output.pdf")
    
    # OPTION 3: Images on your Desktop (Windows)
    # combine_images_to_pdf_pillow("C:/Users/YourName/Desktop/my_jpgs", "output.pdf")