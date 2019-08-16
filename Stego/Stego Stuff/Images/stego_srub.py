# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:03:31 2019

@author: Admin
"""
from PIL import Image
from PIL import ImageOps

def scrub45():
    img = input("Please enter an image to scrub: ")
    image = Image.open(img)
    image = ImageOps.expand(image, border = 200)
    i = 0
    while i < 10:
        image = image.rotate(90)
        image = image.rotate(-90)
        i+=1
    image = ImageOps.crop(image, border=200)
    new_img_name = input("Enter the name of new image(with extension): ")
    image.save(new_img_name, str(new_img_name.split(".")[1].upper()))

if __name__ == '__main__' :

	# Calling main function
	scrub45()