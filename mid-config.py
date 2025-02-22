def menu_midconfig():
    print("="*70)
    print(" " * 5 + "CONFIGURAÇÕES 'MID-LEVEL', OLT ZTE C300, C320 E C350" + " " * 10)
    print("="*70)
    print("[1] - COMO SALVAR AS CONFIGURAÇÕES")
    print("[2] - COMO ATIVAR E DESATIVAR INTERFACES")
    print("[3] - VERIFICAÇÃO DE CONFIGURAÇÕES APLICADAS")
    print("[4] - INTERFACES DA OLT")
    print("[5] - SAIR")
    print("="*70)
    opcao = input("Para prosseguir, escolha uma opção válida: ")
    return opcao

while True:
    opcao = menu_midconfig()

    if opcao == "1":
        print("""
Opção escolhida com sucesso, prossiga!
""")
        print("""COMO SALVAR SUAS CONFIGURAÇÕES?
•Você pode salvar suas configurações de forma manual com o comando abaixo:

[CONFIGURAÇÃO FEITA]
exit
write

•Você també pode ativar o auto-save:

auto-write
auto-write 24
""")
    elif opcao == "2":
        print("""
Opção escolhida com sucesso, prossiga!
""")
        print("""ATIVANDO E DESATIVANDO INTERFACES:

•Geralmente ativação e desativação de interfaces seguem um padrão, os mais usados:

enable
no shotdown
shotdown
""")
    elif opcao == "3":
        print("""
Opção escolhida com sucesso, prossiga!
""")
        print("""VERIFICAÇÃO DE CONFIGURAÇÕES APLICADAS:

•Aqui também temos um padrão geralmente usado para verificar configurações gerais:

show this
show running-config
show running-config interface mngl
show running-config interface gpon-onu
show remote-onu wan-ip gpon-onu_1/1/1
""")
    elif opcao == "4":
        print("""
Opção escolhida com sucesso, prossiga!
""")
        print("""INTERFACES DA OLT:

•Para melhor compreensão, é interessante saber quais interfaces presentes e pra que servem:

conf t\configure terminal:
Este comando é utilizado para entrar na configuração geral da OLT, onde você pode definir várias configurações do dispositivo. "t" é de "terminal", o modo de configuração.

INTERFACE GPON OLT:
Aqui você está configurando a porta da OLT que se conecta à rede de fibra ótica GPON. Essa interface é onde você vai gerenciar a comunicação entre a OLT e os clientes (geralmente as ONUs).

INTERFACE GPON ONU:
Este comando é para configurar as ONUs (Optical Network Units), que são os dispositivos na ponta da rede (do lado do cliente). Elas conectam os dispositivos da casa do cliente à OLT.

INTERFACE XGEI:
É uma interface de rede de alta velocidade (10G Ethernet), geralmente usada para comunicação entre a OLT e outros dispositivos ou redes. É mais rápida do que as interfaces comuns.

INTERFACE GEI:
Essa interface é uma porta Ethernet (1G) usada para comunicação em velocidades mais baixas, conectando dispositivos à rede.

INTERFACE PON:
A PON (Passive Optical Network) é a interface que conecta a OLT ao backbone da rede de fibra ótica. É a porta principal para a distribuição da internet para os clientes.             
""")
    elif opcao == "5":
        print("""

Confira Também as Configurações de High Level...Até logo!

""")
        break
