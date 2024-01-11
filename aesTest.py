from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def cifra_AES(testo_da_cifrare, chiave):
    cipher = AES.new(chiave, AES.MODE_ECB)
    testo_padded = testo_da_cifrare + ((16 - len(testo_da_cifrare) % 16) * ' ')  # Padding per lunghezza multipla di 16
    ciphertext = cipher.encrypt(testo_padded.encode('utf-8'))
    return ciphertext

def decifra_AES(testo_cifrato, chiave):
    cipher = AES.new(chiave, AES.MODE_ECB)
    decrypted = cipher.decrypt(testo_cifrato).rstrip()
    return decrypted.decode('utf-8')

# Chiave AES (128 bit = 16 byte)
chiave = get_random_bytes(16)

# Richiesta del testo da cifrare all'utente
testo_da_cifrare = input("Inserisci il testo da cifrare con AES: ")

# Cifra il testo
testo_cifrato = cifra_AES(testo_da_cifrare, chiave)
print("Testo cifrato:", testo_cifrato)

# Decifra il testo cifrato
testo_decifrato = decifra_AES(testo_cifrato, chiave)
print("Testo decifrato:", testo_decifrato)