from PIL import Image

def resize_images(image_names, new_size=(200, 200)):
    for image_name in image_names:
        img = Image.open(image_name)
        img = img.resize(new_size)
        img.save("resized_" + image_name)


images= ["pic01.jpg","pic02.jpg","pic03.jpg","pic04.jpg","pic05.jpg","pic06.jpg"]
# resize_images(images)
for hh in images:
    python_img =Image.open(hh)
    python_img2 =python_img
    python_img.show()
    python_img=python_img2.crop((50,50,500,500))
    python_img.show()
    python_img=python_img2.rotate(45)
    python_img.show()
    python_img=python_img.crop((200,100,450,550))
    python_img.show()