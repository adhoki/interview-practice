import sys
import os

def isStringUnique(string, naive=True):
    
    if naive:
        # naive, using additional data structure - set
        # O(n) runtime, n is length of string
        isVisited = set()
        for char in string:
            if char in isVisited:
                return False
            isVisited.add(char)
        return True

    else:
        # sort the string and make one pass along it to see if adjacent repeated
        # O(n log(n)) run time

        string = ''.join(sorted(string))
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                return False
        return True


def isStringPermutation(s1, s2):
    # 
    
    if len(s1) != len(s2):
        return False
    
    # maintain characters with number of occurrences in a hash-table
    s1_hash, s2_hash = {}, {}
    for char in s1:
        if char in s1_hash:
            s1_hash[char] += 1
        else:
            s1_hash[char] = 1
    for char in s2:
        if char in s2_hash:
            s2_hash[char] += 1
        else:
            s2_hash[char] = 1
    
    if s1_hash == s2_hash:
        return True

    return False

def isStringPalindromePermutation(base_string, compare_string):
    """
    Algorithm:
    - Check if the two strings are of same length, after removing non-alphanumeric characters
    - create hashmap of both strings with chars as keys.
    - if length is even, all counts should be even, and if odd, only one char can have odd count
    """
    base_string = base_string.replace(' ', '')
    compare_string = compare_string.replace(' ', '')
    
    if len(base_string) != len(compare_string):
        print('returning false in length compare')
        return False

    base_hash, compare_hash = {}, {}

    for char in base_string:
        if char in base_hash:
            base_hash[char] += 1
        else:
            base_hash[char] = 1

    for char in compare_string:
        if char in compare_hash:
            compare_hash[char] += 1
        else:
            compare_hash[char] = 1

    # added values to both hash-tables 
    # atmost 1 character can have odd values.
    isOdd = 0
    for val in compare_hash.values():
        if val % 2 == 1:
            isOdd += 1
        if isOdd > 1:
            return False

    if compare_hash == base_hash:
        return True

    return False

print(isStringPalindromePermutation('taco cat', 'atco cta'))