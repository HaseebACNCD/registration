
import glob
import cv2
import os


# Replace these paths with your source and destination folders
source_folder = r'E:\AI\Extra\gitCheck\register\muzzles\testdata/'
destination_folder = r'E:\AI\Extra\gitCheck\register/destination_folder/'


# Specify the filename of the image you want to process
# filename_to_process = 'E:\AI\Extra\gitCheck\register\muzzles/co88_1c.jpg'  # Replace with the actual filename

for i in glob.glob(source_folder +'**'):
    print(i)

# Construct the full path to the source image
# source_image_path = os.path.join(source_folder, filename_to_process)

# # Load the image
# image = cv2.imread(filename_to_process, cv2.IMREAD_GRAYSCALE)

# # Apply median filter for noise removal
# image_filtered = cv2.medianBlur(image, 5)  # Adjust kernel size as needed

# # Perform Canny edge detection on the filtered image
# edges = cv2.Canny(image_filtered, threshold1=5, threshold2=10)

# # Construct the full path to the destination image
# destination_image_path = os.path.join(destination_folder, filename_to_process)


# source_image_path = os.path.join(source_folder, filename_to_process)

# # Save the edge-detected image to the destination folder
# cv2.imwrite(destination_image_path, edges)

# print("Edge detection with noise removal complete. Edge-detected image is saved in:", destination_folder)

