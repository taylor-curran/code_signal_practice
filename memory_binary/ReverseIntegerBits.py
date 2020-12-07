def csReverseIntegerBits(n):
    binary = bin(n)
    
    reverse = binary[-1:1:-1] 
    reverse = reverse + (2 - len(reverse))*'0'
    
    return (int(reverse, 2))

# Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

# Examples:

# csReverseIntegerBits(417) -> 267
# 417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
# csReverseIntegerBits(267) -> 417
# csReverseIntegerBits(0) -> 0
# Notes:

# The input integer will not be negative.
# [execution time limit] 4 seconds (py3)

# [input] integer n

# [output] integer