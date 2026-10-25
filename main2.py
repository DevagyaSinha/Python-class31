def list_sum(lst):
    if lst==[]:
        return 0
    return lst[0]+list_sum(lst[1:])

input("recursive sum - ADD HEAD TO SUM OF TAIL UNTIL EMPTY")
print("list_sum([1,2,3])=",list_sum([1,2,3]))
print("list_sum([4,5,6])=",list_sum([4,5,6]))

lst=[int(x) for x in input("enter any 3 numbers.").split()]
print("sum of the list=",list_sum(lst))