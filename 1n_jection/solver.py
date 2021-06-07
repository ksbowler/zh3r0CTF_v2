import gmpy2

def inv_nk2n(enc,dep):
	if enc < 128:
		print(chr(enc))
		return
	e,_ = gmpy2.iroot(2*enc,2) #e = i+jになっていたらいいな
	e = int(e)
	#print("enc,e")
	#print(enc,e)
	
	while True:
		j = (2*enc-(e*(e+1)))//2
		if j < 0:
			e -= 1
			continue
		e1,_ = gmpy2.iroot(2*enc-2*j,2) #e1 = i+jのはず。e=e1ならちゃんと求められている
		if e == e1:
			i = e-j
			assert ((i+j)*(i+j+1))//2 +j == enc
			break
		e -= 1
	#print("depth:",dep)
	#print("i =",i)
	#print("j =",j)
	if i < 128:
		print(chr(i),end="")
		print(chr(j),end="")
		return
	elif j < 128:
		#print(chr(j),end="")
		inv_nk2n(i,dep+1)
		print(chr(j),end="")		
	else:
		inv_nk2n(i,dep+1)
		inv_nk2n(j,dep+1)
	"""
	print(e)
	print(e1)
	i = e-j
	print(i)
	print(j)
	print(((i+j)*(i+j+1))//2 +j == enc)
	"""

enc = 2597749519984520018193538914972744028780767067373210633843441892910830749749277631182596420937027368405416666234869030284255514216592219508067528406889067888675964979055810441575553504341722797908073355991646423732420612775191216409926513346494355434293682149298585
inv_nk2n(enc,0)
print()


