from PIL import Image

# Define a valid key
VALID_KEY = "my_secret_key"

def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ''
    
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for n in range(3):  # RGB channels
                binary_message += str(pixel[n] & 1)
    
    # Split by 8 bits and convert to characters
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111111':  # Delimiter found
            break
        message += chr(int(byte, 2))
        
    return message

if __name__ == "__main__":
    user_key = input("Enter the key to decode the message: ")
    if user_key == VALID_KEY:
        secret_message = decode_image("encoded_image.png")
        print(f"Decoded Message: {secret_message}")
    else:
        print("Invalid key! Access denied.")
