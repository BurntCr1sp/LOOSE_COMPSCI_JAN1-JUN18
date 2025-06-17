def choice():
    choose = input("Encrypt (1) or Decrypt (2): ")
    
    if choose == '1':
        input_text = input("Enter text to encrypt: ")
        encrypt_output = ENCRYPT(input_text)
        print("Encrypted text:", encrypt_output)
        
    elif choose == '2':
        encrypted_text = input("Enter text to decrypt: ")
        decrypt_output = DECRYPT(encrypted_text)
        print("Decrypted text:", decrypt_output)
    else:
        print("Invalid choice. Please select 1 for Encrypt or 2 for Decrypt.")

def ENCRYPT(text):
    encrypt_representation = []
    for char in text:
        encrypt_value = oct(ord(char))[2:]  # Convert character to octal
        encrypt_representation.append(encrypt_value)
    return ' '.join(encrypt_representation)  # Join the octal values with spaces

def DECRYPT(encrypted_text):
    decrypted_text = []
    encrypted_values = encrypted_text.split()  # Split the encrypted string into its octal values
    for octal_value in encrypted_values:
        char = chr(int(octal_value, 8))  # Convert octal back to character
        decrypted_text.append(char)
    return ''.join(decrypted_text)  # Join the characters to return the decrypted string

# Main function to run the program
if __name__ == "__main__":
    print("Welcome to the Encrypt/Decrypt program!")
    choice()
