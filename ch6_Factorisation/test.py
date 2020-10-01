def modPow(m,e,N): # for message, exponent, modulus
	if e==0:
		return 1
	elif e%2==0:
		return (modPow(m,e//2,N)**2)%N
	else:
		return (modPow(m,e-1,N)*m)%N

def extendedEuclide(a,b):
	r1=a
	r2=b
	u1=1
	v1=0
	u2=0
	v2=1
	while r2!=0:
		print(r1,r2)
		q=r1//r2
		(r1, u1, v1, r2, u2, v2)=(r2, u2, v2, r1-q*r2, u1-q*u2,v1-q*v2)

	print(r1,u1,v1)
	assert(u1*a+v1*b==1)
	return r1,u1,v1

def continuedFractionExpansion(a,b):
	r1=a
	r2=b
	u1=1
	v1=0
	u2=0
	v2=1
	res=[]
	while r2!=0 or len(res)>1000:
		q=r1//r2
		res.append(q)
		print(r1,r2,q)
		(r1, u1, v1, r2, u2, v2)=(r2, u2, v2, r1-q*r2, u1-q*u2,v1-q*v2)

	assert(u1*a+v1*b==1)
	return(res)

with open('modulus','r') as f:
	a=f.read()
	N=int(a[8:],16)

E=0x10001

#=====================================

with open('encrypted','rb') as f:
	c=int.from_bytes(f.read(),'big')


t=int.from_bytes(b'test','big')
int_c=modPow(t,E,N)

# ----  test all d in the list

#for d in dList:
for i in range(1000000):
	int_c=modPow(int_c,E,N)
	b_c=int_c.to_bytes(256,'big')
	c=''.join([chr(b) for b in b_c if b!=0])
	if c=='test':
		print("WIN")
		break
	 

"""
p*q=N

m**E=c [N]

c**D=m [N]


a**2 [N]

"""

