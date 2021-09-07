import sys
import os
import numpy as np
import string

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

def isOneAwayReplace(s1, s2):
    oneAway = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            oneAway += 1
        if oneAway > 1:
            return False
    return True

def oneAwayInsertDelete(s1, s2):
    ind1, ind2 = 0, 0
    buffer = False

    while (ind1 < len(s1) and ind2 < len(s2)):
        if (s1[ind1] == s2[ind2]):
            ind1 += 1
            ind2 += 1
        elif (s1[ind1] != s2[ind2] and not buffer):
            ind1 += 1
        else:
            return False
    
    return True

def oneAwayString(s1, s2):
    """
    Two cases:
    1. Insert/Delete, if the difference in the lengths of the strings is 1
    2. Replace, if the lengths are same... Need a function to figure 1-step away
    """
    if len(s1) == len(s2):
        return isOneAwayReplace(s1, s2)
    else:
        # ensure the first variable has the bigger word...
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        # bigger word is in s1, smaller one is in s2
        return oneAwayInsertDelete(s1, s2)

def createZeroMatrix(arr):
    """
    Input is a MxN matrix which has some elements as 0. 
    All rows and columns containing 0 in the original matrix to be converted to 0's

    Algorithm:
    - get set of row and column indexes, and then in the end, only make these rows and columns zero
    """
    indices = np.argwhere(arr == 0)
    x_s, y_s = set(indices[:, 0]), set(indices[:, 1])

    for i in x_s:
        arr[i, :] = 0
    for j in y_s:
        arr[:, j] = 0

    return arr

def isStringRotation(string, rotation):
    if len(string) != len(rotation):
        return False
    
    string_concatenated = string + string
    if rotation in string_concatenated:
        return True

    return False

# np.random.seed(2)
# arr = np.random.randint(0, 5, size=(4, 4))