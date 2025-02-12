class Config:
    _id_counter = 1

    def _init_(self, name, description, command):
        self.code = Config._id_counter
        Config._id_counter += 1
        self.name = name
        self.description = description
        self.command = command

    def _str_(self):
        return f"[Cód: {self.code}] {self.name} - {self.description}\n{self.command}\n"


configs = []  # Lista de configurações

class Config:
    def _init_(self, name, description, command):
        self.name = name
        self.description = description
        self.command = command

    def _str_(self):
        return f"Nome: {self.name}\nDescrição: {self.description}\nComando: {self.command}\n"


configs = []  # Lista de configurações
def add_authorize_onu():
    name = input("Nome da configuração: Autorizar ONU")
    description = input("Descrição: Entrar na interface G-PON antes de autorizar, inserir o número da ONU, tipo e SN.")
    command = input("""Comando:
interface gpon-olt_?/?/?
    onu 1 type ZTE-F601 sn ZTEGCCE7B888
""")
    config = Config(name, description, command)
    configs.append(config)
    print("Último Comando: Autorizar ONU!")  


def add_enable_pon():
    name = input("Nome da configuração: Habilitar PON")
    description = input("Descrição: Entrar na interface G-PON para habilitar, selecione a PON específica.")
    command = input("""Comando:
interface gpon-olt_1/1/1
show this
shutdown (DESATIVADA)
linktrap disable
""")
    config = Config(name, description, command)
    configs.append(config)
    print("Último Comando: Autorizar ONU!") 

def add_script_vsol():
    name = input("Nome da configuração: Script VSOL")
    description = input("Descrição: Entrar na interface PON, Modelo de Script para VSOL.")
    command = input("""Comando:
onu-type VSOL-BRIDGE-1P gpon
onu-type VSOL-BRIDGE-1P gpon max-tcont 8
onu-type VSOL-BRIDGE-1P gpon max-gemport 32
onu-type VSOL-BRIDGE-1P gpon max-switch-perslot 8
onu-type VSOL-BRIDGE-1P gpon max-flow-perswitch 8
onu-type VSOL-BRIDGE-1P gpon max-iphost 5
onu-type-if VSOL-BRIDGE-1P eth_0/1
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Script VSOL' executado com sucesso!")  

def add_script_F601():
    name = input("Nome da configuração: Script ZTE-F601")
    description = input("Descrição: Entrar na interface PON, Modelo de Script para ZTE-F601.")
    command = input("""Comando:
onu-type ZTE-F601 gpon
onu-type ZTE-F601 gpon max-tcont 8
onu-type ZTE-F601 gpon max-gemport 32
onu-type ZTE-F601 gpon max-switch-perslot 8
onu-type ZTE-F601 gpon max-flow-perswitch 8
onu-type ZTE-F601 gpon max-iphost 5
onu-type-if ZTE-F601 eth_0/1
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Script ZTE-F601' executado com sucesso!")  

def add_script_gei():
    name = input("Nome da configuração: Interface GEI")
    description = input("Exemplo de configuração na interface GEI, para verificar, execute o comando show this na inferface GEI.")
    command = input("""Comando:
interface gei_1/4/1   
no shutdown  
hybrid-attribute fiber  
negotiation auto
flowcontrol disable 
linktrap enable 
switchport mode trunk  
switchport vlan 1,11-19,50,100 tag  
port-protect disable  
uplink-isolate disable 
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração GEI' executado com sucesso!")  

def add_script_xgei():
    name = input("Nome da configuração: Interface XGEI")
    description = input("Exemplo de configuração na interface XGigabit, XGEI.")
    command = input("""Comando:
interface xgei_1/4/2 
phy-attribute lan 
shutdown 
hybrid-attribute fiber 
no negotiation auto  
speed 10000   
duplex full
flowcontrol disable  
linktrap enable
switchport mode trunk 
switchport vlan 1 tag  
port-protect disable 
uplink-isolate disable 
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração XGEI' executado com sucesso!")  

def add_config_gpon():
    name = input("Nome da configuração: Configuração GPON")
    description = input("Configuração GPON para controle de banda (sir=banda garantida)(pir=banda máxima).")
    command = input("""Comando:
gpon
profile tcont 1G-UP type 5 fixed 64 assured 64 maximum 1048064
profile traffic 1G-DOWN sir 1048064 pir 1048064 
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração GPON' executado com sucesso!")  

def add_pnp():
    name = input("Nome da configuração: Ativação do Plug-and-Play(PnP)")
    description = input("A primeira linha ativa o Plug-and-Play (PnP), a segunda aplica para ONUs e o restante são configurações que influenciam o PnP.")
    command = input("""Comando:
onu-pnp                   
set-pnp enable 
add-rack rackno 1 racktype C320Rack
add-shelf rackno 1 shelfno 1 shelftype C320_SHELF
add-card rackno 1 shelfno 1 slotno 1 GTGH
add-card rackno 1 shelfno 1 slotno 3 PRAM
add-subcard rackno 1 shelfno 1 slotno 4 subcardno 1 UCDC/3
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Ativação do Plug-and-Play(PnP)' executado com sucesso!")  

def add_tcp():
    name = input("Nome da configuração: Configuração TCP")
    description = input("Configurações TCP, para máximo de conexões na fila TCP, tempo de resposta, tamanho de janela TCP para controle de fluxo.")
    command = input("""Comando:
ip tcp finwait-time 600 
ip tcp queuemax 5  
ip tcp synwait-time 30 
ip tcp window-size 2144
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração TCP' executado com sucesso!")  

def add_veip_onu():
    name = input("Nome da configuração: Configuração VEIP da ONU")
    description = input("Para configurar o VEiP na ONU, entre na interface de configuração geral, (ZXAN(config)#pon-onu-mng).")
    command = input("""Comando:
flow mode 1 tag-filter vlan-filter untag-filter discard
flow 1 pri 0 vlan 100
gemport 1 flow 1
switchport-bind switch_0/1 iphost 1
switchport-bind switch_0/1 veip 1
dhcp-ip ethuni eth_0/1 from-internet
security-mgmt 998 state enable mode forward ingress-type lan protocol web https
security-mgmt 999 state enable ingress-type lan protocol ftp telnet ssh snmp tr069
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'VEIP de ONU' executado com sucesso!")  

def add_vlans():
    name = input("Nome da configuração: Configuração de VLAN e VLAN de QINQ")
    description = input("Primeiro bloco com as VLANS para VOIP e tráfego GPON, depois VLANS configuradas e por último de QINQ.")
    command = input("""Comando:
no vlan-reserve 4091 out-voip
no vlan-reserve 4092 in-voip 
no vlan-reserve 4094 gpon
!
vlan database
vlan 1,11-19,50,100
!
vlan 100
description VLAN_de_QINQ
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração de VLAN' executado com sucesso!")  

def add_mac():
    name = input("Nome da configuração: Gerenciamento de MAC")
    description = input("Define o tempo de expiração dos endereços, estabelece o tempo de monitoramento da tabela MAC e limite de atualização da mesma.")
    command = input("""Comando:
mac aging-time 300 
mac monitor-period 10 
mac usage-threshold 70
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Gerenciamento de MAC' executado com sucesso!")  

def add_mng():
    name = input("Nome da configuração: Interface de Gerenciamento")
    description = input("Permite que a OLT seja acessada remotamente via IP e define parâmetros básicos para sua conectividade e inicialização.")
    command = input("""Comando:
interface mng1
ip address 131.1.1.100 255.255.0.0
config-filename startrun.dat 
negotiation auto
tag-mode untag 
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Interface de Gerenciamento' executado com sucesso!")  

def add_arp():
    name = input("Nome da configuração: Conectividade da OLT")
    description = input("Configura a rota padrão da OLT e ajusta os tempos de atualização do ARP para melhor conectividade.")
    command = input("""Comando:
p route 0.0.0.0 0.0.0.0 10.300.50.1
!
ipoa inatmarp-interval 10  
ipoa gateway-arp-interval 10 
!
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Conectividade da OLT' executado com sucesso!")  

def add_nat():
    name = input("Nome da configuração: Configuração de NAT")
    description = input("Define os tempos limite para sessões de NAT, Telnet, FTP e SNMP das ONUs e modems, além de desativar a alocação automática de portas de gerenciamento. Isso otimiza o uso de recursos da OLT e evita conexões ociosas por muito tempo.")
    command = input("""Comando:
mpnat trans-table aging-time 60 
mpnat onu-telnet idle-time 3 
mpnat onu-ftp aging-time 5 
mpnat onu-snmp aging-time 30 
mpnat onu-ftp-data aging-time 5 
mpnat onu-mng-port auto-alloc disable 
mpnat modem-telnet idle-time 3  
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração de NAT' executado com sucesso!")  

def add_dhcp():
    name = input("Nome da configuração: Portas DHCP")
    description = input("Habilita o controle de portas para DHCP Snooping, melhorando a segurança contra ataques DHCP, e define a identificação da porta baseada no MAC em banda e na estrutura física (rack e frame).")
    command = input("""Comando:
ip dhcp snooping control-port enable 
port-identification access-node-id-type inband-mac
port-identification rackno 1 frameno 1 
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração de DHCP' executado com sucesso!")  

def add_snmp():
    name = input("Nome da configuração: Acesso SNMP")
    description = input("Localização e contato de suporte técnico, grupos SNMPv3, comunidade SNMP, definição de MIBs.")
    command = input("""Comando:
snmp-server location No.889 BiBo Rd.PuDong District, Shanghai, China 
snmp-server contact +86-21-68895000  
snmp-server packetsize 8192
snmp-server engine-id mode mac 
snmp-server group GroupPriv15 v3 priv read AllView write AllView 
snmp-server group GroupPriv10 v3 priv read AllView write ViewPriv10 
snmp-server group GroupPriv5 v3 priv read AllView write ViewPriv5 
snmp-server group GroupPriv0 v3 priv read AllView
snmp-server community oltcloud view AllView rw 
snmp-server view AllView 1.2 included
snmp-server view AllView 1.3 included  
snmp-server view ViewPriv5 1.2 included  
snmp-server view ViewPriv5 1.3 included  
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.10.1 excluded 
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.10.10 excluded   
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.20.1 excluded  
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.20.10 excluded   
snmp-server view ViewPriv10 1.2 included 
snmp-server view ViewPriv10 1.3 included  
snmp-server view ViewPriv10 1.3.6.1.4.1.3902.1082.20.10 excluded 
!  
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Acesso SNMP' executado com sucesso!")  

def add_ftp():
    name = input("Nome da configuração: Servidor FTP")
    description = input("Habilita o servidor FTP para escutar na porta 21 (padrão do FTP) e define o diretório raiz como /flash, onde os arquivos poderão ser acessados ou armazenados.")
    command = input("""Comando:
ftp-server enable listen 21
ftp-server top-directory /flash  
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Configuração de servidor FTP' executado com sucesso!")  


# Loop principal
while True:
    print("1. Autorizar ONU")
    print("2. Habilitar PON")
    print("3. Script VSOL")
    print("4. Script ZTE-F601")
    print("5. Configuração GEI")
    print("6. Configuração XGEI")
    print("7. Configuração GPON")
    print("8. Ativação Plug-and-Play(PnP)")
    print("9. Configuração TCP")
    print("10. VEIP da ONU")
    print("11. Configuração de VLAN")
    print("12. Gerenciamento de MAC")
    print("13. Interface de Gerenciamento")
    print("14. Conectividade da OLT")
    print("15. Configuração de NAT")
    print("16. Portas DHCP")
    print("17. Acesso SNMP")
    print("18. Servidor FTP")
    print("?. Sair")  
    opcao = input("Escolha: ")

    if opcao == "1":             #Funçao pra adicionar os scripts
        add_authorize_onu()   
    elif opcao == "2":
        add_enable_pon()      
    elif opcao == "3":
        add_script_vsol()    
    elif opcao == "4": 
        add_script_F601()     
    elif opcao == "5": 
        add_script_gei()       
    elif opcao == "6": 
        add_script_xgei()       
    elif opcao == "7": 
        add_config_gpon()       
    elif opcao == "8": 
        add_pnp()       
    elif opcao == "9": 
        add_tcp()       
    elif opcao == "10": 
        add_veip_onu()       
    elif opcao == "11": 
        add_vlans()       
    elif opcao == "12": 
        add_mac()       
    elif opcao == "13": 
        add_mng()       
    elif opcao == "14": 
        add_arp()       
    elif opcao == "15": 
        add_nat()       
    elif opcao == "16": 
        add_dhcp()       
    elif opcao == "17": 
        add_snmp()       
    elif opcao == "18": 
        add_ftp()       
    
    elif opcao == "?":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")