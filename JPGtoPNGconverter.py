import sys 
import os
from PIL import Image

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new/ exists, if not create
try:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
except FileExistsError as err:
    print('File already exist')

# loop through Pokedex
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        img = Image.open(f'{image_folder}{filename}')
        #convert images to png
        clean_name = os.path.splitext(filename)[0]
        #save to the new folder
        img.save(f'{output_folder}{clean_name}.png','png')
        #save to the new folder
        continue
    else:
        continue

