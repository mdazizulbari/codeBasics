monthly_sales = [42,38,33,38,40,45]
months = ["Jan","Feb","March","April","May","June"]

threshold = 35

# for sales_amount in monthly_sales:
#     if sales_amount < threshold:
#         print(f"Salse amount {sales_amount} is less than the threshold")
#         break
#     else:
#         print(f"Salse amount {sales_amount} is greater than the threshold")

for sales_amount, month in zip(monthly_sales, months):
    if sales_amount < threshold:
        print(f"Salse amount {sales_amount} is less than the threshold in {month}")
        break
    else:
        print(f"Salse amount {sales_amount} is greater than the threshold in {month}")

for i in range(5):
    print(i)
else:
    print("For loop terminated")