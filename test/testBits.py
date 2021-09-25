import struct
from typing import Tuple


def format(i):
    text = hex(int(i)).replace("0x", "").upper()
    return text if len(text) == 2 else "0" + text


def print_hex(buf):
    print("<Buffer %s>" % " ".join([format(i) for i in buf]))


def pack(length, cmd, port):
    assert 0 < length < 256, '0<length < 256'
    assert cmd > 0, ' cmd>0'
    assert port > 0, 'port>0'
    return struct.pack(
        '!14B',
        0, 0, 0, 0, 0, 0, 0xDA,
        length,
        0x02,
        0x7F & (cmd >> 7),
        0x7F & cmd,
        0x7F & (port >> 14),
        0x7F & (port >> 7),
        port & 0x7F
    )


def unpack(buf) -> Tuple[int, int, int]:
    return \
        buf[7], \
        ((buf[9] << 7) | buf[10]), \
        ((buf[11] << 14) | (buf[12] << 7) | buf[13])


def main():
    length = 255
    cmd = 1249
    port = 145598
    bin_buf = pack(length, cmd, port)
    print_hex(bin_buf)
    u_length, u_cmd, u_port = unpack(bin_buf)
    assert u_length == length, 'length unpack error!'
    assert u_cmd == cmd, 'cmd unpack error!'
    assert u_port == port, 'port unpack error!'
    print(u_length, u_cmd, u_port)


main()
