#!/usr/bin/python3

import gnupg
from pathlib import Path

private=Path("/home/mariusz/.ssh/private_key_file.asc")

# initialize GPG instance
gpg = gnupg.GPG()

# get user's public and private keys
public_key = gpg.import_keys(open('public_key_file.asc').read())
private_key = gpg.import_keys(open(private).read())

# define function for encrypting message
def encrypt_message(message, recipient):
    encrypted_data = gpg.encrypt(message, recipient)
    return str(encrypted_data)

# define function for decrypting message
def decrypt_message(encrypted_message):
    decrypted_data = gpg.decrypt(encrypted_message, passphrase='your_passphrase')
    return str(decrypted_data)

# define function for sending message
def send_message(message, recipient):
    # encrypt message
    encrypted_message = encrypt_message(message, recipient)
    # send encrypted message to recipient
    # code for sending message goes here

# define function for receiving message
def receive_message():
    # receive encrypted message from sender
    # code for receiving message goes here
    encrypted_message = received_message
    # decrypt message
    decrypted_message = decrypt_message(encrypted_message)
    return decrypted_message

# main program loop
while True:
    # get user input
    message = input("Enter message: ")
    recipient = input("Enter recipient email: ")
    
    # send message
    send_message(message, recipient)
    
    # receive message
    received_message = receive_message()
    print("Received message: ", received_message)
