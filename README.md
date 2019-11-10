# Color-based-Object-Segmentation
The project uses clustering using color features as a simple approach to object segmentation.  The input image is divided into n clusters based on the RGB values of the pixels, where n is provided by the user. The dataset for clustering consists of 3 columns, each corresponding to the R,G and B values of the pixels respectively. Using K-means clustering, pixels with almost similar colors are grouped into the same cluster, thereby segmenting the image.

# Command to run
python3  filename.py  imagename.jpg  no_of_clusters_to_be_formed

E.g: python3 segment.py a.jpeg 4
