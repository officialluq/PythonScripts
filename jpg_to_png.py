from PIL import Image
import sys
import os
print(sys.argv[1])
im1 = Image.open(sys.argv[1])
im1.save(f'{os.getcwd()}/photo.png')