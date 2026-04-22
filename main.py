from Source.encryption import encrypt_message, decrypt_message
from Source.steganography import hide_data, extract_data
from Source.validator import validate_message_length, validate_password_length
import os

def main():
    while True:
        print("\n1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            message = input("Enter the message: ")
            password = input("Enter the password: ")

            if not validate_message_length(message):
                continue
            if not validate_password_length(password):
                continue

            encrypted = encrypt_message(message, password)

            # Show available images
            images = [img for img in os.listdir("Images") if img.startswith("input")]
            print("\nAvailable images:",images)

            # User selects image
            image_name = input("Enter image name (with extension): ")

            input_path = "Images/" + image_name
            output_path = "Images/output.png"

            hide_data(input_path, encrypted, output_path)

            print("Message hidden successfully")

            # Check file comparison:
            same = open(input_path,"rb").read() == open(output_path,"rb").read()
            print("\n=== Integrity Check ===")
            print("Image modified successfully:", not same)

        elif choice == "2":
            password = input("Enter the password: ")

            if not validate_password_length(password):
                continue

            extracted = extract_data("Images/output.png")

            decrypted = decrypt_message(extracted, password)

            print("Hidden message: ", decrypted)

        elif choice == "3":
            print("Existing---")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()