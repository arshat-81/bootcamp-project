import hashlib

#using hexdigest()
print(hashlib.md5("This is Cybersecurity".encode('utf-8')).hexdigest())
print(hashlib.md5("This is Nothing ".encode('utf-8')).hexdigest())

#using digest()
print(hashlib.md5("This is ShapeAI".encode('utf-8')).digest())
print(hashlib.md5("This is awesome".encode('utf-8')).digest())
