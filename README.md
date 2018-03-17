# Network_security-Assignment
Wrote a function that creates a 32-bit hash of a file using the BitVector module through the following steps: 
- Initialize the hash to all zeros; 
- Scan the file one byte at a time; 
- Before a new byte is read from the file, circularly shift the bit pattern in the hash to the left by four positions; 
- XOR the new byte read from the file with the least significant byte of the hash.

Scan your directory and compute the hash of all your files. Dump the hash values in some output file. Now, write another script to check if your hashing function is exhibiting any collisions. Even though we have a trivial hash function, it is very likely that you will not see any collisions even if your directory is large.

## Results:
Researched Speed Optimizations and security concerns with AES.
