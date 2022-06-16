import base64

message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

# import base64
# import hashlib


# def encriptar_cuerpo(body):
#     body_message= bytes(body)
#     md = hashlib.md5(body_message)
#     md.update()
#     print(md.digest())
    

# import hashlib
# import time
# # md5_hash = hashlib.md5()
# # md5_hash.update(b'Hello World')
# mensaje = '1235245'
# aux=bytes(mensaje, 'ascii')
# print(aux)
