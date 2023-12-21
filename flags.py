# Python 3.8.6

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


def make_flags(path_to_image: str, tag: str, output_dir: str = 'output',
               large_width: int = 82, large_height: int = 52,
               medium_width: int = 41, medium_height: int = 26,
               small_width: int = 10, small_height: int = 7) -> None:
    img_base = Image.open(path_to_image).convert('RGBA')

    # Make large flag tga
    make_folder(f'{output_dir}')
    img_large = img_base.resize((large_width, large_height))
    save_to_tga(img_large, f'{output_dir}/{tag}')

    # Make medium flag tga
    make_folder(f'{output_dir}/medium')
    img_med = img_base.resize((medium_width, medium_height))
    save_to_tga(img_med, f'{output_dir}/medium/{tag}')

    # Make small flag tga
    make_folder(f'{output_dir}/small')
    img_small = img_base.resize((small_width, small_height))
    save_to_tga(img_small, f'{output_dir}/small/{tag}')


def main():
    make_folder('input')
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
