
# # # # 1. Илова кардани адад ба охири лист.
# # # # # # Пример
# # # # # # Ввод: список = [1, 2, 3], число = 4
# # # # # # Выход: [1, 2, 3, 4]
# # # def add_to_list(lst, num):
# # #     lst.append(num)
# # #     return lst


# # # list1 = [1, 2, 3]
# # # num = 4
# # # print(add_to_list(list1, num))       



# # # # 2. Тавсифи калидаҳое, ки арзишашон калонтар аз як адад дар дикт.
# # # # Пример
# # # # Ввод: словарь = {'a': 1, 'b': 2, 'c': 3}, число = 1
# # # # # Выход: ['b', 'c']
# # # def filter(dct, num):
# # #     return [key for key, value in dct.items() if value > num]


# # # dictionary = {'a': 1, 'b': 2, 'c': 3}
# # # num = 1
# # # print(filter(dictionary, num))  


# # # # 3. Ҷамъ кардани ду рақам дар лист.
# # # # # Пример
# # # # # Ввод: список = [1, 2, 3], индексы = 0, 2
# # # # # Выход: 4
# # # # def sum_from_list(lst, idx1, idx2):
# # # #     return lst[idx1] + lst[idx2]


# # # # list1 = [1, 2, 3]
# # # # idx1, idx2 = 0, 2
# # # # print(sum_from_list(list1, idx1, idx2)) 


# # # # 4. Дастрас кардани арзиш аз дикт 
# # # # # Пример
# # # # # Ввод: словарь = {'a': 1, 'b': 2}, ключ = 'b'
# # # # # Выход: 2

# # # dic1={
# # #     'a':1,
# # #     # 'b':2
# # # }
# # # print(dic1['b'])



# # # # 1. Филтратсияи дикт барои баргардонидани калидаҳои арзишашон калонтар аз як адад.
# # # # # Пример
# # # # # Ввод: словарь = {'a': 1, 'b': 2, 'c': 3}, число = 1
# # # # # Выход: ['b', 'c']
# # # def dici(dct, num):
# # #     return [key for key, value in dct.items() if value > num]


# # # dictionary = {'a': 1, 'b': 2, 'c': 3}
# # # num = 1
# # # print(dici(dictionary, num))  

# # # # 2. Тағйир додани ду элементи аввал ва охирини лист.
# # # # Пример
# # # # Ввод: список = [1, 2, 3, 4]
# # # # Выход: [4, 2, 3, 1]

# # # def rez(a):
# # #     a[0],a[len(a)-1] = a[len(a)-1],a[0]
# # #     return a
# # # res=rez(list(map(int,input().split())))
# # # print(res)

# # # #  3. Илова кардани калида ва арзиш ба дикт.
# # # # # Пример
# # # # # Ввод: словарь = {'a': 1, 'b': 2}, ключ = 'c', значение = 3
# # # # # Выход: {'a': 1, 'b': 2, 'c': 3}

# # # # dic1={
# # # #    'a': 1, 
# # # #    'b': 2 
# # # # }
# # # # def dicti(a):
# # # #    dic1['c']=3
# # # #    return dic1
# # # # rez=dicti(dic1)  
# # # # print(rez)  

# # # #  4. Ёфтани максимуми лист.
# # # # # Пример
# # # # # Ввод: список = [1, 2, 3, 4]
# # # # # Выход: 4

# # # # lis1=[1,2,3,4]
# # # # def max_lis(a):
# # # #     max=-999999
# # # #     for i in a:
# # # #         if i>max:
# # # #          max=i
# # # #     return max 
# # # # rez=max_lis(lis1)
# # # # print(rez)        




# # # # 9. Мерж кардани ду лист.
# # # # # Пример
# # # # # Ввод: список1 = [1, 2], список2 = [3, 4]
# # # # # Выход: [1, 2, 3, 4]
# # # # lis1=[1,2]
# # # # lis2=[3,4]

# # # # def num_i(a,b):
# # # #     lis3=[]
# # # #     for i in a:
# # # #       lis3.append(i)
# # # #     for j in b:
# # # #       lis3.append(j)
# # # #     return lis3
# # # # rez=num_i(lis1,lis2)
# # # # print(rez)


# # # # 1. Ҷустуҷӯи арзиш дар дикт бо калида.
# # # # # Пример
# # # # # Ввод: словарь = {'a': 1, 'b': 2}, ключ = 'b'
# # # # # Выход: 2
# dic1={
#     'a':1,
#     'b':2
# }  
# def fil(dct, num):
#     for key, value in dct.items():
#         if num==key:
#             return value
                
# num=input()
# rez=fil(dic1,num)
  
# print(rez)      



