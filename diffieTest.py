from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Parametri condivisi (pubblici)
p = 23  # Numero primo che funge da modulo
g = 5   # Generatore

# Valori segreti delle due parti
a = 6   # Segreto della prima parte
b = 15  # Segreto della seconda parte

# Calcolo delle chiavi parziali
A = (g ** a) % p
print("chiave parziale A " , A)
B = (g ** b) % p
print("chiave parziale B " , B)
# Calcolo della chiave segreta condivisa
secret_key_A = (B ** a) % p
secret_key_B = (A ** b) % p

# Verifica che entrambe le parti abbiano ottenuto la stessa chiave segreta
assert secret_key_A == secret_key_B

# Utilizzo della chiave segreta condivisa per AES
# Converti la chiave in un formato binario con una lunghezza adatta per AES
key = secret_key_A.to_bytes(16, byteorder='big')[:16]  # Prendiamo i primi 16 byte come chiave per AES
iv = get_random_bytes(16)  # Vettore di inizializzazione casuale

# Input del messaggio da cifrare
message = input("Inserisci il messaggio da cifrare: ").encode()

# Cifra il messaggio con AES
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = cipher.encrypt(pad(message, AES.block_size))

print("Messaggio cifrato:", cipher_text)

# Decifra il messaggio con AES
decipher = AES.new(key, AES.MODE_CBC, iv)
plain_text = unpad(decipher.decrypt(cipher_text), AES.block_size)

print("Messaggio decifrato:", plain_text.decode())
