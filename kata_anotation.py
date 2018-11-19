def hello() -> None:
    print("hello world")

hello()

def say_hello(name: str) -> None:
    print(f"Hi {name}")

say_hello("けんじ")

def double(number: int) -> int:
    return number * 2


def warikan(amount: int, number_of_people: int) -> str:
    quotient = amount // number_of_people
    remainder = amount % number_of_people

    return f"1人あたり{quotient}円, 端数{remainder}円"


print(warikan(amount=5000, number_of_people=20))
