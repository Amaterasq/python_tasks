def backspace(string) -> str:
    string = list(string)
    string.reverse()
    stars = 0
    for i in string:
        if i == '*':
            stars += 1
            string[i] = None
    else:
        if stars > 0:
            stars -= 1
            string[i] = None
    string.reverse()
    return string


print(backspace('aa*bb*'))
print(backspace('aa**bb*'))

# assert backspace('aa*bb*') == "ab"
# assert backspace('aa**bb*') == "b"
# assert backspace('help**sos*') == 'heso'
# assert backspace('*aa') == 'aa'
