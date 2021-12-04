#1.
int_a = 55
print (id(int_a))
#9790720
str_b = 'cursor'
print(id(str_b))
#139966508301360
set_c = {1, 2, 3}
print(id(set_c))
#139966508271872
lst_d = [1, 2, 3]
print(id(lst_d))
# 139966509174528
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))
#139966509126336

#2.
# lst_d.append([4, 5])
print(id(lst_d))
#140688019873536

#3.
print(type(int_a))
#<class 'int'>

print(type(str_b))
#<class 'str'>

print(type(set_c))
#<class 'set'>

print(type(lst_d))
#<class 'list'>

print(type(dict_e))
#<class 'dict'>

#4.
print(isinstance(int_a, int))
#True
print(isinstance(str_b, str))
#True
print(isinstance(set_c,set))
#True
print(isinstance(lst_d,list))
#True
print(isinstance(dict_e,dict))
#True

#5.
print("Anna has {} apples and {} peaches.".format(2, 3))
#Anna has 2 apples and 3 peaches.

#6.
print("Anna has {1} apples and {0} peaches.".format(2, 3))
#Anna has 3 apples and 2 peaches.

#7.
print("Anna has {first} apples and {second} peaches.".format(first=4, second=5))
#Anna has 4 apples and 5 peaches.

#8.
print("Anna has {0:5} apples and {1:3} peaches.".format(5, 3))
#Anna has     5 apples and   3 peaches.

#9.
num1 = 4
num2 = 5
print(f"Anna has {num1} apples and {num2} peaches.")
#Anna has 4 apples and 5 peaches.

ten = '10'
ninth = '9'
print(f"Anna has {ten} apples and {ninth} peaches.")
#Anna has 10 apples and 9 peaches.

#10.
seven = '7'
six = '6'
print(f"Anna has %s apples and %s peaches." % (seven, six))
#Anna has 7 apples and 6 peaches.

#11.
second = "2"
four = "4"
data_dict = {"apple": second, "peaches": four}
print('Anna has %(apple)s apples and %(peaches)s peaches.' % data_dict)
# Anna has 2 apples and 4 peaches.

#12.
lst_comprehension = [num**2 if num % 2 ==1 else num **4 for num in range(10)]
print(lst_comprehension)

#13.
list =[]
for num in range(10):
    if num % 2 == 0:
        list.append(num // 2 )
    else:
        list.append(num * 10 )
print(list)

#14.
d_comprehension = {num: num**2 for num in range(1, 11) if num % 2 == 1}
print(d_comprehension)

#15.
d_comprehension = {num: num**2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_comprehension)

#16.
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)

#17.
d ={}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print(d)

#18.
foo = lambda x, y: x if x < y else y
print(foo(8, 9))

#19.
def foo(x, y, z):
    if y < x > z:
        return z
    else:
        return y
print(foo(1,2,5))

#20.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

#21.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))
list()
#22
lst2 = list(map(lambda x: x * 2, lst_to_sort))
print(lst2)

#23.
list_A = [2, 3, 4]
list_B = [5, 6, 7]
raise_r = [a ** b for a, b in zip(list_A, list_B)]
print(raise_r)
#[32, 729, 16384]

#24.
import functools
print(functools.reduce(lambda x, y: x + y, lst_to_sort))
#164

#25.
lst_to_sort_2 = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_to_sort_2)

#26.
lst_2 = list(filter(lambda x: x < 0, range(-10, 10)))
print(lst_2)

#27.
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_new = list(filter(lambda x: x in list_1, list_2)) #27
print(list_new)