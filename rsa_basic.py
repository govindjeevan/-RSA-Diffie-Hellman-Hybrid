import random 

def gcd(a,b):
	while b!=0:
		a,b = b, a%b
	return a

def inverse(e, phi):
	m1=phi
	y=0
	x=1
	while (e>1):
		q = e/phi
		t= phi
		phi, e = e%phi, t
		t=y
		y= x- q*y
		x=t
	if(x<0):
		x=x+ m1
	return int(x)

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
	p= input('Enter prime number p')
	q= input('Enter another prime number q not equal to p')
	p= int(p)
	q= int(q)

	public, private = generatekey(p,q);
	print("public key:", public, "private key:", private)

	message = input("enter message to be encrypted")
	message= int(message)
	encrypted_message = encrypt(message, private)
	print("encrypted message is :", encrypted_message)
	print("decrytping message")
	decrypted_message= decrypt(encrypted_message, public)
	print ("decrypted message", decrypted_message)
