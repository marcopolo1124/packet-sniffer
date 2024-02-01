import struct
import socket

def unpack_data(data):
    #uint8, uint8, uint32, uint16, uint8, n
    device, packet_length, checksum, data_address, rw = struct.unpack("! B B I H B", data[:9])
    return {
        "device": device,
        "packet_length": packet_length,
        "checksum": checksum,
        "addr": data_address,
        "readwrite": rw,
        "data": data[9:]
    }
    


# def main():
#     HOST = socket.gethostbyname(socket.gethostname())
#     s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
#     s.bind((HOST, 0))
#     s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#     s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    
#     while True:
#         raw_data, addr = s.recvfrom(65536)
#         print(unpack_data_inet(raw_data))

# def unpack_data_inet(data):
#     dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
#     return get_mac_addr(dest_mac), get_mac_addr(src_mac), proto, data[14:]

# def get_mac_addr(bytes_addr):
#     bytes_str = map("{:02x}".format, bytes_addr)
#     return ":".join(bytes_str).upper()

# main()