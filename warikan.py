def warikan(amount, number_of_people):
    payment, franction = divmod(amount, number_of_people)

    return f"1人あたり: {payment}円, 端数: {franction}円"
