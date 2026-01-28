my_list = [1,2]
print(my_list)
print(my_list)
print(my_list)
print(my_list)
print(my_list)
print(type(my_list))

mylist_2 = [1,2,3,"apple","banana",13,25,"a","b",13.5]
mylist_3 = [1,2,3,[1,2,3],"apple","banana",["apple","banana"]]
print(type(mylist_2))
print(type(mylist_3))


# tuple      tuples are immutable
mytuple = (1,2,3,4,5,7,8)
print(type(mytuple))
mytuple_2 =(1,2,3,"apple","banana",13,25,"a","b",13.5)
print(type(mytuple_2))
mytuple_3 = (1,2,3,[1,2,3],"apple","banana",["apple","banana",["apple","banana"]])
mytuple_4 = (5,)
print(type(mytuple_2),"mytupl_2")
print(type(mytuple_3),"mytupl_3")
print(type(mytuple_4),"mytupl_4")
print(type(mytuple),"mytuple")


# dictionary         can have multiple value for a single key
                #    -->keys should be immutable datatype
mydict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6}
print(type(mydict))
mydict_E = {}
print(type(mydict_E))
 
mydict_2 = {"january":31,"february":28, "march":31}
print(type(mydict_2))

mydict_3 = {"name":"pankaj","surname":"sharma","job":"unemployed","job":"software developer"}
print(type(mydict_3))
print("mydict_3['job']: ", mydict_3["job"])
      



                           # sets
myset ={1,2,3,4,5}
myset_2 = {"a","b","c","d"}
print(type(myset))
print(type(myset_2),"myset_2")
myset_3 = {1,2,2,3,3,3,3,4,4,5,}
print(myset_3,"myset_3")
print(type(myset))
print(type(myset))
print(type(myset))
