import re


def solution(substring: str) -> None:
    ninja_pattern = re.compile(r"ninja{[a-z0-9!@#$%^&*_\-+=|\/?.,:;\"~]{1,}}")
    symbols = '{}[]()<>!@#$%^&*_-+=|\/?.,:;"~'

    # находим все такие подстроки
    ninja_substrings = ninja_pattern.findall(substring)

    # оставляем только те, которые не содержат заглавных букв
    ninja_substrings = [
        substring for substring in ninja_substrings if substring.lower() == substring
    ]

    # # оставляем только те, которые содержат не более 5 спец. символов
    ninja_substrings = [
        substring
        for substring in ninja_substrings
        if len([symbol for symbol in substring if symbol in symbols]) <= 5
    ]

    # содержит 10 цифр
    ninja_substrings = [
        substring
        for substring in ninja_substrings
        if len([symbol for symbol in substring if symbol.isdigit()]) == 10
    ]

    print(ninja_substrings)


if __name__ == "__main__":
    data = open("source.txt", "r", encoding="utf-8").read()
    solution(data)
