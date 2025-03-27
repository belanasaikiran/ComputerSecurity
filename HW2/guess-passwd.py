#!/usr/bin/python3
import itertools
import crypt
from hmac import compare_digest as compare_hash
import sys
import argparse

# some predefined character sets in string
# for example:
# string.ascii_lowercase
# string.ascii_uppercase
import string

# the function that guesses a password that is a decimal number
# no leading 0's 
def guess_password_numbers(hashed, end):
    for n in range(end):
        s = str(n)
        if compare_hash(hashed, crypt.crypt(s, hashed)):
            return s
    return ''

def genPasswords(min_len, max_len):
    # character sets
    chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    for i in range(min_len, max_len + 1):
        for guess in itertools.product(chars, repeat=i):
            yield ''.join(guess)

# pass proper parameters to genPasswords()
# see the test mode below for the usage of genPasswords()  
# check if passwords from genPasswords()  
def guess_password(hashed, min_len, max_len):
    # check any of the words returned by genPasswords produced hashed 
    # only need a few lines if not for multiple threads
    # TODO
    return ''

# pass arguments
parser = argparse.ArgumentParser(description='Guess passwords.')

parser.add_argument('hashed', nargs='?', default='', 
        help='hashed password. Enclose the hashed password with single quotation'
        'marks if the hash has special characters like $')
parser.add_argument('--number', action='store_true', default=False, 
        help='password is a number without leadning 0s') 
parser.add_argument('--min', type=int, default=1, help='min length of the password')
parser.add_argument('--max', type=int, default=8, help='max length of the password')
parser.add_argument('--test', action='store_true', default=False, help='test mode.') 

args = parser.parse_args()

# test mode
if args.test:
    for pw in genPasswords(args.min, args.max):
        print(pw)
    exit(0)

if not args.hashed:
    print("Please enter the hashed password:")
    # do not add quotation marks
    hashed = input("")
else:
    hashed = args.hashed

# filter out the input that do not look like a hash 
if len(hashed) != 13 and not hashed.startswith('$'):
    print(f"{hashed} does not look like a valid hashed password.\n"
        "Try to enclose the hash with signle quotation marks on command line.")
    exit(1)

if args.number:
    end = 10 ** args.max 
    print(f"Trying numbers from 0 to {end-1}...")
    r = guess_password_numbers(hashed, end)
else:
    print(f"Trying passwords of lengths from {args.min} to {args.max}...")
    r = guess_password(hashed, args.min, args.max)

if r:
    print(r)
    exit(0)
else:
    print("Not found.")
    exit(1)

# you can try multiple threads
'''
threads = [] 
for i in range(n_threads):
    mythread = threading.Thread(target=function, args=(arg1, arg2, ...))
    mythread.start()
    threads.append(mythread)
for i in range(n_threads):
    threads[i].join()
'''
