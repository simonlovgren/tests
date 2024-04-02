from dostuff import *

# Tests
def test_add():
    assert add(2, 3) == call_via_lib(MATHCALLBACK(add), 2, 3)


def test_sub():
    assert sub(2, 3) == call_via_lib(MATHCALLBACK(sub), 2, 3)


def test_mul():
    assert mul(2, 3) == call_via_lib(MATHCALLBACK(mul), 2, 3)


def test_div():
    assert div(2, 3) == call_via_lib(MATHCALLBACK(div), 2, 3)


def test_read_data():
    mystruct = MyStruct(
        read_callback_t=RWCALLBACK(read_callback),
        write_callback_t=RWCALLBACK(write_callback),
    )

    read_len = 10
    buf = (ctypes.c_uint8 * read_len)()

    success = cfunctions.read_from_buffer(ctypes.byref(mystruct), 0, 10, buf)
    print(type(success))
    assert success == True
    assert bytes(buf) == b'\xff' * 10


def test_write_data():
    mystruct = MyStruct(
        read_callback_t=RWCALLBACK(read_callback),
        write_callback_t=RWCALLBACK(write_callback),
    )

    data = b'HELLO WORLD!'

    success = cfunctions.write_to_buffer(ctypes.byref(mystruct), 0, len(data), data)
    assert success == True
    assert DATA_BUFFER[:len(data)] == data