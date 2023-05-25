def definisi(word, dictionary) :
    a = 0
    b = len(dictionary) - 1

    while a <= b :
        n = (a + b) // 2

        if dictionary[n][0] == word :
            return dictionary[n][1]
        elif dictionary[n][0] < word :
            a = n + 1
        else :
            b = n - 1
    return "Definisi tidak ditemukan"

dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]
word = input(dictionary)
definition = definisi(word, dictionary)
print("Definisi dari kata", word, "adalah:", definition)
