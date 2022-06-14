from asyncio.subprocess import PIPE
from subprocess import Popen
import matplotlib.pyplot as plt

# executa o algoritmo e guarda seu tempo de execucao em um arquivo de log
def executaAlgoritmo(entrada):
    # abre o arquivo de logs
    arquivo = open(f"./logs/log-entrada-{entrada}.txt", 'w')

    # executa o algoritmo e guarda os tempos de execucao no arquivo
    for i in range(13):
        processo = Popen(f'./codigo/hanoi {entrada}', stdout= PIPE).communicate()[0]

        # guarda em retorno o tempo de execução recebido em stdout e o salva no arquivo
        retorno = str(processo.decode('utf-8')).replace("\n", '')
        arquivo.write(retorno)

    # fecha o arquivo de logs
    arquivo.close()

# retorna o tempo medio de execucao de uma entrada com base nos logs
def getTempoExecucaoMedio(entrada):
    arquivo = open(f"./logs/log-entrada-{entrada}.txt", 'r')
    temposExecucao = arquivo.readlines()
    soma = 0
    for tempo in temposExecucao:
        tempo = tempo.replace('\n', '')
        soma += float(tempo)
    media = soma/temposExecucao.__len__()
    return media

def plotGraph(inicio, fim):
    # inicializa as tuplas de dados
    temposExecucao = []
    entradas = []

    for i in range(inicio, fim + 1, 1):
        # guarda os tempos de execução médios e suas respectivas entradas nas tuplas
        temposExecucao.append(getTempoExecucaoMedio(i)/1000)
        entradas.append(i)
    
    #limites de x
    limiteInferior = 0
    limiteSuperior = 1600
    
    # cria um grafico de linha com tendo x como as entradas e y como os tempos de execução
    plt.plot(entradas, temposExecucao)
    plt.ylim(limiteInferior, limiteSuperior)
    plt.title('Torre de Hanoi \n (tempo em função da quantidade de discos)')
    plt.xlabel('Quantidade de discos')
    plt.ylabel('Tempo de execução médio (s)')
    plt.savefig(f"./imagens/grafico{limiteInferior}-{limiteSuperior}.png")
           
# range das entradas da torre de hanoi
inicio = 25
fim = 38

# executa o algoritmo para o range de entradas especificado
for i in range(inicio, fim + 1, 1):
    print(f'testando entrada {i}')
    executaAlgoritmo(i)

# cria e salva um grafico com base nas informacoes geradas
plotGraph(inicio, fim)