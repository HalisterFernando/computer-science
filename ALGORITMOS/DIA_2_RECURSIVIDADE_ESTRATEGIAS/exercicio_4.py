def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


if __name__ == "__main__":
    print(mdc(16, 36))
