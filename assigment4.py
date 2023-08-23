# 1. What exactly is []?
# '[]' is a symbol of list.

#2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
#third value? (Assume [2, 4, 6, 8, 10] are in spam.)

spam = [2, 4, 6, 8, 10]
spam.insert(3,'&#39;hello&#39;')
print(spam)

spam = ['a','b','c','d']
#3. What is the value of spam[int(int('3'* 2) / 11)]?
# step1---> spam[int((33)/11)]
#step2---> spam[int(3.0)]
# step3----> spam[3]
# therfore spam[3] = 'd'

#4. What is the value of spam[-1]?
# last value in the spam list which is d

#5. What is the value of spam[:2]?
# staring form the first value in the list till 2nd value excluding 2nd value
#which is a,b

bacon = [3.14,'cat',11,'cat',True]
print(bacon)

#6. What is the value of bacon.index('cat')?
# 1 is the output of bacon.index('cat')
print(bacon.index('cat'))

#7. How does bacon.append(99) change the look of the list value in bacon?
# number 99 gets added at the last in the bacon list.
bacon.append(99)
print(bacon)

#8. How does bacon.remove('cat') change the look of the list in bacon?
#bacon.remove('cat') command removes the string cat from the list in the first instance.
bacon.remove('cat')
print(bacon)

#9. What are the list concatenation and list replication operators?
# list concatenation operator is +
# list repetation operator is *

#10. What is difference between the list methods append() and insert()?
# append function adds the element in the list. At the last position by default
# insert adds the element at the mentioned position.

#11. what are the two methods of removing items from a list?
# pop and remove are the two function to remove items from a list

#12.Describe how list values and string values are identical?
# string and list are both mutable entities therefore if we indexing method are same for 
# both string and list.

# 13.What&#39;s the difference between tuples and lists?
# tuples are immutable, They are limited only to some functions
# lists are mutable, COmparitively they have lot of function as compared
# to tuples.

# 14.How do you type a tuple value that only contains the integer 42?
tup=(42,)
print(tup,type(tup))

# 15 How do you get a list value's tuple form? How do you get a tuple value's list form?
# we can convert list into tuple and tuple into a list by the following way
# list(tuple)
# tuple(list)

# 16 Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
# contain?
li = [1,2,3,4,5]
li_a=li
li_a[0]=10000
print(li_a)

# 17 How do you distinguish between copy.copy() and copy.deepcopy()?
# copy.copy is shallow
# example
a=[1,2,3,4]
b=a
print(a,b)
b[0]=10000
print(a,b)
# value in the both the variable changes. It is getting stored in the same memory 
# location that is the reason it is overwriting the original list. If we use
# shallow copy original list does not get changed
a=[1,2,3,4]
import copy
b=a.copy()
print(a,b)
b[0]=10000
print(a,b)
# here the original data does not get change. but the duplicate data changes 
# this is called shallow copy
a=[[1,2,3,4],[1,2,3,4,5,6]]
import copy
b=copy.deepcopy(a)
print(a,b)
b[1][0]=10000
print(a,b)
# shallow copy does not work with nested list that is the reason i am using
#copy.deepcopy



