from PIL import Image

img = Image.open('girlboss.jpg')
# img.thumbnail((400,400)) #keeps aspect ratio when resizing images
img.save('girlboss.png')