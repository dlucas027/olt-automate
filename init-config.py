def menu_config():
    print("="*60)
    print(" " * 5 + "CONFIGURAÇÕES INICIAIS, OLT ZTE C300, C320 E C350" + " " * 10)
    print("="*60)
    print("[1] - VERIFICAÇÃO DE STATUS")
    print("[2] - FAZENDO SEU PRIMEIRO ACESSO")
    print("[3] - NOME DA OLT")
    print("[4] - DATA E HORA")
    print("[5] - SAIR")
    print("="*60)
    opcao = input("Para prosseguir, escolha uma opção válida: ")
    return opcao

while True:
    opcao = menu_config()

    if opcao == "1":
        print("""
Opção escolhida com sucesso!
""")
        print("""VERIFICAÇÃO DE STATUS:

INSERVICE - Funcionando normalmente
CONFIGING - Placa sendo configurada
CONFIGFAILED - Falha no processo de configuração
DISABLE -Sem comunicação
HWONLINE - Versão diferente de software
OFFLINE - Placa adicionada lógicamente, não fisicamente
STANDBY - Modo de espera
TYPE MISMATCH - Placa diferente do tipo físico
NO POWER - Desligada
""")
    elif opcao == "2":
        print("""
Opção escolhida com sucesso!
""")
        print("""PRIMEIRO ACESSO, OLT ZTE:

O endereço IP de fábrica da OLT é 136.1.1.100.
A senha de acesso inicial é zte.

Se não for possível fazer o acesso remoto, faça via porta CLI:

A conexão com a OLT deve ser feita através da porta CLI com a velocidade de 9600 baud.

Para acessar o modo privilegiado, utilize o comando:
enable
A senha para entrar no modo privilegiado é zxr10.
""")
    elif opcao == "3":
        print("""
Opção escolhida com sucesso!
""")
        print("""ALTERAÇÃO DE NOME PARA A OLT:

hostname [NOVO NOME]
exit
""")
    elif opcao == "4":
        print("""
Opção escolhida com sucesso!
""")
        print("""AJUSTE DE DATA E HORA:

•Importante para identificação de logs e erros no horário correto.

conf t
clock timezone BRT -3                           
exit

clock set 00:00:00 mês - dia - ano
ptp
exit
""")
    elif opcao == "5":
        print("""

Confira Também as Configurações de Mid Level...Até logo!

""")
        break