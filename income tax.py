income=float(input("please enter your income"))
dependants=int(input("please enter the number of dependants"))
taxable_income=income-10000-3000*dependants
tax=0.2*taxable_income
print("your income tax amount is ",tax)
