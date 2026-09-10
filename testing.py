import string
from string import digits


def tokenize(expression):
    expression_list = []
    for i in range(len(expression)):
        if expression[i] in tokens["digit"]:  # if char at index I is a digit -->
            print(f"{expression[i]} is in group 'digit'")
            number = expression[i]  # declare number string variable as that digit
            if i < len(expression):
                j = i + 1
                while expression[j] in tokens["digit"] and j != len(expression):
                    number = number + expression[j]
                    j += 1
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

