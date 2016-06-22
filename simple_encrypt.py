#!/usr/bin/python
# simple encryption program that will take a text file or string, and output the
# encrypted version of it either within the text file given or output a string.
# By: Lemon65

import os
import sys
import keyword_cipher as kc
import optparse

# Create the Variables for all the options.
def create_opts():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="Path to local file.", action="store")
    parser.add_option("-s", "--string", dest="string",
                      help="String to use as an input.", action="store_true")
    parser.add_option("-i", "--index", dest="index_val",
                      help="Index used to create the key cipher", action="store")
    parser.add_option("-e", "--encrypt", dest="encrypt", default=False,
                      help="Flag to encrypt the data.", action="store_true")
    parser.add_option("-d", "--decrypt", dest="decrypt", default=False,
                      help="Flag to decrypt the data.", action="store_true")
    (opts, args) = parser.parse_args()
    return (opts, args)

# Start of the main function to start the simple encryption.
def main():
    opts, args = create_opts()
    data_payload = ""
    if int(opts.index_val) == 0 or int(opts.index_val) > len(kc.CIPHER_LIST):
        print 'Error Use an Index between 1:%s Or -1:-%s' % (len(kc.CIPHER_LIST), len(kc.CIPHER_LIST))
        sys.exit()
    if opts.string and not opts.filename:
        data_payload = raw_input('Enter Data: ')
    if opts.filename and not opts.string:
        if os.path.exists(opts.filename):
            with open(opts.filename, 'r') as myfile:
                data_payload = myfile.read()
        else:
            print 'Error: Looks like [%s] isnt a Real File path...' % opts.filename
            sys.exit()
    result = kc.cipher_worker(data_payload.lower(), opts.encrypt, opts.decrypt, int(opts.index_val))
    if opts.string and not opts.filename:
        print result
    if opts.filename and not opts.string:
        f = open(opts.filename, "w")
        f.write(result)
        f.close()

if __name__ == "__main__":
    sys.exit(main())
