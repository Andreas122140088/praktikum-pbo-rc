key=input("Key : ")
key=int(key)
for i in range(key):
  name=input("Name "+ str(i+1) +" : ")
  grade=int(input("Grade "+str(i+1)+" : "))
  grade_dict[name]=grade
print("Grade : "+ str(grade_dict))
