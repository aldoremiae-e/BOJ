from hashlib import sha256
s = input()

print(sha256(s.encode()).hexdigest())