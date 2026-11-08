import string
from string import digits


def tokenize(expression: str)-> list:
    """
    :param expression:
    :returns: a 2d array containing arrays of tokens followed by their token type
    """
    global number
    number = 0
    expression_list = []
    for i in range(len(expression)):
        if expression[i] in tokens["digit"]:  # if char at index I is a digit -->
            if i == 0 or i == len(expression)-1: #possible out of range error
                if i == 0 and (expression[i+1] in tokens["terminator"] or expression[i+1] in tokens["operator"]): #one digit number (at start of string)
                    number = expression[i]  # declare number string variable as that digit
                    expression_list.append([float(number), "number"])
                if i == 0 and expression[i+1] in tokens["digit"]: #start of multi digit number (start of string)
                    number = expression[i]
                if i == len(expression)-1: # end of a number / single number at (end of string)
                    if expression[i-1] in tokens["terminator"] or expression[i-1] in tokens["operator"]: #single number (at end of string)
                        number = expression[i]  # declare number string variable as that digit
                        expression_list.append([float(number), "number"])
                    if expression[i-1] in tokens["digit"]: #end of multi digit number (at end of string)
                        number += expression[i]
                        expression_list.append([float(number), "number"])
            elif (expression[i-1] in tokens["terminator"] or expression[i-1] in tokens["operator"]) and expression[i+1] in tokens["digit"]: #if character before is not a digit, and the character after is a digit, then that means this is the start of a two/more digit number
                number = expression[i]  # declare number string variable as that digit
            elif expression[i-1] in tokens["digit"] and expression[i+1] in tokens["digit"]: #if digit before and after is digit, then it's in between first and last digit of a number
                number += expression[i]
            elif expression[i-1] in tokens["digit"] and (expression[i+1] in tokens["terminator"] or expression[i+1] in tokens["operator"]): #end of a multi
                number += expression[i]
                expression_list.append([float(number), "number"])
            elif (expression[i-1] in tokens["terminator"] or expression[i-1] in tokens["operator"]) and (expression[i+1] in tokens["terminator"] or expression[i+1] in tokens["operator"]): #one digit number
                number = expression[i]  # declare number string variable as that digit
                expression_list.append([float(number), "number"])
        if expression[i] in tokens["operator"]:
            expression_list.append([expression[i], "operator"])
        if expression[i] in tokens["punctuator"]:
            expression_list.append([expression[i], "punctuator"])
    return expression_list
tokens = {
    "digit": string.digits,
    "operator": "*+-/^",
    "punctuator": "()",
    "terminator": " ,"
}

def table2dlist(array, title1, title2):
    print("-"*20)
    print(f"{title1}    | {title2}")
    for row in array:
        a = row[0]
        b = row[1]
        print(f"{a:<8} | {b}")
