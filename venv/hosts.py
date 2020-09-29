from socket import *
import threading
from datetime import datetime
from queue import Queue
import geoip2.database
import time


# Abre arq. onde estão os IP's para teste
lista_ip = open("lista_ip.txt", "r")

# Lê as linhas do arq. aberto anteriormente
ip_em_lista = lista_ip.readlines()

# se não existe, cria um arq. e armazena informação sobre os hosts ativos
resultado_backup = open("hosts_ativos.txt", "a")

# conta nr de hosts no arq.
numero_host = len(open("lista_ip.txt").readlines())

# armazena os hosts detectados
lista_host_ativo = []

porto = 80


# impede que a ação das Threads multiplique o mesmo output e o repita
segura_saida = threading.Lock()


def localizador():

    # se não houver hosts na lista fecha programa
    if len(lista_host_ativo) == 0:
        print("[-]Não foram encontrados hosts ativos")
    else:
        # escreve data no arquivo ref. anteriormente
        resultado_backup.write("Data:{}\n\n".format(str(datetime.now())))
        # percorre a lista de hosts ativos, onde são aplicadas as intruções dadas no bloco que segue a cada iteração... até ao ultimo host.
        for hosts in lista_host_ativo:
            try:
                # inicia objeto socket
                sock_head = socket(AF_INET, SOCK_STREAM)
                # Faz a conexão a cada host na lista no porto definido
                sock_head.connect_ex((hosts, porto))
                # Faz requisição HTTP com método HEAD
                sock_head.sendall(
                    b"HEAD / HTTP/1.1\r\nHost:%a\r\n\r\n" % hosts)
                # Recebe resposta com cabeçalho
                header = sock_head.recv(1024)
                # fecha socket
                sock_head.close()
            except:
                pass

            # Pausa o programa dois segundo
            time.sleep(2)

            # identifica host
            print("\033[5;92m[+]Host ativo\033[00m: {}".format(hosts))
            # inicia leitura base dados para identificar localização do host
            base_dados = geoip2.database.Reader('GeoLite2-City.mmdb')
            # é armazenada a resposta da localização do host que passa na função city()
            resposta = base_dados.city(hosts)
            # informa país origem
            print("\033[1;93m-País:\033[00m {}".format(resposta.country.name))
            # informa cidade origem
            print("\033[1;93m-Cidade:\033[00m {}".format(resposta.city.name))
            print("\033[1;96m««« HTTP HEAD Request »»»\033[00m\n{}\n\n".format(
                header.decode()))  # converte resposta em formato de byte para string
            # escreve no arq. de backup host identificado
            resultado_backup.writelines("Host ativo: {}\n".format(hosts))
            # escreve no arq. de backup país identificado
            resultado_backup.writelines(
                "País: {}\n".format(resposta.country.name))
            # escreve no arq. de backup headers
            resultado_backup.writelines("{}\n\n".format(header.decode()))
            time.sleep(3)

        # fecha arquivo backup
        resultado_backup.close()
        # output hosts em lista
        print(lista_host_ativo)


def scan_tcp(host):
    try:
        # inicia objecto socket
        sock = socket(AF_INET, SOCK_STREAM)
        # define o tempo de ligação no porto definido
        setdefaulttimeout(1)
        # Faz a conexão a cada host na lista no porto definido
        resultado = sock.connect_ex((host, porto))
        # informa host a ser testado no momento
        print("TCP/{} a testar Host: {} \r".format(porto, host), end="")
        with segura_saida:
            # confirma se ligação é efetuada... se sim, passa para instruções dadas
            if resultado == 0:
                # adiciona cada host ativo à lista
                lista_host_ativo.append(host.rstrip())
            else:
                pass
    except:
        pass


def thread():
    while True:
        # retira e recebe dados em fila
        acao = q.get()
        # função scan_tcp recebe parametros em fila ... host
        scan_tcp(acao)
        # termina tarefa
        q.task_done()


def executa_scan_tcp():
    global q

    # inicia objeto
    q = Queue()

    # Define número de Threads
    for y in range(5):
        tarefa = threading.Thread(target=thread)
        tarefa.daemon = True
        tarefa.start()

    t1 = datetime.now()

    # percorre lista de ip
    for host in ip_em_lista:
        # põe dados em fila... parâmetros que vão passar na função scan_tcp()
        q.put(host)
    # Espera que todos os dados sejam tratados, e as threads terminem,
    q.join()
    # para terminar com auxilio da função task_done()

    t2 = datetime.now()
    total_tempo = t2-t1
    # informa tempo de duração do programa
    print("Operação terminada em {}\n\n".format(total_tempo))


# output inf. inicio prog. com total de hosts a tratar
print("\033[1;35m>>>>  A Iniciar Scan ---- Nº Hosts:\033[00m {}\n\n".format(numero_host))
time.sleep(2)


def main():
    executa_scan_tcp()
    print("\n\nA Resolver Total de {} Hosts encontrados\n\n".format(len(
        lista_host_ativo)))               # Informa nr de hosts encontrados para resolver
    time.sleep(3)
    localizador()


if __name__ == '__main__':
    main()
