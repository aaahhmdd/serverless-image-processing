from PIL import Image, ImageDraw, ImageFont

def resize_image(input_path: str, output_path: str, size=(800, 600)):
    """
    Opens an image from input_path, resizes it to fit within 'size'
    while preserving aspect ratio, and saves to output_path.
    """
    with Image.open(input_path) as img:
        img.thumbnail(size)
        img.save(output_path)

def watermark_image(input_path: str, output_path: str,
                    text: str = "© MyCompany",
                    position=(10, 10),
                    font_size=24):
    """
    Opens an image, adds a text watermark, and saves to output_path.
    """
    with Image.open(input_path).convert("RGBA") as base:
        txt_layer = Image.new("RGBA", base.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt_layer)
        font = ImageFont.load_default()
        draw.text(position, text, font=font, fill=(255,255,255,128))
        watermarked = Image.alpha_composite(base, txt_layer)
        watermarked.convert("RGB").save(output_path)