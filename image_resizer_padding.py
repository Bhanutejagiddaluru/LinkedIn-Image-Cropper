from PIL import Image, ImageOps

def resize_for_linkedin(input_path, output_path, size=(1200, 627), fill_color=(255, 255, 255)):
    """
    Resize any image to fit LinkedIn's recommended post size (1200x627).
    Keeps aspect ratio and pads with background color if needed.
    
    :param input_path: str - path to the input image
    :param output_path: str - path to save resized image
    :param size: tuple - target size (width, height)
    :param fill_color: tuple - background color (R, G, B)
    """
    # Open image
    img = Image.open(input_path)
    
    # Fit image while preserving aspect ratio, add padding
    img = ImageOps.pad(img, size, method=Image.Resampling.LANCZOS, color=fill_color)
    
    # Save output
    img.save(output_path, quality=95)
    print(f"Resized image saved to {output_path}")

# Example usage
resize_for_linkedin("input.jpg", "linkedin_resized.jpg")
