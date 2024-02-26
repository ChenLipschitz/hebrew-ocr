import cv2
import pytesseract
import os

# Read the input image
image = cv2.imread('text.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR to extract text and bounding boxes
data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

# Set the output folder name
output_folder = 'images_after_splitting'

# Check if the output folder already exists
if not os.path.exists(output_folder):
    # If the folder doesn't exist, create it
    os.makedirs(output_folder)

# Initialize a counter for words
word_counter = 0

# Iterate over each word bounding box
for i, word_text in enumerate(data['text']):
    # Filter out non-word regions (ignore empty strings)
    if word_text.strip():
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        
        # Crop the region corresponding to the word
        word_image = image[y:y+h, x:x+w]
        
        # Save the word image into the folder
        cv2.imwrite(os.path.join(output_folder, f'word_{word_counter}.jpg'), word_image)

        # Print the text of each word along with its bounding box coordinates
        print(f"Word {word_counter}: {word_text}, Bounding Box: (x={x}, y={y}, w={w}, h={h})")
        
        # Increment the word counter
        word_counter += 1