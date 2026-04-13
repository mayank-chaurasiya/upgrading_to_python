"""Calculate and print a salary summary."""

LEAVE_ALLOWANCE = 2
LEAVE_DEDUCTION_AMOUNT = 250


def calculate_allowance(base_salary):
    """Return the total allowance based on salary components."""
    hra = base_salary * 0.08
    food_allowance = base_salary * 0.12
    travel_allowance = base_salary * 0.15
    dearness_allowance = base_salary * 0.09
    return hra + food_allowance + travel_allowance + dearness_allowance


def calculate_leave_deduction(leaves):
    """Return the deduction for extra leaves."""
    if leaves > LEAVE_ALLOWANCE:
        return (leaves - LEAVE_ALLOWANCE) * LEAVE_DEDUCTION_AMOUNT
    return 0


def calculate_tax(base_salary):
    """Return the tax amount for the given salary."""
    if base_salary <= 20000:
        return 0
    if base_salary <= 40000:
        return (base_salary - 20000) * 0.05
    if base_salary <= 70000:
        return (20000 * 0.05) + (base_salary - 40000) * 0.10
    if base_salary <= 105000:
        return (20000 * 0.05) + (30000 * 0.10) + (base_salary - 70000) * 0.25
    if base_salary <= 120000:
        return (
            (20000 * 0.05)
            + (30000 * 0.10)
            + (35000 * 0.25)
            + (base_salary - 105000) * 0.30
        )
    return (
        (20000 * 0.05)
        + (30000 * 0.10)
        + (35000 * 0.25)
        + (15000 * 0.30)
        + (base_salary - 120000) * 0.35
    )


def main():
    """Collect input, calculate salary values, and print the summary."""
    base_salary = float(input("Enter your salary : "))
    leaves = int(input("Enter no. of leaves you took : "))

    total_allowance = calculate_allowance(base_salary)
    leave_deduction = calculate_leave_deduction(leaves)
    tax = calculate_tax(base_salary)

    gross_salary = base_salary + total_allowance
    net_salary = gross_salary - tax - leave_deduction

    print("------------------------------------------")
    print("Base Salary : ", base_salary)
    print("Total Allowance : ", total_allowance)
    print("Gross Salary : ", gross_salary)
    print("Taxes : ", tax)
    print("Leaves Deducted : ", leave_deduction)
    print("------------------------------------------")
    print("Net Salary : ", net_salary)
    print("------------------------------------------")


if __name__ == "__main__":
    main()
