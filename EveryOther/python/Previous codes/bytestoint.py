print(int.from_bytes(b'\x00\x01', "big")) 
print(int.from_bytes(b'\x00\x01', "little"))
print(int.from_bytes(b'\x00\x10', byteorder='little'))  
print(int.from_bytes(b'\xfc\x00', byteorder='big',signed=True))