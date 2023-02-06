parentheses = input()

opening_parentheses = []
parentheses_dict = {'(': ')', '{': '}', '[': ']'}

balanced = True

for el in parentheses:
    if el in "({[":
        opening_parentheses.append(el)

    elif not opening_parentheses:
        balanced = False

    else:
        last_open_parenthesis = opening_parentheses.pop()
        if parentheses_dict[last_open_parenthesis] != el:
            balanced = False

    if not balanced:
        break

if balanced and len(opening_parentheses) < 1:
    print("YES")
else:
    print("NO")
