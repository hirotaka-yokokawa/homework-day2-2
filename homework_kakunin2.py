def warikan (amount, number_of_people):
    quotient = amount // number_of_people
    remainder = amount % number_of_people

    return f"1人あたり: {quotient}円, 端数: {remainder}円"


def check_warikan():
    parameters = [
        (1500, 3, "1人あたり: 500円, 端数: 0円"),
        (2000, 3, "1人あたり: 666円, 端数: 2円"),
    ]



    for p in parameters:
        amount = p[0]    #0は1500､2000
        number_of_people = p[1]
        expected = p[2]


        result = expected == warikan(amount, number_of_people)


        if result:
            print("OK")
        else:
            print("なにかがおかしいよん")


check_warikan()