# n=input("Enter a number: ")
# n = int(n)

# if n%2==0:
#     print(f"{n} is an even number.")
# else:
#     print(f"{n} is an odd number.")

# message = "Number is even" if n%2==0 else "Number is odd"
# print(message)

# if not n%2==0:
#     print(f"{n} is an odd number.")
# else:
#     print(f"{n} is an even number.")
#
# p = 8
# if p > 10 and n % 2 == 0:
#     print("Yay")
# else:
#     print("No")

indian = ["samosa","daal","naan"]
chinese = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta","risotto"]

dish = input("Enter a dish: ")

if dish in indian:
    print(f"{dish} is indian")
elif dish in chinese:
    print(f"{dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print("I don't know which cusine is this")