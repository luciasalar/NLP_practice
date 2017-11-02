import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') 
d = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') 
e = random.choice('!@#$%^&*(') 
f = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') 


def password():
	pa = []
	pa.append(a)
	pa.append(b)
	pa.append(c)
	pa.append(d)
	pa.append(e)
	pa.append(f)
	return ''.join(str(i) for i in pa)

print(password())

