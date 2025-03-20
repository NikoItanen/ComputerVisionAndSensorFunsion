from PIL import Image
import os

# Define the input and output directories
input_dir = 'exercises3/data/traficl'
output_dir = 'exercises3/data/images_jpg'

os.makedirs(output_dir, exist_ok=True)

incorrect_files = []
iteration_counter = 1

for filename in os.listdir(input_dir):

    if filename.endswith(('.png', '.bmp', '.webp', '.jpeg')):
        img = Image.open(os.path.join(input_dir, filename))
        img = img.convert('RGB') # Make sure the image is in RGB format
        img.save(os.path.join(output_dir, 't_lights_' + str(iteration_counter) + '.jpg'), 'JPEG')
        iteration_counter += 1
        print(f'{filename} converted to JPG format', '\n')

    elif filename.endswith('.jpg'):
        img = Image.open(os.path.join(input_dir, filename))
        img.save(os.path.join(output_dir, 't_lights_' + str(iteration_counter) + '.jpg'), 'JPEG')
        iteration_counter += 1
        print(f'{filename} copied to the output directory', '\n')

    else:
        incorrect_files.append(filename)
        iteration_counter += 1

print('Conversion completed! Amount of non-converted files:', len(incorrect_files))

if incorrect_files:
    print('Non-converted files:', incorrect_files)