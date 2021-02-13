import hashlib

# hash = hashlib.sha256()
# hash.update(b'test1234')
# hashed_password = hash.hexdigest()
# print(hashed_password)

# hash = hashlib.sha256()
# hash.update(b'test1234')
# hashed_password = hash.hexdigest()
# print(hashed_password)

# hash = hashlib.sha256()
# hash.update('test1234'.encode())
# hashed_password = hash.hexdigest()
# print(hashed_password)

# hash = hashlib.sha256()
# hash.update('test1234'.encode('utf8'))
# hashed_password = hash.hexdigest()
# print(hashed_password)

import bcrypt

real_pwd = bcrypt.hashpw(b'test1234', bcrypt.gensalt())

test_pwd = 'test1234'
is_correct = bcrypt.checkpw(test_pwd.encode('utf8'), real_pwd)
print(is_correct)