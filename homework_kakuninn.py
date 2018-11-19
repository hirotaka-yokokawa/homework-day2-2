def warikan(amount: int, number_of_people: int):
    quotient = amount / number_of_people
    remainder = amount % number_of_people

    return f"1人あたり{quotient}円, 端数{remainder}円"

check_result = warikan(1500,3) == "1人あたり: 500円, 端数: 0円"

print(check_result)


print(warikan(3000, 5))
# 商が小数点まで記載されているので意図した成果物と異なる｡

