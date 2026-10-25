input("Head-Tail - head is list of 0 and tail is list of 1:. Base case is []")
print("[10,20,30] , Head=",[10,20,30][0],"Tail=",[10,20,30][1:])
print("[5,15,25] , Head=",[5,15,25][0],"Tail=",[5,15,25][1:])
print("[a,b,c] , Head=",['a','b','c'][0],"Tail=",['a','b','c'][1:])

lst=[int(x) for x in input("enter any 3 numbers.").split()]

input("head:list =[0], tail:list=[1:]")
print("head=",lst[0])