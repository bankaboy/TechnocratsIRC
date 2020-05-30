import sys
from smbus2 import SMBus

def cmd(val):
    with SMBus(1) as bus:
        bus.write_byte(0x1a>>1, val)
        bus.write_byte(0x1a>>1, val)

if __name__ == "__main__":
    a = int(sys.argv[1])
    cmd(a)

