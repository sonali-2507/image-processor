### Separates text and visual elements from image

This project aims to develop an image processing tool that can separate text and visual elements from an image. The tool will utilize various image processing techniques to analyze the image and extract the relevant information.

### Requirements
1. Python 3.x
2. OpenCV (cv2)
3. NumPy
4. Pillow (PIL)
5. Tesseract-OCR and pytesseract

### To use this tool, follow the steps below:

1. Install Python 3.x if it is not already installed on your system.
2. Install the required Python libraries by running the following command in your terminal or command prompt:

'''  pip install opencv-python numpy pillow pytesseract '''


3. Install Tesseract-OCR by following the installation instructions specific to your operating system. You can find the installation guide at the following link: [Tesseract-OCR Installation Guide](https://github.com/UB-Mannheim/tesseract/wiki)

4. Once Tesseract-OCR is installed, you can use the pytesseract library to interface with it in Python.
5. Open the terminal or command prompt and navigate to the directory where the imageProcessor project is located.
6. Run the following command to execute the image processing too
 
python image_processor.py

7. The tool will prompt you to provide the path to the image file you want to process. Enter the path and press Enter. (choose the image path from your local and enter at line number 8)
8. The tool will analyze the image and separate the text and visual elements.
9. The processed image will be saved in the same directory as the original image with the prefix "image1" added to the file name.
10. You can now access the separated text and visual elements for further analysis or use from output.html(open the file in any browser and check the ouput).

### Chalanges encountered
1. Faced chelange in configuration of tesseract.
2. Tried project in java first, Encountered chalenge in configuration of open cv, So switch to python.
