How to Set Everything Up?


1. **Instal requirements**
    ```bash
    pip3 install fastapi pydantic openai numpy pillow opencv-python
    ```

2. **Instal pytesseract**
    
    please follow the instructions in https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/?fbclid=IwAR1K-IA7oktIebBFcj4zFBw6UU7BdfWvj1jwIR9_XH1QNyFtYGmkmjgNoYg


1. **Run the API**
    ```bash
    python3 api.py
    ```

2. **Access the API Documentation**
    - Go to `localhost:8000/docs`

3. **Run the Docker Container for the Model**
    - Build the new model:
        ```bash
        docker build . -t model
        ```
        
    - Run the new model:
        ```bash
        sudo docker run -d -p 8010:8010 -v ./images_after_splitting:/tmp/images_after_splitting model
        ```
