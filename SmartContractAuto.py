class ContrattoAuto:
    def __init__(self):
        self.proprietario = None
        self.info_auto = {}

    def imposta_proprietario(self, proprietario):
        self.proprietario = proprietario

    def aggiorna_chilometri(self, indirizzo_auto, chilometri):
        if indirizzo_auto not in self.info_auto:
            self.info_auto[indirizzo_auto] = {"chilometri": chilometri, "incidente": False, "stato_elettrico": "OK"}
        else:
            self.info_auto[indirizzo_auto]["chilometri"] = chilometri

    def rileva_incidente(self, indirizzo_auto):
        if indirizzo_auto in self.info_auto:
            self.info_auto[indirizzo_auto]["incidente"] = True

    def aggiorna_stato_elettrico(self, indirizzo_auto, stato):
        if indirizzo_auto in self.info_auto:
            self.info_auto[indirizzo_auto]["stato_elettrico"] = stato

# Creazione del "contratto" e gestione delle informazioni simulate
contratto_auto = ContrattoAuto()
contratto_auto.imposta_proprietario("Alice")

# Simulazione di transazioni: Aggiornamento chilometri
contratto_auto.aggiorna_chilometri("Auto123", 10000)

# Simulazione di transazioni: Rilevamento di un incidente
contratto_auto.rileva_incidente("Auto123")

# Simulazione di transazioni: Aggiornamento stato elettrico
contratto_auto.aggiorna_stato_elettrico("Auto123", "Difettoso")

# Stampa delle informazioni dell'auto dopo le transazioni
print("Informazioni sull'auto:", contratto_auto.info_auto)
print("Proprietario attuale:", contratto_auto.proprietario)
