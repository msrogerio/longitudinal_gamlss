# Longitudinal Gamlss

Plataforma web para análise de dados logitudinais em `R`. 

Criado como parte do processo de aperfeiçoamento de saída de dados para análise longitudinais com Gamlss.

Esse projeto é uma iniciativa do Programa de Pós-graduação em Ciências da Computação (PPGCC) da Universidade Federal do Acre (UFAC), cujo objetivo é pluralizar o uso e entendimento da estatística computacional. 

Na plataforma, com alguns cliques, é possível realizar análise de regressão para dados longitudinais, sendo possível escolher o modelo de distribuição a ser usado na análise. 


### 1. Requisitos

Para rodar localmente o projeto faz-se necessário a instalação de algumas linguagens e bibliotecas. 

#### 1.1 R

É necessário que a linguagem `r` esteja instalada na máquina. Se esse não for o caso, porceda a instalação conforme recomentação do site oficial para seu sistema operacioanal. 

Com o `r` instalado, instalar também as bibliotecas:

`nlme`; `hnp`; `gamlss`; `dplyr`; `tidyr`; `ggplot2`; `httr`; `sqldf`; `stringr`; e `rjson`.

#### 1.2 Python

Para o projeto foi utilizada a versão 3.10.6, podendo ser utilizada em versões ateriores até a versão 3.4. 
Caso sua máquina não tenha uma versão do python instalada, proceda a instalação forme recomendação do site oficial para seu sistema operacional.

É altamente recomendado que a execução de projeto python sejam realizadas em ambiente virtuais separados para não interfeir na instalação padrão do python. 

*Caso não tenha o vitualizador de ambientes python, proceder a instalação `venv` conforme recomendação do site oficial.* 

Com `venv` instalado, executar o comando: `python3 -p venv venv`

Ative o ambiente virtual com: `source venv/bin/activate` 

Instale as bibliotecas do projeto: `pip install -r requirements.txt`


### 2. Execute o script:

Pelo terminal, na pasta do projeto, ativar o ambiente virtual: `source venv/bin/activate`

Setar as variáveis de ambiente para execução do Flask: `source .bashrc` 

Executar servidor local: `flask run`

O projeto deve ser acessado via navegador por meio endereço: `http://localhost:5000`


### 3. Uso da plataforma:

#### 3.1 Página 01

Informe o conjunto de dados em .txt que deseja atrabalhar. Submeta o formulário e aguarde o redirecionamento.

#### 3.1 Página 02

Aqui deverão ser informadas as colunas do conjunto de dados que se pretende trabalhar, selecionando quais dados serão categorizados como **tratamento**, quais como **época**, e quais serão as **variáveis resposta**. Por fim, deve-se escolher a distribuição com a qual se pretende trabalhar. Submeta o formulário e aguarde o processamento dos dados e redirecionamento.

#### 3.1 Página 05

Após a análise dos dados, a plataforma retornará um arquivo zip com todos os dados compatativos entre cada tratamento dentro de cada época em tabelas .csv. Além de um gráfico de perfíl para tratamento em função da época. 


### Autor

#### Marlon Rogério

[![Twitter Badge](https://img.shields.io/badge/-@MarlonRogrio3-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/MarlonRogrio3)](https://twitter.com/MarlonRogrio3) 


<blockquote>
    Todos os direitos reservados à UFAC.
</blockquote>
