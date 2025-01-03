category_dict = {
    'M': 'Monthly',
    'Y': 'Yearly'
}

tax_brackets = [
    (600000, 0),
    (1200000, 0.05),
    (2200000, 0.15),
    (3200000, 0.25),
    (4100000, 0.30),
    (float('inf'), 0.35)
]


def get_salary() -> tuple[int, str]:
    """
    Prompts the user to enter their salary and its category (Monthly or Yearly).

    Returns:
        tuple[int, str]: A tuple containing the salary as an integer and the category as a string.

    Raises:
        ValueError: If the input category is not 'M' or 'Y'.
        ValueError: If the salary input is not an integer.
    """
    while True:
        category = input('Enter "M" for Monthly salary and "Y" for Yearly salary: ').upper()

        if category in category_dict:
            break

        print('Invalid input. Enter "M" or "Y".')

    while True:
        salary = input(f'Enter your {category_dict[category]} salary: ')

        if salary.isdigit() and int(salary) > 0:
            break

        print('Invalid input. Enter an integer value for salary.')

    return int(salary), category


def convert_amount(amount: int, to_yearly: bool) -> int:
    """
    Converts the given amount between monthly and yearly values.

    Args:
        amount (int): The amount to be converted.
        to_yearly (bool): If True, converts the amount to yearly. If False, converts the amount to monthly.

    Returns:
        int: The converted amount, rounded to the nearest integer.
    """
    return round(amount * 12 if to_yearly else amount / 12)


def calculate_yearly_income_tax(yearly_salary: int) -> int:
    """
    Calculates the yearly income tax based on the given yearly salary.

    Args:
        yearly_salary (int): The yearly salary for which the income tax is to be calculated.

    Returns:
        int: The calculated yearly income tax, rounded to the nearest integer.
    """
    yearly_income_tax, previous_bracket_limit = 0, 0

    for bracket_limit, tax_rate in tax_brackets:
        if yearly_salary <= bracket_limit:
            yearly_income_tax = yearly_income_tax + (yearly_salary - previous_bracket_limit) * tax_rate
            break

        yearly_income_tax = yearly_income_tax + (bracket_limit - previous_bracket_limit) * tax_rate
        previous_bracket_limit = bracket_limit

    return round(yearly_income_tax)


def main() -> None:
    """
    Main function to calculate and display monthly and yearly salaries
    along with income tax deductions.

    - Accepts salary and category (Monthly 'M' or Yearly 'Y') from the user.
    - Converts salary between monthly and yearly based on the category.
    - Calculates and displays income tax for both monthly and yearly salaries.
    - Prints salary details before and after tax.

    Returns:
        None
    """
    salary, category = get_salary()

    yearly_salary = convert_amount(salary, to_yearly=(category == 'M'))
    monthly_salary = convert_amount(yearly_salary, to_yearly=False)

    yearly_income_tax = calculate_yearly_income_tax(yearly_salary)
    monthly_income_tax = convert_amount(yearly_income_tax, to_yearly=False)

    print(f'\n{category_dict.get("M")} salary {monthly_salary} PKR')
    print(f'Monthly income tax {monthly_income_tax} PKR')
    print(f"Your monthly salary after tax {monthly_salary - monthly_income_tax} PKR")

    print(f'\n{category_dict.get("Y")} salary {yearly_salary} PKR')
    print(f'Yearly income tax {yearly_income_tax} PKR')
    print(f"Yearly salary after tax {yearly_salary - yearly_income_tax} PKR")


if __name__ == '__main__':
    main()
