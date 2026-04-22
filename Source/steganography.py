from PIL import Image

DELIMITER = "#####"

def hide_data(image_path, message, output_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    # Step 1: prepare data
    message = message + DELIMITER
    binary = ""
    for ch in message:
        binary += format(ord(ch), '08b')
    data_index = 0
    new_pixels = []

    # Step 2: hide data
    for pixel in pixels:
        r, g, b = pixel
        if data_index < len(binary):
            r = (r & ~1) | int(binary[data_index])
            data_index += 1
        if data_index < len(binary):
            g = (g & ~1) | int(binary[data_index])
            data_index += 1
        if data_index < len(binary):
            b = (b & ~1) | int(binary[data_index])
            data_index += 1
        new_pixels.append((r, g, b))
    image.putdata(new_pixels)
    image.save(output_path)



def extract_data(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary = ""

    # Step 1: get LSB bits
    for pixel in pixels:
        r, g, b = pixel
        binary += str(r & 1)
        binary += str(g & 1)
        binary += str(b & 1)
    message = ""

    # Step 2: convert to text
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        char = chr(int(byte, 2))
        message += char

        if message.endswith(DELIMITER):
            return message[:-len(DELIMITER)]
    return message

