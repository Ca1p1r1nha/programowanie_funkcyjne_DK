#Stwórz generator, który produkuje nieskończony ciąg liczb Fibonacciego.
#Napisać generator, który czyta duży plik tekstowy linią po linii, unikając wczytywania całego pliku do pamięci.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
file_reader = read_large_file(r"C:\Users\dawid\Desktop\funkcyjne\programowanie_funkcyjne_DK\pakiet5\plik.txt")
for line in file_reader:
    print(line)