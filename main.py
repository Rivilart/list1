import random

int_list = []

for n in range(random.randint(5, 10)):
    int_list.append(random.randint(1, 100))

print("Исходный список:", int_list)

for i in range(len(int_list)):
  int_list[i] = int_list[i] ** 2

print("Измененный список:", int_list)

input()