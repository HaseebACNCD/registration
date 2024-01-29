
import cv2
import os
import shutil

# Replace these paths with your source and destination folders
source_folder = r'E:\AI\Extra\gitCheck\register\muzzles/testdata/'
destination_folder = r'E:\AI\Extra\gitCheck\register\Savingfolder/'

# Ensure the destination folder exists, or create it if not
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all the files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg"):  # Assuming you're working with JPEG images
        # Construct the full path to the source image
        source_image_path = os.path.join(source_folder, filename)
        # Load the image
        image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)

        # Apply median filter for noise removal
        image_filtered = cv2.medianBlur(image, 5)  # Adjust kernel size as needed

        # Perform Canny edge detection on the filtered image
        edges = cv2.Canny(image_filtered, threshold1=5, threshold2=10)

        folder_name = filename[0:4]
        destination_subfolder = os.path.join(destination_folder, folder_name)

        if not os.path.exists(destination_subfolder):
            os.makedirs(destination_subfolder)
            # print(f"Folder '{folder_name}' created in {destination_folder}")

        # Construct the full path to the destination image
        destination_image_path = os.path.join(destination_subfolder, filename)

        # Save the edge-detected image to the destination folder
        cv2.imwrite(destination_image_path, edges)
        print('done')



