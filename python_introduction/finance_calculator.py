monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.5)

print("Your monthly income is", monthly_income)
print("Your monthly expenses are", monthly_expenses)
print("Your monthly savings are", monthly_savings)
print("Your monthly savings after one year, with interest, is", projected_savings)
