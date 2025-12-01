import os
import numpy as np
from PIL import Image

# What's this PIL thing?
# PIL stands for Python Imaging Library. It is a library in Python that adds support for opening, manipulating, and saving many different image file formats.

# Build a safe path to the image (relative to this script) and provide a fallback if it doesn't exist
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'Images', 'nature.jpg')

if os.path.exists(img_path):
	image = Image.open(img_path)
else:
	# fallback: create a placeholder image to avoid FileNotFoundError
	image = Image.new('RGB', (250, 250), color=(128, 128, 128))

# Ensure a consistent mode and size
image = image.convert('RGB').resize((250, 250))  # Resize image to 250x250 pixels and force RGB

# Convert the image to a numpy array
arr = np.array(image)

print("Array Shape:", arr.shape)  # Print the shape of the array
print("Pixel Value at (0,0):", arr[0, 0])  # Print the pixel value at the top-left corner

# Convert back to an image from the numpy array
new_image = Image.fromarray(arr)

# Display the image once
new_image.show()
