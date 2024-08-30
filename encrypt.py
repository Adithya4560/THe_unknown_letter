'''
Create a website with the help of streamlit where Title is written in the center of the screen and the name of the title is "Convert Text to Encrypted Text".\
Then create a label it will be placed in the screen and the name of the label is "Enter Text" and also create a text box to enter the text.
Create a label it will be ask the user to enter the how much should the text be shifted and create an text box to enter the shift.
Create the button to convert the text to encrypted text and display the encrypted text on the screen give the name of the button as "Encrypt".
Now, write the code to convert an text to encrypted text with the help of cipher.
Ask the user to enter the text and display the encrypted text on the screen and also ask the user to enter the shift.
Create a button to copy the encrypted text to the clipboard and give the name of the button as "Copy Encrypted Text".
Use the dropbox for to select wheather to encrypt or decrypt the text.
Now to enter the encrypted text for that we will create a label and also create a text box to enter the encrypted text and the label name will be "Enter Encrypted Text".
Now we will create a button to convert the encrypted text to decrypted text and the button name will be "Decrypt".
Now write the code to decrypt the encrypted text with the help of cipher and the decrypted text will be displayed on the screen.
Create a button to copy the decrypted text to the clipboard and the button name will be "Copy Decrypted Text".
You have to guess wheather how many shift has happened in the encrypted text.
'''

import streamlit as st
import pyperclip

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result

st.title("Convert Text to Encrypted Text")

mode = st.selectbox("Select mode", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
    plaintext = st.text_area("Enter Text")
    shift = st.number_input("Enter shift value", min_value=1, max_value=25, value=3, step=1)
    
    if st.button("Encrypt"):
        encrypted_text = caesar_cipher(plaintext, shift)
        st.session_state.encrypted_text = encrypted_text
        st.text_area("Encrypted Text", encrypted_text, height=100)

    if st.button("Copy Encrypted Text"):
        if 'encrypted_text' in st.session_state:
            pyperclip.copy(st.session_state.encrypted_text)
            st.success("Encrypted text copied to clipboard!")
        else:
            st.warning("Please encrypt the text first.")

else:
    encrypted_text = st.text_area("Enter Encrypted Text")
    
    if st.button("Decrypt"):
        st.write("All possible decryptions:")
        all_decryptions = []
        for shift in range(1, 26):
            decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')
            all_decryptions.append(f"Shift {shift}: {decrypted_text}")
            st.write(f"Shift {shift}: {decrypted_text}")
        st.session_state.all_decryptions = "\n".join(all_decryptions)

    if st.button("Copy All Decryptions"):
        if 'all_decryptions' in st.session_state:
            pyperclip.copy(st.session_state.all_decryptions)
            st.success("All decryptions copied to clipboard!")
        else:
            st.warning("Please decrypt the text first.")

