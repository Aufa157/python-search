def mencari_posisi_tersembunyi(data,target) :
    a = 0
    b = len(data) - 1

    while a <= b :
        n = (a + b) // 2

        if data[n] == target:
            return n
        elif data[n] < target :
            a = n + 1
        else :
            b = n - 1

    return a

data = [2,4,6,8,10,12,14]
target = 9
posisi_tersembunyi = mencari_posisi_tersembunyi(data,target)
print("Elemen", target, "dapat di sisipkan pada index ",posisi_tersembunyi, "untuk menjaga daftar tetap terurut")
    
