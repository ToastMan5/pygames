import string
from string import digits


def tokenize(expression):
    expression_list = []
    for i in range(len(expression)):
        if expression[i] in tokens["digit"]:  # if char at index I is a digit -->
            print(f"{expression[i]} is in group 'digit'")
            number = expression[i]  # declare number string variable as that digit
            if expression[i-1] is not in tokens["digit"] and expression[i+1] in tokens["digit"]: #if character before is not a digit, and the character after is a digit, then that means this is the start of a two/more digit number
                pass
            if expression[i-1] in tokens["digit"] and expression[i+1] in tokens["digit"]: #if digit before and after is digit, then it's in between first and last digit of a number
                pass
            if expression[i] in tokens["digit"]





                number = number + expression[j]
            number = int(number)
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

