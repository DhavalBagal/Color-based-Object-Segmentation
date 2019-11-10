import cv2
import sys
import numpy as np
from sklearn.cluster import KMeans

size = 500

#Number of clusters to be formed
nc = int(sys.argv[2])

#Reading the image as input
im = cv2.imread(sys.argv[1])

#Resizing the image into a standard size
im = cv2.resize(im, (size,size))

x, y, z = im.shape

#Creating feature vectors from the image
image_2d = im.reshape(x*y, z)

#Creating a list of random colors for each cluster
colors = np.random.randint(255, size=(nc,3))

kmeans = KMeans(n_clusters=nc, random_state=0).fit(image_2d)

labels = kmeans.labels_

#Creating a blank image to display the clustering results
im1 = np.zeros((size,size,3), np.uint8)

#Coloring each pixel according to the cluster it belongs to.
for i in range(size):
    for j in range(size):

        c = labels[i*size+j]

        im1[i,j] = colors[c]
    
v = np.hstack((im, im1))
cv2.imshow('sf',v)
cv2.waitKey(0)

