import time
import tracemalloc

# SHA-256 Implementation

K = [
    0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
    0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3, 0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
    0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC, 0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
    0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7, 0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
    0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13, 0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
    0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3, 0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
    0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5, 0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
    0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208, 0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2,
]

def generate_hash(message: bytearray) -> bytearray:
    if isinstance(message, str):
        message = bytearray(message, "ascii")
    elif isinstance(message, bytes):
        message = bytearray(message)
    elif not isinstance(message, bytearray):
        raise TypeError

    # Padding
    length = len(message) * 8
    message.append(0x80)
    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0x00)
    message += length.to_bytes(8, "big")

    assert (len(message) * 8) % 512 == 0 

    # Parsing
    blocks = []
    for i in range(0, len(message), 64):
        blocks.append(message[i: i + 64])

    # Initial Hash Value
    h0, h1, h2, h3 = 0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A
    h4, h5, h6, h7 = 0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19

    # SHA-256 Hash Computation
    for message_block in blocks:
        message_schedule = []
        for t in range(64):
            if t <= 15:
                message_schedule.append(message_block[t * 4: (t * 4) + 4])
            else:
                term1 = _sigma1(int.from_bytes(message_schedule[t - 2], "big"))
                term2 = int.from_bytes(message_schedule[t - 7], "big")
                term3 = _sigma0(int.from_bytes(message_schedule[t - 15], "big"))
                term4 = int.from_bytes(message_schedule[t - 16], "big")
                schedule = ((term1 + term2 + term3 + term4) % 2**32).to_bytes(4, "big")
                message_schedule.append(schedule)

        assert len(message_schedule) == 64

        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        for t in range(64):
            t1 = (h + _capsigma1(e) + _ch(e, f, g) + K[t] + int.from_bytes(message_schedule[t], "big")) % 2**32
            t2 = (_capsigma0(a) + _maj(a, b, c)) % 2**32
            h, g, f, e = g, f, e, (d + t1) % 2**32
            d, c, b, a = c, b, a, (t1 + t2) % 2**32

        h0, h1, h2, h3 = (h0 + a) % 2**32, (h1 + b) % 2**32, (h2 + c) % 2**32, (h3 + d) % 2**32
        h4, h5, h6, h7 = (h4 + e) % 2**32, (h5 + f) % 2**32, (h6 + g) % 2**32, (h7 + h) % 2**32

    return (
        h0.to_bytes(4, "big") + h1.to_bytes(4, "big") + h2.to_bytes(4, "big") +
        h3.to_bytes(4, "big") + h4.to_bytes(4, "big") + h5.to_bytes(4, "big") +
        h6.to_bytes(4, "big") + h7.to_bytes(4, "big")
    ) # type: ignore

def _sigma0(num: int):
    return _rotate_right(num, 7) ^ _rotate_right(num, 18) ^ (num >> 3)

def _sigma1(num: int):
    return _rotate_right(num, 17) ^ _rotate_right(num, 19) ^ (num >> 10)

def _capsigma0(num: int):
    return _rotate_right(num, 2) ^ _rotate_right(num, 13) ^ _rotate_right(num, 22)

def _capsigma1(num: int):
    return _rotate_right(num, 6) ^ _rotate_right(num, 11) ^ _rotate_right(num, 25)

def _ch(x: int, y: int, z: int):
    return (x & y) ^ (~x & z)

def _maj(x: int, y: int, z: int):
    return (x & y) ^ (x & z) ^ (y & z)

def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << (size - shift)) & ((1 << size) - 1)


# -------------------------------------------------------------- Blockchain Implementation --------------------------------------------------------------


class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        message = (
            str(self.index) + str(self.previous_hash) + str(self.timestamp) +
            str(self.data) + str(self.nonce)
        ).encode('utf-8')
        return generate_hash(message).hex() # type: ignore

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        start_time = time.time()
        new_block.mine_block(self.difficulty)
        end_time = time.time()
        self.chain.append(new_block)
        return end_time - start_time

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {current_block.index}")
                return False
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash at block {current_block.index}")
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index} [Current Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}]")


# -------------------------------------------------------------- Performance Analysis --------------------------------------------------------------


def performance(__name__, Block, Blockchain):
    if __name__ == "__main__":
        blockchain = Blockchain(difficulty=5)
        mining_times = []

    # Start tracking memory
        tracemalloc.start()
        start_overall_time = time.time()

        for i in range(1, 5):
            mining_time = blockchain.add_block(Block(i, "", f"Block {i} Data"))
            mining_times.append(mining_time)
            print(f"Time to add block {i}: {mining_time:.2f} seconds")

        end_overall_time = time.time()
        
    # Get memory usage
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        is_valid = blockchain.is_chain_valid()
        print(f"is Blockchain valid?\n{is_valid}")

        blockchain.print_chain()

        total_time = end_overall_time - start_overall_time
        avg_mining_time = sum(mining_times) / len(mining_times)
        print(f"\nMining times: {mining_times}")
        print(f"Average mining time: {avg_mining_time:.2f} seconds")
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Current memory usage: {current / 10**6:.2f} MB; Peak: {peak / 10**6:.2f} MB")

performance(__name__, Block, Blockchain)


# -------------------------------------------------------------- Security Analysis --------------------------------------------------------------


def security(__name__, Block, Blockchain):
    if __name__ == "__main__":
        blockchain = Blockchain(difficulty=5)
        blockchain.add_block(Block(1, blockchain.get_latest_block().hash, "Block 1 Data"))
        blockchain.add_block(Block(2, blockchain.get_latest_block().hash, "Block 2 Data"))
        blockchain.add_block(Block(3, blockchain.get_latest_block().hash, "Block 3 Data"))

    # Verify blockchain validity
        print("is Blockchain valid?\n", blockchain.is_chain_valid())

    # Attempt to tamper with the blockchain
        print("Tampering with the blockchain...")
        blockchain.chain[1].data = "Tampered Data 1"
        blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()
        
        blockchain.chain[2].data = "Tampered Data 2"
        blockchain.chain[2].hash = blockchain.chain[2].calculate_hash()

        blockchain.chain[3].data = "Tampered Data 3"
        blockchain.chain[3].hash = blockchain.chain[3].calculate_hash()

    # Verify blockchain validity again
        print("is Blockchain valid after tampering?\n", blockchain.is_chain_valid())

security(__name__, Block, Blockchain)
