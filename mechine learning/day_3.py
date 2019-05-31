'''s="Mechine_Learning"
for si in range(0,5):
    print(s[si])
a=s.split("_")
print(a)
b=s.find("l")
print(b)
print("========= ======")
c= "i" in s
print(c)
print("======= ========")
d=s[:-9]
print(d)
print("===============")
e=s[-10::-1]
print(e)
print("===============")
f=s[-1:-9:-1]
print(f)
print("===============")
g=s[-1::-2]
print(g)
print("============ ===")
a="10"
print(a*3)
print(a+"3")
print(type(a))
print("===============")
print(id(a))
print("===============")
h=s.startswith("M")
print(h)
print("========= ======")
print(s.endswith("g"))
print("===============")
li=["name","roll no.","email","marks ","phone number :"]
print(li[-1])
print("======== =======")
for i in range(0,3):
    print(li[i])
print("===============")
print(max(li))
print("===============")
print(min(li))
print("===============")
'li1=[12,34,5,60]'''
'''li1.append(13)
print(li1)
li1.extend([12,56])
print(li1)
li1.insert(1,123)
print(li1)
li1.replace(34,"mahesh")
print(li1)

'count=0
'li=[78]
'print(li1<li)
'for i in li1:
 '   count+=1
'print(count)'''
d={"key":"values","key2":"values2"}
(d.update({"key":"mahesh"}))
print(d)
