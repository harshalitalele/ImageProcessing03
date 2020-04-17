"""
K-Means Segmentation Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to segment image using k-means clustering.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint: 
Please complete all the functions that are labeled with '#to do'. 
You are allowed to add your own functions if needed.
You should design you algorithm as fast as possible. To avoid repetitve calculation, you are suggested to depict clustering based on statistic histogram [0,255]. 
You will be graded based on the total distortion, e.g., sum of distances, the less the better your clustering is.
"""


import utils
import numpy as np
import json
import time

#np.seterr(over='ignore')
def kmeans(img,k):
    """
    Implement kmeans clustering on the given image.
    Steps:
    (1) Random initialize the centers.
    (2) Calculate distances and update centers, stop when centers do not change.
    (3) Iterate all initializations and return the best result.
    Arg: Input image;
         Number of K. 
    Return: Clustering center values;
            Clustering labels of all pixels;
            Minimum summation of distance between each pixel and its center.  
    """
    # TODO: implement this function.
    intensity_info = {}

    for i, row in enumerate(img):
        for j, pix in enumerate(row):
            if pix not in intensity_info:
                intensity_info[pix] = {'stat': 1, 'c': 0}
            else:
                intensity_info[pix]['stat'] += 1
                
    centers = []
    newcenters = []
    for c in range(k):
        a = list(intensity_info.keys())
        centers.append(a[c])
        newcenters.append(0)
    mindist = 0

    while centers[0] != newcenters[0] or centers[1] != newcenters[1]:
        c1_cnt = 0
        c2_cnt = 0
        if newcenters[0] != 0 and newcenters[1] != 0:
            centers[0] = newcenters[0]
            centers[1] = newcenters[1]
        newcenters[0] = 0
        newcenters[1] = 0
        mindist = 0
        for i, ival in enumerate(intensity_info):
            least_dist = -1
            i_center = 0
            for c in centers:
                dist = abs(ival - c)
                if least_dist == -1 or dist < least_dist:
                    least_dist = dist
                    i_center = c
            mindist += least_dist*intensity_info[ival]['stat']
            intensity_info[ival]['c'] = i_center
            if i_center == centers[0]:
                newcenters[0] += int(ival)*intensity_info[ival]['stat']
                c1_cnt += intensity_info[ival]['stat']
            else:
                newcenters[1] += int(ival)*intensity_info[ival]['stat']
                c2_cnt += intensity_info[ival]['stat']
        newcenters[0] = float(int(newcenters[0]/c1_cnt))
        newcenters[1] = float(int(newcenters[1]/c2_cnt))

    labels = np.array(img, copy=True)
    for i, row in enumerate(img):
        for pix, col in enumerate(row):
            labels[i][pix] = int(intensity_info[col]['c'])
    
    return newcenters, labels, mindist

def visualize(centers,labels):
    """
    Convert the image to segmentation map replacing each pixel value with its center.
    Arg: Clustering center values;
         Clustering labels of all pixels. 
    Return: Segmentation map.
    """
    # TODO: implement this function.
    return labels

     
if __name__ == "__main__":
    img = utils.read_image('lenna.png')
    k = 2
    #img = [[1,2,6],[4,2,6],[7,8,6]]
    start_time = time.time()
    centers, labels, sumdistance = kmeans(img,k)
    result = visualize(centers, labels)
    end_time = time.time()

    running_time = end_time - start_time
    print(running_time)

    centers = list(centers)
    with open('results/task1.json', "w") as jsonFile:
        jsonFile.write(json.dumps({"centers":centers, "distance":sumdistance, "time":running_time}))
    utils.write_image(result, 'results/task1_result.jpg')
