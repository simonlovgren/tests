#!/usr/bin/env python

import struct, binascii
from ctypes import *

class DataHeader( Structure ):
    _pack_ = 1
    _fields_ = [
        ("size", c_uint64),
        ("type", c_ubyte * 4)
    ]

class TestHeader( Structure ):
    _pack_ = 1
    _fields_ = [
        ("id", c_ubyte * 4),
        ("pad1", c_ubyte * 4),
        ("data_header", DataHeader)
    ]

    def receiveSome(self, bytes):
        fit = min(len(bytes), sizeof(self))
        memmove(addressof(self), bytes, fit)

    def calcsize( self ):
        return sizeof(self)


if __name__ == "__main__":
    header = TestHeader()
    with open('testdata', 'rb') as f:
        print("Header size: {} bytes".format(sizeof(header)))
        header.receiveSome(f.read(header.calcsize()))
        # Header data
        print("Header ID: {}".format(str(cast(header.id, c_char_p).value.decode())))
        # Data header
        print("Data type: {}".format(str(cast(header.data_header.type, c_char_p).value.decode())))
        print("Data size: {}".format(header.data_header.size))
        # # Read end byte of data to verity integrity
        f.seek(header.data_header.size - sizeof(c_ubyte), 1) # Go (data_size - 1) bytes forward from current position
        endbyte = f.read(1) # Read last byte
        print("End byte:  {}".format(binascii.hexlify(endbyte).decode()))
