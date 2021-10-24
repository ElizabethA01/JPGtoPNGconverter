from PIL import Image, ImageFilter

img = Image.open('.\Pokedex\pikachu.jpg')



print(img.format)
print(img.size) #size of image
print(img.mode) #mode (colours)
print(dir(img)) #tells you all the functions you can use on the image
filtered_img = img.filter(ImageFilter.BLUR) #how to change the filter of the image
filtered_img = img.convert('L') #converts to greyscale
box = (100, 100, 400, 400)
region = filtered_img.crop(box)

crooked = filtered_img.resize((300,300))
region.save('grey.png', 'png') #png is the best format to convert to
# filtered_img.show() #shows the image


img = Image.open('sunset.jpg')
img.thumbnail((400,400)) #keeps aspect ratio when resizing images
img.save('profile.jpg')

print(img.size)


