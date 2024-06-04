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

1. Fixed-Length Output: SHA-256 always produces a 256-bit hash regardless of the infinite input size. This property is essential for ensuring uniformity and predictability in hash values.

2. Deterministic: The same input will always produce the same hash output. This determinism is crucial for verifying data integrity.

3. Pre-Image Resistance: It is computationally infeasible to reverse-engineer the original input from its hash output. This property is vital for security, ensuring that hashed data cannot be easily deciphered.[21]

4. Collision Resistance: It is improbable that two different inputs will produce the same hash output. This minimizes the risk of two distinct pieces of data being treated as identical.

5. Avalanche Effect: A small change in the input (even a single bit) significantly alters the output hash, making the hash function sensitive to input variations.

<br>

<h2>Working Principle of SHA-256</h2>
SHA-256 processes data in fixed-size blocks of 512 bits (64 bytes). The algorithm follows these primary steps:

- **Hash Generation Function:**

The ‘generate_hash’ function takes a message and processes it to produce a  256-bit hash value.

1.	**Padding:**
-	Padding ensures that the message length is a multiple of 512 bits. 
-	This involves appending a single 1 bit, followed by enough 0 bits and finally,
-	 The message length is a 64-bit integer.[20,22]
  
2.	**Parsing:**
-	Splits the padded message into 512-bit blocks for processing.
  
3.	**Initial Hash Values:**
-	Now we create 8 hash values. These are hard-coded constants that represent the first 32 bits of the fractional parts of the square roots of the first 8 primes: 2, 3, 5, 7, 11, 13, 17, 19.

```Bash
h0 := 0x6a09e667
h1 := 0xbb67ae85
h2 := 0x3c6ef372
h3 := 0xa54ff53a
h4 := 0x510e527f
h5 := 0x9b05688c
h6 := 0x1f83d9ab
h7 := 0x5be0cd19
```

4. **Constants:**
- The K array contains 64 constant values used in the SHA-256 algorithm. These values are derived from the fractional parts of the cube roots of the first 64 prime numbers(2 - 311).

```Bash
K = [
0x428a2f98 0x71374491 0xb5c0fbcf 0xe9b5dba5 0x3956c25b 0x59f111f1 0x923f82a4 0xab1c5ed5
0xd807aa98 0x12835b01 0x243185be 0x550c7dc3 0x72be5d74 0x80deb1fe 0x9bdc06a7 0xc19bf174
0xe49b69c1 0xefbe4786 0x0fc19dc6 0x240ca1cc 0x2de92c6f 0x4a7484aa 0x5cb0a9dc 0x76f988da
0x983e5152 0xa831c66d 0xb00327c8 0xbf597fc7 0xc6e00bf3 0xd5a79147 0x06ca6351 0x14292967
0x27b70a85 0x2e1b2138 0x4d2c6dfc 0x53380d13 0x650a7354 0x766a0abb 0x81c2c92e 0x92722c85
0xa2bfe8a1 0xa81a664b 0xc24b8b70 0xc76c51a3 0xd192e819 0xd6990624 0xf40e3585 0x106aa070
0x19a4c116 0x1e376c08 0x2748774c 0x34b0bcb5 0x391c0cb3 0x4ed8aa4a 0x5b9cca4f 0x682e6ff3
0x748f82ee 0x78a5636f 0x84c87814 0x8cc70208 0x90befffa 0xa4506ceb 0xbef9a3f7 0xc67178f2
]
```

5.	**Message Schedule:**
- Processes each block through 64 iterations, using the constants and bitwise operations to update the hash values. A 64-entry message schedule array is prepared from each 512-bit block. For entries 16 to 63, the values are derived using specific bitwise operations and previous entries.
<br>

![Msg Schedule Logic](https://github.com/Soumya-glitch-charlie/SHA-256-Encryption-Algorithm/assets/127016329/c4ae5375-1be1-478e-b26a-410c5d34ec4a)
<br>
<p align="left"><i><b>Fig 1:</b> SHA-256 Message Schedule Circuit Diagram </i></p>
<br>

6. **Compression Function:**

We implement the core logic as a word-shift register with combinational logic that computes the next state for the word-shifter registers.
Here is a simplified depiction of the hash core logic datapath, with the core registers (a .. h) and the combinational functions (Maj, Ch, ∑0, ∑1).
The whole block is processed in a single clock cycle for each of the 64 cycles of the algorithm.

These functions perform bitwise operations required by the SHA-256 algorithm:
- *_sigma0 and _sigma1:* Performs specific bitwise rotations and right-shift operation.
- *_capsigma0 and _capsigma1:* Performs additional bitwise rotations and right-shift operation.
- *_ch:* Chooses bits from user inputs (x or y based on z).
- *_maj:* Majority function based on those inputs (x, y, and z).
- *_rotate_right:* Rotates bits of a number to the right.

<br>

   ![HASH Core Logic](https://github.com/Soumya-glitch-charlie/SHA-256-Encryption-Algorithm/assets/127016329/67c5088b-2e07-48d0-a92d-fdf0a2e8d3bc)
<br>
<p align="center"><i><b>Fig 2:</b>SHA-256 HASH Core Logic</i></p>

<br>

# Custom HASH Algorithm (MD-5 like)
This article presents a custom hash function for blockchain networks, balancing ease of use and security. It employs innovative techniques to improve performance and protection against attacks, using a simplified algorithm that maintains strong encryption. Rigorous testing confirms its effectiveness in preserving blockchain data integrity and immutability, enhancing system defence against malicious activities. Designed for scalability, it ensures sustained efficiency amid evolving technology and growing network demands. This solution offers blockchain developers a practical, robust tool for secure data management in decentralized environments.

- <h4>OBJECTIVE FOR CREATING A CUSTOM HASH FUNCTION</h4>

    This article addresses the need for efficient and secure encryption in blockchain technology by proposing a custom hash function designed specifically for blockchain networks. Balancing ease of use and security, the hash function incorporates new techniques to enhance performance and attack protection. Its simplified algorithm design ensures user-friendliness without compromising encryption strength. Rigorous analysis and testing have confirmed its effectiveness in maintaining blockchain data integrity and immutability, thereby fortifying the system against malicious actors. The hash function is scalable, ensuring viability and efficiency in evolving technological landscapes and growing network demands. This contribution aims to advance the debate on cryptographic foundations and support blockchain developers in creating secure, decentralized networks for the future.

<br>

# SECURITY ANALYSIS OF HASH FUNCTION AND ITS PARAMETERS

<br>
Hash functions form the basis of digital security and are used in applications ranging from blockchain networks to data integrity verification. However, security analysis is required to ensure that it can protect against attacks. This analysis helps identify vulnerabilities that may affect the integrity and authenticity of data and recommends improving protection to strengthen the encryption process and make improvements that will increase security. Additionally, effective analysis can ensure cryptographic resilience in the face of emerging technologies by anticipating emerging threats such as quantum computing.

<br>
In the field of cryptography, three main functions play an important role in measuring the security and integrity of hash functions: <b>collision resistance, avalanche effect and preimage resistance.</b>

- <b>Collision Effect:</b> A hash function exhibits collision inconsistency when it fails to compute two different inputs that result in the same hash output. This device ensures that even a small change in the input data causes a difference in the hash, reducing the risk of data collisions and the control integrity of the cryptographic process. 

- <b>Avalanche Effect:</b> The avalanche effect describes the most common feature of hashing operations; Small changes in input data cause significant and uncertain changes in the results of the hash. This device ensures that even small changes in input data are propagated throughout the hashed data, leaving no patterns or relationships visible and ensuring the security of cryptographic applications.

<br>

#  CREATION OF CUSTOM HASH FUNCTION:

<h4>The steps regarding the creation of our Custom Hash Function:</h4>

Here are the block diagrams for a better understanding of the Custom Hash function:

<h4>Block Diagram 1 :</h4>

   ![Block DIagram of Custom Hash func](https://github.com/Soumya-glitch-charlie/Performance-and-Security-Analysis-of-a-Custom-Hash-function/assets/127016329/dcf649e2-651d-4133-b36e-ee7a7228174c)

<br>

<h4>Block Diagram 2 :</h4>

   ![Block DIagram of Custom Hash func 2](https://github.com/Soumya-glitch-charlie/Performance-and-Security-Analysis-of-a-Custom-Hash-function/assets/127016329/b5d59967-087e-47ea-b3e1-726143ef72f3)

<br>

1.  Initially, the message is encoded in utf-8 encoding to include all special characters.

2.  The message is then permuted with the secret key. The secret key can be provided externally by the user of the hash function. If a secret key is not provided, it will take the default secret key, which is AfmOG7TfhPh2IAS9b3HwXg==. This default secret key is 16 bytes in length and has been generated using openssl with base64 encoding. The secret key is necessary for the hash function to work properly. That’s why we’ve provided the default secret key here. We divide the secret key into two parts, the left part and the right part. The left part is modified as:
- <b>mod_left = left <<_c 2 (left circular shift by 2)</b>
and the right part is modified as:
- <b>mod_right = right >>_c 3 (right circular shift by 3)</b>
and the original message is modified as:
- <b>mod_left + orig_message + mod_right.</b>
  <ul> Further operations are performed on this modified message. </ul>
<br>

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

8.  Finally, we pack the final hash state variables into a byte array in a specific format. In our case, 4 unsigned integers are packed together to form the hash of the message. The hash obtained will be 128 bits in length.


<h3>Implementation and analysis of custom blockchain:</h3>

This article introduces a custom hash function tailored for blockchain networks, aiming to balance ease of use and security. The proposed hash function employs innovative techniques to enhance both performance and protection against attacks. By utilizing a simplified algorithm, it remains user-friendly without compromising encryption strength. Rigorous testing has shown that this hash function effectively preserves blockchain data integrity and immutability, thus bolstering the system's defence.


1. Blockchain Implementation:

- Block Class (Block),
- Blockchain Class (Blockchain).

2. Analysis of the Hash functions :

- <h3> Analysis 1 </h3>
  
   ![Block DIagram of Custom Hash func 4](https://github.com/Soumya-glitch-charlie/Performance-and-Security-Analysis-of-a-Custom-Hash-function/assets/127016329/a1975367-a707-456a-ad0b-3cbdda448807)

2.1 **Collision Resistance:**
- Custom Hash Function: Higher (54.237%), similar to SHA-256, less susceptible to collision attacks.
-	SHA-256: High(more than 51%), making it suitable for secure applications.

2.2 **Pre-image Resistance:**
- Custom Hash Function: Moderate, easier to find a message with a specific hash.
- SHA-256: High, difficult to find a message that hashes to a specific value.

2.3 **Second Pre-image Resistance:**
- Custom Hash Function: Second Pre-image resistance was successful
- SHA-256: For the existing hash function (SHA-2series) the second pre-image resistance was successful.

2.4 **Digest Length**
- Custom Hash function Digest length: 128 bits (32 hex characters)
- SHA-256 Digest Length: 256 bits (64 hex characters).

2.5 **Memory Usage**
- Custom Hash function Memory Usage: 0.69 MB
- SHA-256 Memory Usage: 1.79 MB

2.6 **Implementation:**
- Custom Hash Function: Custom implementation, unique to your needs.
- SHA-256: Standardized and widely available across various programming languages and libraries.


- <h3> Analysis 2 </h3>
  
   ![Block DIagram of Custom Hash func 3](https://github.com/Soumya-glitch-charlie/Performance-and-Security-Analysis-of-a-Custom-Hash-function/assets/127016329/55c52a12-bab7-45a8-8cea-46acb3b1b8d6)

<h4>Details:</h4>

3.1 **Algorithm Type:**
-	Custom Hash Function: Our custom function is similar to the MD5 algorithm, which processes data in blocks and uses bitwise operations.
-	SHA-256: Part of the SHA-2 family, it uses bitwise operations, modular additions, and compression functions.


3.2 **Security:**
-	Custom Hash Function: Moderate security, only PoW based
-	SHA-256: Designed for high security, resistant to known vulnerabilities, and widely used in cryptographic applications.

3.3 **Speed:**
-	Custom Hash Function: Generally faster due to simpler operations.
-	SHA-256: Slower due to more complex and numerous operations.

3.4 **Memory Usage:**
-	Custom Hash Function: Lower memory usage (), simpler state management.
-	SHA-256: Moderate memory usage, requires more state information.

3.5 **Complexity:**

   3.5.1	**Time Complexity of Custom Hash:**
   - Hash Function: O(N) per message of length N.
   - Mining a Single Block: O(2^d) ,where d is the difficulty.
   - Blockchain: O(M * 2^d), where M is the no. of blocks.

   3.5.2	**Space Complexity of Custom Hash:**
   - Hash Function: O(N) for a message of length N.
   - Blockchain: O(M), where M is the no. of blocks.

   3.5.3 **Time Complexity of SHA-256:**
   - Hash Function: O(N) per message of length N.
   - Blockchain: O(M * N), where M is the no. of blocks.

  3.5.4 **Space Complexity of SHA-256:**
  - Hash Function: O(1).
  - Blockchain: O(M * N), where M is the no. of blocks.

3.6 **Use Case:**
- Custom Hash Function: Suitable for applications where security is not the primary concern, such as checksums.
- SHA-256: Used in security-sensitive applications like digital signatures, blockchain, and data integrity verification.
 
