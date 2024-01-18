from PIL import Image, ImageDraw

def generate_gradient(width, height, color1, color2, output_path):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (width, height)], fill=color1)
    for i in range(height):
        r = int((i / height) * (color2[0] - color1[0]) + color1[0])
        g = int((i / height) * (color2[1] - color1[1]) + color1[1])
        b = int((i / height) * (color2[2] - color1[2]) + color1[2])
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    image.save(output_path)

if __name__ == "__main__":
    generate_gradient(800, 200, (138, 58, 185), (255, 109, 112), "gradient.png")
