exerc3 = [10, 9.5, 8.0, 7.0]
media = 0
for i in range(0, len(exerc3)):
    print("nota", i+1,":", exerc3[i])
    media = media + exerc3[i]
media = media / len(exerc3)
print("Média:", media)
