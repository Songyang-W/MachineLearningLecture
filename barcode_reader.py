import ctypes
from PIL import Image
from pyzbar.pyzbar import decode

# Set the ZBar library path
zbar_lib = ctypes.CDLL('venv/lib/python3.8/site-packages/pyzbar/zbar_library.py')

def read_barcode(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Decode barcodes
    barcodes = decode(img)

    if barcodes:
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            print(f"Barcode Type: {barcode_type}, Data: {barcode_data}")
    else:
        print("No barcode detected in the image")

# Replace 'image.jpg' with the path to your image file
image_file_path = '1.png'
read_barcode(image_file_path)

