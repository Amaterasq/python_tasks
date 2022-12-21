def backspace(string) -> str:
    string = list(string)
    string.reverse()
    stars = 0
    for id, i in enumerate(string):
        if i == '*':
            stars += 1
            string[id] = ''
        else:
            if stars > 0:
                stars -= 1
                string[id] = ''
    string.reverse()
    return ''.join(string)


print(backspace('aa*bb*'))

# assert backspace('aa*bb*') == "ab"
# assert backspace('aa**bb*') == "b"
# assert backspace('help**sos*') == 'heso'
# assert backspace('*aa') == 'aa'
