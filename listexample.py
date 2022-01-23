fruits=['mango','orange','banana']
print(fruits)
print(fruits[1])
fruits[0]='jambura'
print(fruits)
fruits.append('grapes')
print(fruits)
fruits.insert(1,'mango')
print(fruits)
fruits.extend(['cherry','apple','mango','banana'])
print(fruits)
temp=fruits.copy()
print(temp)
print(temp.count('banana'))
print(temp.index('banana'))
temp.remove('banana')
print(temp)
temp.reverse()
print(temp)
temp.sort()
print(temp)
del temp[4]
print(temp)
print(len(temp))
fruits.extend(temp)
print(fruits)
print(len(fruits))
temp.clear()
print(temp)
# cars=[]
# n=int(input('how many cars :'))
# for x in range(n):
#     c=input('enter a car name :')
#     cars.append(c)

# print(cars)

print(fruits)
print(fruits[-1])
print(fruits[-3])
print(fruits[0:4])
print(fruits[:4])
print(fruits[4:8])
print(fruits[8:])


nums=list(range(10))
print(nums)
print(sum(nums))
print(max(nums))
print(min(nums))
avg=sum(nums)/len(nums)
print(avg)

print(dir(fruits))
print(fruits.pop())
print(fruits.pop(1))

for data in fruits:
    print(data)

# list1=[]
# for i in range(5):
#     list1.append(i*i)
# print(list1)

#list compehension
list1=[i*i for i in range(5)] 
print(list1)

list2=[2**i for i in range(10)] 
print(list2)