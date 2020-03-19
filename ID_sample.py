while True:
    id = input("Enter ID No: ('end' to exit) ")
    if id == "end":
        exit()
    if id.isdigit() == False:
        print("ID has only digits")
        continue
    if len(id) > 9:
        print(id, "has more than 9 digits")
        continue
    if len(id) == 9:
        lst_id = list(map(int, id))
        lst_id[1::2] = map(lambda x: x * 2, lst_id[1::2])
        lst_id = map(lambda x: (x % 10 + x // 10), lst_id)
        num1 = sum(lst_id)
        if num1 % 10 != 0:
            print("Your ID is wrong")
        else:
            print("ID is correct")
        continue
    '''
    while len(id) < 8:
    id = "0" + id
    lst_id = list(map(int, id))
    lst_id[1::2] = map(lambda x : x * 2, lst_id[1::2])
    lst_id = map(lambda x : (x % 10 + x // 10), lst_id)
    num1 = sum(lst_id)
    digit9 = 0 if num1 % 10 == 0 else 10 – num1 % 10
    new_id = id + str(digit9)
    print("Your ID is:", new_id)'''