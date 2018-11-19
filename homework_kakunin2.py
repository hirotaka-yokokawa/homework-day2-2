def warikan (amount, number_of_people):
    quotient = amount // number_of_people
    remainder = amount % number_of_people

    return f"1人あたり: {quotient}円, 端数:{remainder}円"


def check_warikan():
    parameters = [(1500, 3 "1人あたり: 500円, 端数: 0円"), (2000, 3 "1人あたり: 666円, 端数: 2円"),]


    for p in parameters:
