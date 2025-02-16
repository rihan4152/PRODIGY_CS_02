from PIL import Image
import numpy as np
import random
import os

def swap_pixels(image_array):
    height, width, _ = image_array.shape
    for _ in range(1000):  # Number of swaps
        x1, y1 = random.randint(0, height-1), random.randint(0, width-1)
        x2, y2 = random.randint(0, height-1), random.randint(0, width-1)
        image_array[x1, y1], image_array[x2, y2] = image_array[x2, y2], image_array[x1, y1]
    return image_array

def apply_math_operations(image_array):
    # Example operation: Add 50 to each pixel's RGB values (mod 255 to stay in valid range)
    image_array = (image_array + 50) % 256
    return image_array

def encrypt_image(input_path, output_path):
  
    image = Image.open(input_path)
    image_array = np.array(image)

    encrypted_image = swap_pixels(image_array)
    encrypted_image = apply_math_operations(encrypted_image)

    encrypted_image = Image.fromarray(encrypted_image.astype('uint8'))

    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path):
   
    image = Image.open(input_path)
    image_array = np.array(image)
   
    decrypted_image = (image_array - 50) % 256

    decrypted_image = swap_pixels(decrypted_image)
   
    decrypted_image = Image.fromarray(decrypted_image.astype('uint8'))

    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    print("Welcome to the Simple Image Encryption Tool!")
    
    action = input("Would you like to (e)ncrypt or (d)ecrypt an image? (e/d): ").strip().lower()

    if action == 'e':
        input_path = input("Enter the path of the image to encrypt: ").strip()
        
        if not os.path.exists(input_path):
            print("The specified file does not exist. Please try again.")
            return
        
        output_path = input("Enter the output path for the encrypted image (e.g., encrypted_image.jpg): ").strip()
        encrypt_image(input_path, output_path)

    elif action == 'd':
        input_path = input("Enter the path of the image to decrypt: ").strip()
        
        if not os.path.exists(input_path):
            print("The specified file does not exist. Please try again.")
            return
        
        output_path = input("Enter the output path for the decrypted image (e.g., decrypted_image.jpg): ").strip()
        decrypt_image(input_path, output_path)

    else:
        print("Invalid option! Please choose either (e)ncrypt or (d)ecrypt.")
        
if __name__ == "__main__":
    main()
