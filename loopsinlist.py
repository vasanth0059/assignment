mylist = ["vasanth","umesh","venu"]
for x in range(len(mylist)):
    print(mylist[x])
for x in mylist:
    print(x)
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1
#list comprehensions
newlist = [l for l in mylist if "a" in x]
newlist = [j for j in mylist]
#newlist with range() specified
newlist = [x for x in range(10)]
#list.sort() it sorts the items in the list alphabetically
#it also sorts numerical values in the list
newlist.sort()
# this sort() function works in the ascending order, if we give another variable as reverse=True, it works in the descending order.
newlist.sort(reverse=True)
# sort() functionn is case sensitive, it prints capital lettered items first
#reverse() function will be used to reverse all the items in a list
newlist.reverse()
#copy() function will copy one list to others
newlist1= newlist.copy()
#another method to copy list is to use the function list()
newlist2=list(newlist)
# joining two list
""" list1+list2
for x in list2:
    list1.append(x)
list1.extend(list2)"""

