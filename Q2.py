def bin_to_int_signed(bin_str):
    bits = len(bin_str)
    val = int(bin_str, 2)
    if bin_str[0] == '1':
        val -= (1 << bits)
    return val

def int_to_bin(n, bits):
    return format(n & ((1 << bits) - 1), f'0{bits}b')

def twos_complement_sub(a, b, bits=12):
    x = bin_to_int_signed(a)
    y = bin_to_int_signed(b)

    result = x - y

    min_val = -(1 << (bits - 1))
    max_val = (1 << (bits - 1)) - 1

    if result < min_val or result > max_val:
        print("overflow")

    return int_to_bin(result, bits)

def ones_complement_add(a, b, bits=12):
    mask = (1 << bits) - 1

    x = int(a, 2)
    y = int(b, 2)
    raw = (x + y)

    sign_a = a[0]
    sign_b = b[0]
    sign_r = format(raw & mask, f'0{bits}b')[0]

    if sign_a == sign_b and sign_a != sign_r:
        print("overflow")
    
    if raw >> bits:
        raw = (raw & mask) + 1

    return format(raw, f'0{bits}b')

def xs3_to_decimal(bin_str):
    digits = [bin_str[i:i+4] for i in range(0, len(bin_str), 4)]
    result = 0
    for d in digits:
        result = result * 10 + (int(d, 2) - 3)
    return result

def decimal_to_xs3(n, digits_count):
    res = ""
    for d in str(n).zfill(digits_count):
        res += format(int(d) + 3, '04b')
    return res

def xs3_add(a, b):
    digits = len(a) // 4

    x = xs3_to_decimal(a)
    y = xs3_to_decimal(b)

    result = x + y

    if len(str(result)) > digits:
        print("overflow")

    return decimal_to_xs3(result, digits)

def group_bits(bin_str):
    padded_len = ((len(bin_str) + 7) // 8) * 8
    bin_str = bin_str.zfill(padded_len)
    
    return ' '.join(bin_str[i:i+8] for i in range(0, padded_len, 8))