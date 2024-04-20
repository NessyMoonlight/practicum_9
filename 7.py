for send in range(1000, 9999 + 1):
    send = str(send)
    if len(set(send)) == len(send):

        for more in range(1000, 9999 + 1):
            more = str(more)
            if len(set(more)) == len(more) and \
                    send[1]==more[-1] and \
                    more[1] not in set(send) and more[2] not in set(send) and \
                    more[0] not in set(send):

                    money = str(int(send) + int(more))

                    if money[0:2] == more[0:2] and \
                            money[2] == send[2] and \
                            money[-2] == more[-1] and \
                            money[-1] != set(send) and money[-1] != set(more)\
                            and len(set(money)) == len(money)\
                            and money[-1] not in set(send)\
                            and money[-1] not in set(more):
                                print(f"{send} + {more} = {money}")
                                break