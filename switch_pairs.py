"""
Write a function named switch_pairs that accepts a string as a parameter and returns that string with each pair of neighboring letters reversed.
If the string has an odd number of letters, the last letter should not be modified.
For example, the call switch_pairs("example") should return "xemalpe" and the call switch_pairs("hello there") should return "ehll ohtree".
"""
def switch_pairs(str):
    response = ''
    i = 0
    if len(str) < 2:
        return str
    while i < len(str) - 1:
        response += str[i + 1]
        response += str[i]
        i += 2
    if len(str) % 2 != 0:
        response += str[-1]
    return response
