import os

# Calcula a média de atividades

quantidade_atividade = 0
nota_atividade = []

quantidade_atividade = int(
    input("Digite a quantidade de atividades por matéria: "))

i = quantidade_atividade
while i:
    nota = int(input("Digite a nota: "))
    nota_atividade.append(nota)
    i -= 1

soma_notas = sum(nota_atividade)

nota_final_atividade = ((soma_notas / quantidade_atividade) * 0.2)
print("\nA sua nota final de atividade é:")
print(round(nota_final_atividade, 2))

# Calcula a média de provas

nota_p1 = float(input("\nDigite a nota da P1: "))
nota_p2 = float(input("Digita a nota da P2: "))
media_provas = (((nota_p1 + nota_p2) / 2) * 0.8)

print("\nA sua nota final de prova é:")
print(round(media_provas, 2))

# Calcula a média da FSA

media_geral = media_provas + nota_final_atividade

# Se a média geral seja maior igual a 5, o aluno passa. Caso seja menor que 5 porém maior igual a 3, o aluno fará P3. Em caso de média menor que 3, o aluno está reprovado.

if media_geral >= 5:
    print("\nA sua média geral foi:")
    print(round(media_geral, 2))
    print("\nVocê passou! Parabéns!")
elif (media_geral >= 3) and (media_geral < 5):
    print("\nA sua nota foi:")
    print(round(media_geral, 2))
    print("\nVocê reprovou e terá que fazer P3")
    nota_p3 = float(input("\nDigite a nota da P3: "))
    media_final = ((media_geral + nota_p3) / 2)
    if media_final >= 5:
        print("\nA sua nota final foi:")
        print(round(media_geral, 2))
        print("\nVocê passou! Parabéns!")
    else:
        print("\nA sua nota final foi:")
        print(round(media_geral, 2))
        print("\nVocê foi reprovado!")
else:
    print("Você foi reprovado!")

os.system("pause")
