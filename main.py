import math


def citire_lista():
    '''
    Citește dimensiunea apoi elementele unei liste.
    :return: result_list este lista introdusă de utilizator
    '''
    dimensiune = int(input("Dimensiune listă: "))
    result_list = []
    while dimensiune:
        element = int(input("Introduceți un element: "))
        result_list.append(element)
        dimensiune -= 1
    return result_list


def is_prime(n: int) -> int:
    '''
    Funcția verifică dacă un număr este prim.
    :param n: numărul care se verifică
    :return: True sau False în funcție de primalitatea numărului n
    '''
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def get_longest_all_primes(lst: list[int]) -> list[int]:
    '''
    Verifică toate secventele posibile dintr-o listă și evaluează dacă toate elementele unei
    secvențe sunt prime. Compară secvențele ce conțin doar numere prime și o afișează pe cea
    mai lungă.
    :param lst: lista ale carei secvente sunt verificate
    :return: cea mai lungă secventa ce conține doar numere prime
    '''
    secventa_max = []
    for start in range(0, len(lst)):
        for end in range(start+1, len(lst)+1):
            doar_prime = True
            for element in lst[start: end]:
                if not is_prime(element):
                    doar_prime = False
            if doar_prime:
                if len(lst[start: end]) > len(secventa_max):
                    secventa_max = lst[start: end]
    return secventa_max


def nr_divizori(n: int) -> int:
    '''
    Numără divizorii comuni și proprii ai unui număr dat.
    :param n: un număr întreg
    :return: numărul de divizori ai lui n
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    divizori = 2
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            divizori += 2
        i += 1
    if i ** 2 == n:
        divizori += 1
    return divizori


def get_longest_same_div_count(lst: list[int]) -> list[int]:
    '''
    Verifică toate secventele posibile dintr-o listă și evaluează dacă toate elementele unei
    secvențe au același număr de divizori. Compară secvențele ce conțin doar elemente cu un
    număr identic de divizori și o afișează pe cea mai lungă.
    :param lst: lista ale carei secvente sunt verificate
    :return: cea mai lungă secventa ce conține doar elemente cu un număr identic de divizori
    '''
    secventa_max = []
    for start in range(0, len(lst)):
        for end in range(start + 1, len(lst)+1):
            div_identici = True
            divizori = nr_divizori(lst[start])
            for element in lst[start: end]:
                if nr_divizori(element) != divizori:
                    div_identici = False
            if div_identici:
                if len(lst[start: end]) > len(secventa_max):
                    secventa_max = lst[start: end]
    return secventa_max


###################################
#Problema din timpul laboratorului#
###################################
def is_palindrome(number: int) -> int:
    temp = number
    reverse_num = 0
    while number > 0:
        digit = number % 10
        reverse_num = reverse_num * 10 + digit
        number = number // 10
    if temp == reverse_num:
        return True
    else:
        return False


def get_longest_all_palindromes(lst: list[int]) -> list[int]:
    '''
    Verifică toate secventele posibile dintr-o listă și evaluează dacă toate elementele unei secvențe sunt
    toate palindromuri. Compară secvențele ce conțin doar elemente palindromuri și o afișează pe cea mai lungă.
    :param lst: lista ale carei secvente sunt verificate
    :return: cea mai lungă secventa ce conține doar elemente palindromuri
    '''
    secventa_max = []
    for start in range(0, len(lst)):
        for end in range(start + 1, len(lst)+1):
            only_palindromes = True
            for element in lst[start: end]:
                if is_palindrome(element) is False:
                    only_palindromes = False
            if only_palindromes:
                if len(lst[start: end]) > len(secventa_max):
                    secventa_max = lst[start: end]
    return secventa_max
##############################


def test_get_longest_all_primes():
    assert get_longest_all_primes([2, 3, 5, 7, 8, 11, 13, 17, 19]) == [2, 3, 5, 7]
    assert get_longest_all_primes([-2, 111, 41, 73]) == [41, 73]
    assert get_longest_all_primes([2, 4, 6, 8]) == [2]
    assert get_longest_all_primes([0, 0, 0, 0, 0]) == []


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([2, 3, 5, 7, 11, 13, 17, 19]) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert get_longest_same_div_count([4, 9, 25, -49, 121]) == [4, 9, 25]
    assert get_longest_same_div_count([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert get_longest_same_div_count([1, 2, 4, 6, 12]) == [1]
    assert get_longest_same_div_count([11, 13, 17, 6, 8, 1]) == [11, 13, 17]

    
def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([121, 234, 232, 111]) == [121]
    assert get_longest_all_palindromes([53344335, 2332, 121, 3233, 989]) == [53344335, 2332, 121]


def main():
    while True:
        print("1. Introdu lista")
        print("2. Cea mai lungă secvență în care toate numerele sunt prime.")
        print("3. Cea mai lungă secvență în care toate numerele au același număr de divizori.")
        print("4. Cea mai lungă secvență în care toate numerele sunt palindromuri")
        print('')
        print("x. Încheie programul")
        optiune = input("Alege opțiunea: ")
        if optiune == '1':
            lista = citire_lista()
            print(f"Lista citita este {lista}")
            print('')

        elif optiune == '2':
            if lista != []:
                lista_max_prime = get_longest_same_div_count(lista)
                print(f"Cea mai lungă secvență de numere cu toate numerele prime: {lista_max_prime}")
                print('')
            else:
                print("Apasă 1 și Enter pentru a introduce lista")

        elif optiune == '3':
            if lista != []:
                lista_max_acelasi_nr_div = get_longest_same_div_count(lista)
                print(f"Cea mai lungă secvență de numere cu număr identic de divizori este: {lista_max_acelasi_nr_div}")
                print('')
            else:
                print("Apasă 1 și Enter pentru a introduce lista")

        elif optiune == '4':
            if lista != []:
                lista_max_palidromuri = get_longest_all_palindromes(lista)
                print(f"Cea mai lungă secvență de numere cu numere palindromuri este: {lista_max_palidromuri}")
                print('')
            else:
                print("Apasă 1 și Enter pentru a introduce lista")

        elif optiune == 'x':
            break


test_get_longest_all_primes()
test_get_longest_same_div_count()
test_get_longest_all_palindromes()
main()
