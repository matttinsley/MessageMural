from PIL import Image, ImageDraw, ImageFont


im = Image.open("source.jpg")
char_width = 8
char_height = 11
im_width = im.size[0]
im_height = im.size[1]

image = Image.new("RGB", (im_width, im_height), color="white")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("Courier New Bold.ttf", 16)

# iterate through chunks the size of 1 character
for i in range(0, im_width, char_width):
    for j in range(0, im_height, char_height):
        box = (i, j, i+char_width, j+char_height)
        region = im.crop(box)
        main_color = region.getcolors()[0][1]
        draw.text((i, j), "a", fill=main_color, font=font)


image.save("out.jpg")
