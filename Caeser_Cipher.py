def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        # If the character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        # If the character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        # If it's not a letter, leave it unchanged
        else:
            encrypted_text += char
            
    return encrypted_text

# Ask the user whether they want to encrypt or decrypt
action = input("Would you like to encrypt or decrypt the text? (Enter 'encrypt' or 'decrypt'): ").strip().lower()

# Get the text and shift value from the user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))  # You can change this shift value

if action == 'encrypt':
    # Encrypt the text
    encrypted_text = caesar_cipher(text, shift)
    print(f"Encrypted text: {encrypted_text}")
elif action == 'decrypt':
    # Decrypt the text by shifting in the opposite direction
    decrypted_text = caesar_cipher(text, -shift)
    print(f"Decrypted text: {decrypted_text}")
else:
    print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
