"""
Write a function named reverse_chunks that accepts a string s and integer k as parameters and returns a new string that reverses the relative order of every k characters of s.
For example, the call of reverse_chunks("MehranSahami", 3) should view the string in groups of 3 characters at a time, reversing "Meh" into "he_m", and "ran" into "nar", and so on, returning a result of "he_mnarha_sima".

If the string's length is not an exact multiple of k, the last chunk of fewer-than-k characters at the end of the string should be left in its original order. 
For example, if the call is reverse_chunks("MartyStepp", 4), the first chunk "Mart" becomes "tra_m" and the second chunk "y_ste" becomes "et_sy". The last two characters, "pp", are fewer than 4, so they are left as-is. 
So the result returned should be "tra_met_sypp".

You may assume that the value passed for k will be a positive integer.

Constraints: You should not create any data structures such as lists. But you may create as many strings as you like, and you may use as many simple variables (such as ints) as you like.
"""

def reverse_chunks(a, x):
    res = ''
    i = 0
    while i + x <= len(a):
       slice = a[i:i+x]
       res += slice[::-1]
       i+= x
    j = len(a) % x
    if j!= 0:
        res += a[-j:]
    return res
