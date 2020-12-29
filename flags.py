from PIL import Image
import os
import pyTGA


def save_to_tga(im, path):
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    pixels.reverse()
    image = pyTGA.Image(data=pixels)
    image.set_first_pixel_destination('bl')
    image.save(path)


def make_flags(path_to_image, tag):
    img_base = Image.open(path_to_image).convert('RGBA')
    try:
        os.mkdir('output')
    except FileExistsError:
        pass
    img_large = img_base.resize((82, 52))
    save_to_tga(img_large, f'output/{tag}')

    try:
        os.mkdir('output/medium')
    except FileExistsError:
        pass
    img_med = img_base.resize((41, 26))
    save_to_tga(img_med, f'output/medium/{tag}')

    try:
        os.mkdir('output/small')
    except FileExistsError:
        pass
    img_small = img_base.resize((10, 7))
    save_to_tga(img_small, f'output/small/{tag}')


if __name__ == '__main__':
    files = os.listdir('input')
    for file in files:
        if '.png' in file:
            tag = file[:3]
            make_flags(f'input/{file}', tag)
