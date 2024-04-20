for a in range(1, 10):
    for b in range(0, 10):
        AB = 10*a + b
        CAB = AB * AB
        if CAB % 100 == AB and 99 < CAB < 1000:
            print(CAB)