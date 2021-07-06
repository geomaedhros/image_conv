#!/usr/bin/env python3

import os
import sys
from PIL import Image

def rotate_resize_img(in_path, out_path):

    img_paths = [os.path.join(pth, filename) for pth, dirs, files in os.walk(in_path) for filename in files]: # iterate through files in the image folder, ignoring folders
    for f in img_paths:
        img = Image.open(in_path+"/"+f) # open original image
        rot_img = img.rotate(270) # degrees counter-clockwise
        rsz_img = rot_img.resize((128, 128)) # resize the image
        new_img = rsz_img.convert("RGB") # convert image to RGB in order to save it
        new_img.save(out_path+"/"+f+".jpeg", "JPEG") # rename and save with different format
        
#in_dir = "/home/xxxx/"
#out_dir = "/opt/icons"

in_dir = "/mnt/c/users/geomaedhros/new_dir"
out_dir = "/mnt/c/users/geomaedhros/new_dir/remastered"

rotate_resize_img(in_dir, out_dir)