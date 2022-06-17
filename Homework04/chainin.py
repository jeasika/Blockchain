#############################
# By: Jeasika López
#       A00821863
# Programa que construye una cadena de bloques
#############################

from hashlib import sha256, sha1
from time import time, gmtime, localtime
from numpy import block

class Block:
    #Constructor
	def __init__(self, prev_hash:str, txn:str, timestamp=gmtime()) -> None:
		self.prev_hash = prev_hash
		self.txn = txn
		self.timestamp = '-'.join(list(map(str, [timestamp.tm_year, timestamp.tm_mon, timestamp.tm_mday])))+ ' ' + ':'.join(list(map(str, [timestamp.tm_hour, timestamp.tm_min, timestamp.tm_sec])))
		self.block_data = str(txn) + '-' + prev_hash
		self.block_hash = sha1(self.block_data.encode()).hexdigest()

class Chain:
    #Constructor
	def __init__(self) -> None:
		self.chain = []
		self.generate_genesis()

	#Crea el bloque Genesis
	def generate_genesis(self):
		self.chain.append(Block(input(), 0))

    #"Apunta" al siguiente bloque
	def next_block(self, txn):
		prev_hash = self.last_block().block_hash
		self.txn = txn
		self.chain.append(Block(prev_hash, self.txn))
	
    #Devuelve el bloque anterior
	def last_block(self):
		return self.chain[-1]	

    #Retorna el tamaño de la cadena
	def size_of_chain(self) -> int:
		return len(self.chain)

    #Imprime la cadena de blique
	def display(self):
		for ele in self.chain:
			print(ele.block_data, ele.block_hash, ele.timestamp)

############################
# Aquí inicia el main()
############################
test_block = Chain()
for i in range(1, 4):
	test_block.next_block(i)
    
test_block.display()
print("size of Blockchain - {test_block.size_of_chain()}")