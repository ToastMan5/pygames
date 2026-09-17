import string
from string import digits
from functions import tokenize
from functions import table2dlist

string1 = "11 + 1 + 11 * 44 + 222"
print(string1)
table2dlist(tokenize(string1), "TOKEN", "TYPE")

