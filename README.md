# Packet decoding

This is a simple data packet decoder. If you have a bytestring and pass it into unpack_data, it will unpack the data.

The idea is rather simple. Since we already know the length of each individual sections of the header, we can do a simple slice on the data packet and read the information as the given type. For example, the device is a unsigned 8 bit integer. So we can just chop off 2 bytes off the bytestring and interpret the 2 bytes as an integer. After decoding the header, we can then just take the rest and we will know that its the payload.