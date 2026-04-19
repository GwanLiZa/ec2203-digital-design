EBCDIC = {
    '0': 'F0', '1': 'F1', '2': 'F2', '3': 'F3',
    '4': 'F4', '5': 'F5', '6': 'F6', '7': 'F7',
    '8': 'F8', '9': 'F9',
    '+': 'C0', '-': 'D0'
}

def oct_fraction_to_dec(oct_str):
    integer, frac = oct_str.split('.')
    
    int_part = int(integer, 8)

    frac_part = 0
    for i, digit in enumerate(frac):
        frac_part += int(digit) * (8 ** -(i+1))
    
    return int_part + frac_part

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:]

def dec_to_twos_complement(dec_str, bits=16):
    dec_str = int(dec_str)
    if dec_str >= 0:
        return format(dec_str, f'0{bits}b')
    else:
        return format((1 << bits) + dec_str, f'0{bits}b')

def bin_to_dec(bin_str):
    return int(bin_str, 2)

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].upper()

def dec_to_ebcdic(dec_str):
    dec_str = int(dec_str)

    sign = '+' if dec_str >= 0 else '-'
    num_str = str(abs(dec_str))

    result = [EBCDIC[d] for d in num_str]
    result[-1] = EBCDIC[sign][0] + result[-1][1]  # 마지막 digit에 sign 넣기

    return ' '.join(result)

def group_bits(bin_str):
    return ' '.join(bin_str[i:i+4] for i in range(0, len(bin_str), 4))