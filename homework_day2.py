def hello():
    print("hello world")


def say_hello(name):
    print(f"Hi {name}")


say_hello("Bob")
say_hello("Tom")


def double(number):
    return 2 * number


print(double(1))
print(double(2))
print(double(3))


def warikan(amount, number_of_people):
    quotient = amount // number_of_people
    remainder = amount % number_of_people

    return f"1人あたり: {quotient}円, 端数{remainder}円"


print(warikan(amount=200, number_of_people=3))

