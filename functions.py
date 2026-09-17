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
            #print(f"{expression[i]} is in group 'digit', {i=}")
            if i == 0 or i == len(expression)-1: #possible out of range error
                if i == 0 and expression[i+1] in tokens["terminator"]: #one digit number (at start of string)
                    number = expression[i]  # declare number string variable as that digit
                    #print("start of string")
                    expression_list.append([int(number), "digit"])
                if i == 0 and expression[i+1] in tokens["digit"]: #start of multi digit number (start of string)
                    number = expression[i]
                    #print("start of string")
                if i == len(expression)-1: # end of a number / single number at (end of string)
                    if expression[i-1] in tokens["terminator"]: #single number (at end of string)
                        number = expression[i]  # declare number string variable as that digit
                        #print("end of string")
                        expression_list.append([int(number), "digit"])
                    if expression[i-1] in tokens["digit"]: #end of multi digit number (at end of string)
                        number += expression[i]
                        #print("end of string")
                        expression_list.append([int(number), "digit"])
            elif expression[i-1] in tokens["terminator"] and expression[i+1] in tokens["digit"]: #if character before is not a digit, and the character after is a digit, then that means this is the start of a two/more digit number
                #print(f"{number=}, {i=}, start of multi")
                number = expression[i]  # declare number string variable as that digit
                #print(f"{number=}, {i=}, start of multi")
            elif expression[i-1] in tokens["digit"] and expression[i+1] in tokens["digit"]: #if digit before and after is digit, then it's in between first and last digit of a number
                #print(f"{number=}, {i=}, between multi")
                number += expression[i]
                #print(f"{number=}, {i=}, between multi")
            elif expression[i-1] in tokens["digit"] and expression[i+1] in tokens["terminator"]: #end of a multi
                number += expression[i]
                expression_list.append([int(number), "digit"])
            elif expression[i-1] in tokens["terminator"] and expression[i+1] in tokens["terminator"]: #one digit number
                number = expression[i]  # declare number string variable as that digit
                #print(f"{number=}, {i=}, one digit")
                expression_list.append([int(number), "digit"])
        if expression[i] in tokens["operator"]:
            #print(f"{expression[i]} is in group 'operator', {i=}")
            expression_list.append([expression[i], "operator"])
        if expression[i] in tokens["punctuator"]:
            expression_list.append([expression[i], "punctuator"])
            #print(f"{expression[i]} is in group 'punctuator', {i=}")
    return expression_list
tokens = {
    "digit": string.digits,
    "operator": "*+-/",
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