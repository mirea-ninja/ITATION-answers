def solution(number: int) -> None:
    alphabet = "abcdefghijklmnopqrstuvwxy_1234567890{}"
    row, col = map(int, number)
    index = (row - 1) * 6 + (col - 1)
    return alphabet[index]


if __name__ == "__main__":
    data = "32 23 32 24 11 71 51 66 43 52 11 36 55 52 11 53 31 66 41 42 52 42 22 55 36 55 52 55 54 65 61 14 13 13 14 65 64 55 62 72".split()
    print("".join(solution(num) for num in data))
