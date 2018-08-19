import struct

def read_bool(buffer) -> bool:
    return struct.unpack("<?", buffer.read(1))[0]

def read_ubyte(buffer) -> int:
    return struct.unpack("<B", buffer.read(1))[0]

def read_ushort(buffer) -> int:
    return struct.unpack("<H", buffer.read(2))[0]

def read_uint(buffer) -> int:
    return struct.unpack("<I", buffer.read(4))[0]

def read_float(buffer) -> float:
    return struct.unpack("<f", buffer.read(4))[0]

def read_double(buffer) -> float:
    return struct.unpack("<d", buffer.read(8))[0]

def read_ulong(buffer) -> int:
    return struct.unpack("<Q", buffer.read(8))[0]

def read_string(buffer) -> str:
    strlen = 0
    strflag = read_ubyte(buffer)
    if (strflag == 0x0b):
        strlen = 0
        shift = 0
        # uleb128
        # https://en.wikipedia.org/wiki/LEB128
        while True:
            byte = read_ubyte(buffer)
            strlen |= ((byte & 0x7F) << shift)
            if (byte & (1 << 7)) == 0:
                break
            shift += 7
    return (struct.unpack("<" + str(strlen) + "s", buffer.read(strlen))[0]).decode("utf-8")
