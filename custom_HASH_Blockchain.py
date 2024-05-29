import struct
import time
import sys


def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


def hash(msg, secret="default"):
    message = mix(msg, secret)
    message = bytearray(message, "ascii")
    orig_len_in_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)

    while len(message) % 64 != 56:
        message.append(0)

    message += struct.pack("<Q", orig_len_in_bits)

    init_a = 0x67452301
    init_b = 0xEFCDAB89
    init_c = 0x98BADCFE
    init_d = 0x10325476

    a = init_a
    b = init_b
    c = init_c
    d = init_d

    for i in range(0, len(message), 64):
        w = [0] * 16

        for j in range(16):
            w[j] = struct.unpack_from("<I", message, i + j * 4)[0]

        a = hash_ff(a, b, c, d, w[0], 7, 0xD76AA478)
        d = hash_ff(d, a, b, c, w[1], 12, 0xE8C7B756)
        c = hash_ff(c, d, a, b, w[2], 17, 0x242070DB)
        b = hash_ff(b, c, d, a, w[3], 22, 0xC1BDCEEE)
        a = hash_ff(a, b, c, d, w[4], 7, 0xF57C0FAF)
        d = hash_ff(d, a, b, c, w[5], 12, 0x4787C62A)
        c = hash_ff(c, d, a, b, w[6], 17, 0xA8304613)
        b = hash_ff(b, c, d, a, w[7], 22, 0xFD469501)
        a = hash_ff(a, b, c, d, w[8], 7, 0x698098D8)
        d = hash_ff(d, a, b, c, w[9], 12, 0x8B44F7AF)
        c = hash_ff(c, d, a, b, w[10], 17, 0xFFFF5BB1)
        b = hash_ff(b, c, d, a, w[11], 22, 0x895CD7BE)
        a = hash_ff(a, b, c, d, w[12], 7, 0x6B901122)
        d = hash_ff(d, a, b, c, w[13], 12, 0xFD987193)
        c = hash_ff(c, d, a, b, w[14], 17, 0xA679438E)
        b = hash_ff(b, c, d, a, w[15], 22, 0x49B40821)

        a = hash_gg(a, b, c, d, w[1], 5, 0xF61E2562)
        d = hash_gg(d, a, b, c, w[6], 9, 0xC040B340)
        c = hash_gg(c, d, a, b, w[11], 14, 0x265E5A51)
        b = hash_gg(b, c, d, a, w[0], 20, 0xE9B6C7AA)
        a = hash_gg(a, b, c, d, w[5], 5, 0xD62F105D)
        d = hash_gg(d, a, b, c, w[10], 9, 0x2441453)
        c = hash_gg(c, d, a, b, w[15], 14, 0xD8A1E681)
        b = hash_gg(b, c, d, a, w[4], 20, 0xE7D3FBC8)
        a = hash_gg(a, b, c, d, w[9], 5, 0x21E1CDE6)
        d = hash_gg(d, a, b, c, w[14], 9, 0xC33707D6)
        c = hash_gg(c, d, a, b, w[3], 14, 0xF4D50D87)
        b = hash_gg(b, c, d, a, w[8], 20, 0x455A14ED)
        a = hash_gg(a, b, c, d, w[13], 5, 0xA9E3E905)
        d = hash_gg(d, a, b, c, w[2], 9, 0xFCEFA3F8)
        c = hash_gg(c, d, a, b, w[7], 14, 0x676F02D9)
        b = hash_gg(b, c, d, a, w[12], 20, 0x8D2A4C8A)

        a = hash_hh(a, b, c, d, w[5], 4, 0xFFFA3942)
        d = hash_hh(d, a, b, c, w[8], 11, 0x8771F681)
        c = hash_hh(c, d, a, b, w[11], 16, 0x6D9D6122)
        b = hash_hh(b, c, d, a, w[14], 23, 0xFDE5380C)
        a = hash_hh(a, b, c, d, w[1], 4, 0xA4BEEA44)
        d = hash_hh(d, a, b, c, w[4], 11, 0x4BDECFA9)
        c = hash_hh(c, d, a, b, w[7], 16, 0xF6BB4B60)
        b = hash_hh(b, c, d, a, w[10], 23, 0xBEBFBC70)
        a = hash_hh(a, b, c, d, w[13], 4, 0x289B7EC6)
        d = hash_hh(d, a, b, c, w[0], 11, 0xEAA127FA)
        c = hash_hh(c, d, a, b, w[3], 16, 0xD4EF3085)
        b = hash_hh(b, c, d, a, w[6], 23, 0x4881D05)
        a = hash_hh(a, b, c, d, w[9], 4, 0xD9D4D039)
        d = hash_hh(d, a, b, c, w[12], 11, 0xE6DB99E5)
        c = hash_hh(c, d, a, b, w[15], 16, 0x1FA27CF8)
        b = hash_hh(b, c, d, a, w[2], 23, 0xC4AC5665)

        a = hash_ii(a, b, c, d, w[0], 6, 0xF4292244)
        d = hash_ii(d, a, b, c, w[7], 10, 0x432AFF97)
        c = hash_ii(c, d, a, b, w[14], 15, 0xAB9423A7)
        b = hash_ii(b, c, d, a, w[5], 21, 0xFC93A039)
        a = hash_ii(a, b, c, d, w[12], 6, 0x655B59C3)
        d = hash_ii(d, a, b, c, w[3], 10, 0x8F0CCC92)
        c = hash_ii(c, d, a, b, w[10], 15, 0xFFEFF47D)
        b = hash_ii(b, c, d, a, w[1], 21, 0x85845DD1)
        a = hash_ii(a, b, c, d, w[8], 6, 0x6FA87E4F)
        d = hash_ii(d, a, b, c, w[15], 10, 0xFE2CE6E0)
        c = hash_ii(c, d, a, b, w[6], 15, 0xA3014314)
        b = hash_ii(b, c, d, a, w[13], 21, 0x4E0811A1)
        a = hash_ii(a, b, c, d, w[4], 6, 0xF7537E82)
        d = hash_ii(d, a, b, c, w[11], 10, 0xBD3AF235)
        c = hash_ii(c, d, a, b, w[2], 15, 0x2AD7D2BB)
        b = hash_ii(b, c, d, a, w[9], 21, 0xEB86D391)

        a = (a + init_a) & 0xFFFFFFFF
        b = (b + init_b) & 0xFFFFFFFF
        c = (c + init_c) & 0xFFFFFFFF
        d = (d + init_d) & 0xFFFFFFFF

    return "{:08x}{:08x}{:08x}{:08x}".format(a, b, c, d)


def mix(s, t):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))


def hash_ff(a, b, c, d, x, s, ac):
    a = a + ((b & c) | (~b & d)) + x + ac
    a = left_rotate(a, s)
    return (a + b) & 0xFFFFFFFF


def hash_gg(a, b, c, d, x, s, ac):
    a = a + ((b & d) | (c & ~d)) + x + ac
    a = left_rotate(a, s)
    return (a + b) & 0xFFFFFFFF


def hash_hh(a, b, c, d, x, s, ac):
    a = a + (b ^ c ^ d) + x + ac
    a = left_rotate(a, s)
    return (a + b) & 0xFFFFFFFF


def hash_ii(a, b, c, d, x, s, ac):
    a = a + (c ^ (b | ~d)) + x + ac
    a = left_rotate(a, s)
    return (a + b) & 0xFFFFFFFF


class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = (
            f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        )
        return hash(block_string)

    def __repr__(self):
        return (
            f"Block(Index: {self.index}, Previous Hash: {self.previous_hash}, "
            f"Timestamp: {self.timestamp}, Data: {self.data}, Nonce: {self.nonce}, "
            f"Hash: {self.hash})"
        )


class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        self.chain.append(block)

    def mine_block(self, data):
        last_block = self.get_last_block()
        new_index = last_block.index + 1
        new_timestamp = time.time()
        new_block = Block(new_index, last_block.hash, new_timestamp, data)

        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()

        self.add_block(new_block)


import tracemalloc


def performance(Blockchain):
    blockchain = Blockchain(difficulty=2)
    return blockchain


blockchain = performance(Blockchain)

tracemalloc.start()


def analysis(blockchain):
    start_time = time.time()
    blockchain.mine_block("Block 1 Data")
    blockchain.mine_block("Block 2 Data")
    blockchain.mine_block("Block 3 Data")
    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nBlockchain:")
    for block in blockchain.chain:
        print(block)

    print(f"\nTotal mining time: {end_time - start_time:.4f} seconds")
    print(f"Current memory usage: {current / 10**6:.2f} MB")
    print(f"Peak memory usage: {peak / 10**6:.2f} MB")


analysis(blockchain)
