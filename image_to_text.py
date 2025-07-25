!sudo add-apt-repository ppa:alex-p/tesseract-ocr

!sudo apt-get update

!sudo apt install tesseract-ocr

!sudo apt install libtesseract-dev

!sudo pip install pytesseract

!tesseract --version

print('starting to download!')

url = '/content/sample_data/2.jpg'

# Instead of using requests.get, which is for web URLs,
# use open to read the local file directly
with open(url, 'rb') as infile:  # 'rb' mode for reading binary data
    file_content = infile.read()

filename = '2.jpg'

with open(filename, 'wb') as out_file:
    out_file.write(file_content)

print("Download complete!")

import cv2
import numpy as np
import pytesseract
from PIL import Image

def get_string(img_path):
    # Check if the image file exists
    if not cv2.haveImageReader(img_path):
        print(f"Error: Image file not found or could not be read: {img_path}")
        return ""  # Return an empty string if image is not found

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite("removed_noise.png", img)

    cv2.imwrite(img_path, img)

    result = pytesseract.image_to_string(Image.open(img_path))

    return result

print('--- Start recognize text from image ---')
print(get_string('2.jpg'))  # Changed the image path to '2.jpg'
print("----- Done -----")
