def trim_and_repeat(string, offset=0, repetitions=1):
    """
    Обрезает строку слева на offset символов и повторяет её repetitions раз.
    """
    trimmed = string[offset:]
    return trimmed * repetitions


if __name__ == "__main__":
    print(trim_and_repeat("Hello, World!")) 
    print(trim_and_repeat("Hello, World!", 7))
    print(trim_and_repeat("Hello, World!", 7, 3))
    print(trim_and_repeat("abcdef", 2, 2))
