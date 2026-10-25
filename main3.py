def list_max(lst):
    if len(lst)==1:
        return lst[0]
    rest=list_max(lst[1:])
    return lst[0] if lst[0]>rest else rest

print("lst[3,7,2]",list_max([3,7,2]))
print("lst{3,5,8}",list_max([3,5,8]))
