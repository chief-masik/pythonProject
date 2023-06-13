from struct import unpack_from, calcsize


class Types:
    uint16 = 'H'
    int16 = 'h'
    char = 's'
    float = 'f'
    int8 = 'b'
    int64 = 'q'
    uint64 = 'Q'
    uint32 = 'I'
    int32 = 'i'
    double = 'd'


class BinaryReader:
    def __init__(self, data, offset, order='>'):
        self.data = data
        self.offset = offset
        self.order = order

    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_e(reader):
    e1 = reader.read(Types.int64)
    e2 = reader.read(Types.int32)
    e3 = reader.read(Types.int32)
    e4 = reader.read(Types.uint32)
    e5 = reader.read(Types.int32)
    e6 = [reader.read(Types.int16) for _ in range(7)]
    e7 = reader.read(Types.double)
    e8 = [reader.read(Types.int32) for _ in range(5)]
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6, E7=e7, E8=e8)


def read_d(reader):
    d1 = [reader.read(Types.uint32) for _ in range(4)]
    d2 = reader.read(Types.uint32)
    d3 = reader.read(Types.int16)
    return dict(D1=d1, D2=d2, D3=d3)


def read_c(reader):
    c1 = reader.read(Types.int16)
    c2 = read_d(reader)
    c3 = reader.read(Types.int16)
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader):
    b1 = reader.read(Types.int16)
    b2 = reader.read(Types.int8)
    return dict(B1=b1, B2=b2)


def read_a(reader):

    a1_size = reader.read(Types.uint16)
    a1_offset = reader.read(Types.uint32)
    a1_reader = reader.jump_to(a1_offset)
    a1 = [read_b(a1_reader) for _ in range(a1_size)]
    a2 = b''.join([reader.read(Types.char) for _ in range(8)]).decode()
    a3 = read_c(reader)
    a4 = reader.read(Types.double)
    a5_offset = reader.read(Types.uint16)
    a5_reader = reader.jump_to(a5_offset)
    a5 = read_e(a5_reader)
    a6 = reader.read(Types.int16)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)


def main(data):
    return read_a(BinaryReader(data, 4))


print(main((b'\x8fKBD\x00\x02\x00\x00\x008pzuyvxfdr\x05\xde\x02\xf9\x03\x9e\t\xc1\xea'
    b'bI\xdc\xdd<r\xff\x9a\xe9\x11\xe2\xa8*:\x9e\xf9\xbf\xbf\xb8|BQ\x9a\xe0\x00>Fp'
    b'\xc8\x18\x13\x8c\x1f\x88\xf9\xcf\x80\xdb\xbe{r3h\x11j\xba\r\xe5\xf5A\xa31'
    b'\xdd\xfd\x1c\x01\x83l\x05\x18\x97\xcfSR\xc3NMJ&\xa0\xc9\xf4?\xe6\x96\x96'
    b"\x13ou\\\xfau\x98\rq\x9bs\x04\xf71\x87,X'^\xa4\x17\xb1VB")))
