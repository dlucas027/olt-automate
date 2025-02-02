# OLT ZTE C320

Este é um guia completo, linha a linha das principais configurações da OLT ZTE C320.

---

## Funcionalidades  

- **Como se conectar**: Instruções para acesso à OLT via Telnet e SSH.  

- **Ativação e desativação de PON**: Instruções de ativação nas PONS.

- **Como salvar alterações**: Como salvar alterações.

- **Autorização e desautorização de ONUS**: Instruções para autorização de ONUS.

- **Como acessar as interfaces**: Como acessar as intefaces G-PON, PON, etc.

- **Configuração de VLANs**: Modelo de configuração de VLAN.

- **Exemplos de scripts para ONUs**: Scripts usados, que podem ser reaproveitados.

- **Configuração de porta Trunk**: Ativação e VLAN.

- **Segurança e autenticação**: Configurações de segurança.

- **Data, hora, login e senhas**: Como configurar.

---

## Objetivo  

O objetivo deste guia é fornecer uma maneira simples de configurar e gerenciar a OLT ZTE C320, facilitando a conexão e a gestão de ONUs.

---

## 📚 Instruções de Configuração  

### Conectar via Telnet
Para conectar à OLT via Telnet, use o comando abaixo:
```bash
telnet 131.198.0.202 IP fictício
```
Telnet usa a porta 23 por padrão.
SSH usa a porta 22 por padrão.

---

## Ativação de PON

INTERFACE GPON OLT
interfaceno  gpon-olt_1/1/1
show this
 shutdown (DESATIVADA)
  linktrap disable

---

## Desativação de PON

Shutdown

---

## Salvar configurações

exit
write (SALVAR)
show running-config (VISUALIZAR CONFIGURAÇÕES)

---

## Autorizar ONU

-INTERFACE OLT

interface gpon-olt_1/17/12
  onu 1 type ZTE-F601 sn ZTEGCCE7B888

---

## Desautorizar ONU

-INTERFACE OLT

interface gpon-olt_?/?/?
no onu 2

---

## Configurar VLAN da ONU

-INTERFACE ONU

interface gpon-onu_1/1/3:1
  description TESTE_NOKIA_G1426GA
  sn-bind enable sn 
  tcont 1 profile 1G-UP
  gemport 1 tcont 1
  service-port 1 vport 1 user-vlan 100 vlan 100 (ESPECIFICAR VLAN)

---

 ## Exemplos de script para ONU


PON
onu-type VSOL-BRIDGE-1P gpon
onu-type VSOL-BRIDGE-1P gpon max-tcont 8
onu-type VSOL-BRIDGE-1P gpon max-gemport 32
onu-type VSOL-BRIDGE-1P gpon max-switch-perslot 8
onu-type VSOL-BRIDGE-1P gpon max-flow-perswitch 8
onu-type VSOL-BRIDGE-1P gpon max-iphost 5
onu-type-if VSOL-BRIDGE-1P eth_0/1

onu-type ZTE-F601 gpon
onu-type ZTE-F601 gpon max-tcont 8
onu-type ZTE-F601 gpon max-gemport 32
onu-type ZTE-F601 gpon max-switch-perslot 8
onu-type ZTE-F601 gpon max-flow-perswitch 8
onu-type ZTE-F601 gpon max-iphost 5
onu-type-if ZTE-F601 eth_0/1

pon
  onu-type ZTE-F660 gpon
  onu-type ZTE-F660 gpon max-tcont 8
  onu-type ZTE-F660 gpon max-gemport 32
  onu-type ZTE-F660 gpon max-switch-perslot 8
  onu-type ZTE-F660 gpon max-flow-perswitch 8
  onu-type ZTE-F660 gpon max-iphost 5
  onu-type DLINK-MODELOX gpon
  onu-type DLINK-MODELOX gpon max-tcont 8
  onu-type DLINK-MODELOX gpon max-gemport 32
  onu-type DLINK-MODELOX gpon max-switch-perslot 8
  onu-type DLINK-MODELOX gpon max-flow-perswitch 8
  onu-type DLINK-MODELOX gpon max-iphost 5
  onu-type NOKIA_G1425GB gpon
  onu-type NOKIA_G1425GB gpon max-tcont 8
  onu-type NOKIA_G1425GB gpon max-gemport 32
  onu-type NOKIA_G1425GB gpon max-switch-perslot 8
  onu-type NOKIA_G1425GB gpon max-flow-perswitch 8
  onu-type NOKIA_G1425GB gpon max-iphost 5
  onu-type NOKIA_G1426GA gpon description 4xETH_2xWIFI
  onu-type NOKIA_G1426GA gpon max-tcont 8
  onu-type NOKIA_G1426GA gpon max-gemport 32
  onu-type VSOL-BRIDGE-1P gpon
  onu-type VSOL-BRIDGE-1P gpon max-tcont 8
  onu-type VSOL-BRIDGE-1P gpon max-gemport 32
  onu-type VSOL-BRIDGE-1P gpon max-switch-perslot 8
  onu-type VSOL-BRIDGE-1P gpon max-flow-perswitch 8
  onu-type VSOL-BRIDGE-1P gpon max-iphost 5
  onu-type-if ZTE-F660 eth_0/1
  onu-type-if DLINK-MODELOX eth_0/1
  onu-type-if NOKIA_G1425GB eth_0/1
  onu-type-if VSOL-BRIDGE-1P eth_0/1
  uncfg-onu-display-info model sn pw 

---

## Configurar VEIP na ONU

-INTERFACE DE CONFIGURAÇÃO GERAL

-pon-onu-mng gpon-onu_1/1/3:1

  flow mode 1 tag-filter vlan-filter untag-filter discard
  flow 1 pri 0 vlan 100
  gemport 1 flow 1
  switchport-bind switch_0/1 iphost 1
  switchport-bind switch_0/1 veip 1
  dhcp-ip ethuni eth_0/1 from-internet
security-mgmt 998 state enable mode forward ingress-type lan protocol web https
security-mgmt 999 state enable ingress-type lan protocol ftp telnet ssh snmp tr069

---

## Configuração interface GEI

-(config-if)#show this

      interface gei_1/4/1
        no shutdown
        hybrid-attribute fiber
        negotiation auto
        flowcontrol disable
        linktrap enable
        switchport mode trunk
        switchport vlan 1,13,11-12,50,100 tag (VERIFICAR SE A VLAN ESTÁ NA INTERFACE)

---

## Visualizar configurações

show running-config

---

## Modos operacionais

crtv disable (Desativa a Compact Routing Table View (CRTV), o que é comum em redes maiores para otimizar o uso de memória)
load-balance enable (Habilitar balanceamento de carga entre links é uma funcionalidade suportada, especialmente em OLTs de grande porte)
operator-mode NORMAL (configura o dispositivo para operar de maneira padrão)
system-forwarding-mode normal-mode (configura o dispositivo para operar de maneira padrão)

---

## Configurações TCP 

ip tcp finwait-time 600 (Tempo no estado de FIN WAIT)
ip tcp queuemax 5  (Máximo de conexões na fila TCP)
ip tcp synwait-time 30 (Tempo de espera para resposta SYN)
ip tcp window-size 2144 (Tamanho da janela TCP para controle de fluxo)

---

## Configurações GPON

gpon
  profile tcont 1G-UP type 5 fixed 64 assured 64 maximum 1048064
  profile traffic 1G-DOWN sir 1048064 pir 1048064

    profile tcont: Configura um perfil de T-CONT (alocação de banda no GPON).
    1G-UP: (Upload)
    fixed 64: (Banda fixa)
    assured 64: (Banda garantida)
    maximum 1048064: (Banda máxima)
    profile traffic: Perfil de tráfego para download (1G-DOWN).
        
        -sir: Banda garantida.
        -pir: Banda máxima permitida.

---

## Configuração de PNP

set-pnp enable (Habilita o Plug-and-Play (PnP) na OLT, que pode ser usado para facilitar a configuração automática de dispositivos conectados, como ONUs ou outras unidades de rede. Isso ajuda a simplificar a implementação e a integração de novos dispositivos)
add-rack rackno 1 racktype C320Rack
add-shelf rackno 1 shelfno 1 shelftype C320_SHELF
add-card rackno 1 shelfno 1 slotno 1 GTGH
add-card rackno 1 shelfno 1 slotno 3 PRAM
add-subcard rackno 1 shelfno 1 slotno 4 subcardno 1 UCDC/3

---

## Verificação de segurança URPF

urpf log off (Unicast Reverse Path Forwarding: é um mecanismo de segurança que verifica se os pacotes de dados recebidos em uma interface possuem um caminho de retorno válido, ou seja, se eles poderiam ter sido enviados de volta através da mesma interface pela qual chegaram. Isso ajuda a prevenir ataques de falsificação de IP (spoofing) e injeção de pacotes maliciosos na rede.)

---

## Gerenciamento de MAC

mac aging-time 300 (Define o tempo de expiração dos endereços MAC como 5 minutos)
mac monitor-period 10 (Estabelece que a tabela de endereços MAC será monitorada a cada 10 segundos)
mac usage-threshold 70 (Define o limite de utilização da tabela de endereços MAC como 70% da sua capacidade)

---

## Quadros ethernet e logs de diagnóstico

eth-switch max-frame-length  1600 (tamanho máximo do quadro Ethernet como 1600 bytes (comum para quadros Ethernet padrão))
port diaglog status-info disable (Reduz o volume de logs: Ao desabilitar o log de status, o dispositivo não registra informações relacionadas ao status das portas, como alterações de estado (up/down) ou falhas)

---

## Desativação de atualizações automáticas

auto-update backup disable (Impede que o dispositivo faça backup automático da configuração ou do sistema durante ou após uma atualização de software)
auto-update activate disable (Desativa a ativação automática de atualizações)

---

## Economia de recursos

sdisk disable (Desabilita o uso do disco de armazenamento no dispositivo, o que pode ser necessário em casos de economia de recursos ou para impedir o uso não autorizado do armazenamento)

---

## pnp para ONUS

onu-pnp (habilita o Plug and Play para as ONUs)
 
---

## Configuração de VLANs

no vlan-reserve 4091 out-voip (Desativa a reserva da VLAN 4091 para voip de saída (out-voip))
no vlan-reserve 4092 in-voip (Desativa a reserva da VLAN 4092 para voip de entrada (in-voip))
no vlan-reserve 4094 gpon (A VLAN 4094 estava reservada para o tráfego relacionado ao GPON. O comando no vlan-reserve permite que a VLAN 4094 seja usada para outros propósitos, caso necessário.)
!
vlan database  (Este comando abre a seção onde as VLANs são definidas e configuradas)
  vlan 1,11-19,50,100 (VLANs são configuradas para serem usadas no dispositivo, faixa 11-19 indica várias VLANs consecutivas, de 11 a 19, e as VLANs 1, 50 e 100 são definidas)
!
vlan 100 ((uma técnica de encapsulamento de VLANs), que permite encapsular uma VLAN dentro de outra, sendo útil para expansão e escalabilidade de redes de provedores.)
  description VLAN_de_QINQ

---

## Monitoramento de desempenho

his-performance sample enable (Este comando ativa a coleta de dados de desempenho históricos do dispositivo)
his-performance alarm enable (Com este comando, o dispositivo começará a gerar alarmes ou notificações caso algum parâmetro de desempenho predefinido seja excedido (como uso excessivo de CPU, memória ou tráfego). Isso permite que o administrador seja alertado sobre possíveis problemas no desempenho da rede)
his-performance auto-upload disable (Este comando desativa a função de envio automático dos dados de desempenho registrados para um servidor ou sistema de monitoramento externo. Isso pode ser útil caso o administrador queira armazenar os dados localmente ou tenha restrições de largura de banda ou armazenamento para o upload)
!

--- 

## Data e hora

clock set 14:30:00 Jan 31 2025
ptp (Ativa ou configura o Protocolo de Sincronização de Tempo de Precisão (PTP), essencial para redes que requerem sincronização de tempo precisa)

---

## Controle de portas DHCP

ip dhcp snooping control-port enable (Habilita o controle de portas para DHCP snooping, ajudando na segurança contra ataques DHCP)
port-identification access-node-id-type inband-mac (Configura a identificação do nó de acesso usando o MAC em banda.)
port-identification rackno 1 frameno 1 (Define a identificação física da porta com base no número do rack e frame)

---

## Multicast

igmp enable (Habilita o IGMP para gerenciar multicast na rede)
mld disable (Desabilita o MLD, desativando o gerenciamento de multicast para IPv6)
  mib-compatibility iftable v1 ( Ativa a compatibilidade com MIB versão 1 para a tabela de interfaces, garantindo interoperabilidade com sistemas legados de gerenciamento de rede)

---

## Segurança de portas

security port-protect enable (Habilita a proteção de segurança nas portas, impedindo o acesso não autorizado e ataques na camada de rede)

---

## Gerenciamento de MACs virtuais

virtual-mac flexible-syntax-profile MT (Configura um perfil flexível para endereços MAC virtuais)
add Ctrl-Byte 0 width 6 index 6 (Adiciona um byte de controle ao endereço MAC virtual, com especificações de largura e índice)
exit
virtual-mac access-node-id 0 (Define o ID do nó de acesso associado ao endereço MAC)
!
epm  (Configura o modo passthrough para EPON, permitindo que os dados passem sem processamento)
 mode passthrough  

---

## Interface de gerenciamento MNG1

interface mng1
  ip address 136.1.1.100 255.255.0.0 (Define o IP 136.1.1.100 para acesso remoto à OLT. A máscara 255.255.0.0 cobre um range maior de IPs)
  config-filename startrun.dat (Define o nome do arquivo de configuração inicial que será carregado ao iniciar a OLT)
  negotiation auto (Configura a negociação automática de velocidade e duplex na interface)
  tag-mode untag (Define que essa interface de gerenciamento não usará VLANs (tráfego não marcado))


---

## VLANS Configuradas (interface vlan x)

interface vlan 11 (VLAN 11 está criada, mas sem configuração adicional)
!
interface vlan 12 (VLAN 12 também foi criada, mas sem IP ou regras)
!
interface vlan 50 (Define um IP para a VLAN 50, possivelmente para um gateway de comunicação. A máscara 255.255.255.252 indica que essa VLAN suporta apenas 2 hosts (ponto a ponto))
  ip address 10.200.50.2 255.255.255.252
!
interface vlan 100 (VLAN 100 foi criada, mas sem IP ou configuração adicional)
!
interface null1 (A interface null é usada para descartar pacotes que não devem ser roteados, funcionando como um "black hole" para tráfego indesejado)

---

## Inteface GPON 

interface gpon-olt_1/1/1
  no shutdown (Ativa a porta GPON 1/1/1)
  linktrap disable ( Desativa os traps SNMP para eventos de link (evita alertas automáticos para falhas de conexão))

---

## Interface GEI (Trunk)

interface gei_1/4/1 (Seleciona a interface Gigabit Ethernet 1/4/1)  
  no shutdown (Ativa a interface, permitindo o tráfego de rede)  
  hybrid-attribute fiber (Configura a interface como híbrida, associando-a ao tipo de mídia fibra)  
  negotiation auto (Habilita a negociação automática da velocidade e do modo duplex da interface)  
  flowcontrol disable (Desativa o controle de fluxo para essa interface)  
  linktrap enable (Habilita notificações (trap) quando o estado da interface muda (up/down))  
  switchport mode trunk (Configura a interface como trunk, permitindo o tráfego de múltiplas VLANs)  
  switchport vlan 1,11-19,50,100 tag (Define as VLANs permitidas no trunk e aplica a tag VLAN para elas)  
  port-protect disable (Desativa a proteção de porta, permitindo a utilização normal)  
  uplink-isolate disable (Desativa a isolação de uplink, permitindo o tráfego normal entre interfaces)  

---

## Interface XGEI (Trunk de tráfego VLAN)

interface xgei_1/4/2 (Seleciona a interface 10 Gigabit Ethernet 1/4/2)  
  phy-attribute lan (Define a interface como LAN, ajustando parâmetros físicos)  
  shutdown (Desativa a interface, impedindo o tráfego de rede)  
  hybrid-attribute fiber (Configura a interface como híbrida, associando-a ao tipo de mídia fibra)  
  no negotiation auto (Desativa a negociação automática de velocidade e duplex)  
  speed 10000 (Define a velocidade da interface para 10 Gbps)  
  duplex full (Configura a interface para modo full-duplex)  
  flowcontrol disable (Desativa o controle de fluxo para essa interface)  
  linktrap enable (Habilita notificações (trap) quando o estado da interface muda (up/down))  
  switchport mode trunk (Configura a interface como trunk, permitindo o tráfego de múltiplas VLANs)  
  switchport vlan 1 tag (Permite apenas a VLAN 1 no trunk e aplica a tag VLAN)  
  port-protect disable (Desativa a proteção de porta, permitindo a utilização normal)  
  uplink-isolate disable (Desativa a isolação de uplink, permitindo o tráfego normal entre interfaces)  

---

## LDP (Label Distribution Protocol)

mpls ldp dynamic-capability (Habilita a capacidade dinâmica do LDP para MPLS)  

---

## Rota e conectividade

p route 0.0.0.0 0.0.0.0 10.200.50.1 (Cria uma rota padrão para o gateway 10.200.50.1)  
!
ipoa inatmarp-interval 10 (Define o intervalo de atualização do inATMARP para 10 segundos)  
ipoa gateway-arp-interval 10 (Define o intervalo de atualização do ARP do gateway para 10 segundos)  
!

---

## Parametros de NAT

mpnat trans-table aging-time 60 (Define o tempo de expiração das entradas na tabela de tradução NAT para 60 segundos)  
mpnat onu-telnet idle-time 3 (Define o tempo máximo de inatividade para conexões Telnet de ONUs como 3 minutos)  
mpnat onu-ftp aging-time 5 (Define o tempo de expiração para sessões FTP em ONUs como 5 minutos)  
mpnat onu-snmp aging-time 30 (Define o tempo de expiração para sessões SNMP em ONUs como 30 minutos)  
mpnat onu-ftp-data aging-time 5 (Define o tempo de expiração para conexões de transferência de dados FTP em ONUs como 5 minutos)  
mpnat onu-mng-port auto-alloc disable (Desativa a alocação automática de portas de gerenciamento para ONUs)  
mpnat modem-telnet idle-time 3 (Define o tempo máximo de inatividade para conexões Telnet de modems como 3 minutos)  

---

## Segurança e usuários

! (Separador de configuração, geralmente indica fim ou início de um bloco de comandos)  
auto-write disable (Desativa a gravação automática da configuração, exigindo que o administrador salve manualmente)  
!  
inband-management enable (Habilita o gerenciamento inband, permitindo a administração do equipamento pela própria rede de dados)  
!  
username user-suspend mode none (Desativa a suspensão automática de contas de usuário)  
!  
username high-level-security disable (Desativa requisitos de segurança elevados para senhas de usuários)  
username inactivity-day 120 (Define que contas de usuário inativas por 120 dias serão desativadas)  
username pwd-expire-day 90 (Define que senhas de usuários expiram após 90 dias, exigindo alteração)  

---

## Senhas e Login

! (Separador de configuração, geralmente indica fim ou início de um bloco de comandos)  
enable secret level 15 5 *********/UA== (Define uma senha criptografada para acesso de nível 15, que é o mais alto na hierarquia de permissões)  
!  
service password-encryption (Habilita a criptografia de senhas no sistema para maior segurança)  
!  
!  
username  LOGIN password 7 5U3sresLuvB2I+t5+C7zXA== privilege 15 first-login true (Cria o usuário 'LOGIN' com senha criptografada e nível de privilégio 15, exigindo alteração na primeira vez que fizer login)  
username SENHA  password 7 5U3sresLuvB2I+t5+C7zXA== max-sessions 16 (Permite até 16 sessões simultâneas para o usuário 'LOGIN')  
username SENHA enable (Habilita a conta de usuário 'oltcloud')  
username login-range name LOGIN login-begin 00:00:00 login-end 23:59:59 (Define que o usuário 'LOGIN' pode fazer login em qualquer horário do dia)  
username expire-date name LOGIN datetime 12-31-2099 23:59:59 (Define que a conta 'LOGIN' expira apenas em 31 de dezembro de 2099 às 23:59:59)  
username password-changed name LOGIN is-changed false (Indica que a senha do usuário 'LOGIN' ainda não foi alterada desde a criação)  

---

## Autenticação e autorização

user-authentication-type local (Define que a autenticação de usuários será realizada localmente, usando as credenciais configuradas diretamente no dispositivo)  
user-authorization-type local (Define que a autorização de usuários será feita localmente, com base nas permissões configuradas no dispositivo)  
!  
help message full (Exibe a mensagem completa de ajuda no dispositivo, fornecendo informações detalhadas sobre os comandos e configurações)  

---

## data e hora para logs e depuração

service timestamps log datetime localtime (Ativa a exibição de carimbos de data e hora em logs, utilizando o horário local do dispositivo)  
service timestamps debug datetime localtime (Ativa a exibição de carimbos de data e hora em mensagens de depuração (debug), utilizando o horário local do dispositivo)  

---

## Configuração de acesso SNMP

snmp-server location No.889 BiBo Rd.PuDong District, Shanghai, China (Define o local físico do dispositivo para SNMP, útil para identificar a localização do equipamento em grandes redes)  
snmp-server contact +86-21-68895000 (Define um número de contato para suporte técnico ou administração do dispositivo via SNMP)  
snmp-server packetsize 8192 (Define o tamanho máximo dos pacotes SNMP para 8192 bytes, o que pode ser útil em redes com grandes volumes de dados)  
snmp-server engine-id mode mac (Configura o **Engine ID** SNMP usando o **endereço MAC** do dispositivo, que é uma identificação única no SNMPv3)  
snmp-server group GroupPriv15 v3 priv read AllView write AllView (Cria um grupo SNMP `GroupPriv15` com **privilégios de leitura e escrita** completos usando SNMPv3 com **autenticação e criptografia** (priv))  
snmp-server group GroupPriv10 v3 priv read AllView write ViewPriv10 (Cria o grupo `GroupPriv10` com **leitura total** e **escrita restrita** (ViewPriv10), também com autenticação e criptografia)  
snmp-server group GroupPriv5 v3 priv read AllView write ViewPriv5 (Cria o grupo `GroupPriv5` com **leitura total** e **escrita restrita** (ViewPriv5), também com autenticação e criptografia)  
snmp-server group GroupPriv0 v3 priv read AllView (Cria o grupo `GroupPriv0` com **leitura total** e **sem privilégios de escrita** usando SNMPv3 com autenticação e criptografia)  
snmp-server community oltcloud view AllView rw (Define uma comunidade SNMP `oltcloud` com **leitura e escrita** (`rw`), acessando a `AllView`)  
snmp-server view AllView 1.2 included (Define o MIB (Management Information Base) `AllView`, incluindo o **OID 1.2**)  
snmp-server view AllView 1.3 included (Inclui o OID **1.3** no MIB `AllView`)  
snmp-server view ViewPriv5 1.2 included (Define a visualização `ViewPriv5` para **incluir** o OID **1.2**)  
snmp-server view ViewPriv5 1.3 included (Define a visualização `ViewPriv5` para **incluir** o OID **1.3**)  
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.10.1 excluded (Exclui o OID **1.3.6.1.4.1.3902.1082.10.1** da visualização `ViewPriv5`)  
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.10.10 excluded (Exclui o OID **1.3.6.1.4.1.3902.1082.10.10** da visualização `ViewPriv5`)  
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.20.1 excluded (Exclui o OID **1.3.6.1.4.1.3902.1082.20.1** da visualização `ViewPriv5`)  
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.20.10 excluded (Exclui o OID **1.3.6.1.4.1.3902.1082.20.10** da visualização `ViewPriv5`)  
snmp-server view ViewPriv10 1.2 included (Inclui o OID **1.2** na visualização `ViewPriv10`)  
snmp-server view ViewPriv10 1.3 included (Inclui o OID **1.3** na visualização `ViewPriv10`)  
snmp-server view ViewPriv10 1.3.6.1.4.1.3902.1082.20.10 excluded (Exclui o OID **1.3.6.1.4.1.3902.1082.20.10** da visualização `ViewPriv10`)  
!  

---

## Servidor FTP

ftp-server enable listen 21 (Habilita o servidor FTP para escutar na porta **21**, que é a porta padrão do FTP)  
ftp-server top-directory /flash (Define o diretório raiz do servidor FTP como **/flash**, onde os arquivos poderão ser acessados ou armazenados)  

---

## Registro de logs, limite de usuarios e timeout

logging alarmlog enable (Habilita o registro de logs de alarmes, útil para monitorar e identificar falhas ou problemas)  
logging exc-event auto-write enable (Habilita o **registro automático** de eventos de exceção, facilitando a análise de erros ou condições fora do normal)  
logging level notification (Configura o nível de log para **notificações**, ou seja, mensagens de alerta importantes para o administrador)  
logging cmdlog enable (Habilita o registro de **comandos executados**, útil para auditoria e rastreamento de atividades)  
logging snmplog disable (Desabilita o registro de logs de SNMP, o que pode reduzir a quantidade de logs gerados)  
logging igmplog disable (Desabilita o registro de logs de IGMP, usado em redes multicast)  
syslog facility local0 (Define o **local0** como a instalação do syslog, que pode ser um local de armazenamento específico para logs)  
syslog severity 6 (Define o nível de severidade para **informações**, sendo 6 para mensagens informativas que não indicam erro)  
syslog hostname-field hostname (Define o campo de nome do host no **syslog** para o **nome do dispositivo**, ajudando na identificação dos logs)  
line console idle-timeout 15 (Define o tempo de **timeout** para a linha de console como **15 minutos**, ou seja, desconecta a sessão após 15 minutos de inatividade)  
line console absolute-timeout 1440 (Define o tempo de **timeout absoluto** para a linha de console como **1440 minutos** (24 horas))  
line telnet idle-timeout 15 (Define o tempo de **timeout** para a linha de Telnet como **15 minutos**, desconectando após esse tempo de inatividade)  
line telnet absolute-timeout 1440 (Define o tempo de **timeout absoluto** para a linha de Telnet como **1440 minutos** (24 horas))  
line telnet users 16 (Define o número máximo de **usuários Telnet** permitidos como 16)  
line cli detail-info-show disable (Desabilita a exibição detalhada de **informações de comando** no CLI, para simplificar a saída de comandos)  

---

## Atalhos de teclado

no hotkey ctrl_g (Desativa o atalho de teclado **Ctrl+G** no dispositivo)  
no hotkey ctrl_l (Desativa o atalho de teclado **Ctrl+L** no dispositivo)  
no hotkey ctrl_o (Desativa o atalho de teclado **Ctrl+O** no dispositivo)  
no hotkey ctrl_r (Desativa o atalho de teclado **Ctrl+R** no dispositivo)  
no hotkey ctrl_s (Desativa o atalho de teclado **Ctrl+S** no dispositivo)  
no hotkey ctrl_t (Desativa o atalho de teclado **Ctrl+T** no dispositivo)  
!  

---

## SSh Configs

ssh server enable (Habilita o servidor **SSH** no dispositivo, permitindo conexões remotas via SSH)  
ssh server authentication mode local (Define que o modo de autenticação será feito localmente, utilizando as credenciais configuradas no dispositivo)  
ssh server authentication type pap (Configura o tipo de autenticação SSH como **PAP** (Password Authentication Protocol), onde a senha será transmitida durante a autenticação)  
no ssh server only (Desativa a opção de **acesso exclusivo** por SSH, permitindo o uso de outros métodos de acesso, como console ou Telnet, conforme a configuração)  
ssh server version 2 (Força o uso da **versão 2 do SSH**, que é mais segura e possui recursos adicionais em relação à versão 1)  

---

## Integração com servidor RADIUS

radius attribute vendor-specific vendor-id 3902 (Configura um **atributo específico de fornecedor** (Vendor-Specific Attribute) para o servidor RADIUS com o **ID do fornecedor 3902**, que é associado a equipamentos ou sistemas específicos da ZTE)  
!  
!  
!  
radius server-port-check on (Habilita a **verificação da porta do servidor RADIUS**, garantindo que a comunicação com o servidor RADIUS seja validada antes de aceitar a conexão)  

---

## Tactacs (serviço de autenticação baseado em TACACS+)

tacacs disable (Desativa o serviço **TACACS+** no dispositivo, impedindo o uso de autenticação, autorização e contabilidade via TACACS+)  
tacacs-server timeout 5 (Define o **tempo limite (timeout)** para a comunicação com o servidor TACACS+ como **5 segundos**)  
tacacs-server deadtime 5 (Configura o **tempo de inatividade (deadtime)** do servidor TACACS+ como **5 segundos**, o tempo que o dispositivo espera antes de tentar uma nova conexão com o servidor em caso de falha)  
tacacs-server packet 1024 (Define o tamanho máximo do **pacote** que pode ser enviado ao servidor TACACS+ como **1024 bytes**)  

--- 

## Alarmes 

alarm enable (Habilita o **sistema de alarmes**, permitindo que o dispositivo envie alertas quando ocorrerem eventos específicos)  
alarm confirm (Ativa a **confirmação de alarmes**, que requer que os alarmes sejam confirmados manualmente para indicar que foram reconhecidos)  
alarm trap-confirm retry 3 timeout 20 (Configura o **número de tentativas (retry)** para enviar alarmes como **3 tentativas**, e o **tempo limite (timeout)** entre as tentativas como **20 segundos**)  
nms-hello-trap disable (Desativa o envio do **trap de saudação NMS** (Network Management System), que é um tipo de alerta inicial enviado ao sistema de gerenciamento de rede)  
alarm report-speed 0 (Configura a **velocidade de relatório de alarmes** para **0**, o que pode significar que o dispositivo envia alarmes com uma frequência mínima)  
alarm anti-jitter 0 (Desativa a **proteção contra jitter** nos alarmes, que ajuda a suavizar variações no tempo de envio dos alarmes)  
