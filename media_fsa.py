import os

repetidor = "s"

while repetidor == "s":

  print("Programa Média Aritmética - FSA")

  # Calcula a nota de atividade

  def calcular_nota_atividade():
    while True:
      try:
        total_at = float(input("\nDigite a sua nota de atividade: "))
        return total_at * 0.2
      except:
        print("\nValor inválido! Tente novamente")
        
  nota_atividade = calcular_nota_atividade()      
  print("\nA sua nota final de atividade é:")
  print(round(nota_atividade, 2))

# Calcula a média de provas

  def calcular_nota_p1():
    while True:
      try:       
        nota_p1 = float(input("\nDigite a nota da P1: "))
        return nota_p1
      except:
        print("\nValor inválido! Tente novamente")
        
  def calcular_nota_p2():
    while True:
      try:       
        nota_p2 = float(input("\nDigite a nota da P2: "))
        return nota_p2
      except:
        print("\nValor inválido! Tente novamente")
      
  total_prova = (((calcular_nota_p1() + calcular_nota_p2()) / 2) * 0.8)  
  media_provas = total_prova
  print("\nA sua nota final de prova é:")
  print(round(media_provas, 2))

# Calcula a média da FSA

  media_geral = media_provas + nota_atividade

# Se a média geral seja maior igual a 4.75, o aluno passa. Caso seja menor que 4.75 porém maior igual a 3, o aluno fará P3.

  if media_geral >= 4.75:
    print("\nA sua média geral foi:")
    print(round(media_geral, 1))
    print("\nVocê passou! Parabéns!")
    repetidor = input("\nDeseja continuar? (s/n) ")
  
  elif media_geral < 4.75:
    print("\nA sua nota foi:")
    print(round(media_geral, 2))
    print("\nVocê reprovou e terá que fazer P3")
    
    # Calculo de P3
    
    def calcular_nota_pf():
      while True:
        try: 
          nota_p3 = float(input("\nDigite a nota da P3: "))
          media_p3 = ((media_geral + nota_p3) / 2)
          return media_p3
        except:
          print("\nValor inválido! Tente novamente")
    
    media_final = calcular_nota_pf()
    
    if media_final >= 4.75:
        print("\nA sua nota final foi:")
        print(round(media_final, 1))
        print("\nVocê passou! Parabéns!")
        repetidor = input("\nDeseja continuar? (s/n) ")
    else:
        print("\nA sua nota final foi:")
        print(round(media_final, 2))
        print("\nVocê foi reprovado!")
        repetidor = input("\nDeseja continuar? (s/n) ")
    
  os.system("pause")
