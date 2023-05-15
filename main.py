def step_by_number_of_days(initial_amount, apy, number_of_days):
    return initial_amount * (1 + apy / 365 * number_of_days)


def step_by_month(initial_amount, apy):
    return step_by_number_of_days(initial_amount, apy, 30.44)


def by_month_from_day(initial_amount, apy):
    for i in range(30):
        initial_amount = step_by_number_of_days(initial_amount, apy, 1)
    return step_by_number_of_days(initial_amount, apy, 0.44)


def by_month_from_week(initial_amount, apy):
    for i in range(4):
        initial_amount = step_by_number_of_days(initial_amount, apy, 7)
    return step_by_number_of_days(initial_amount, apy, 2.44)


funct_dict = {
    "day": by_month_from_day,
    "week": by_month_from_week,
    "month": step_by_month
}


def main():
    print("APR Calculator with compound\n")

    initial_amount = None
    while initial_amount is None:
        try:
            print("Enter the initial amount (ex: 1000)")
            initial_amount = float(input("Initial amount : ").replace(",", "."))
        except ValueError as e:
            # traitement de la ValueError
            print("Incorrect value :\n", e)
        except Exception as e:
            # traitement de toutes les autres erreurs
            print("An Error occurred :", e)

    apy = None
    while apy is None:
        try:
            print("Enter the APY in percent (ex: 6.5)")
            apy = float(input("APY  : ").replace(",", "."))/100
        except ValueError as e:
            # traitement de la ValueError
            print("Incorrect value :\n", e)
        except Exception as e:
            # traitement de toutes les autres erreurs
            print("An Error occurred :\n", e)

    period = None
    while period is None:
        try:
            period = input("Period (day, week, month) : ")
            if period not in ["day", "week", "month"]:
                period = None
                raise ValueError("Period must be day, week or month")
        except ValueError as e:
            print("Incorrect value :\n", e)
        except Exception as e:
            print("An Error occurred :\n", e)

    month_funct = funct_dict[period]

    amounts = list()
    for i in range(5*12):
        initial_amount = month_funct(initial_amount, apy)
        amounts.append(initial_amount)

    for i in range(12):
        print(f"Month {(i+1):02d} : {amounts[i]:.2f}    {amounts[i+12]:.2f}    {amounts[i+24]:.2f}    {amounts[i+36]:.2f}    {amounts[i+48]:.2f}")


if __name__ == "__main__":
    main()
