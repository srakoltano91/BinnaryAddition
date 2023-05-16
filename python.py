def add_binary(a, b):
    sum_decimal = a + b
    sum_binary = bin(sum_decimal)[2:]  # Convert to binary and remove the "0b" prefix
    return sum_binary
