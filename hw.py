import sys


from glob import *


def main():
    # Scan the directory (current) and compute the hash of all the files
    dirScan = glob('input/*.*')
    fileCount = 0

    while (fileCount < len(dirScan)):
        bv = BitVector(filename=dirScan[fileCount])

        # Initializing the hash to all zeros.
        # The size of the bit vector will be set to 32 bits
        my_hash = BitVector(size=32)

        # If no more data to read,
        # Stop after shifting
        while (bv.more_to_read):
            # Scan the file one byte (8bits) at a time.
            bv1 = bv.read_bits_from_file(8)

            # XOR the new byte read from the file with
            # the least significant byte (the rightmost) of the hash.
            my_hash[0:8] = bv1 ^ my_hash[0:8]

            # Circularly shift bit pattern in hash to left by 4 positions
            my_hash << 4

        bv.close_file_object()

        # Converting to Hexadecimal
        mynewHash = my_hash.getHexStringFromBitVector()

        # Dump the hash values in some output file.
        dumpFile = open('output/dump.txt', 'a')
        dumpFile.write('\n')
        dumpFile.write(dirScan[fileCount])
        dumpFile.write(":")
        dumpFile.write(mynewHash)
        dumpFile.close()
        fileCount += 1


main()