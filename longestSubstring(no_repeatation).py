# question is to find longest substring in a given string with no repeatation of any alphabet
def longestSubstring(str):
    alpha=[-1 for i in range(26)]
    starting_index=0
    ll_start=0
    longest_length=0
    for i in range(len(str)):
        if alpha[ord(str[i]) -97 ] ==-1 or alpha[ord(str[i]) -97 ]<starting_index :
            alpha[ord(str[i]) -97 ]=i

        else:
            if longest_length < i-starting_index:
                ll_start= starting_index
                longest_length= i-starting_index
            starting_index=alpha[ord(str[i]) -97 ]+1
            alpha[ord(str[i]) -97 ]=i
            

    if longest_length < i-starting_index:
                ll_start= starting_index
                longest_length= i-starting_index+1
                 
    print(ll_start, longest_length)
    for i in range(ll_start,ll_start+ longest_length):
        print(str[i],end='')
    print()
    return
longestSubstring('aaaaaabcdefghij')
longestSubstring('irregardless')
longestSubstring('akshitsaxena')
longestSubstring('kaushalsaraswat')
longestSubstring('yoshitmathur')
longestSubstring('swamikeshvanandisntituteoftechnology')


#the approach is to store the index of each alphabet but if any alphabet is present before the
# ith index then we have to check for the longest substring and keep the record of the starting
# index of the longest substring.