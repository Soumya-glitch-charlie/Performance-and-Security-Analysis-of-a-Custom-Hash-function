# SHA-256 HASH Algorithm
SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that belongs to the SHA-2 family, designed by the National Security Agency (NSA) and published by the National Institute of Standards and Technology (NIST) in 2001. It produces a fixed-size, 256-bit (32-byte) hash value, typically rendered as a 64-character hexadecimal number.
SHA256 algorithm

<br>

- The SHA256 hash is a block transformation algorithm based on LFSR message expansion.
- The algorithm has 2 parts: the Message Schedule and the Hash Core.
- The message schedule can be implemented as a compact 16-word circular buffer, that is cycled for the 64 clock cycles.
- Here is a simplified diagram of implementing the message schedule datapath, with the circular buffer (r0 ... r15) and the combinational functions (σ0, σ1).


<br>

##
![Msg Schedule Logic](https://github.com/Soumya-glitch-charlie/SHA-256-Encryption-Algorithm/assets/127016329/c4ae5375-1be1-478e-b26a-410c5d34ec4a)
<br>
<i><b>Preview:</b> SHA-256 Message Schedule Circuit Diagram </i>

<br>


We implement the core logic as a word-shift register with combinational logic that computes the next state for the word-shifter registers.
Here is a simplified depiction of the hash core logic datapath, with the core registers (a .. h) and the combinational functions (Maj, Ch, ∑0, ∑1).
The whole block is processed in a single clock cycle for each of the 64 cycles of the algorithm.


<br>

##
![HASH Core Logic](https://github.com/Soumya-glitch-charlie/SHA-256-Encryption-Algorithm/assets/127016329/67c5088b-2e07-48d0-a92d-fdf0a2e8d3bc)
<br>
<p align="center"><i><b>Preview:</b>SHA-256 HASH Core Logic</i></p>

<br>


Note on the combinational functions (Maj, Ch, ∑0, ∑1, σ0, σ1): The Sigma function shifters are implemented as fixed bit remaps (zero-logic), and the Maj and Ch are canonical implementations of the FIPS-180-4 description. These boolean functions can be rearranged to match the target gate library. The boolean remap saves no area for LUT-based FPGA targets, but for ASIC targets and the more limited FPGA sea of gates, the remap can hold combinational depth.

Note on the wide port adders: The hash algorithm is heavily dependent on adder architecture. When implemented with 2-port 32+32 bit adders, a cascade of adders can be used for the adder chain, reducing interconnect complexity. However, aggressive implementation with wide port parallel adders can reduce combinational path length and increase top clock rates, at the expense of interconnect and area constraints.


<br>

# Custom HASH Algorithm (MD-5 like)
This article introduces a custom hash function tailored for blockchain networks, aiming to balance ease of use and security. The proposed hash function employs innovative techniques to enhance both performance and protection against attacks. By utilizing a simplified algorithm, it remains user-friendly without compromising encryption strength. Rigorous testing has shown that this hash function effectively preserves blockchain data integrity and immutability, thus bolstering the system's defense against malicious activities. Designed with scalability in mind, it ensures sustained efficiency and viability amid evolving technological landscapes and increasing network demands. This solution provides blockchain developers and enthusiasts with a practical and robust tool for secure data management in decentralized environments.
