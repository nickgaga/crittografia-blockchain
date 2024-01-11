import hashlib
import datetime

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.datetime.now()

class Block:
    def __init__(self, timestamp, transactions, previous_hash=''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_info = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_info.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(datetime.datetime.now(), [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Creazione della blockchain e transazione
my_blockchain = Blockchain()
transaction = Transaction("Bob", "Lisa", 10)
block = Block(datetime.datetime.now(), [transaction])

# Aggiunta del blocco alla blockchain
my_blockchain.add_block(block)

# Stampare la blockchain
for block in my_blockchain.chain:
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {[(t.sender, t.recipient, t.amount) for t in block.transactions]}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("")

# Verifica della validità della blockchain
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        if current_block.hash != current_block.calculate_hash():
            return False

        if current_block.previous_hash != previous_block.hash:
            return False

    return True

print("Is blockchain valid?", is_chain_valid(my_blockchain.chain))
