import base64

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
		#print(r1,r2)
		q=r1//r2
		(r1, u1, v1, r2, u2, v2)=(r2, u2, v2, r1-q*r2, u1-q*u2,v1-q*v2)

	#print(r1,u1,v1)
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
	print('N=',N)

E=0x10001

#=====================================

c=b"e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA"
print(c)
c=base64.b64decode(c)
print(c)
c=int.from_bytes(c,'big')

p=398075086424064937397125500550386491199064362342526708406385189575946388957261768583317
q=472772146107435302536223071973048224632914695302097116459852171130520711256363590397527


# phi = (p-1)*(q-1)
phi=(p-1)*(q-1)

print("phi=",phi)

# E*d + k*phi = 1 
r,d,k=extendedEuclide(E,phi)

print("d=",d)

assert(p*q==N)
assert(E*d+k*phi==1)

clear=modPow(c,d,N)
print(clear)
clear-=0
clear=clear.to_bytes(75,'big')
print(clear)
clear=''.join([chr(b) for b in clear])

print(clear)

"""
p*q=N

m**E=c [N]

c**D=m [N]


a**2 [N]
"""

