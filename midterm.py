import numpy as np

import Q1
 
# part a
print(Q1.oct_fraction_to_dec(oct_str = "15.3"))
# part b
print(Q1.hex_to_dec(hex_str = "D2B3"))
# part c
print(Q1.group_bits(Q1.hex_to_bin(hex_str = "B9A2")))
# part d
print(Q1.group_bits(Q1.dec_to_twos_complement(dec_str = "-29", bits = 16)))
# part e
print(Q1.bin_to_dec("1010010001111011"))
# part f
print(Q1.bin_to_hex("0101100111111011"))
# part g
print(Q1.dec_to_ebcdic("7192"))

import Q2

# part a
print(Q2.group_bits(Q2.twos_complement_sub("001110000110", "111100110000")))
# part b
print(Q2.group_bits(Q2.ones_complement_add("111101111001", "000010000110")))
# part c
print(Q2.group_bits(Q2.xs3_add("100001111010", "010010000110")))

import Q3

constraints = Q3.parse_expr("b6'b5b4b3b1'b0")
minterms = Q3.get_minterms(constraints)
print("F = Σ(" + ", ".join(map(str, minterms)) + ")")

import Q4

gates = np.array([
    [0, 0, 1, 1, 0],  # x4
    [0, 0, 1, 1, 0],  # x3
    [0, 1, 0, 0, 0],  # x2
    [0, 0, 1, 1, 0],  # x1
    [0, 0, 0, 1, 0]   # x0
]).T

minterms = Q4.get_minterms(gates)
print("F = Σ(" + ", ".join(map(str, minterms)) + ")")