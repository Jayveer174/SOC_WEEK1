import numpy as np
from PIL import Image

# Make sure that image for you want to get output should be present
# in same folder as of python file. Run this code using some others images too :)
Image_name = "c.png"

# Open the image file
img = Image.open(Image_name)

# Convert the image to a numpy array and extract the grayscale values (ravel() extracts the grayscale values )
img_array = np.array(img)
gray_values = img_array.ravel()
# Now numpy array gray_values contains gray value of each pixel.

##### TO DO #####

# Using Introduction.py see If image contains all pixel values are zero or not.
# Convert the given black image (Image is black because all grayscale values are near to zero) into
# img_stretched so that our eyes can see what's actually there in the image.
# This process is a real life application in Biology using Digital Image Processing.
# Change something in img_array :)
# Run your code with given 3 images by changing Image name in the code.

# HINTS
# 1. Increase the contrast (Read last week theory- Histogram Stretching)
# 2. min_value = np.min(gray_values) - This gives minimum value from the numpy array gray_values. Similarly you can find maximum value :)

# ACTIVITY
# I have given three images a.png, b.png, c.png. The time order of taking this image is as follows:
# a.png b.png c.png
#   t    t+T   t+2T
# Can you guess process?

#### WRITE YOUR CODE HERE ####
min_value= np.min(gray_values)
max_value= np.max(gray_values)
newgray_values=(gray_values-min_value)*(2^8)/(max_value-min_value)




# Remove any newline characters from the gray scale values
# newgray_values = [line.strip() for line in gray_values]

# Extract the size of the image from the first line of gray scale values
size = tuple(map(int, newgray_values[0].split('=')[1].strip().split(',')))

# Create a new image with the specified size
img = Image.new("L", size)

# Get a pixel access object for the image
pixels = img.load()

# Loop through the gray scale values and set the corresponding pixel in the image
for line in newgray_values[1:]:
    # Extract the pixel coordinates and gray scale value from each line
    coordinates, gray_scale = line.split(':')
    x, y = map(int, coordinates.strip().lstrip('Pixel(').rstrip(')').split(','))
    gray_scale = int(gray_scale.split('=')[1].strip())
    
    # Set the pixel value in the image
    pixels[x, y] = gray_scale

# Save the reconstructed image
img.save("reconstructed_image.png")





############# END ############


# Convert the numpy array back to an image and save it
img_stretched = Image.fromarray(np.uint8(img_array))
img_stretched.save(f"final-{Image_name}")