"""
Identifiers: (within a regex expression)

\d - any number
\D - anything BUT a number
\s - space
\S - anything BUT a space
\w - any character
\W - anything BUT a character
. - ANY character, except for newline
\b - whitespace AROUND words

N.B: finding a full-stop measns the character
     HAS to be escaped by a backslash like so: "\."

Modifiers: (add these on the end of any of the above identifiers to specify consecutive frequency)

{1,3} - expect the specified identifier sequence within the range of 1 to 3 consecutive instances
{5} - expect the specified number of consecutive instances of the idetifier
+ - match multiple (ONE OR MORE) times consecutively
? - match zero to one times (optional match). If it has more than 1 consecutive match then the regex would return false/not match
* - match zero to infite consecutive instances (optional match)

Other modifiers:
$ - match the end of a target string
^ - match the start of a string
<identifier> | <identifier> - match either identifier (OR statement)

White space chars:
\n - new line
\s - space
\t - tab
\e - escape
\f - form feed
\r - return

Misc:

[<char> - <char>] - range of characters between the specified values

See below for an example re script for names and ages:
"""
#import regex module
import re

#specify a target string to operate regex evaluations on
exampleString = """
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
"""
#N.B: the 'r' preceding the 1st backtick inside parenthesis of re.findall TELL Python this is a regular expression
#This regular expression below searched for any whole numbers which are 1 to 3 digits in length.
ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(names)
print(ages)

#zip both lists into one sequence of tuple pairs using zip() function
#this specific zip will be [(<name>, <age>), (<name>, <age>)......]
peopleDict = zip(names, ages)

print(list(peopleDict))
for elem in peopleDict:
    print(elem)
