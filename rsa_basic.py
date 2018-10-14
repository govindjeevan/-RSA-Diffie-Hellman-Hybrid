import random 
# function to find extended gcd
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

# function to find modular inverse
def inverse(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m


def generateprime():
	count=0
	while count<1:
		p= random.randint(50,500)
		if is_probable_prime(p):
			count+=1
	while count<2:
		q= random.randint(50,500)
		if is_probable_prime(q):
			if q!=p:
				count+=1
	return p,q


_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite


def gcd(a,b):
	while b!=0:
		a,b = b, a%b
	return a


def generatekey(p,q):
	n= p*q
	phi = (p-1)*(q-1)
	g= 10
	while(g!=1):
		e= random.randrange(1,phi)
		g= gcd(e, phi)

	d= inverse(e, phi)

	return ((e,n), (d,n))

def stringtonum(message):
	list=[]
	for i in message:
		list.append(ord(i))
	return list

def encrypt(m,p):
	key, n = p
	return (m**key)%n

def decrypt(m,p):
	key, n = p
	return (m**key)%n

if __name__ == '__main__':
	
	p,q = generateprime()
	print(p,q)
	public, private = generatekey(p,q)
	print("public key:", public, "private key:", private)

	message = input("enter message to be encrypted")
	message= int(message)
	encrypted_message = encrypt(message, private)
	print("encrypted message is :", encrypted_message)
	print("decrytping message")
	decrypted_message= decrypt(encrypted_message, public)
	print ("decrypted message", decrypted_message)
