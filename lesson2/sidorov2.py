# Создание 3ех переменных с одинаковыми данными и одинаковыми идентификаторами
index1 = 300
index2 = 300
index3 = 300
print('index1 =', index1, ',', 'index2 = ', index2, ', ' 'index3 = ', index3)
print('id(index1) = ', id(index1))
print('id(index2) = ', id(index2))
print('id(index3) = ', id(index3))
print()

# Создание 2ух переменных с одинаковыми данными и разными идентификаторами
weight = float(80)
age = float(80)
print('weight = ', weight, ',', 'age = ', age)
print('id(weight)', '=', id(weight))
print('id(age)', '   =', id(age))
print()

# Замена типов переменных, где у 1ых трех разные идентификаторы, а 2ух последних одинаковые

index1 = 300
index2 = '300'
index3 = 300.0
print('index1 =', index1, ',', 'index2 = ', index2, ', ' 'index3 = ', index3)
print('id(index1) = ', id(index1))
print('id(index2) = ', id(index2))
print('id(index3) = ', id(index3))
print()

print()

weight = 80
age = 80
print('weight = ', weight, ',', 'age = ', age)
print('id(weight)', '=', id(weight))
print('id(age)', '   =', id(age))
