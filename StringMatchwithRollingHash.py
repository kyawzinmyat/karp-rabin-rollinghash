
#abcdefb

#fb 

#size =2
#hash(abc)=hash(a)+hash(b)+hash(c)

#hash(bcd)= (hash(abc)-a*base^size)*base + hash(d)


class KarpRabinStringMatch:
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
			self.magic*= self.base%self.prime
		self._hash=self._hash%self.prime
		
	
	def rolling_hash(self):
		for i in range(len(self.text),len(self.paragraph)):
			old = ord(self.paragraph[i-len(self.text)])%self.prime## constant ?
			new = ord(self.paragraph[i])%self.prime
			self._hash = (self._hash-old*self.magic)%23#self._hash,old,self.magic<self.prime 
			self._hash = ((self._hash*self.base%self.prime)%self.prime+new)%self.prime
			self.check_substring(i)
		return self.answer
			
	def check_substring(self,index):
		#print(self.paragraph[index+1-len(self.text):index+1])
		if self.paragraph[index+1-len(self.text):index+1] == self.text:
			self.answer.append((index+1-len(self.text),index+1))
		
	def match(self):
		if self.paragraph[:len(self.text)]==self.text:
			self.answer.append((0,len(self.text)))
		return self.rolling_hash()
		
		
		
		
	
			




