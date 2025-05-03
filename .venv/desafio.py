salario = float(input("Digite o seu salario mensal: R$ "))

despesa_total = 0


while True:
    descricao = input("Digite a descrição da despesa (ou 'sair' para encerrar): ")
    if descricao.lower() == 'sair':
        break
    valor = float(input(f"Digite o valor da despesa: R$ {descricao}: R$ "))
    despesa_total += valor
print("")
print("------ RESUMO ------")
print(f"Salario mensal: {salario:.2f}")
print(f"Total de despesas: {despesa_total:.2f}")

diferenca = salario - despesa_total

if diferenca > 0:
    print(f"Voce esta no azul! seu saldo é de R$ {diferenca:.2f}")
elif diferenca == 0:
    print("Atenção! Você esta no limite do orçamento!")
else:
    print(f"Voce esta no vermelho! faltam R$  {abs(diferenca):.2f} para cobrir as despesas")


