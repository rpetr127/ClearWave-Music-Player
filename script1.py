from PIL import Image
import re

def get_color_of_image(file):
    image = Image.open(file)
    img_colors = image.getcolors()
    print(img_colors)

def resize_image(fp):
    im = Image.open(fp)
    resized_im = im.resize((22, 22))
    filedir = fp.split('\\')[0]
    filename = fp.split('\\')[1]
    if re.search(r'\d+', filename):
        filename = re.sub(r'\d+', str(resized_im.size[0]), filename)
    else:
        filename = re.sub(r'\.\w+', '', filename)
        filename = f'{filename}-{resized_im.size[0]}.{im.format}'
    resized_im.save(f'{filedir}\\{filename}')

resize_image('Icons\stop-48.png')