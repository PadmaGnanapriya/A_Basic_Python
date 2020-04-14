from PIL import Image,ImageFilter, ImageEnhance

images= ["pic01.jpg","pic02.jpg","pic03.jpg","pic04.jpg","pic05.jpg","pic06.jpg"]
# resize_images(images)
for hh in images:
    python_img = Image.open(hh)
    #python_img.show()
    width,height=python_img.size
    for x in range(width):
        for y in range(height):
            pixel_coordinate=(x,y)
            r, g, b  = python_img.getpixel(pixel_coordinate)
            negative_color=(255-r, 255-g, 255-b)
            python_img.putpixel(pixel_coordinate,negative_color)
    python_img.show()

