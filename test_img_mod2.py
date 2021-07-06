#!/usr/bin/env python3

import os
import re
import time
from PIL import Image
from PIL import UnidentifiedImageError

def rotate_resize_img(in_path, out_path):
    
    starttime = time.time()

    # regex to find image extensions
    regex = r"((\.)(jpe?g|png|gif|jfif|bmp|tiff)$)"
    prod = re.compile(regex, re.IGNORECASE)
    
    img_paths = [filename for pth, dirs, files in os.walk(in_path) for filename in files] # iterate through files in the image folder, ignoring folders
    for f in img_paths:
        if (re.search(prod, f)):
                
            try:
                img = Image.open(in_path+"/"+f) # open original image
                rot_img = img.rotate(270) # degrees counter-clockwise
                rsz_img = rot_img.resize((128, 128)) # resize the image
                new_img = rsz_img.convert("RGB") # convert image to RGB in order to save it
                new_fname = re.sub(prod, ".jpeg", f) # replaces extension with .jpeg
                new_img.save(out_path+"/"+new_fname, "JPEG") # rename, relocate and save with different format#
                    
            except FileNotFoundError:
                continue

            
        elif os.path.splitext(f)[1] == "":  # if file has no extension, function adds and saves as .jpeg while not throwing errors
            try:
                img = Image.open(in_path+"/"+f) # open original image
                rot_img = img.rotate(270) # degrees counter-clockwise
                rsz_img = rot_img.resize((128, 128)) # resize the image
                new_img = rsz_img.convert("RGB") # convert image to RGB in order to save it
                new_fname = os.path.splitext(f)[0]+".jpeg" # adds .jpeg extension
                new_img.save(out_path+"/"+new_fname, "JPEG") # rename, relocate and save with different format#
                print(out_path+"/"+new_fname)
                    
            except FileNotFoundError:
                continue

            except UnidentifiedImageError:
                continue
            
        else:
            continue

    endtime = time.time()

    print("Elapsed time: {:.2f} seconds".format(endtime - starttime))
    print("Image conversion completed.\n")

  
in_dir = "/home/student-00-3a3c27fe3a6a/images"
out_dir = "/opt/icons"

rotate_resize_img(in_dir, out_dir)