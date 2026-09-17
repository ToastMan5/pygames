def table2dlist(array, title1, title2):
    print("-"*20)
    print(f"{title1}    | {title2}")
    for row in array:
        a = row[0]
        b = row[1]
        print(f"{a:<8} | {b}")