"""
version 1.0. assume image names are strings 'a.b.c.d.ext'
    a is game number
    b is chain number
    c is position in chain
    d is name of person
    ext is file extension e.g. jpg or png

version 2.0 (current version). assume image names are strings 'x.y.ext'
    x is name of person who started chain
    y is name of person who created that particular image
    ext is file extension e.g. jpg or png

    The possible names are in the names variable
"""

import os
import shutil
from skimage import io
from skimage.transform import resize
import numpy as np

path_raw = "./raw_photos"
path_copy = "./copy_photos/"
path_final = "./final_photos/"

# to be manually updated for each game
game_number = 3
names = ['t', 'a', 's', 'p', 'j', 'l', 'al', 'i', 'd', 'r']

# copy raw images into new directory, to ensure raw photos are never modified
# accidentally
def copy_raw():
    try:
        shutil.rmtree(path_copy)
    finally:
        shutil.copytree(path_raw, path_copy)

# see docstring at top for assumptions on filenames
# have try except block because sometimes get random unwanted files
def rename_files():
    for filename in os.listdir(path_copy):
        try:
            name1, name2, _ = filename.split(".")
            chain_number = names.index(name1)
            position_in_chain = (names.index(name2) - chain_number) % len(names)
            new_filename = f'{game_number:03}.{chain_number:03}.{position_in_chain:03}.jpg'
            os.rename(path_copy+filename, path_copy+new_filename)
        except:
            os.remove(path_copy+filename)
    
def combine_raw():    
    current_sequence = ""
    black_line = np.zeros((5,1000,3))
    
    for f in sorted(os.listdir(path_copy)):
        # extract game num, sequence num and step num from file name
        a,b,c,end = f.split(".")

        # open image and rescale so it is 1000 pixels wide
        image = io.imread(path_copy+f)
        scale_factor = image.shape[1] / 1000
        image_resized = resize(image,
                               (image.shape[0] // scale_factor, 1000),
                               anti_aliasing=True)

        # check if current image is part of previous sequence or new sequence
        if current_sequence == "":
            new_image = image_resized
            current_sequence = a + b
        elif a + b == current_sequence:
            new_image = np.concatenate([new_image,
                                        black_line,
                                        image_resized], axis=0)
        else:
            io.imsave(path_final+'.'.join([current_sequence,end]), new_image)
            current_sequence = a + b
            new_image = image_resized

    io.imsave(path_final+'.'.join([current_sequence,end]), new_image)

if __name__ == '__main__':
    copy_raw()
    rename_files()
    combine_raw()