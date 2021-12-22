#!/bin/python3
#
# Projetinho simples que eu fiz baseado no meu aprendizado de tratamento de erros e  multiplas escolhas
#
#
print('''
  .---------.
  |.-------.|
  ||>run#  ||
  ||       ||
  |"-------'|etf
.-^---------^-.
| ---~ N3w.elf|
"-------------'
      
      ''')
try:
  idade = int(input('[️*] Informe sua idade: '))
except:
	print("[x] Erro!!!!")
	exit()

if idade < 18:
  print("\n[x] Acesso negado!!!")
  print("[!] Apenas maiores de 18 anos.")

elif idade >= 18 and idade < 100:
  print("\n[OK️] Acesso Permitido!!!")
  print(f"[✔]Você tem {idade} anos, pode entrar na festa.")

elif idade >= 100:
  print('Apenas motais.')

else:
  print("[x] Comando invalido!!!")
