str='username=test01'
str1='password=Aaaaa'
list1=str.split('=')
list2=str1.split('=')
dict1={}
dict1[list1[0]]=list1[1]
dict1[list2[0]]=list2[1]
print(dict1['password'])