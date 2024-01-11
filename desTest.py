from Crypto.Cipher import DES

# Chiave DES (8 byte)

key = b'Chiave88'  # Assicurati che la chiave sia esattamente di 8 byte
# Chiave predefinita

# Richiesta del dato da crittografare
data = input("Inserisci il dato da crittografare: ").encode('utf-8')

# Padding per garantire che il dato sia multiplo di 8 byte
if len(data) % 8 != 0:
    data += b' ' * (8 - len(data) % 8)

# Inizializzazione del cifrario DES con la chiave
cipher = DES.new(key, DES.MODE_ECB)

# Cifratura del dato
ciphertext = cipher.encrypt(data)
print("Dato Cifrato:", ciphertext)

# Decifratura del dato cifrato
decrypted = cipher.decrypt(ciphertext)
print("Dato Decifrato:", decrypted.rstrip().decode('utf-8'))  # Decodifica il dato decifrato in stringa
