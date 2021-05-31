#PF-Assgn-53
#This verification is based on string match.
import re
poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

#Write your logic here for question 1
count=0
for i in poem:
    if(i=="v"):
        count+=1

print(count)
print(re.sub(r"\n"," ",poem))
a=re.sub(r"co","Co",poem)
b=re.sub(r"ch","Ch",a)
print(b)
a=re.sub(r"ai...","ai*\*",poem)
b=re.sub(r"hi...","hi*\*",a)
print(b)#print(#Write your regular expression here for question 3)

#print()
#print(#Write your regular expression here for question 4)