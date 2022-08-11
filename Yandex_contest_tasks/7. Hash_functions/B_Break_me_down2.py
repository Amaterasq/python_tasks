import random


def polynom_hash(s, q, R):
    res = 0
    for sym in s:
        res = (res * q + ord(sym))
    return res % R


def main():
    q = 1000
    R = 123_987_123
    print(
        polynom_hash('ezhgeljkablzwnvuwqvp', q, R)
        == polynom_hash('gbpdcvkumyfxillgnqrv', q, R)
    )

    s1 = list('ezhgeljkablzwnvuwqvp')
    s2 = list('gbpdcvkumyfxillgnqrv')

    while True:
        random.shuffle(s1)
        random.shuffle(s2)

        if polynom_hash(''.join(s1), q, R) == polynom_hash(''.join(s2), q, R):
            print(''.join(s1))
            print(''.join(s2))
            break


if __name__ == '__main__':
    main()
