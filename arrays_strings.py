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
            s1_hash[char] = 0
    for char in s2:
        if char in s2_hash:
            s2_hash[char] += 1
        else:
            s2_hash[char] = 0
    
    if s1_hash == s2_hash:
        return True

    return False
