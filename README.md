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