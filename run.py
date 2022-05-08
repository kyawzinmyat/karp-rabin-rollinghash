from text import *
import time
from general_rolling_hash import RollingHash
from StringMatchwithRollingHash import KarpRabinStringMatch





def test_rolling_hash(docs,pattern):
	start = time.time()
	rh = RollingHash(docs,pattern)	
	print(rh.roll())
	end = time.time()
	print("Total time ",end-start)
	#cap_index(docs,rh.roll())

	

				
def test_karprabin_string_match(docs,pattern):	
	
	start = time.time()
	kr= KarpRabinStringMatch(pattern,docs)
	print(len(kr.match()))
#	print("count",len(kr.match()))
	end = time.time()
	print("Karp rabin- ",end-start)
	print(kr.answer)
	
	#cap_index(docs,kr.match())
	
	
	

def cap_index(docs,index_list):
	answer = list(docs)
	for index_pair in index_list:
		for index in range(index_pair[0],index_pair[1]):
			answer[index]=answer[index].upper()
	answer = "".join(answer)
	print(answer)
	

def test_count(docs,pattern):
	
	start = time.time()
	print(docs.count(pattern))
	end = time.time()
	print("python count - ",end-start)	
		
			
					
	
if __name__ =="__main__":
	test_rolling_hash(docs,pattern)	
	test_karprabin_string_match(docs,pattern)
	
	test_count(docs,pattern)

