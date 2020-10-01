import sys
import numpy

import math

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

#	print(r1,u1,v1)
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
	while r2!=0 and len(res)<1000:
		q=r1//r2
		res.append(q)
		#print(r1,r2,q)
		(r1, u1, v1, r2, u2, v2)=(r2, u2, v2, r1-q*r2, u1-q*u2,v1-q*v2)

	assert(u1*a+v1*b==r1)
	return(res)

def root(N,sqrt): # find M s.t. M**3=N
	minM=1
	l=len(str(N))
	maxM=int('1'+'0'*(l))
	while True:
		M=(maxM+minM)//2
		#print(minM)
		if M**sqrt>N:
			maxM=M
		elif M**sqrt<=N:
			minM=M
		if maxM-minM==1:
			if maxM==int('1'+'0'*l):
				print("Error")
			else:
				return minM


sys.setrecursionlimit(5000)


E=0xf70b3bd74801a25eccbde24e01b077677e298391d4197b099a6f961244f04314da7de144dd69a8aa84686bf4ddbd14a6344bbc315218dbbaf29490a44e42e5c4a2a4e76b8101a5ca82351c07b4cfd4e08038c8d5573a827b227bce515b70866724718ec2ac03359614cdf43dd88f1ac7ee453917975a13c019e620e531207692224009c75eaef11e130f8e54cce31e86c84e9366219ae5c250853be145ea87dcf37aa7ece0a994195885e31ebcd8fe742df1cd1370c95b6684ab6c37e84762193c27dd34c3cf3f5e69957b8338f9143a0052c9381d9e2ecb9ef504c954b453f57632705ed44b28a4b5cbe61368e485da6af2dfc901e45868cdd5006913f338a3

N=0x0207a7df9d173f5969ad16dc318496b36be39fe581207e6ea318d3bfbe22c8b485600ba9811a78decc6d5aab79a1c2c491eb6d4f39820657b6686391b85474172ae504f48f02f7ee3a2ab31fce1cf9c22f40e919965c7f67a8acbfa11ee4e7e2f3217bc9a054587500424d0806c0e759081651f6e406a9a642de6e8e131cb644a12e46573bd8246dc5e067d2a4f176fef6eec445bfa9db888a35257376e67109faabe39b0cf8afe2ca123da8314d09f2404922fc4116d682a4bdaeecb73f59c49db7fa12a7fc5c981454925c94e0b5472e02d924dad62c260066e07c7d3b1089d5475c2c066b7f94553c75e856e3a2a773c6c24d5ba64055eb8fea3e57b06b04a3

# ======== WEINER's ATTACK =======

# ---- compute continued fraction expansion
#N=7978886869909
#E=3594320245477

t=int.from_bytes(b'test123456','big')
c=modPow(t,E,N)

continuedExpansionList=continuedFractionExpansion(E,N)
#print(continuedExpansionList)

# ---- compute convergents denominators 

qOld=continuedExpansionList[1]
qveryOld=1
pOld=continuedExpansionList[0]*continuedExpansionList[1]+1
pveryOld=continuedExpansionList[0]

dList=[qveryOld,qOld]
kList=[pveryOld,pOld]

for i in range(2,len(continuedExpansionList)):
	p = continuedExpansionList[i] * kList[i-1] + kList[i-2] 
	q = continuedExpansionList[i] * dList[i-1] + dList[i-2]

	# ========== Verheul Van Tilborg test ==========

	#if (p/q-E/N) > 2.122*E/(N**(3/2)):	
	#	print("Here WTF")
	#	assert(0)


	# ==============================================

	kList.append(p)
	dList.append(q)

# ----  test all d in the list

for d,k in zip(dList,kList):
	res=modPow(c,d,N).to_bytes(1000,'big')
	res=''.join([chr(b) for b in res if b!=0])
	if res=='test123456':
		print("WIN")
		#print(d,k)
		#print(res)
		break
	 
print("d=",d,"\nk=",k)
a,b=k,d
phi=(b*E-1)//a

print("phi=",phi)

a1=(N-phi+1)//2

a2=a1*a1-N
a2=root(a2,2)

p=a1-a2
q=a1+a2

print("p=",p)
print("q=",q)

# q * x + k * p = 1

r,k,x=extendedEuclide(p,q)

x=x+p

print("inv_q=",x)


"""
p*q=N

m**E=c [N]

c**D=m [N]


a**2 [N]

"""

