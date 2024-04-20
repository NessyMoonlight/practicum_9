for send in range(1000, 9999 + 1):
    if len(set(str(send))) == len(str(send)):
        for more in range(1000, 9999 + 1):
            if len(set(str(more))) == len(str(more)) and \
                    str(send)[1]==str(more)[-1] and \
                    set(str(send)[0]+str(send)[2:]) != set(str(more)[:3]+str(send)[-1]):
                    money = str(send + more)
                    if money[0:2] == str(more)[0:2] and \
                            money[2] == str(send)[2] and \
                            money[-2] == str(more)[-1] and \
                            money[-1] != set(str(send)) and money[-1] != set(str(more))\
                            and len(set(money)) == len(money)\
                            and money[-1] not in set(str(send))\
                            and money[-1] not in set(str(more)):
                                print(f"{send} + {more} = {money}")
                                break