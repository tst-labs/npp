# npp

Projeto para fazer o _ETL (Extract Transform Load)_ de arquivos PDF da Receita Federal. O projeto está dividido nos seguintes módulos:

## DIRPF

Declaração do Imposto de Renda de Pessoa Física

### Como o programa funciona:

1. Lê a pasta de entrada, definida por dirIn, em busca de arquivos com extensão “.pdf”
2. Identifica se o arquivo é declaração de imposto de renda de pessoa física, modelo completo ou simplificado.
3. Grava na pasta de saída, definida por dirOut, o mesmo nome de arquivo com extensão “.txt” mas no formato CSV.

### Dados recuperados e gravados:

1. Identificação do Contribuinte
    - Nome
    - CPF
2. Resumo - Rendimentos Tributáveis
    - Recebidos de Pessoa Jurídica pelo Titular
    - Recebidos de Pessoa Jurídica pelos Dependentes
    - Recebidos de Pessoa Física/Exterior pelo Titular
    - Recebidos de Pessoa Física/Exterior pelos Dependentes
    - Recebidos acumuladamente pelo titular
    - Recebidos acumuladamente pelos dependentes
    - Resultado tributável da Atividade Rural
    - TOTAL DE RENDIMENTOS TRIBUTÁVEIS
3. Resumo - Evolução Patrimonial
    - Bens e direitos em 31/12/Ano Anterior
    - Bens e direitos em 31/12/Ano Atual
    - Dívidas e ônus reais em 31/12/Ano Anterior
    - Dívidas e ônus reais em 31/12/Ano Atual
4. Resumo - Outras Informações
    - Rendimentos isentos e não tributáveis
    - Rendimentos sujeitos à tributação exclusiva/definitiva
    - Rendimentos tributáveis - imposto com exigibilidade suspensa


## DOI

Declaração sobre Operações Imobiliárias

### Como o programa funciona:
1. Lê a pasta de entrada, definida por dirIn, buscando todos os arquivos “.pdf”
2. Identifica se o documento recebido é uma DOI, buscando o termo: “Declaração sobre Operações Imobiliárias”
3. Grava a saída na pasta de saída, definida por dirOut, com extensão “.txt” mas no formato CSV.

### dados recuperados e gravados:

1. Identificação do Cartório
    - Complemento e Bairro estão agrupados

2. Identificação da Operação
    - Livro e Folha estão agrupados
    - Registro e Situação estão agrupados
    - Matricula - Quando estiver em branco ou com zeros grava-se “ND” Número de Controle

3. Identificação dos Alienantes
    - Participação - Quando estiver em branco arbitrar percentual igual para todas listados
    - Inferido - Indica se o valor de participação foi inferido ou não. S-Inferido N-Informado

4. Identificação dos Adquirentes
    - Participação - Quando estiver em branco arbitrar percentual igual para todas listados
    - Inferido - Indica se o valor de participação foi inferido ou não. S-Inferido N-Informado

5. Informações sobre a Alienação
    - Valor Alienação - Quando não estiver preenchido com números, utilizar o valor Base_Calculo
    - Inferido - Indica se o Valor Alienação foi inferido ou não. S-Inferido, N-Informado

6. Informações sobre o Imóvel
    - Gravado sem qualquer tratameto
    
