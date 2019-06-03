# total_cost = 1,000,000
portion_down_payment = 0.25
# current_savings = 0
# current_savings*r/12
r = 0.04
# portion_saved = 0.10
# annual_salary = 120,000   
print("got here")

annual_salary = int(input("What is your annual salary? "))
portion_saved = float(input("Enter the percent of your salary to save as a decimal "))
total_cost = float(input("What is the cost of your dream home? "))
current_savings = 0
month = 0
while current_savings < (total_cost * portion_down_payment):
    month = month + 1
    current_savings = (current_savings) + (portion_saved*annual_salary/12) + (current_savings*r/12)
    print(str(month) + str(current_savings)) 
    print("debug interest added" + str(current_savings*r/12))
print(month)


