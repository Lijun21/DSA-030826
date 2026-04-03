"""
Given an array of strings words, 
return true if it forms a valid word square.

A sequence of strings forms a valid word square 
if the kth row and column read the same string, 
where 0 <= k < max(numRows, numColumns).

Input: words = ["abcd","bnrt","crmy","dtye"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crmy".
The 4th row and 4th column both read "dtye".
Therefore, it is a valid word square.

Input: words = ["abcd","bnrt","crm","dt"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crm".
The 4th row and 4th column both read "dt".
Therefore, it is a valid word square.

Input: words = ["ball","area","read","lady"]
Output: false
Explanation:
The 3rd row reads "read" while the 3rd column reads "lead".
Therefore, it is NOT a valid word square.
"""

def valid_word_square(words:list[list[str]])->bool:
    r_count = len(words)
    c_count = len(words[0])

    if r_count != c_count:
        return False

    for i in range(len(words)):
        for j in range(len(words[i])):
            # i, j in bound
            # words[i][j] is in bound, 0<=i<len(words), 0<=j<len(words[i]) 
            # words[j][i] is in bound, 0<=j<len(words), 0<=i<len(words[j]) 
            if j >= len(words) or i >= len(words[j]):
                return False
            if words[i][j] != words[j][i]:
                return False


    

# ["a"]
# "ab"

# ["ball",
#  "asee",
#  "let",
#  "lep"]