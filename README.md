# My_first_repository
Studying
![image](https://user-images.githubusercontent.com/86930406/124711393-b25a6b00-df06-11eb-991e-bd219790aeb9.png)
import random
random.seed()

list1=[]
list2=[]
serial=0
n_serial=0
biggest=-101

for i in range(30):
    list1.append(random.randint(-100, 100))
print("First list: \n", list1)
biggest=max(list1)
serial=list1.index(biggest)
print("Number",serial)
print("MAx is: \n",biggest)

for i in range(len(list1)):
    if list1[i]%2!=0:
        list2.append(list1[i])
list2.sort(reverse=True)
print("List with odd numbers in descending order: \n", list2)

