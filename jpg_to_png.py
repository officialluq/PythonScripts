from PIL import Image
import sys
import os
from pathlib import Path
print(sys.argv[1])
im1 = Image.open(sys.argv[1])
im1.save(f'{os.getcwd()}/photo.png')



def foo(path:Path):
    im1 = Image.open(path)
    im1.save(path.with_suffix('.png'))



path_to_f = 'photo.jpg'
path_to_f = 'dog.jpg'
path_to_f = 'cat.dog.jpg'
path_to_f = 'cat.dog.webp'
foo(path_to_f)