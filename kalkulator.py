def dodawanie(a, b):
	return a+b

try:
	a = int(input("Podaj pierwsza liczbe: "))
	b = int(input("Podaj druga liczbe: "))
	print(dodawanie(a,b))
except ValueError as ve:
	print('Wprowadzono bledne dane, koncze dzialanie...')
	
def get_info():
	return "To jest program kalkulator stworzony przez Huberta"
	
print(get_info())
input()