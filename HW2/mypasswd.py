#!/usr/bin/python3
import crypt
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Hash passwords.')

group = parser.add_mutually_exclusive_group()

# specify either salt or a method for generating salt randomly
group.add_argument('-m', '--method', help='sepcify the method',
        default='crypt', choices=['crypt', 'sha256', 'md5', 'sha512'])
group.add_argument('-s', '--salt', help='specify a salt.') 
parser.add_argument('-v', '--verbose', action='store_true', default=False, help='verbose mode') 

args = parser.parse_args()

# recent versions of Python support rounds argument
# we use default values

if args.salt:
    # if the salt is specified, use the salt
    # otherwise, randomly generate a salt 
    salt = args.salt
elif args.method == "crypt":
    salt = crypt.mksalt(method=crypt.METHOD_CRYPT)
elif args.method == "sha256":
    salt = crypt.mksalt(method=crypt.METHOD_SHA256)
elif args.method == "sha512":
    salt = crypt.mksalt(method=crypt.METHOD_SHA512)
elif args.method == "md5":
    salt = crypt.mksalt(method=crypt.METHOD_MD5)
else: 
    print("Unkown method:", args.method) 
    exit(1)

if args.verbose:
    print(args.method)

pw = input("Please enter a password: (note that the password is echoed on screen.)\n")
hashed = crypt.crypt(pw, salt)
if args.verbose:
    print(salt)     # use -v option to see the salt
print(hashed)
