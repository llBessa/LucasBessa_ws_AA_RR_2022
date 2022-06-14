#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int count = 0; // Contador de movimentos

void TorreHanoi(int origem, int destino, int auxiliar, int quantidade){
  if( quantidade == 1 ){
    count+=1;
  } else{
    TorreHanoi(origem, auxiliar, destino, quantidade-1);
    TorreHanoi(origem, destino, auxiliar, 1);
    TorreHanoi(auxiliar, destino, origem, quantidade-1);
  }
}

int main(int argc, char **argv){
  // armazena o tempo de execucao
  clock_t tempo;
  int quantidade = atoi(argv[1]);

  // guarda o tempo antes da execucao do algoritmo
  tempo = clock();
  // Chama a função Torre de Hanoi passando como parâmetro a origem, o destino, o pino auxiliar e a quantidade de discos
  TorreHanoi(0, 2, 1, quantidade);

  // guarda a diferenca do tempo antes e depois da execucao do algoritmo
  tempo = clock() - tempo;

  // exibe o tempo de execucao em milissegundos
  printf("%.5lf\n", ((double) tempo / (CLOCKS_PER_SEC/1000)));
  return 0;
}