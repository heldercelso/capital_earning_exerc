## Descrição

O objetivo deste exercício é implementar um programa que calcula o imposto a ser pago sobre lucros ou prejuízos de operações no mercado.
Para isso é realizado a leitura de entradas (input.txt) e calculado o resultado baseado nas informções contidas no pdf `exerc.pdf`.

## Decisões técnicas:

* Uso de Docker para evitar problemas de portabilidade;
* Foram mantidos os arquivos Dockerfile e requirements.txt no projeto porém não estão sendo utilizados porque não há dependencias a serem instaladas. Porém caso haja necessidade futura já fariam parte do projeto;
* O arquivo input.txt é lido como stdin dos casos de teste: cada linha um caso.


## Arquitetura:

* Devido a simplicidade do problema não foi utilizado orientação a objeto;
* O software é dividido em duas partes:
    1. Leitura dos dados de entrada (casos de teste) através do método read_inputs() onde cada entrada é obtida por stdin;
    2. Chamada do método calculate_all_inputs() para todas entradas obtidas onde é executado o cálculo das taxas através do método calculate_tax(). O resultado é direcionado ao stdout.


## Instruções para executar:

1. Ter instalado e inicializado Docker (docker-compose) na máquina;
2. Preencher o arquivo input.txt com as entradas dos casos de teste (cada linha um caso);
3. Abra um terminal na pasta do projeto ou navegue para dentro da pasta (cd caminho/para/capital_earning);
4. Execute o comando:
```shell
$ docker-compose up
```
5. O resultado aparecerá no proprio terminal.


OBS: Também é possivel executar o código sem Docker mas só foi testado no SO Windows 10 com python 3.7.6. Basta executar diretamente o comando no terminal:
```shell
$ python capital_earning.py < input.txt
```