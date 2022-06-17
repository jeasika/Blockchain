#############################
# By: Jeasika López
#       A00821863
# Bloque con estructura similar a los bloques de Bitcoin y 
# generar un hash en SHA-256
#############################

import hashlib

#Definicion de la clase Block
class Block():
   def __init__(self, height, timestamp, tx, nonce, prev_blockhash): 
      self.height = height
      self.timestamp = timestamp
      self.tx = tx
      self.nonce = nonce
      self.prev_blockchash = prev_blockhash
      self.curr_blockhash = ''
      pass
   
   #Método que genera un hash criptográfico 
   def hash_block(self): 
      #Crea un objeto SHA-256.
      m = hashlib.sha256()
      
      all = (str(self.height) + self.timestamp + self.tx + str(self.nonce) + self.prev_blockchash)
      all = all.encode()

      m.update(all)

      #Variable en la que se guarda el HASH
      self.curr_blockhash = m.hexdigest()
      return self.curr_blockhash

############################
# Aquí inicia el main()
############################
height = 0
timestamp = '2021-02-25 11:59:59.134365'
tx = 'Alice, Bob, 10'
nonce = 0
# Hash de bytes(0) utilizando SHA-256
prev_blockhash = '3af366504b556c3802248387ee16eb51ffee5ba52906bae95f0eff7ea454218e'
hash = "25ce50cbc8594188fc14aeec1a64699d9e4bf942695a72c4c984d84ca7dca2e2"
block = Block(height, timestamp, tx, nonce, prev_blockhash)
print(block.hash_block())