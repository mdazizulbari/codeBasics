x = input("Enter number 1: ")
y = input("Enter number 2: ")


try:
    d = int(x) / int(y)
except ZeroDivisionError as ze:
    print("Exception occurred: ", ze)
    d = -1
except TypeError as te:
    print("Exception occurred: ", te)
    d = -1
except Exception as e:
    print("Exception occurred: ", e)
    d = -1

print("Division is: ", d)
