import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_block, index):
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calc_hash()
        self.index = index

        self.next = None
        self.previous_hash = None

        # double linked list
        if previous_block != None:
            self.previous_hash = previous_block.hash
            previous_block.next = self

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.blocks = [];

    def mine_block(self, data):
        timestamp = time.time()
        if len(self.blocks) == 0: # geneis block
            new_block = Block(timestamp, data, None, 1)
        else:
            previous_block = self.blocks[-1]
            new_block = Block(timestamp, data, previous_block, len(self.blocks) + 1)

        self.blocks.append(new_block)

    def print_chain(self, current_block = None):
        if current_block is None: # init call
            self.print_chain(self.blocks[0])
        else:
            print("===========================================================================")
            print("    Index:", current_block.index, "| Data:", current_block.data)
            print("     Hash:", current_block.hash)
            print("Prev hash:", current_block.previous_hash)

            if current_block.next != None: # go through the chain block by block
                self.print_chain(current_block.next)


if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.mine_block("Genesis block")
    blockchain.mine_block("Second block")
    blockchain.mine_block("Third block")
    blockchain.mine_block("Fourth block")
    blockchain.mine_block("Fith block")

    blockchain.print_chain()
