import re


def count_words(text):

    word_pattern = r'''
        \b(                              
            (?:                         
                in|from|to|on|out|at|  
                but|because|although|so|and|  
                you|I|me|he|him|himself|ourselves|mine|hers|  
                a|an|the|  
                yipe|yum|yak|ugh|huh|  
                \d{1,}th               
            )\b                        
            |                           
            (?:                        
                \w+\s+\d{1,}\w*\s+\d{4}  
                |                     
                \d+\s+\w+              
                |                       
                \w+\s+\w+\s+\w+       
            )\b                        
            |                           
            (?:                        
                [A-Za-z]+'[A-Za-z]+   
                |                      
                cannot|can't           
            )\b                        
        )\b                           
    '''


    words = re.findall(word_pattern, text, re.VERBOSE)


    valid_words = [word for word in words if word]


    return len(valid_words)



example_text = """
In September 11th 2014, you’ll see that it’s true! But he didn’t expect that. 
25 Londýnská, Praha is a good address. 2 is not a word. 
1st, 2nd, 3rd are ordinal numbers. 
I can’t wait for the fun. Yum!
"""

word_count = count_words(example_text)
print(f"Počet slov: {word_count}")
