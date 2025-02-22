def menu_highconfig():
    print("="*70)
    print(" " * 5 + "CONFIGURAÇÕES 'HIGH-LEVEL', OLT ZTE C300, C320 E C350" + " " * 10)
    print("="*70)
    print("[1] - PNP DAS PLACAS NA OLT")
    print("[2] - IP DE ACESSO")
    print("[3] - GATEWAY PADRÃO")
    print("[4] - VLAN DE GERENCIA")
    print("[5] - INTERFACE DE UP-LINK")
    print("[6] - ACESSO REMOTO DE OLT")
    print("[7] - CONFIGURAÇÃO DE BANDA")
    print("[8] - VLAN DE ONU")
    print("[9] - ACESSO REMOTO DA ONU")
    print("[10] - PPPOE, REDE E SENHA DA ONU")
    print("[50] - HISTÓRICO")
    print("[100] - SAIR")
    print("="*70)
    opcao = input("Para prosseguir, escolha uma opção válida: ")
    return opcao

historico = " "

while True:
    opcao = menu_highconfig()

    if opcao == "1":
        print("""HABILITAR A DETECÇÃO PLUG-AND-PLAY DAS PLACAS E TIPO DE CHASSI:

conf t
set-pnp enable
add-rack rackno 1 racktype C320Rack
add-shelf rackno 1 shelfno 1 shelftype C320_SHELF
""")
        historico += "[1] - PNP DAS PLACAS NA OLT\n"
        print("Comando salvo em'HISTÓRICO'")
    
    elif opcao == "2":
        print(""" CONFIGURAR UM NOVO IP DE ACESSO:

interface mng1
ip address [IP] [MASK]                          (Define o IP para acesso remoto à OLT. A máscara cobre um range maior de IPs)
config-filename startrun.dat                    (Define o nome do arquivo de configuração inicial que será carregado ao iniciar a OLT)
negotiation auto                                (Configura a negociação automática de velocidade e duplex na interface)
tag-mode untag                                  (Define que essa interface de gerenciamento não usará VLANs (tráfego não marcado))
""")
        historico += "[2] - IP DE ACESSO\n"
        print("Comando salvo em 'HISTÓRICO'")    
    
    elif opcao == "3":
        print("""ADICIONAR GATEWAY PADRÃO:

conf t
no ip route 0.0.0.0 0.0.0.0
ip route 0.0.0.0 0.0.0.0 [IP do GATEWAY]          (Cria uma rota padrão para o gateway)
exit
write
""")
        historico += "[3] - GATEWAY PADRÃO\n"
        print("Comando salvo em 'HISTÓRICO'")  
    
    elif opcao == "4":
        print("""VLAN DE GERENCIA:

vlan 100
name GERENCIA
exit

interface vlan100                                (Definir IP na VLAN de gerencia apenas, se o seu objetivo é que a OLT seja gerenciada exclusivamente por ela)
ip address [IP][MASK]
exit
""")
        historico += "[4] - VLAN DE GERENCIA\n"
        print("Comando salvo em 'HISTÓRICO'")    
    
    elif opcao == "5":
        print("""INTERFACE DE UP-LINK\GEI:

interface gei_1/1/1
no shutdown
switchport vlan 100 tag                          (Define as VLANs permitidas no trunk e aplica a tag VLAN para elas)
linktrap enable                                  (Habilita notificações quando o estado de fase muda, Up/Down)
port-protect disable                             (Desativa a proteção de porta, permitindo a utilização normal)
uplink-isolate disable                           (Desativa a isolação de uplink, permitindo o tráfego normal entre interfaces)
""")
        historico += "[5] - INTERFACE DE UP-LINK\n"
        print("Comando salvo em 'HISTÓRICO'") 
    
    elif opcao == "6":
        print("""HABILITAR SSH:

ssh server authentication type chap
ss server version 2
username zte password zte privilege 15           (Privilégio máximo)


HABILITAR TELNET:

security-mgmt 999 state enable ingress-type lan protocol telnet
username zte password zte privilege 15
show security-mgmt
""")
        historico += "[6] - ACESSO REMOTO DE OLT\n"
        print("Comando salvo em 'HISTÓRICO'")
    
    elif opcao == "7":
        print("""CONFIGURAÇÃO DE BANDA:

profile tcont 1G-UP type 5 fixed 64 assured 64 maximum 1048064             (sir = Banda garantida | pir = Banda máxima)
profile traffic 1G-DOWN sir 1048064 pir 1048064
""")
        historico += "[7] - CONFIGURAÇÃO DE BANDA\n"
        print("Comando salvo em 'HISTÓRICO'")
    
    elif opcao == "8":
        print("""ONU PROFILE VLAN:

onu profile vlan 100 tag-mode tag cvlan 100
""")
        historico += "[8] - VLAN DE ONU\n"
        print("Comando salvo em 'HISTÓRICO'")
    
    elif opcao == "9":
        print("""ACESSO REMOTO E VEIP DE ONU:

flow mode 1 tag-filter vlan-filter untag-filter discard
flow 1 pri 0 vlan 100
gemport 1 flow 1
switchport-bind switch_0/1 iphost 1
switchport-bind switch_0/1 veip 1
dhcp-ip ethuni eth_0/1 from-internet

security-mgmt 998 state enable mode forward ingress-type lan protocol web https                
security-mgmt 999 state enable ingress-type lan protocol ftp telnet ssh snmp tr069     (Acesso remoto da ONU)        
""")
        historico += "[9] - ACESSO REMOTO DA ONU\n"
        print("Comando salvo em 'HISTÓRICO'")
    
    elif opcao == "10":
        print("""PPPOE, REDE E SENHA DA ONU:

pon-onu-mng gpon-onu_1/1/1
mode pppoe username [REDE] password [SENHA]
password senha vlan-profile 100

ssid ctrl wifi_0/1 name 2.4G         (0/1 ao 0/4 2.4G)
ssid crtl wifi_0/5 nome 5G

wifi_0/1 encrypt aes key senha
wifi_0/5 encrypt aes key senha

ssid ctrl wifi_0/1 user-isolation disable     (Desabilitar isolamento wifi)
""")
        historico += "[10] - PPPOE, REDE E SENHA DA ONU\n"
        print("Comando salvo em 'HISTÓRICO'")
    
    elif opcao == "50":
        print("Histórico das opções escolhidas até agora:")
        if historico.strip() != "":  #verificando se a variável historico não está vazia
            print(historico) 
        else:
            print("Nenhuma opção foi escolhida ainda.\n")

    elif opcao == "100":
        print("Espero ter ajudado... Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")