
def readfile(filename):
	data = []
	with open (filename,'r',encoding ='utf-8-sig') as f:
		for line in f:
			data.append(line.strip())
	return data

def convert(datas):
	new_data=[]
	person = None
	for d in datas:
		if d == 'Allen':
			person = 'Allen'
			continue
		elif d == 'Tom':
			person = 'Tom'
			continue
		if person:
			new_data.append(person+': '+d+'\n')
	return new_data

def writefile(filename,datas):
	with open (filename,'w',encoding ='utf-8-sig') as f:
		for d in datas:
			f.write(d)
				
def main():
	data = readfile('input.txt')
	data = convert(data)
	writefile('output_me.txt',data)


main()