
def oranges(big_cups=10, small_cups=7):
    print(f"number on small {small_cups} and Big cups {big_cups}")

oranges(12,130)


#Global
c = [1,2,3,45,5]

def foo3():
    c.append(55)
    c[3] = 55
    print(c)

foo3()
print(c)