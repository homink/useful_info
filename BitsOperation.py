# bit operation for dec2bin and bin2dec 

def dec2bin(x):
	if x == 0:
		return "0"
	y=[]
	while x>0:
		q = x / 2
		r = x % 2
		#print("input:%d, quotient:%d, remainder:%d" % (x, q, r))
		y.append(str(r));
		x = q
		
	y.reverse()
	y = "".join(y)
	return y

def bin2dec(x):
	digit_cn = 0; dec_sum = 0
	x = list(x)
	x.reverse()
	for b in x:
		dec_sum = dec_sum + 2 ** digit_cn * int(b)
		digit_cn += 1

	return dec_sum


bin_numbers=[]
for i in range(18):
	print("%d - %s" % (i,dec2bin(i)))
	bin_numbers.append(dec2bin(i))

for b in bin_numbers:
	print("%s - %d" % (b,bin2dec(b)))
