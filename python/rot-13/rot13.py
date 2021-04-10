source = "enjoytocode"
abc = "abcdefghijklmnopqrstuvwxyz"

def encode(src):
 return "".join([abc[(abc.find(c)+13)%26] for c in src])

def decode(dest):
 return "".join([abc[(abc.find(c)-13)%26] for c in dest])

encrypted_str = encode(source) 
print(encrypted_str)
# to decrypt
decrypted_str = decode(encrypted_str)
print(decrypted_str)
# or use encode again 
print(encode(encrypted_str))

