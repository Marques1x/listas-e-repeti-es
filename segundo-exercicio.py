
Listanumerica= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exercicioEnvertido = []
for i in range(0, len(Listanumerica)):
    exercicioEnvertido.append(Listanumerica[len(Listanumerica)-1])
    Listanumerica.pop()
print("inversao",exercicioEnvertido)





