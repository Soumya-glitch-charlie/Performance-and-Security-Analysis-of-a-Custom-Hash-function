# CHALLENGES FACED BY HASH FUNCTIONS

1. Vulnerabilities and Attacks:
-	Hash functions face challenges from vulnerabilities and attacks, such as collision attacks, where two different inputs produce the same hash value, compromising data integrity.
-	Other potential threats include pre-image attacks, where an attacker tries to find an input that corresponds to a specific hash value, and length extension attacks, which exploit the properties of hash functions to extend a given hash value.
   
2. Advancements in Computing Power:
-	With the rapid advancements in computing power and algorithms, current hash functions may become susceptible to brute-force attacks.
-	The increasing availability of powerful hardware and distributed computing resources raises concerns about the resilience of hash functions against attacks.

3. Future Improvements:
-	Future improvements in hash functions aim to address these challenges by developing more robust and secure algorithms.
-	This includes designing hash functions with enhanced resistance against known attacks and vulnerabilities, ensuring their continued effectiveness in securing sensitive data.

4. Post-Quantum Cryptography:
-	The advent of quantum computing poses a significant threat to current cryptographic systems, including hash functions.
-	Future improvements may involve the development of post-quantum cryptographic hash functions that can withstand the computational power of quantum computers.

5. Efficiency and Performance:
-	Improving the efficiency and performance of hash functions is crucial to meet the scalability demands of emerging technologies like blockchain, IoT, and big data analytics.
-	Research efforts focus on optimizing hash function algorithms to ensure fast and reliable processing of large volumes of data.

The three main purposes of a hash function are:

- To scramble data deterministically,
- To accept an input of arbitrary length and output a fixed-length result,
- To manipulate data irreversibly. The input cannot be derived from the output.

<br>

# SHA-256 HASH Algorithm
SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that belongs to the SHA-2 family, designed by the National Security Agency (NSA) and published by the National Institute of Standards and Technology (NIST) in 2001. A cryptographic hash, also often referred to as a “digest”, “fingerprint” or “signature”, is an almost perfectly unique string of characters that is generated from a separate piece of input text. SHA-256 generates a 256-bit (32-byte) signature.


Key Features of SHA-256:

1. Fixed-Length Output: Regardless of the input size, SHA-256 always produces a 256-bit hash. This property is essential for ensuring uniformity and predictability in hash values.

2. Deterministic: The same input will always produce the same hash output. This determinism is crucial for verifying data integrity.

3. Pre-Image Resistance: It is computationally infeasible to reverse-engineer the original input from its hash output. This property is vital for security, ensuring that hashed data cannot be easily deciphered.[21]

4. Collision Resistance: It is improbable that two different inputs will produce the same hash output. This minimizes the risk of two distinct pieces of data being treated as identical.

5. Avalanche Effect: A small change in the input (even a single bit) significantly alters the output hash, making the hash function sensitive to input variations.

<br>

<h2>Working Principle of SHA-256</h2>
SHA-256 processes data in fixed-size blocks of 512 bits (64 bytes). The algorithm follows these primary steps:

![Msg Schedule Logic](https://github.com/Soumya-glitch-charlie/SHA-256-Encryption-Algorithm/assets/127016329/c4ae5375-1be1-478e-b26a-410c5d34ec4a)
<br>
<i><b>Preview:</b> SHA-256 Message Schedule Circuit Diagram </i>

<br>

We implement the core logic as a word-shift register with combinational logic that computes the next state for the word-shifter registers.
Here is a simplified depiction of the hash core logic datapath, with the core registers (a .. h) and the combinational functions (Maj, Ch, ∑0, ∑1).
The whole block is processed in a single clock cycle for each of the 64 cycles of the algorithm.

<br>

![HASH Core Logic](https://github.com/Soumya-glitch-charlie/SHA-256-Encryption-Algorithm/assets/127016329/67c5088b-2e07-48d0-a92d-fdf0a2e8d3bc)
<br>
<p align="center"><i><b>Preview:</b>SHA-256 HASH Core Logic</i></p>

<br>

Note on the combinational functions (Maj, Ch, ∑0, ∑1, σ0, σ1): The Sigma function shifters are implemented as fixed bit remaps (zero-logic), and the Maj and Ch are canonical implementations of the FIPS-180-4 description. These boolean functions can be rearranged to match the target gate library. The boolean remap saves no area for LUT-based FPGA targets, but for ASIC targets and the more limited FPGA sea of gates, the remap can hold combinational depth.

Note on the wide port adders: The hash algorithm is heavily dependent on adder architecture. When implemented with 2-port 32+32 bit adders, a cascade of adders can be used for the adder chain, reducing interconnect complexity. However, aggressive implementation with wide port parallel adders can reduce combinational path length and increase top clock rates, at the expense of interconnect and area constraints.

<br>

# Custom HASH Algorithm (MD-5 like)
This article introduces a custom hash function tailored for blockchain networks, aiming to balance ease of use and security. The proposed hash function employs innovative techniques to enhance both performance and protection against attacks. Utilizing a simplified algorithm remains user-friendly without compromising encryption strength. Rigorous testing has shown that this hash function effectively preserves blockchain data integrity and immutability, thus bolstering the system's defence against malicious activities. Designed with scalability in mind, it ensures sustained efficiency and viability amid evolving technological landscapes and increasing network demands. This solution provides blockchain developers and enthusiasts with a practical and robust tool for secure data management in decentralized environments.

- <h4>OBJECTIVE FOR CREATING A CUSTOM HASH FUNCTION</h4>

    There is always a search for efficient and secure encryption foundations in blockchain technology. Our hash function is designed to provide a practical solution for blockchain developers and enthusiasts, striking a balance between ease of use and security, our custom hash function combines new techniques to improve both performance and attack protection. By leveraging a simplified algorithm design, we make it easier to use without sacrificing encryption strength. and security is important.

     <ul>Through rigorous analysis and testing, we have demonstrated the effectiveness of the hash function in preserving the integrity and immutability of blockchain data, thereby strengthening the underlying system that protects against malicious and potentially malicious actors. Our hash function is designed to meet the needs of blockchain networks without compromising performance or security. This scalability ensures that our solutions remain viable and efficient in the face of changing technology environments and increasing network connectivity. Through collaboration and innovation, we strive to provide blockchain developers with the tools and technology they need to create a secure and collaborative network that will pave the way to the future.</ul>

<br>

# SECURITY ANALYSIS OF HASH FUNCTION AND ITS PARAMETERS

<br>
Hash functions form the basis of digital security and are used in applications ranging from blockchain networks to data integrity verification. However, security analysis is required to ensure that it can protect against attacks. This analysis helps identify vulnerabilities that may affect the integrity and authenticity of data and recommends improving protection to strengthen the encryption process and make improvements that will increase security. Additionally, effective analysis can ensure cryptographic resilience in the face of emerging technologies by anticipating emerging threats such as quantum computing.

<br>
In the field of cryptography, three main functions play an important role in measuring the security and integrity of hash functions: collision resistance, avalanche effect and preimage resistance. 

- <b>Collision Effect:</b> A hash function exhibits collision inconsistency when it fails to compute two different inputs that result in the same hash output. This device ensures that even a small change in the input data causes a difference in the hash, reducing the risk of data collisions and the control integrity of the cryptographic process. 

- <b>Avalanche Effect:</b> The avalanche effect describes the most common feature of hashing operations; Small changes in input data cause significant and uncertain changes in the results of the hash. This device ensures that even small changes in input data are propagated throughout the hashed data, leaving no patterns or relationships visible and ensuring the security of cryptographic applications.

<br>

#  CREATION OF CUSTOM HASH FUNCTION:

<h4>The steps regarding the creation of our Custom Hash Function:</h4>

1.  Initially, the message is encoded in utf-8 encoding to include all special characters.

2.  The message is then permuted with the secret key. The secret key can be provided externally by the user of the hash function. If a secret key is not provided, it will take the default secret key, which is AfmOG7TfhPh2IAS9b3HwXg==. This default secret key is 16 bytes in length and has been generated using openssl with base64 encoding. The secret key is necessary for the hash function to work properly. That’s why we’ve provided the default secret key here. We divide the secret key into two parts, the left part and the right part. The left part is modified as:
- <b>mod_left = left <<_c 2 (left circular shift by 2)</b>
and the right part is modified as:
- <b>mod_right = right >>_c 3 (right circular shift by 3)</b>
and the original message is modified as:
- <b>mod_left + orig_message + mod_right.</b>

<br>
Further operations are performed on this modified message.

3.  <b>The entire message is converted into a byte array (with utf-8 encoding) so that the message is represented as a sequence of bytes, which is necessary for further binary manipulation. We also have to consider the original length of the message in bits as a 64-bit integer. This is done by calculating the length of the message in bits and performing a bitwise AND operation with 0xffffffffffffffff</b>. The bitwise AND operation is used for 64-bit masking and ensures that the length of the message is within 64 bits. We’ll need that for further processing. After that, we have to pad  0x80, which is 10000000 in binary, to the bytearray. The next bits are padded with 0s until we are 56 bytes short of 64 bytes or a multiple of 64 bytes. The remaining 8 bytes are appended with the length of the message in bytes (We did bit masking on the message length to make it 64 bits or 8 bytes). After this computation, we pack the bytes in little-endian format.

4.  <b>We have to define 4 constants init_a, init_b, init_c and init_d whose values are 0x243f6a88, 0x85a308d3, 0x13198a2e and 0x03707344 respectively.</b> These values are taken from Blowfish constants. Blowfish is a symmetric keyblock cypher designed by Bruce Schneier in 1993. It is known for its speed and effectiveness, making it popular in software applications. The blowfish constants are derived from the hexadecimal representation of the digits of the mathematical constant pi(π). We’ve chosen blowfish constants because they are tried and tested constants and are widely used in the software industry. Also, Blowfish constants are cryptographically secure. These constants will be further used in permuting the message to get our hashed value.

5.  We move on to the final processing block. We iterate over the message with steps of 64. In other words, we pick up a chunk of 64 bytes, perform calculations and then we move on to the next 64-byte chunk. For every chunk, we create a ‘w’ array (word array). Word array is a 16-length 32-bit word from the padded message.

```python
for j in range(16):
    w[j] = struct.unpack_from('<I', message, i + j * 4)[0]
```
   <ul>
         <li> where ‘i’ is the outer loop variable that loops over the entire message byte array in chunks of 64 bytes.</li>
   </ul> 
<br>

6.  After that, we declare and modify 4 variables (corresponding to init_a, init_b, init_c and init_d) by using some core transformation functions. The core transformation functions are an integral part of the hash function as they permute the whole message. There are 4 core transformation functions in this hash function. They are defined as follows;

```python
def hash_ff(a, b, c, d, x, s, ac):
    a = (a ^ ((b & c) | ((~b) & d)) ^ x ^ ac)
    a = (left_rotate(a, s) ^ b) & 0xffffffff
    return a

def hash_gg(a, b, c, d, x, s, ac):
    a = (a ^ ((b & d) | (c & (~d))) ^ x ^ ac)
    a = (left_rotate(a, s) ^ b) & 0xffffffff
    return a

def hash_hh(a, b, c, d, x, s, ac):
    a = (a ^ (b ^ c ^ d) ^ x ^ ac)
    a = (left_rotate(a, s) ^ b) & 0xffffffff
    return a

def hash_ii(a, b, c, d, x, s, ac):
    a = (a ^ (c ^ (b | (~d))) ^ x ^ ac)
    a = (left_rotate(a, s) ^ b) & 0xffffffff
```
  <ul>
        <li>The functions perform non-linear operations on the aforementioned variables and modify their states which will be further combined with the initial constants to obtain our hash value.</li>
  </ul>

7.  After that a, b, c and d are added with their corresponding initial values and a bitwise AND operation is taken of the sum to take its modulo 2^32.

8. 	Finally, we pack the final hash state variables into a byte array in a specific format. In our case, 4 unsigned integers are packed together to form the hash of the message. The hash obtained will be 128 bits in length.

<br>

<h3>Implementation and analysis of custom blockchain:</h3>

This article introduces a custom hash function tailored for blockchain networks, aiming to balance ease of use and security. The proposed hash function employs innovative techniques to enhance both performance and protection against attacks. By utilizing a simplified algorithm, it remains user-friendly without compromising encryption strength. Rigorous testing has shown that this hash function effectively preserves blockchain data integrity and immutability, thus bolstering the system's defense.[41]
Hash function generation:


1.	Left Rotate Function (‘left_rotate’),

2. Mix Function (mix),

3. Hash Rounds Functions,
 
4. Main Hash Function (hash),

5. Blockchain Implementation:
<ul>
     -  5.1	Block Class (Block),
     -	5.2 Blockchain Class (Blockchain).
</ul>



