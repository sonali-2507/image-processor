import cv2
import numpy as np
from PIL import Image
import pytesseract

# Load the image

image_path = r'D:/scaler/bday1.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use edge detection to find edges
edges = cv2.Canny(gray, 50, 150)

# Use contour finding to find the contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask of the same size as the original image, filled with 0s
mask = np.zeros_like(image)

# Draw the contours on the mask
cv2.drawContours(mask, contours, -1, (255,255,255), 3)

# Use image inpainting to remove the text
result = cv2.inpaint(image, cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY), 3, cv2.INPAINT_TELEA)

# Save the result
cv2.imwrite('image1.png',result)

# Open an image file
img = Image.open(r'D:/scaler/bday1.jpg')

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# print(text)

# Create an HTML file
with open('output.html', 'w') as f:
    f.write('<html>\n')
    f.write('<body>\n')
    f.write('<h1>Extracted Text:</h1>\n')
    f.write('<p>{}</p>\n'.format(text))
    f.write('<h1>Image:</h1>\n')
    f.write('<img src="image1.png" alt="Output image">\n')
    f.write('</body>\n')
    f.write('</html>\n')