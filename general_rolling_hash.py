class RollingHash:
	def __init__(self,docs,pattern):
		self.docs = docs
		self.pattern = pattern
		self.hash=0
		self.magic = 1
		self.base = 256
		self.prime = 257
		self.hash_of_pattern =0
		self.calculate_hash_of_pattern()
		self.answer=[]
		self.mul_inverse_mod= pow(self.base,self.prime-2,self.prime)
		
	def append(self,new):
		self.hash = (self.hash*self.base+new)%self.prime
		self.magic = (self.magic*self.base)%self.prime
		
	def calculate_hash_of_pattern(self):
		if self.hash_of_pattern==0:
			for i in range(len(self.pattern)):
				self.hash_of_pattern=(self.hash_of_pattern*self.base+ord(self.pattern[i]))%self.prime
			
		
	def pop(self,old):
		self.magic = (self.magic*self.mul_inverse_mod)%self.prime
		self.hash = (self.hash-old*self.magic)%self.prime
		
		
		
	def change_base(self,new_base):
		self.base = base
		
	def roll(self):
		self.precalculate()
		if self.hash == self.hash_of_pattern:
			self.answer.append((0,len(self.pattern)))
		self.slide_window()
		return self.answer
	
		
	# pop by 1 append by 1
	def slide_window(self):
		for i in range(len(self.pattern),len(self.docs)):
				self.pop(ord(self.docs[i-len(self.pattern)]))
				self.append(ord(self.docs[i]))	
				if self.hash==self.hash_of_pattern:						
					if self.check_substring(i):
						self.answer.append((i+1-len(self.pattern),i+1))## is work like python range (x,y) include x but not y
	
	def check_substring(self,index):
			return self.pattern == self.docs[index+1-len(self.pattern):index+1]
			
	# if you match substring of 	
	def slide_right(self):
		for i in range(0,len(self.docs)):
			if self.hash != self.hash_of_pattern:
				self.append(ord(self.docs[i]))
			else:
				return (0,i)
	# calculate the first n length of pattern of docs
	## eg pattern 123
	## calculate 	from 0 to 3 of docs
	
		
				
	def precalculate(self):
		for i in range(len(self.pattern)):
			self.append(ord(self.docs[i]))
			
docs ="abc esf ghj kjd kdbdkd djdkd  dkbd dk kdjdb kdbd "
pattern ="kdjdb"

rh = RollingHash(docs,pattern)
#print(rh.roll())
		
		
			
		
		
		