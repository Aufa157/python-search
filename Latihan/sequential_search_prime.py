def sequential_search_prime(x):
    if x <= 1 :
        return False 
    for i in range(2, int(x**0.5) + 1) :
        if x % i == 0 :
            return False
    return True

def prime_numbers(angka):
    prima = []
    for a in angka :
        if sequential_search_prime(a) :
            prima.append(a)
    return prima

angka = [7,10,13,6,17,22,19]
prima = prime_numbers(angka)
print("Bilangan prima dalam daftar adalah", prima)

