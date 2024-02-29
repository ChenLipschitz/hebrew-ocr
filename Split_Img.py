import cv2
import pytesseract
import os

# Read the input image

def perform_ocr(image_path: str) -> None:
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    output_folder = 'images_after_splitting'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    word_counter = 0

    expansion_factor = 12  

    for i, word_text in reversed(list(enumerate(data['text']))):
        if word_text.strip():
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            
            x -= expansion_factor
            y -= expansion_factor
            w += 2 * expansion_factor
            h += 2 * expansion_factor
            
            x = max(0, x)
            y = max(0, y)
            w = min(w, image.shape[1] - x)
            h = min(h, image.shape[0] - y)
            
            word_image = image[y:y+h, x:x+w]

            resized_word_image = cv2.resize(word_image, (128, 32))
            
            cv2.imwrite(os.path.join(output_folder, f'word_{word_counter}.jpg'), resized_word_image)
            print(f"Word {word_counter}: {word_text}, Expanded Bounding Box: (x={x}, y={y}, w={w}, h={h})")
            word_counter += 1