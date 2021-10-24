import sys 
import os
from PIL import Image

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# print(image_folder)
# print(output_folder)

new_path = os.path.join(image_folder, output_folder)
print(new_path)

#check if new/ exists, if not create
try:
    if not os.path.exists('.\Pokedex\new'):
        os.makedirs(new_path)
except FileExistsError as err:
    print('File already exist')

# loop through Pokedex
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        img = Image.open(os.path.join(image_folder, filename))
        #convert images to png
        name =  filename + '.png'
        img.save(name)
        #save to the new folder
        complete_name = os.path.join(new_path, filename)
        print(complete_name)
        continue
    else:
        continue

