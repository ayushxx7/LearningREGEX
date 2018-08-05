#importing necessary libs
import re #for regex
import os #for file handling

match_my_characters = 'I am string! I have a purpose given by my creator! To help him in learning regular expressions'
digit_text_match = 'phone number 1: 808112 2: 232323 3: 101 4: 91-9333'

find_all = re.findall('a',match_my_characters)
print(find_all)

find_all = re.findall('\w*a\w*',match_my_characters)
print(find_all)

find_all = re.findall('a{1}',match_my_characters)
print(find_all)

find_all = re.findall('\w{4}',match_my_characters)
print(find_all)

find_all = re.findall('\s\w{4}\s',match_my_characters)
print(find_all)

find_all = re.findall('\w*a\w*|\w*t\w*',match_my_characters)
print(find_all)

find_all = re.findall('\sa\w*|\st\w*',match_my_characters)
print(find_all)

search = re.search('i',match_my_characters, re.IGNORECASE)
print(search.group(0))

print(match_my_characters)
replace = re.sub('string','awesome',match_my_characters)
print(replace)

split = re.split('a',match_my_characters)
print(split)

split = re.split('\s\w*a\w*\s',match_my_characters)
print(split)

digits = re.findall('\d{2}\d*',digit_text_match)
print(digits)
'''
POPULAR PYTHON RE MODULE
FUNCTIONS
re.findall(A, B) | Matches all instances
of an expression A in a string B and returns
them in a list.
re.search(A, B) | Matches the first instance
of an expression A in a string B, and returns
it as a re match object.
re.split(A, B) | Split a string B into a list
using the delimiter A.
re.sub(A, B, C) | Replace A with B in the
string C.

'''



'''
Regular Expression Basics
.	Any character except newline
a	The character a
ab	The string ab
a|b	a or b
a*	0 or more a's
backslash Escapes a special character


Regular Expression Quantifiers
*	0 or more
+	1 or more
?	0 or 1
{2}	Exactly 2
{2, 5}	Between 2 and 5
{2,}	2 or more
(,5}	Up to 5


Regular Expression Character Classes
[ab-d]	One character of: a, b, c, d
[^ab-d]	One character except: a, b, c, d
[backslah b]	Backspace character
backslash d	One digit
backslash D	One non-digit
backslash s	One whitespace
backslash S	One non-whitespace
backslash w	One word character
backslash W	One non-word character



Regular Expression Assertions
^	Start of string
backslash A	Start of string, ignores m flag
$	End of string
backslash Z	End of string, ignores m flag
backslash b	Word boundary
backslash B	Non-word boundary
(?=...)	Positive lookahead
(?!...)	Negative lookahead
(?<=...)	Positive lookbehind
(?<!...)	Negative lookbehind
(?()|)	Conditional


Regular Expression Flags
i	Ignore case
m	^ and $ match start and end of line
s	. matches newline as well
x	Allow spaces and comments
L	Locale character classes
u	Unicode character classes
(?iLmsux)	Set flags within regex

Regular Expression Special Characters
backslash n	Newline
backslash r	Carriage return
backslash t	Tab
backslash YYY	Octal character YYY
backslash xYY	Hexadecimal character YY

Regular Expression Replacement
backslash g<0>	Insert entire match
backslash g<Y>	Insert match Y (name or number)
backslash Y	Insert group numbered Y
'''

