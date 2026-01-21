import time
import random

def sortowanie_naiwne(arr):
    """
    Algorytm sortowania bąbelkowego (bubble sort) - naiwny sposób sortowania.
    Porównuje sąsiednie elementy i zamienia je jeśli są w złej kolejności.
    
    Złożoność czasowa: O(n²)
    """
    n = len(arr)
    licznik = 0
    # Kopiujemy tablicę, aby nie modyfikować oryginału
    wynik = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Porównaj sąsiednie elementy
            if wynik[j] > wynik[j + 1]:
                # Zamień miejscami
                wynik[j], wynik[j + 1] = wynik[j + 1], wynik[j]
                print(wynik)
                licznik+=1
    
    return wynik,licznik


def sortowanie_przez_scalenie(arr,licznik,ar2):
    """
    Algorytm sortowania przez scalanie (merge sort).
    Dzieli tablicę na mniejsze części, sortuje je i scala z powrotem.
    
    Złożoność czasowa: O(n log n)
    """
    if len(arr) <= 1:
        return arr, licznik,ar2 
    
    # Podziel tablicę na dwie części
    srodek = len(arr) // 2
    lewa = arr[:srodek]
    prawa = arr[srodek:]
    ar3=[]
    j=0
    for i in range(len(ar2)):
        if ar2[i]==arr and j==0:
            ar3.append(lewa)
            ar3.append(prawa)
            j+=1
        else:
            ar3.append(ar2[i])
    print(ar3)
    # Rekurencyjnie sortuj obie części
    lewa,l1,ar3 = sortowanie_przez_scalenie(lewa,licznik,ar3)
    prawa,l2,ar3 = sortowanie_przez_scalenie(prawa,licznik,ar3)
    
    # Scal posortowane części
    return scal(lewa,l1, prawa,l2,ar3)


def scal(lewa,l1, prawa,l2,ar2):
    """
    Funkcja pomocnicza do scalania dwóch posortowanych tablic.
    """
    wynik = []
    i = j = 0
    licznik = l1+l2
    # Porównuj elementy z obu tablic i dodawaj mniejszy do wyniku
    while i < len(lewa) and j < len(prawa):
        if lewa[i] <= prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
            licznik+=1
    # Dodaj pozostałe elementy
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    ar3=[]
    j=0
    for i in range(len(ar2)):
        if ar2[i]==lewa and j==0 and ar2[i+1]==prawa:
            ar3.append(wynik)
            j+=1
            i+=1
        else:
            ar3.append(ar2[i])
    print(ar3)
    return wynik,licznik,ar3


# Przykład użycia
if __name__ == "__main__":
    # Testowa tablica
    x = 1
while x != 0:
    if x == 1:
        rozmiar = input("Podaj rozmiar losowej listy (wpisz 0 żeby zakończyć działanie programu): ")
        
        try:
            r1 = int(rozmiar)
            
            if r1 == 0:
                x = 0
            elif r1 > 0 and r1 <= 20:
                x = 3
            else:
                print("Wartość musi być liczbą całkowitą w zakresie od 1 do 20.")
                x = 1
                
        except ValueError:
            print("Błąd: Proszę podać liczbę całkowitą.")
            x = 1
    
    if x == 3:
        arr = random.sample(range(100), r1)
        print("\nOryginalna tablica:")
        print(arr)
        print()
        
        # Sortowanie naiwne
        start_naiwne = time.perf_counter()
        posortowane_naiwnie, licznikbub = sortowanie_naiwne(arr)
        czas_naiwne = time.perf_counter() - start_naiwne
        print("Po sortowaniu naiwnym (bubble sort):")
        print(posortowane_naiwnie)
        print(f"Czas wykonania: {czas_naiwne:.6f} sekund, liczba inwersji: {licznikbub}")
        print()

        # Sortowanie przez scalanie
        start_scalanie = time.perf_counter()
        posortowane_scalanie, liczniksca, ar4 = sortowanie_przez_scalenie(arr, 0,[arr])
        czas_scalanie = time.perf_counter() - start_scalanie
        print("Po sortowaniu przez scalanie (merge sort):")
        print(posortowane_scalanie)
        print(f"Czas wykonania: {czas_scalanie:.6f} sekund, liczba inwersji: {liczniksca}")
        
        x = 1 
