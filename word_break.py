# the question is given a string and dictionary of words, determine if the string can be segmented into a
# spaced-separated sequence of one or more dictionary words

#Using Recursion
#starting from i=0 of the given string, check of the prefix i.e.str[:i] availabilty in the dict until i==len(str)
# if the given substring is available in dict, then we will recursively for the remaining string after excluding the prefix.
 
##USING RECURSION
# this function return true and false whether the string can be segmented or not.
def wordBreak(dict, str, out=""):
    # base condition: if the given string is empty then it means that string is completed and been found.
    if not str:
        print(out)

    for i in range(1, len(str) + 1):
        prefix = str[:i]
        
        if prefix in dict :
            wordBreak(dict, str[i:], out + "" + mor[prefix])
            # if the prefix is available and the remaining string is available as well then we will return True
            
    # when either prefix is not available in dict and remaining string is not present then false
    
dict = [
    "self", "th", "is", "famous", "Word",
    "break", "b", "r", "e", "a", "k", "br",
    "bre", "brea", "ak", "problem"
]

mor = {
    '.-': 'A',        '-...': 'B',     '-.-.': 'C',
    '-..': 'D',       '.': 'E',        '..-.': 'F',
    '-.': 'G',        '....': 'H',     '..': 'I',  
    '.---': 'J',      '-.-': 'K',      '.-..': 'L',
    '--': 'M',        '-.': 'N',       '---': 'O', 
    '.--.': 'P',      '--.-': 'Q',     '.-.': 'R',
    '...': 'S',       '-': 'T',        '..-': 'U', 
    '...-': 'V',      '.--': 'W',      '-..-': 'X',
    '-.--': 'Y',      '--..': 'Z',     '-----': '0', 
    '.----': '1',     '..---': '2',    '...--': '3',
    '....-': '4',     '.....': '5',    '-....': '6', 
    '--...': '7',     '---..': '8',    '----.': '9',
    ' ':' '
     }

str='.... . .-.. .-.. ---'
# str='.--....-....-.-..-----.'
# str = "Wordbreakproblem"
wordBreak(mor, str)



##USING DYNAMIC PROGRAMMING  #optimal
# Function to determine if a string can be segmented into space-separated
# sequence of one or more dictionary words
def wordBreak(dict, str, lookup,out=""):
    # `n` stores length of the current substring
    
    n = len(str)
    print(str,n, lookup)
    # return true if the end of the string is reached
    if n == 0:
        print(out)
        return True
    # if the subproblem is seen for the first time
    if lookup[n] == -1:
        # mark subproblem as seen (0 initially assuming string
        # can't be segmented)
        lookup[n] = 0
        for i in range(1, n + 1):
            # consider all prefixes of the current string
            prefix = str[:i]
            # if the prefix is found in the dictionary, then recur for the suffix
            if prefix in dict and wordBreak(dict, str[i:], lookup, out + "_"+ prefix):
                # return true if the string can be segmented
                lookup[n] = 1
                print(i,n,str,lookup)
                return True
    # return solution to the current subproblem
    return lookup[n] == 1
 
 


# Word Break Problem Implementation in Python
# List of strings to represent a dictionary
# we can also use a Trie or a set to store a dictionary
dict = ["self", "th", "is", "famous", "Word",
        "break", "b", "r", "e", "a", "k", "br",
        "bre", "brea", "ak", "problem"]

# input string
str = "Wordbreakproblem"

# lookup table to store solutions to subproblems
# `lookup[i]` stores if substring `str[n-i…n)` can be segmented or not
# lookup = [-1] * (len(str) + 1)
# print(len(lookup))
# if wordBreak(dict, str, lookup):
#     print("The string can be segmented")
# else:
#     print("The string can't be segmented")




#this function will print every possibile string which can be segmented using the dict.
def wordBreak_(dict, str, out=""):
     # if the end of the string is reached,
    # print the output string
    if not str:
        print(out)
        return
 
    for i in range(1, len(str) + 1):
        prefix = str[:i]
        # if the prefix is present in the dictionary, add it to the
        # output string and recur for the remaining string
        if prefix in dict:
            wordBreak(dict, str[i:], out + " " + prefix)
dict = [
    "self", "th", "is", "famous", "Word",
    "break", "b", "r", "e", "a", "k", "br",
    "bre", "brea", "ak", "problem"
]
str = "Wordbreakproblem"
# wordBreak_(dict, str)