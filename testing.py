import string
from platform import ios_ver
from string import digits
from functions import *

def interpret_math(tokenes: list[list[str]]):
    multiplicatives = 0
    operators = 0
    print(tokenes)
    print(operators)
    for j in range(len(tokenes)):  # check how many multiplicatives there are
        if tokenes[j][0] == "*" or tokenes[j][0] == "/":
            multiplicatives  += 1
    for i in range(len(tokenes)):
        if i < len(tokenes):
            if tokenes[i][1] == "operator":
                operators += 1
                left = int(tokenes[i-1][0])
                right = int(tokenes[i+1][0])
                match tokenes[i][0]:
                    case "*":
                        tokenes[i][0] = left * right
                        tokenes[i][1] = "number"
                        tokenes.pop(i-1), tokenes.pop(i)
                    case "/":
                        tokenes[i][0] = left / right
                        tokenes[i][1] = "number"
                        tokenes.pop(i-1), tokenes.pop(i)
                    case "+":
                        if multiplicatives == 0:
                            tokenes[i][0] = left + right
                            tokenes[i][1] = "number"
                            tokenes.pop(i-1), tokenes.pop(i)
                        else:
                            i += 1
                    case "-":
                        if multiplicatives == 0:
                            tokenes[i][0] = left - right
                            tokenes[i][1] = "number"
                            tokenes.pop(i-1), tokenes.pop(i)
                        else:
                            i += 1
    #for i in range(len(tokenes)):

    if operators == 0:
        print("sucess")
        return tokenes[0][0]
    else:
        return interpret_math(tokenes)


string1 = "11 + 1 + 2 * 44 + 222"
print(string1)
table2dlist(tokenize(string1), "TOKEN", "TYPE")
print(interpret_math(tokenize(string1)))

