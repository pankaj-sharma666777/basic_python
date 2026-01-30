string_1 = "12345"
list_1 = [1,2,3,4,5]
tuple_1 = (1,2,3,4,5)
dict_1 = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7}
set_1 = {1,2,3,4,5,6,7}

print(string_1[2])
print(list_1[3])
print(tuple_1[1])
print(tuple_1[-1])
print(tuple_1[-2:4],"")

print(string_1[-2])
print(string_1[2:5])
print(string_1[-1])
print(list_1[-3])
print(list_1[:3])

print(len(string_1))
print(len(list_1))
print(len(tuple_1))
print(len(dict_1))
print(len(set_1))
string_1 += "8"
list_1.append(8)
set_1.add(8)
dict_1["eight"]=8
print(string_1)
print(list_1)
print(set_1)
print(dict_1)

s="python"
name="pankaj"
print(s,name,"      ", "hgjgkg")

print(s+name)
print(s*6)
print(s.replace("y","gh"))
print(s.upper())       
print(s.lower())        
print(s.capitalize())   
print(s.replace("p", "q"))  
print(s.split("t"))    

x=list_1.pop(4)
y=list_1.pop(0)
print(x,y)

list_1sorted =list_1.sort()
print(list_1sorted)
list_1.reverse()
len(list_1)
sum(list_1)



print(tuple_1.count(2))
print(tuple_1.index(3))


string_2 = "london"
list_2 = ["L","O","N","D","O","N"]
tuple_2 =("L","O","N","D","O","N")
c1= string_2.count("n")
c2= list_2.count("N")
c3= tuple_2.count("N")

print(c1,c2,c3)

set_2 ={10,11,12}
dict_2 ={"nine":9,"ten":10,"elevan":11,}

set_1.update(set_2)
dict_1.update(dict_2)

print(set_1)
print(dict_1)