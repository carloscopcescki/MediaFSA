import os

# Calcula a média de atividades

def calcular_nota_atividade(total_at):
    return total_at * 0.2
  
repetidor = "s"

while repetidor == "s":
  
  print("Programa Média Aritmética - FSA")
  
  # Calcula a nota de atividade
  
  total_at = float(input("\nDigite a sua nota de atividade: "))
  nota_atividade = calcular_nota_atividade(total_at)
  print("\nA sua nota final de atividade é:")
  print(round(nota_atividade, 2))

# Calcula a média de provas

  nota_p1 = float(input("\nDigite a nota da P1: "))
  nota_p2 = float(input("Digita a nota da P2: "))
  media_provas = (((nota_p1 + nota_p2) / 2) * 0.8)

  print("\nA sua nota final de prova é:")
  print(round(media_provas, 2))

# Calcula a média da FSA

  media_geral = media_provas + nota_atividade

# Se a média geral seja maior igual a 5, o aluno passa. Caso seja menor que 5 porém maior igual a 3, o aluno fará P3. Em caso de média menor que 3, o aluno está reprovado.

  if media_geral >= 4.8:
    print("\nA sua média geral foi:")
    print(round(media_geral, 2))
    print("\nVocê passou! Parabéns!")
    repetidor = input("\nDeseja continuar? (s/n) ")
  elif (media_geral >= 3) and (media_geral < 4.8):
    print("\nA sua nota foi:")
    print(round(media_geral, 2))
    print("\nVocê reprovou e terá que fazer P3")
    nota_p3 = float(input("\nDigite a nota da P3: "))
    media_final = ((media_geral + nota_p3) / 2)
    if media_final >= 4.8:
        print("\nA sua nota final foi:")
        print(round(media_final, 2))
        print("\nVocê passou! Parabéns!")
        repetidor = input("\nDeseja continuar? (s/n) ")
    else:
        print("\nA sua nota final foi:")
        print(round(media_final, 2))
        print("\nVocê foi reprovado!")
        repetidor = input("\nDeseja continuar? (s/n) ")
  else:
    print("Você foi reprovado!")
    repetidor = input("\nDeseja continuar? (s/n) ")
    
  os.system("pause")
