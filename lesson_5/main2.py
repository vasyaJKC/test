# names = ["Ali", "Vasya", "Temur", "Muzaffar", "Ibrohim"]
# for x in names:
#     print(f"Salom {x}")
# result = 0
# for x in names:
#     result = result + 1
#
# print(f"Kod {result} marta ishlatildi")

# num = [1,3,5,7,9]
# result = 3
# for x in num:
#     result *= x
# print(result)
# num = [1,3,5,7,9]
# for x in num:
#     numbers = x ** 3
#
# print(numbers)

while True:
    n = int(input("Bugun nechta odam bln suhbat qldngz?:"))
    name = []
    for x in range(1, n + 1):
        name.append(input("Ism kiriting:"))
    print(name)

