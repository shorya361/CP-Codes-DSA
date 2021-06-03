def wordBreak(dict, str, out=""):
    if not str:
        print(out)

    for i in range(1, len(str) + 1):
        prefix = str[:i]
        
        if prefix in dict :
            wordBreak(dict, str[i:], out + "" + mor[prefix])
   


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
# str1='.--....-....-.-..-----.'
wordBreak(mor, str)