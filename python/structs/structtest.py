#!/usr/bin/env python

import struct, binascii
from ctypes import *

class TestHeader( Structure ):
    _pack_ = 1
    _fields_ = [
        ("id", c_ubyte * 4),
        ("pad1", c_ubyte * 4),
        ("datasize", c_uint64),
        ("type", c_ubyte * 4)
    ]

    def receiveSome(self, bytes):
        fit = min(len(bytes), sizeof(self))
        memmove(addressof(self), bytes, fit)

    def calcsize( self ):
        return sizeof(self)


if __name__ == "__main__":
    header = TestHeader()
    with open('testdata', 'rb') as f:
    #    struct.receiveSome(header, f.read(struct.calcsize(header)))
        print("Header size: {} bytes".format(sizeof(header)))
        header.receiveSome(f.read(header.calcsize()))
        print(str(cast(header.id, c_char_p).value),
              header.datasize,
              str(cast(header.type, c_char_p).value))
        # Read end byte of data to verity integrity
        f.read(header.datasize - sizeof(c_ubyte))
        endbyte = f.read(1)
        print("End byte:", binascii.hexlify(endbyte))
