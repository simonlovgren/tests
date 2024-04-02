#!/usr/bin/env python3

import ctypes
from pathlib import Path
from typing import List

# Load the shared library into ctypes
cfunctions = ctypes.CDLL(str(Path(__file__).parent / "cfunctions.so"))


MATHCALLBACK = ctypes.CFUNCTYPE(
    ctypes.c_int,  # Return type
    ctypes.c_int,  # First argument type
    ctypes.c_int,  # Second argument type
)

RWCALLBACK = ctypes.CFUNCTYPE(
                ctypes.c_int32,
                ctypes.c_uint32,
                ctypes.c_size_t,
                ctypes.POINTER(ctypes.c_uint8),
            )

class MyStruct(ctypes.Structure):
    _fields_ = [
        (
            "read_callback_t",
            RWCALLBACK,
        ),
        (
            "write_callback_t",
            RWCALLBACK
        )
    ]


DATA_BUFFER = bytearray(b'\xFF' * 1024)


def read_callback(address: ctypes.c_uint32, size: ctypes.c_size_t, dst) -> bool:
    print(f"Read {size} bytes from {address}")
    print(type(dst))
    for i in range(size):
        dst[i] = DATA_BUFFER[address + i]
    return 1


def write_callback(address: ctypes.c_uint32, size: ctypes.c_size_t, src) -> bool:
    print(f"Write {size} bytes to {address}")
    for i in range(size):
        DATA_BUFFER[address + i] = src[i]
    return 1


# Some math functions
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


# Call via library
def call_via_lib(operation, a, b):
    return cfunctions.do_math(operation, a, b)


