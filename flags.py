# 8.0.1
from PIL import Image

# 1.1.0
import pyTGA

import os


def make_folder(path: str) -> None:
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def save_to_tga(input_image: Image.Image, path: str) -> None:
    pixels = list(input_image.getdata())
    width, height = input_image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    pixels.reverse()
    image = pyTGA.Image(data=pixels)
    image.set_first_pixel_destination('bl')
    image.save(path)


def make_flags(path_to_image: str, tag: str) -> None:
    img_base = Image.open(path_to_image).convert('RGBA')

    # Make 82 by 52 flag tga
    make_folder('output')
    img_large = img_base.resize((82, 52))
    save_to_tga(img_large, f'output/{tag}')

    # Make 41 by 26 flag tga
    make_folder('output/medium')
    img_med = img_base.resize((41, 26))
    save_to_tga(img_med, f'output/medium/{tag}')

    # Make 10 by 7 flag tga
    make_folder('output/small')
    img_small = img_base.resize((10, 7))
    save_to_tga(img_small, f'output/small/{tag}')


def main():
    files = os.listdir('input')
    count = 0
    length = len(files)
    for file in files:
        if '.png' in file:
            tag_ = file.split('.')[0]
            make_flags(f'input/{file}', tag_)
        count += 1
        number = round((count * 100) / length)
        print(f"\r{number}%", end="\r")


if __name__ == '__main__':
    main()
