import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time
from PIL import ImageGrab
import pyautogui

# Input and output directories
input_dir = "pics"
output_dir = "pics"
output_pdf = "output.pdf"
seconds_per_frame = 1.1

# Function to capture a specific screen area and save it as an image
def capture_and_save_screen_area(x, y, width, height, filename):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    screenshot.save(os.path.join(output_dir, filename))


def create_pdf(num):
    print("convertion to pdf started...")
    # Get a list of image files in the input directory
    image_files = [os.path.join(input_dir, filename) for filename in os.listdir(input_dir) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Sort the image files to maintain order
    image_files.sort()

    # Create a PDF file and set its size
    c = canvas.Canvas(str(num)+output_pdf, pagesize=letter)

    # Iterate through image files and add them to the PDF
    for image_file in image_files:
        with Image.open(image_file) as img:
            width, height = img.size
            c.setPageSize((width, height))
            c.drawImage(image_file, 0, 0, width, height)
            c.showPage()
        os.remove(image_file)

    # Save the PDF file
    c.save()

    print(f"PDF file '{output_pdf}' created successfully with {len(image_files)} images.")

def delete_images_in_dir():
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            else:
                raise RuntimeError(f"Failed to delete {file_path}. It is not a file.")
        except Exception as e:
            print(f"Failed to delete %s. %s" % (file_path, e))
            
def close_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
            
# create_pdf(0)
# close_tab()
# quit()

from time import sleep as wait

wait(5)
books = [163, 121, 147, 517]
for book in range(len(books)):
    pages = books[book]
    delete_images_in_dir()
    for i in range(pages):
        l = i
        prefix = "0"*(4 - len(str(l))) + str(l)
        capture_and_save_screen_area(x=26, y=60, width=1042, height=1475, filename=prefix+"screenshot.png")
        # Simulate pressing the right arrow key
        # quit()
        pyautogui.press('right')
        wait(seconds_per_frame)
    create_pdf(book)
    close_tab()
    wait(2)
    if book == 0:
        quit()
        
