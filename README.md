# Salary and Tax Calculator

This Python project calculates and displays monthly and yearly salaries along with income tax deductions. It accepts salary and category (Monthly 'M' or Yearly 'Y') from the user, converts salary between monthly and yearly based on the category, calculates and displays income tax for both monthly and yearly salaries, and prints salary details before and after tax.

## Features

- Accepts salary and category (Monthly 'M' or Yearly 'Y') from the user.
- Converts salary between monthly and yearly based on the category.
- Calculates and displays income tax for both monthly and yearly salaries.
- Prints salary details before and after tax.

## Tax Brackets

The tax brackets used in this project are as follows:

| Yearly Salary (PKR)      | Tax Rate |
|--------------------------|----------|
| 0 - 600,000              | 0%       |
| 600,001 - 1,200,000      | 5%       |
| 1,200,001 - 2,200,000    | 15%      |
| 2,200,001 - 3,200,000    | 25%      |
| 3,200,001 - 4,100,000    | 30%      |
| 4,100,001 and above      | 35%      |

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/engr-abdulmoeed/salary-tax-calculator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd salary-tax-calculator
    ```

### Usage

Run the `main.py` file to start the program:
```sh
python main.py
