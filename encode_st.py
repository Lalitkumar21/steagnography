from PIL import Image

# Define a valid key
VALID_KEY = "my_secret_key"

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    
    # Convert message to binary
    binary_message = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # Delimiter
    data_index = 0
    
    for y in range(height):
        for x in range(width):
            pixel = list(encoded.getpixel((x, y)))
            for n in range(3):  # RGB channels
                if data_index < len(binary_message):
                    pixel[n] = (pixel[n] & ~1) | int(binary_message[data_index])
                    data_index += 1
            encoded.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break
            
    encoded.save(output_path)
    print(f"Message encoded into {output_path}")

if __name__ == "__main__":
    user_key = input("Enter the key to encode the message: ")
    if user_key == VALID_KEY:
        image_path = "naruto.jpg"
        message_path = "data.txt"
        output_path = "encoded_image.png"

        with open(message_path, 'r') as file:
            message = file.read()
        encode_image(image_path, message, output_path)
    else:
        print("Invalid key! Access denied.")
