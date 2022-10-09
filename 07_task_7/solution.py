import requests


def solution() -> None:
    url = "https://itation.mirea.ninja/api/v1/quest"
    request = requests.get(f"{url}?key=l0v3_IIT")
    response = request.json()
    print(response)
    print(request.headers["x-ninja-key"])


if __name__ == "__main__":
    solution()
