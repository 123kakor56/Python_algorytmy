import time


def sortowanie_naiwne(arr):
    """
    Algorytm sortowania bąbelkowego (bubble sort) - naiwny sposób sortowania.
    Porównuje sąsiednie elementy i zamienia je jeśli są w złej kolejności.
    
    Złożoność czasowa: O(n²)
    """
    n = len(arr)
    # Kopiujemy tablicę, aby nie modyfikować oryginału
    wynik = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Porównaj sąsiednie elementy
            if wynik[j] > wynik[j + 1]:
                # Zamień miejscami
                wynik[j], wynik[j + 1] = wynik[j + 1], wynik[j]
    
    return wynik


def sortowanie_przez_scalenie(arr):
    """
    Algorytm sortowania przez scalanie (merge sort).
    Dzieli tablicę na mniejsze części, sortuje je i scala z powrotem.
    
    Złożoność czasowa: O(n log n)
    """
    if len(arr) <= 1:
        return arr
    
    # Podziel tablicę na dwie części
    srodek = len(arr) // 2
    lewa = arr[:srodek]
    prawa = arr[srodek:]
    
    # Rekurencyjnie sortuj obie części
    lewa = sortowanie_przez_scalenie(lewa)
    prawa = sortowanie_przez_scalenie(prawa)
    
    # Scal posortowane części
    return scal(lewa, prawa)


def scal(lewa, prawa):
    """
    Funkcja pomocnicza do scalania dwóch posortowanych tablic.
    """
    wynik = []
    i = j = 0
    
    # Porównuj elementy z obu tablic i dodawaj mniejszy do wyniku
    while i < len(lewa) and j < len(prawa):
        if lewa[i] <= prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
    
    # Dodaj pozostałe elementy
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    
    return wynik


# Przykład użycia
if __name__ == "__main__":
    # Testowa tablica
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36]
    
    print("Oryginalna tablica:")
    print(arr)
    print()
    
    # Sortowanie naiwne
    start_naiwne = time.perf_counter()
    posortowane_naiwnie = sortowanie_naiwne(arr)
    czas_naiwne = time.perf_counter() - start_naiwne
    print("Po sortowaniu naiwnym (bubble sort):")
    print(posortowane_naiwnie)
    print(f"Czas wykonania: {czas_naiwne:.6f} sekund")
    print()
    
    # Sortowanie przez scalanie
    start_scalanie = time.perf_counter()
    posortowane_scalanie = sortowanie_przez_scalenie(arr)
    czas_scalanie = time.perf_counter() - start_scalanie
    print("Po sortowaniu przez scalanie (merge sort):")
    print(posortowane_scalanie)
    print(f"Czas wykonania: {czas_scalanie:.6f} sekund")
