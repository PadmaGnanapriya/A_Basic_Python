from PIL import Image,ImageFilter, ImageEnhance

def resize_images(image_names, new_size=(200, 200)):
    for image_name in image_names:
        img = Image.open(image_name)
        img = img.resize(new_size)
        img.save("resized_" + image_name)


images= ["pic01.jpg","pic02.jpg","pic03.jpg","pic04.jpg","pic05.jpg","pic06.jpg"]
# resize_images(images)
for hh in images:
    python_img = Image.open(hh)
    python_img2 = python_img
    python_img.show()
    grayscale = python_img.convert('L')
    edge_detect = python_img.filter(ImageFilter.FIND_EDGES)
    edge_detect.show()
