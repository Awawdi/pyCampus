
def validity_check(id_number):
    lst_id = list(map(int, id_number))
    lst_id[1::2] = map(lambda x: x * 2, lst_id[1::2])
    lst_id = map(lambda x: (x % 10 + x // 10), lst_id)
    num1 = sum(lst_id)
    if num1 % 10 != 0:
        print("Your ID is wrong")
    else:
        print("ID is correct")

print(validity_check("053013587"))