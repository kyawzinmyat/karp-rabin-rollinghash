
#abcdefb

#fb 

#size =2
#hash(abc)=hash(a)+hash(b)+hash(c)

#hash(bcd)= (hash(abc)-a*base^size)*base + hash(d)


class KarpRabin:
	def __init__(self,text,paragraph):
		self.text=text
		self.paragraph = paragraph
		self.magic = 1
		self._hash=0
		self.prime=101
		self.base =256
		self.answer=[]
		self.precalculate()
	
	def precalculate(self):
		for i in range(len(self.text)):
			self._hash += ord(self.paragraph[len(self.text)-1-i])*(self.base**i)
			self.magic*= self.base
		self._hash=self._hash%self.prime
		self.magic = self.magic%23
	
	def rolling_hash(self):
		for i in range(len(self.text),len(self.paragraph)):
			old = ord(self.paragraph[i-len(self.text)])## constant ?
			new = ord(self.paragraph[i])
			self._hash = (self._hash-old*self.magic)%23#self._hash,old,self.magic<self.prime 
			self._hash = ((self._hash*self.base)+new)%23
			self.check_substring(i)
			
	def check_substring(self,index):
		#print(self.paragraph[index+1-len(self.text):index+1])
		if self.paragraph[index+1-len(self.text):index+1] == self.text:
			self.answer.append(index+1-len(self.text))
		
	def match(self):
		if self.paragraph[:len(self.text)]==self.text:
			self.answer.append(0)
		self.rolling_hash()
		
		
		
		
	
			




paragraph="1234"
text ="1234"
kr= KarpRabin(text,paragraph)
print(kr._hash)
#kr.match()
#kr.rolling_hash()
##print(kr.pre_)
#print(kr._hash)
#print(kr.magic)
		
#print(kr.answer)

		
#print(pow(10,23-2,23))	