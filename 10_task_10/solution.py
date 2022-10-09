import base64
import json
import sys


def get_phi(n: int) -> int:
    phi = int(n > 1 and n)
    for p in range(2, int(n**0.5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    if n > 1:
        phi -= phi // n
    return phi


def solution(encrypted_data: str, key: dict) -> None:
    for a, (b, m), (c, d) in zip(encrypted_data, key["common_key"], key["private_key"]):
        x = pow(pow(a, b, m), pow(c, d, get_phi(m)), m)
        c1 = chr((x % m) % 256)
        c2 = chr((x % m) // 256 % 256)
        c3 = chr((x % m) // 65536)

        print(c3, c2, c1, sep="", end="")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: solution.py private_key")
        sys.exit(1)

    print("Enter your encrypted data: ", end="")
    encrypted_data = list(map(int, input().split()))

    with open(sys.argv[1], "rb") as f:
        key = json.loads(base64.b64decode(f.read()))

    solution(encrypted_data, key)
