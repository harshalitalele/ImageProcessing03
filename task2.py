"""
Denoise Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to denoise image using median filter.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint: 
Please complete all the functions that are labeled with '#to do'. 
You are suggested to use utils.zero_pad.
"""


import utils
import numpy as np
import json

def median_filter(img):
    """
    Implement median filter on the given image.
    Steps:
    (1) Pad the image with zero to ensure that the output is of the same size as the input image.
    (2) Calculate the filtered image.
    Arg: Input image. 
    Return: Filtered image.
    """
    # TODO: implement this function.
    padded_img = utils.zero_pad(img, 1, 1)
    k = 3
    #img = np.array(img, copy=True)

    for i, row in enumerate(img):
        for j, p in enumerate(row):
            arr = []
            for sui in range(k):
                arr.append(padded_img[i+sui][j:j+k])
            arr = np.sort(arr, axis=None)
            img[i][j] = arr[4]
            
    return img

def mse(img1, img2):
    """
    Calculate mean square error of two images.
    Arg: Two images to be compared.
    Return: Mean square error.
    """    
    # TODO: implement this function.
    mserror = 0
    for i,row in enumerate(img1):
        for j,p in enumerate(row):
            mserror += (p - img2[i][j])**2
    mserror = mserror / ((i+1)*(j+1))
    return mserror
    

if __name__ == "__main__":
    img = utils.read_image('lenna-noise.png')
    gt = utils.read_image('lenna-denoise.png')

    result = median_filter(img)
    error = mse(gt, result)

    with open('results/task2.json', "w") as file:
        json.dump(error, file)
    utils.write_image(result,'results/task2_result.jpg')


