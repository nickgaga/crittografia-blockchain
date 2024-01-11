def cifrario_di_cesare(testo, chiave):
    risultato = ""

    for carattere in testo:
        if carattere.isalpha():
            # Controllo se il carattere è una lettera e applico lo spostamento
            if carattere.islower():
                risultato += chr(((ord(carattere) - 97 + chiave) % 26) + 97)
            else:
                risultato += chr(((ord(carattere) - 65 + chiave) % 26) + 65)
        else:
            # Mantengo i caratteri non alfabetici
            risultato += carattere

    return risultato

# Richiesta del testo da cifrare e della chiave di cifratura all'utente
testo_da_cifrare = input("Inserisci il testo da cifrare: ")
chiave_di_cifratura = int(input("Inserisci la chiave di cifratura (numero intero): "))

# Cifratura del testo inserito
testo_cifrato = cifrario_di_cesare(testo_da_cifrare, chiave_di_cifratura)
print("Testo cifrato:", testo_cifrato)

# Decifratura del testo cifrato
testo_decifrato = cifrario_di_cesare(testo_cifrato, -chiave_di_cifratura)
print("Testo decifrato:", testo_decifrato)
