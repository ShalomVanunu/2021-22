
def name_sort(yes_no, name):
    if yes_no:
        print(sorted(name))
    else:
        print(name)
name_sort(False,[2,6,1,5,8])


dict = {} # for key and value - can change
tuple_i = () #for constant - cant changed
list_t = [] # list of arguments - changed

months = ("jan","Feb","March", "April")
month_names =""
for month in months:
    month_names +=month+' |'
print(month_names[:-1])