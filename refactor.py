import customtkinter

customtkinter.set_appearance_mode("dark") #general theme
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x750")
janela.title("OLT automate")

# Criando um Label de Título
titulo = customtkinter.CTkLabel(janela, text="OLT Automate", font=("Arial", 28))
titulo.pack(pady=(30, 10))

sub_titulo = customtkinter.CTkLabel(janela, text="ZTE C300/320/350", font=("Arial", 15))
sub_titulo.pack(pady=10)

# Criando um Widget de Texto para Exibir os Comandos
output_text = customtkinter.CTkTextbox(janela, width=480, height=230, state="disabled")# output permite inserir texto
output_text.pack(pady=10)

# As funções que serão exibidas ao clicar nos botões
def verificação_status_command():
    output_text.configure(state="normal")  # Habilita edição temporária dentro do widget
    output_text.delete("1.0", "end")  # Limpa o texto anterior, dentro do widget
    output_text.insert("end", "VERIFICAÇÃO DE STATUS:\n\nINSERVICE - Funcionando normalmente\nCONFIGING - Placa sendo configurada\nCONFIGFAILED - Falha no processo de configuração\nDISABLE - Sem comunicação\nHWONLINE - Versão diferente de software\nOFFLINE - Placa adicionada logicamente, não fisicamente\nSTANDBY - Modo de espera\nTYPE MISMATCH - Placa diferente do tipo físico\nNO POWER - Desligada\n")
    output_text.configure(state="disabled")  # Bloqueia edição novamente

def primeiro_acesso_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "PRIMEIRO ACESSO:\n\nO endereço IP de fábrica da OLT é 136.1.1.100.\nA senha de acesso inicial é zte.\n\nSe não for possível fazer o acesso remoto, faça via porta CLI:\n\nA conexão com a OLT deve ser feita através da porta CLI com a velocidade de 9600 baud.\n\nPara acessar o modo privilegiado, utilize o comando:\nenable\nA senha para entrar no modo privilegiado é zxr10\n")
    output_text.configure(state="disabled")

def alteracao_nome_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "ALTERAÇÃO DE NOME PARA A OLT:\n\nhostname [NOVO NOME]\nexit\n")
    output_text.configure(state="disabled")
    
def data_hora_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "AJUSTE DE DATA E HORA:\n\nImportante para identificação de logs e erros no horário correto.\n\nconf t\nclock timezone BRT -3\nexit\n\nclock set 00:00:00 mês - dia - ano\nptp\nexit\n")
    output_text.configure(state="disabled")
    
def autosave_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "ATIVAR AUTO-SAVE E SALVAR:\n\nVocê pode salvar suas configurações de forma manual com o comando abaixo:\n\n[CONFIGURAÇÃO FEITA]\nexit\nwrite\n\n•Você também pode ativar o auto-save:\nauto-write\nauto-write 24\n")
    output_text.configure(state="disabled")
    
def ativacao_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "ATIVANDO E DESATIVANDO INTERFACES:\n\nGeralmente ativação e desativação de interfaces seguem um padrão:\n\nenable\nno shutdown\nshutdown\n")
    output_text.configure(state="disabled")
    
def verificacao_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "VERIFICAÇÃO DE CONFIGURAÇÕES APLICADAS:\n\nAqui também temos um padrão geralmente usado para verificar configurações gerais:\n\nshow this\nshow running-config\nshow running-config interface mngl\nshow running-config interface gpon-onu\nshow remote-onu wan-ip gpon-onu_1/1/1\n")
    output_text.configure(state="disabled")
    
def interfaces_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "INTERFACES DA OLT:\n\nPara melhor compreensão, é interessante saber quais interfaces presentes e pra que servem:\n\nINTERFACE GPON OLT:\nAqui você está configurando a porta da OLT que se conecta à rede de fibra óptica GPON. Essa interface é onde você vai gerenciar a comunicação entre a OLT e os clientes (geralmente as ONUs).\n\nINTERFACE GPON ONU:\nEste comando é para configurar as ONUs (Optical Network Units), que são os dispositivos na ponta da rede (do lado do cliente). Elas conectam os dispositivos da casa do cliente à OLT.\n\nINTERFACE XGEI:\nÉ uma interface de rede de alta velocidade (10G Ethernet), geralmente usada para comunicação entre a OLT e outros dispositivos ou redes. É mais rápida do que as interfaces comuns.\n\nINTERFACE GEI:\nEssa interface é uma porta Ethernet (1G) usada para comunicação em velocidades mais baixas, conectando dispositivos à rede.\n\nINTERFACE PON:\nA PON (Passive Optical Network) é a interface que conecta a OLT ao backbone da rede de fibra ótica. É a porta principal para a distribuição da internet para os clientes.\n")
    output_text.configure(state="disabled")
    
def pnp_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "HABILITAR A DETECÇÃO PLUG-AND-PLAY DAS PLACAS E TIPO DE CHASSI:\n\nconf t\nset-pnp enable\nadd-rack rackno 1 racktype C320Rack\nadd-shelf rackno 1 shelfno 1 shelftype C320_SHELF\n")
    output_text.configure(state="disabled")
    
def ip_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "CONFIGURAR UM NOVO IP DE ACESSO:\n\nDefine o IP para acesso remoto à OLT. A máscara cobre um range maior de IPs\n\ninterface mng1\nip address [IP] [MASK]\nconfig-filename startrun.dat\nnegotiation auto\ntag-mode untag\n")
    output_text.configure(state="disabled")
    
def gateway_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "ADICIONAR GATEWAY PADRÃO:\n\nconf t\nno ip route 0.0.0.0 0.0.0.0\nip route 0.0.0.0 0.0.0.0 [IP do GATEWAY]          \nexit\nwrite\n")
    output_text.configure(state="disabled")
    
def vlangerencia_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "VLAN DE GERENCIA:\n\nvlan 100\nname GERENCIA\nexit\n\ninterface vlan100 ip address [IP] [MASK]\nexit\n")
    output_text.configure(state="disabled")
    
def uplink_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "INTERFACE DE UP-LINK\GEI:\n\ninterface gei_1/1/1\nno shutdown\nswitchport vlan 100 tag\nlinktrap enable\nport-protect disable\nuplink-isolate disable\n")
    output_text.configure(state="disabled")
    
def acessoremoto_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "HABILITAR SSH:\n\nssh server authentication type chap\nss server version 2\nusername zte password zte privilege 15\n\nHABILITAR TELNET:\n\nsecurity-mgmt 999 state enable ingress-type lan protocol telnet\nusername zte password zte privilege 15\nshow security-mgmt\n")
    output_text.configure(state="disabled")
    
def banda_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "CONFIGURAÇÃO DE BANDA:\n\nprofile tcont 1G-UP type 5 fixed 64 assured 64 maximum 1048064\nprofile traffic 1G-DOWN sir 1048064 pir 1048064\n\nsir = Banda garantida\npir = Banda máxima\n")
    output_text.configure(state="disabled")
    
def vlanonu_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "ONU PROFILE VLAN:\n\nonu profile vlan [000] tag-mode tag cvlan [000]\n")
    output_text.configure(state="disabled")
    
def veip_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "ACESSO REMOTO E VEIP DE ONU:\n\nflow mode 1 tag-filter vlan-filter untag-filter discard\nflow 1 pri 0 vlan 100\ngemport 1 flow 1\nswitchport-bind switch_0/1 iphost 1\nswitchport-bind switch_0/1 veip 1\ndhcp-ip ethuni eth_0/1 from-internet\n\nsecurity-mgmt 998 state enable mode forward ingress-type lan protocol web https\nsecurity-mgmt 999 state enable ingress-type lan protocol ftp telnet ssh snmp tr069 ")
    output_text.configure(state="disabled")
    
def rede_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "PPPOE, REDE E SENHA DA ONU:\n\npon-onu-mng gpon-onu_1/1/1\nmode pppoe username [REDE] password [SENHA]\npassword senha vlan-profile 100\n\nssid ctrl wifi_0/1 name 2.4G\nssid crtl wifi_0/5 nome 5G\n\nwifi_0/1 encrypt aes key senha\nwifi_0/5 encrypt aes key senha\n\nssid ctrl wifi_0/1 user-isolation disable\n")
    output_text.configure(state="disabled")
    
def pon_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "ATIVAÇÃO DE PON:\n\ninterface gpon-olt_1/1/1\nshow this\nshutdown (DESATIVADA)\nlinktrap disable\n\nno shutdown (ATIVADA)\nexit\n")
    output_text.configure(state="disabled")
    
def autorizar_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "AUTORIZAR ONU:\n\ninterface gpon-olt_1/3/12\nonu [NÚMERO DA ONU] type [MODELO] sn [MAC]\n")
    output_text.configure(state="disabled")
    
def backup_reset_command():
    output_text.configure(state="normal") 
    output_text.delete("1.0", "end")  
    output_text.insert("end", "BACKUP:\n\n•Usando Mikrotik, vamos encontrar o arquivo de backup, para darmos o comando na OLT.\n\nMIKROTIK > SYSTEM > USERS\nATIVAR PORTA FTP\nFILE LIST0 (ARQUIVO DE BACKUP DA OLT)\n\nTERMINAL DA OLT:\nfile upload cfg-startup *.* ftp ipaddress [IP de FTP] user [USUÁRIO] password [SENHA]\n\nRESET:\nfile delete cfg-startup *.*\nyes\nreboot\nyes\n")
    output_text.configure(state="disabled")
    
# Criando um Frame para os botões
frame_botoes = customtkinter.CTkFrame(janela)
frame_botoes.pack(pady=10)

# Organizando os botões em três colunas
btn_status = customtkinter.CTkButton(frame_botoes, text="STATUS", command=verificação_status_command)
btn_status.grid(row=0, column=0, padx=10, pady=5)

btn_acesso = customtkinter.CTkButton(frame_botoes, text="ACESSO", command=primeiro_acesso_command)
btn_acesso.grid(row=0, column=1, padx=10, pady=5)

btn_alterarnome = customtkinter.CTkButton(frame_botoes, text="MUDAR NOME", command=alteracao_nome_command)
btn_alterarnome.grid(row=0, column=2, padx=10, pady=5)

btn_datahora = customtkinter.CTkButton(frame_botoes, text="DATA E HORA", command=data_hora_command)
btn_datahora.grid(row=1, column=0, padx=10, pady=5)

btn_autosave = customtkinter.CTkButton(frame_botoes, text="AUTO-SAVE", command=autosave_command)
btn_autosave.grid(row=1, column=1, padx=10, pady=5)

btn_ativacao = customtkinter.CTkButton(frame_botoes, text="ATIVAÇÃO", command=ativacao_command)
btn_ativacao.grid(row=1, column=2, padx=10, pady=5)

btn_verificacao = customtkinter.CTkButton(frame_botoes, text="VERIFICAÇÃO", command=verificacao_command)
btn_verificacao.grid(row=2, column=0, padx=10, pady=5)

btn_interfaces = customtkinter.CTkButton(frame_botoes, text="INTERFACES", command=interfaces_command)
btn_interfaces.grid(row=2, column=1, padx=10, pady=5)

btn_pnp = customtkinter.CTkButton(frame_botoes, text="PNP", command=pnp_command)
btn_pnp.grid(row=2, column=2, padx=10, pady=5)

btn_ip = customtkinter.CTkButton(frame_botoes, text="IP", command=ip_command)
btn_ip.grid(row=3, column=0, padx=10, pady=5)

btn_gateway = customtkinter.CTkButton(frame_botoes, text="GATEWAY", command=gateway_command)
btn_gateway.grid(row=3, column=1, padx=10, pady=5)

btn_vlangerencia = customtkinter.CTkButton(frame_botoes, text="VLAN MNG", command=vlangerencia_command)
btn_vlangerencia.grid(row=3, column=2, padx=10, pady=5)

btn_uplink = customtkinter.CTkButton(frame_botoes, text="UPLINK", command=uplink_command)
btn_uplink.grid(row=4, column=0, padx=10, pady=5)

btn_acessoremoto = customtkinter.CTkButton(frame_botoes, text="Telnet/SSH", command=acessoremoto_command)
btn_acessoremoto.grid(row=4, column=1, padx=10, pady=5)

btn_banda = customtkinter.CTkButton(frame_botoes, text="PROFILE BANDA", command=banda_command)
btn_banda.grid(row=4, column=2, padx=10, pady=5)

btn_vlanonu = customtkinter.CTkButton(frame_botoes, text="VLAN ONU", command=vlanonu_command)
btn_vlanonu.grid(row=5, column=0, padx=10, pady=5)

btn_veip = customtkinter.CTkButton(frame_botoes, text="VEIP ONU", command=veip_command)
btn_veip.grid(row=5, column=1, padx=10, pady=5)

btn_rede = customtkinter.CTkButton(frame_botoes, text="REDE ONU", command=rede_command)
btn_rede.grid(row=5, column=2, padx=10, pady=5)

btn_pon = customtkinter.CTkButton(frame_botoes, text="ATIVAR PON", command=pon_command)
btn_pon.grid(row=6, column=0, padx=10, pady=5)

btn_autorizar = customtkinter.CTkButton(frame_botoes, text="AUTORIZAR ONU", command=autorizar_command)
btn_autorizar.grid(row=6, column=1, padx=10, pady=5)

btn_backupreset = customtkinter.CTkButton(frame_botoes, text="BACKUP/RESET", command=backup_reset_command)
btn_backupreset.grid(row=6, column=2, padx=10, pady=5)


btn_sair = customtkinter.CTkButton(frame_botoes, text="SAIR", command=janela.quit, fg_color="red", text_color="white")
btn_sair.grid(row=7, column=1, padx=10, pady=5)






janela.mainloop()