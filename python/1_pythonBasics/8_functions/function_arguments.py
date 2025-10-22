def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

total = sum_all(1,2,3,4,5)
# print(total)

def company_info(**kwargs):
    # if "ticker" in kwargs:
    #     print("Ticker:", kwargs["ticker"])
    # if "ceo" in kwargs:
    #     print("CEO:", kwargs["ceo"])
    # if "revenue" in kwargs:
    #     print("Revenue:", kwargs["revenue"])
    for key in kwargs:
        print(key, kwargs[key])

company_info(ticker='AAPL', ceo="Tim Cook", revenue="200 billion", pe = 20)

def find_square(a):
    return a * a
# find_square(5)
x = lambda a: a*a
print(x(5)) #shortcut way