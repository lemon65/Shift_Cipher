#!/usr/bin/python
# simple encryption program that will take a text file or string, and output the
# encrypted version of it either within the text file given or output a string.
# By: Lemon65

import os
import sys
import keyword_cipher as kc
import optparse
DATA_PAYLOAD = ''

# Create the Variables for all the options.
def create_opts():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="Path to local file.", action="store")
    parser.add_option("-s", "--string", dest="string",
                      help="String to use as an input.", action="store_true")
    parser.add_option("-i", "--index", dest="index_val",
                      help="List of index values that will be used to encrypt and decrypt data. split values by ','", action="store")
    parser.add_option("-e", "--encrypt", dest="encrypt", default=False,
                      help="Flag to encrypt the data.", action="store_true")
    parser.add_option("-d", "--decrypt", dest="decrypt", default=False,
                      help="Flag to decrypt the data.", action="store_true")
    (opts, args) = parser.parse_args()
    return (opts, args)

# Start of the main function to start the simple encryption.
def main():
    opts, args = create_opts()
    check_bool = False
    crypt_level = 1
    index_list = opts.index_val.split(',')
    for in_step in index_list:# Checking the data to see if it will cause index errors.
        if (int(in_step) > int(len(kc.CIPHER_LIST)) or int(in_step) == 0):
            bad_int = in_step
            check_bool = True
            break
    data_payload = ""
    if check_bool:
        print 'Error on %s Index between 1:%s' % (bad_int, len(kc.CIPHER_LIST))
        sys.exit()
    if opts.string and not opts.filename:
        DATA_PAYLOAD = raw_input('Enter Data: ')
    if opts.filename and not opts.string:
        if os.path.exists(opts.filename):
            with open(opts.filename, 'r') as myfile:
                DATA_PAYLOAD = myfile.read()
        else:
            print 'Error: Looks like [%s] isnt a Real File path...' % opts.filename
            sys.exit()
    if opts.encrypt:
        for in_step in index_list:
            print 'Current Encryption Level: %s' % crypt_level
            DATA_PAYLOAD = kc.cipher_worker(DATA_PAYLOAD.lower(), opts.encrypt, opts.decrypt, int(in_step))
            crypt_level += 1
    else:
        index_list.reverse()
        for in_step in index_list:
            print 'Current Decryption Level: %s' % crypt_level
            DATA_PAYLOAD = kc.cipher_worker(DATA_PAYLOAD.lower(), opts.encrypt, opts.decrypt, int(in_step))
            crypt_level += 1
    if opts.string and not opts.filename:
        print 'Final Data After|<--->|%s' % DATA_PAYLOAD
    if opts.filename and not opts.string:
        print 'File has been Updated....' 
        f = open(opts.filename, "w")
        f.write(DATA_PAYLOAD)
        f.close()

if __name__ == "__main__":
    sys.exit(main())
