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
    category = input('Enter "M" for Monthly salary and "Y" for Yearly salary: ').upper()

    if category not in category_dict:
        raise ValueError('Invalid input. Enter "M" or "Y".')

    try:
        salary = int(input(f'Enter your {category_dict[category]} salary: '))
    except ValueError:
        raise ValueError('Invalid input. Enter an integer value for salary.')

    return salary, category
