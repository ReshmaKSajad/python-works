def unique_list(l):
    list=[]
    for a in l:
        if a not in list:
            list.append(a)
    return list
print(unique_list([1,2,3,2,6,5,4,9,10,3,4,5,6,7,8]))



def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique_list([1,2,3,3,3,3,4,6,6,9,34,5]))


def unique_list(lst):
    list=[]
    for i in lst:
        if i not in list:
            list.append(i)
    return list
print(unique_list([1,1,1,2,2,3,3,3,4,4,5,5,5,6,6,6,7,7,7,8,8,9,9]))

















