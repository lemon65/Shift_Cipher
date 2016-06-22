#!/usr/bin/python

# This is the script that will take a block of text and return an encrypted
# or decrypted result.

CIPHER_LIST = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '.', '/', '?', ',', ';', ':', '(', ')', '1', '2', '3', '4', '5',
               '6', '7', '8', '9', '0', ' ', '=', '+', '-', '[', ']', '{', '}',
               '<', '>', '_', '"', "'", '!', '@', '#', '$', '%', '^', '&', '*')

BUFFER_LIST = []
CIPHER_KEY = {}

# Creates the CIPHER_KEY that is used during run time.
def create_cipher_key(index_off_set):
    BUFFER_LIST = list(CIPHER_LIST)
    for char_step in range(0, index_off_set):
        buffer_val = CIPHER_LIST[char_step]
        del BUFFER_LIST[0]
        BUFFER_LIST.append(buffer_val)
    for index, key_step in enumerate(CIPHER_LIST):
        CIPHER_KEY[key_step] = BUFFER_LIST[index]
    return

# This takes args and calls the encrypt and decrypt functions.
def cipher_worker(string_blob, en_bool, de_bool, index_off_set):
    create_cipher_key(index_off_set)
    for string_step in string_blob:
        if en_bool and not de_bool:
            encrypt_data(string_step)
        if de_bool and not en_bool:
            decrypt_data(string_step)
    final_result = "".join(BUFFER_LIST)
    return "".join(final_result)

# encrypt the Char and append the result.
def encrypt_data(input_char):
    de_val = CIPHER_KEY.get(input_char)
    if de_val:
        BUFFER_LIST.append(de_val)
    else:
        BUFFER_LIST.append(input_char)

# decrypt the Char and append the result.
def decrypt_data(input_char):
    for k_val, v_val in CIPHER_KEY.iteritems():
        if input_char == v_val:
            BUFFER_LIST.append(k_val)
            return
    BUFFER_LIST.append(input_char)
