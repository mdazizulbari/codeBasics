def find_total(expenses):
    '''
    :param expenses: input list containing numbers
    :return: total sum of all numbers in the input list
    '''
    total = 0
    for expense in expenses:
        total += expense
    return total

expenses_sergey = [30,45,70,90]
expenses_sundar = [40,23,10,85]

# total_expenses_sergey = 0
# for expense in expenses_sergey:
#     total_expenses_sergey += expense
# print(total_expenses_sergey)
#
# total_expenses_sundar = 0
# for expense in expenses_sundar:
#     total_expenses_sundar += expense
# print(total_expenses_sundar)

print(find_total(expenses_sergey))
print(find_total(expenses_sundar))
print(help(find_total))
total_sundar = sum(expenses_sundar)
print(total_sundar)

