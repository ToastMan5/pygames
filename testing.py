import string
from string import digits


def tokenize(expression):
    global number
    number = 0
    expression_list = []
    for i in range(len(expression)):
        if expression[i] in tokens["digit"]:  # if char at index I is a digit -->
            print(f"{expression[i]} is in group 'digit'")
            if i == 0 or i == len(expression)-1: #possible out of range error
                if i == 0 and expression[i+1] not in tokens["digit"]: #one digit number (at start of string)
                    number = expression[i]  # declare number string variable as that digit
                    expression_list.append([int(number), "digit"])
                if i == 0 and expression[i+1] in tokens["digit"]: #start of multi digit number (start of string)
                    number = expression[i]
                if i == len(expression)-1: # end of a number / single number at (end of string)
                    if expression[i-1] not in tokens["digit"]: #single number (at end of string)
                        number = expression[i]  # declare number string variable as that digit
                        expression_list.append([int(number), "digit"])
                    if expression[i-1] in tokens["digit"]: #end of multi digit number (at end of string)
                        number += expression[i]
                        expression_list.append([int(number), "digit"])


            elif expression[i-1] not in tokens["digit"] and expression[i+1] in tokens["digit"]: #if character before is not a digit, and the character after is a digit, then that means this is the start of a two/more digit number
                number = expression[i]  # declare number string variable as that digit
            elif expression[i-1] in tokens["digit"] and expression[i+1] in tokens["digit"]: #if digit before and after is digit, then it's in between first and last digit of a number
                    number += expression[i]
            elif expression[i-1] not in tokens["digit"] and expression[i+1] not in tokens["digit"]: #one digit number
                number = expression[i]  # declare number string variable as that digit
                expression_list.append([int(number), "digit"])



            expression_list.append([number, "digit"])
        if expression[i] in tokens["operator"]:
            print(f"{expression[i]} is in group 'operator'")
            expression_list.append([expression[i], "operator"])
        if expression[i] in tokens["punctuator"]:
            expression_list.append([expression[i], "punctuator"])
            print(f"{expression[i]} is in group 'punctuator'")
    return expression_list



tokens = {
    "digit": string.digits,
    "operator": "*+-/",
    "punctuator": "()"
}
#print(tokens)

string = "1 + 11 * 44 + 2"
print(tokenize(string))





# #expression = input("Enter your expression: ")
# expression = "1 + 11 * 44 + 2"
# print(expression)
#
# expression = expression.replace(" ", "")
# print(f"{expression=}")
# for i in range(len(expression)):
#     match expression[i]:
#         case '('|')':
#             if expression[i] == '(':
#                 pass
#             if expression[i] == ')':
#                 pass
#         case '*'|'x'|'X':
#             for j in range(i-1, 0, -1):
#                 print(f"{expression[j]=}")
#                 print(f"{j=}")
#         case '/':
#             pass
#         case '+':
#             pass
#         case '-':
#             pass
#     pass

