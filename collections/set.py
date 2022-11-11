#set- elements in the set are unique...it is enclosed in the curly brackets
      #operations such as intersection, union,difference are possible in set
set1={1,2,4,6,76,9,34,5}
set2={2,4,6,8,90,1,4,5,6,12}
print(set1.union(set2))        #includes all elements without repetition
print(set1.intersection(set2))   #includes the common elements in 2 sets
print(set1.difference(set2))     #includes elements in set1 and exclude elements in set2
print(set2.difference(set1))     #includes elements in set2 and excludes elements in set1
print(set1.symmetric_difference(set2))  #includes elements in any one of the sets

print(len(set1))   #length is calculated by avoiding the repeted elements
