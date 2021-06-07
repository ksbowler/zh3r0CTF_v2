from Crypto.Util.number import *
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib
from tqdm import tqdm

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

	
#HOSTはIPアドレスでも可
HOST, PORT = "crypto.zh3r0.cf", 1111
s, f = sock(HOST, PORT)
for _ in range(10): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
a1 = "68656c6c6f20776f726c6421204c6574732067657420676f696e67"
s.send(a1.encode()+b"\n")
print(read_until(f))
for _ in range(4): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
a2 = "4e6f7468696e672066616e63792c206a757374207374616e646172642062797465735f746f5f696e74"
s.send(a2.encode()+b"\n")
print(read_until(f))
recv_m = read_until(f).split()

enc3 = recv_m[-1]
print(enc3)

tmp = "0123456789abcdef"
"""
table = ["" for _ in range(256)]
for h1 in tmp:
	for h2 in tmp:
		for _ in range(3): read_until(f)
		read_until(f,">>> ")
		s.send(b"1\n")
		read_until(f,"message in hex:")
		s.send((h1+h2).encode()+b"\n")
		e3 = read_until(f).strip()
		#print(e3)
		table[int(e3,16)] = h1+h2
a3 = ""
for i in range(0,len(enc3),2):
	a3 += table[int(enc3[i:i+2],16)]
print(a3)
"""
a3 = "6d6f6e6f20737562737469747574696f6e73206172656e742074686174206372656174697665"
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
s.send(a3.encode()+b"\n")
print(read_until(f))
#print(read_until(f))
recv_m = read_until(f).split()
"""
enc4 = recv_m[-1]
print(enc4)
a4 = ""
for i in range(0,len(enc4),2):
	ch = False
	cnt = 0
	for h1 in tmp:
		for h2 in tmp:
			cnt += 1
			if cnt%50 == 0: print(cnt)
			for _ in range(3): read_until(f)
			read_until(f,">>> ")
			s.send(b"1\n")
			read_until(f,"message in hex:")
			s.send((a4+h1+h2).encode()+b"\n")
			e4 = read_until(f).strip()
			if enc4[:len(e4)] == e4:
				print(e4)
				ch = True
				a4 += h1 + h2
				break
		if ch: break

print("a4:",a4)
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
s.send(a4.encode()+b"\n")
while True:print(read_until(f))
"""
a4 = "6372656174696e6720646966666572656e7420737562737469747574696f6e7320666f7220656163682063686172"
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
s.send(a4.encode()+b"\n")
print(read_until(f))
#print(read_until(f))
recv_m = read_until(f).split()
enc5 = recv_m[-1]
"""
E5 = []
for i in range(0,len(enc5),4): E5.append(enc5[i:i+4])
ch5 = [False for _ in range(len(E5))]
val = [[] for _ in range(256)]
tmp1 = "2673"
pot = 0
isFin = False
print("enc5:",enc5)
A5 = []
a5 = '476c616420xy6861xyxy796f752066696775726564206fxy742074686520696e7661xyxyxy6e74'
for i in range(0,len(a5),2):
	A5.append(a5[i:i+2])
	if a5[i:i+2] != "xy": ch5[i//2] = True

while True:
	for h1 in tmp1:
		for h2 in tmp:
			print(h1+h2)
			if h1 == "2":
				if h2 in ["2","3","4","5","6","7","8","9","a","b","d","e","f"]: continue
			elif h1 == "4":
				if h2 == "0": continue
			for i in tqdm(range(100)):
				for _ in range(3): read_until(f)
				read_until(f,">>> ")
				s.send(b"1\n")
				read_until(f,"message in hex:")
				s.send((h1+h2).encode()+b"\n")
				e5 = read_until(f).strip()
				val[int(h1+h2,16)].append(e5)
				if e5 in E5:
					print(e5)
					for j in range(len(E5)):
						if E5[j] == e5:
							A5[j] = h1+h2
							ch5[j] = True
							break
				
	for i in range(pot,len(ch5)):
		if i == len(ch5)-1:
			if ch5[i]:
				isFin = True
				break
			else:
				pot = i
				break
		else:
			if ch5[i] == False:
				pot = i
				break
	print("complete index:",pot)
	print("".join(A5))
	bun = ""
	for i in range(len(A5)):
		if A5[i] == "xy": bun += "?"
		else: bun += chr(int(A5[i],16))
	print(bun)
	if isFin:
		break

a5 = "".join(A5)
"""
"""
for i in range(0,len(enc5),4):
	x = enc5[i:i+4]
	print("i:",i)
	ans = ""
	cou = 0
	for j in range(256):
		if x in val[j]:
			print("find!")
			ans = hex(j)[2:]
			cou += 1
	print("count :",cou)
	if cou == 1:
		a5 += ans
	elif cou == 0:
		a5 += "xy"
"""

#print("a5:",a5)
a5 = "476c6164207468617420796f752066696775726564206f75742074686520696e76617269616e74"
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
s.send(a5.encode()+b"\n")
print(read_until(f))
recv_m = read_until(f).split()
enc6 = recv_m[-1]
print("enc6:",enc6)
E6 = []
for i in range(0,len(enc6),10): E6.append(enc6[i:i+10])
a6 = ""
for i in range(len(E6)-1):
	t = hex(int(E6[i],16)^int(E6[-1],16))[2:]
	while len(t) < 10: t = "0"+t
	a6 += t
#print("a6:",a6)
a6 = a6[:-6]
print("a6:",a6)
print(long_to_bytes(int(a6,16)))
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
s.send(a6.encode()+b"\n")
print(read_until(f))
"""
tmp1 = "267"
#for i in tqdm(range(1000)):
#for _ in range(3): read_until(f)
#read_until(f,">>> ")
#s.send(b"1\n")
#read_until(f,"message in hex:")
#tmp1 = "267"
ch6 = [False for _ in range(len(E6))]
pot = 0
isFin = False
A6 = ["xy" for _ in range(len(ch6))]
a6 = "xy"*len(ch6)
while True:
	for h1 in tmp1:
		for h2 in tmp:
			print(h1+h2)
			if h1 == "2":
				#if if h2 in ["2","3","4","5","6","7","8","9","a","b","d","e","f"]: continue
				if h2 != "0": continue
			for i in tqdm(range(100)):
				for _ in range(3): read_until(f)
				read_until(f,">>> ")
				s.send(b"1\n")
				read_until(f,"message in hex:")
				s.send(((h1+h2)*5).encode()+b"\n")
				e6 = read_until(f).strip()
				ee6 = [e6[i:i+4] for i in range(0,len(e6),4)]
				for str6 in ee6:
					for j in range(len(E6)):
						if E6[j] == str6:
							A6[j] = h1+h2
							ch6[j] = True
							print(str6)

	for i in range(pot,len(ch6)):
		if i == len(ch6)-1:
			if ch6[i]:
				isFin = True
				break
			else:
				pot = i
				break
		else:
			if ch6[i] == False:
				pot = i
				break
	print("complete index:",pot)
	print("".join(A6))
	bun = ""
	for i in range(len(A6)):
		if A6[i] == "xy": bun += "?"
		else: bun += chr(int(A6[i],16))
	print(bun)

	if isFin: break
"""	
"""
f1 = []
f2 = []
f3 = []
f4 = []
rem = []
#20だけ何回も送ってみる
for i in tqdm(range(1000)):
	for _ in range(3): read_until(f)
	read_until(f,">>> ")
	s.send(b"1\n")
	read_until(f,"message in hex:")
	s.send(b"20616263\n")
	e6 = read_until(f).strip()
	#for j in range(len(first)):
	if e6[:4] in f1:
		print("find! f1 in f1")
		print(e6[:4])
	if e6[:4] in f2 or e6[:4] in f3 or e6[:4] in f4:
		print("find! f1 in other")
		print(e6[:4])
	if e6[:4] in rem:
		print("find! f1 in rem")
		print(e6[:4])

	if e6[4:8] in f2:
		print("find! f2 in f2")
		print(e6[4:8])
	if e6[4:8] in f1 or e6[4:8] in f3 or e6[4:8] in f4:
		print("find! f2 in other")
		print(e6[4:8])
	if e6[4:8] in rem:
		print("find! f2 in rem")
		print(e6[4:8])

	if e6[8:12] in f3:
		print("find! f3 in f3")
		print(e6[8:12])
	if e6[8:12] in f1 or e6[8:12] in f2 or e6[8:12] in f4:
		print("find! f3 in other")
		print(e6[8:12])
	if e6[8:12] in rem:
		print("find! f3 in rem")
		print(e6[8:12])

	if e6[12:16] in f4:
		print("find! f4 in f4")
		print(e6[12:16])
	if e6[12:16] in f1 or e6[12:16] in f2 or e6[12:16] in f3:
		print("find! f4 in other")
		print(e6[12:16])
	if e6[12:16] in rem:
		print("find! f4 in rem")
		print(e6[12:16])

	if e6[16:20] in rem:
		print("find! rem in rem")
		print(e6[16:20])
	if e6[16:20] in f1 or e6[16:20] in f2 or e6[16:20] in f3 or e6[16:20] in f4:
		print("rem in f?")
		print(e6[16:20])

	f1.append(e6[:4])
	f2.append(e6[4:8])
	f3.append(e6[8:12])
	f4.append(e6[12:16])
	rem.append(e6[16:20])
	#for j in range(4,len(e6),4): rem.append(e6[j:j+4])

	for i in range(0,len(e6),4):
		if e6[i:i+4] in E6:
			print(f"find! f{(i//4)+1} in enc6")
			print(e6[i:i+4])
	
	for j in range(4,len(e6),4):
		if e6[j:j+4] in E6:
			print("find! rem in enc6")
			print(e6[j:j+4])
"""
import gmpy2
ans = "ffffffffff"
recv_m = read_until(f).split()
enc7 = recv_m[-1]
print("enc7:",enc7)
"""
while True:
	for _ in range(3): read_until(f)
	read_until(f,">>> ")
	s.send(b"1\n")
	read_until(f,"message in hex:")
	s.send(ans.encode()+b"\n")
	e7 = read_until(f).strip()
	m,ch = gmpy2.iroot(int(e7),3)
	if ch:
		ans += "ff"
		print(ans)
	else:
		ans = ans[:-2]
		moo = False
		for h1 in tmp:
			for h2 in tmp:
				print(h1+h2)
				for _ in range(3): read_until(f)
				read_until(f,">>> ")
				s.send(b"1\n")
				read_until(f,"message in hex:")
				s.send((ans+h1+h2).encode()+b"\n")
				e7 = read_until(f).strip()
				x = int(ans+h1+h2,16)
				#m,ch = gmpy2.iroot(int(e7),3)
				if pow(x,3) != int(e7):
					print("x:",x)
					print("e7:",e7)
					print("x3:",pow(x,3))
					#n2 = pow(x,3)
					#print("different")
					n = pow(x,3)-int(e7)
					print("n =",n)
					moo = True
					break
			if moo: break
		break
n = int(input("n = "))
temp_n = input("factor n:")
pp = temp_n.split(",")
phi = 1
bef=0
for k in pp:
	if bef == k: phi *= int(k)
	else: phi *= int(k)-1
	bef = int(k)

c = int(enc7)
d = inverse(3,phi)
m = pow(c,d,n)
print("mes")
print(long_to_bytes(m))
a7 = hex(m)[2:]
"""
a7 = "43756265206d6f64756c6f207072696d652c20616e7920677565737365732077686174206d6967687420626520636f6d696e67206e6578743f"
print("a7 =",a7)
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
s.send(a7.encode()+b"\n")
print(read_until(f))
ans = "ff"*2
ans2 = "fe"*2
recv_m = read_until(f).split()
enc8 = recv_m[-1]
print("enc8:",enc8)
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"1\n")
read_until(f,"message in hex:")
s.send(b"02\n")
e8 = read_until(f).strip()
e8 = bin(int(e8))[2:]
e = len(e8) - 1
print("e =",e)

for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"1\n")
read_until(f,"message in hex:")
s.send(ans.encode()+b"\n")
e8 = read_until(f).strip()
assert pow(int(ans,16),e) > int(e8)
n1 = pow(int(ans,16),e) - int(e8)
for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"1\n")
read_until(f,"message in hex:")
s.send(ans2.encode()+b"\n")
e8 = read_until(f).strip()
assert pow(int(ans2,16),e) > int(e8)
n2 = pow(int(ans2,16),e) - int(e8)
import math
print("n =",math.gcd(n1,n2))
p = int(input("prime p:"))
#q = int(input("prime q:"))
#phi = (p-1)*(q-1)
d = inverse(e,p-1)
m = pow(int(enc8),d,p)
print(long_to_bytes(m))
a8 = hex(m)[2:]
print("a8:",a8)

for _ in range(3): read_until(f)
read_until(f,">>> ")
s.send(b"2\n")
read_until(f,"flag in hex:")
s.send(a8.encode()+b"\n")
while True: print(read_until(f))


#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

