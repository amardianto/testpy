def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        print("keduanya sama besar")
        pass # supaya gak keluar None
    else:
        return y
print(maximum(8,5))
