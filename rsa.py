from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generazione delle chiavi
key = RSA.generate(2048)  # 2048 bit per una maggiore sicurezza

# Ottieni la chiave pubblica e privata
public_key = key.publickey().export_key()
private_key = key.export_key()

print("Chiave pubblica:")
print(public_key.decode())

print("\nChiave privata:")
print(private_key.decode())

# Input del messaggio da cifrare
message = input("\nInserisci il messaggio da cifrare con RSA di Bob: ").encode()

# Cifra il messaggio con la chiave pubblica
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
encrypted_message = cipher.encrypt(message)

print("\nMessaggio cifrato con la chiave pubblica di Alice:", binascii.hexlify(encrypted_message))

# Decifra il messaggio con la chiave privata
cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted_message = cipher.decrypt(encrypted_message)

print("Messaggio decifrato con la chiave privata di Alice:", decrypted_message.decode())
