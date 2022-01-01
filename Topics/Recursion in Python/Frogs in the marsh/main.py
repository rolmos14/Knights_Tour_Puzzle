def number_of_frogs(year):
    # base case
    if year == 1:
        return 120  # initial number of frogs
    # recursive case
    return 2 * (number_of_frogs(year - 1) - 50)
