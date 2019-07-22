# -*- coding: utf-8 -*-
# Objetivo: Ler arquivos DIRPF.PDF e gravar arquivo .csv para leitura pelo Qlik Sense
# Lê todos os arquivos da pasta dirIn e grava o txt em dirOut
# dirIn e dirOut precisam refletir o ambiente de instalação
# versão 1.0 de 18/07/2019
# Esta versão lê 4 blocos de dados: 
# 1 - Identificação do contribuinte; 2 - Resumo: rendimentos; 3 - Evolução Patrimonial; 4 - Outras informações

import re
import pdftotext
import os

def csv(num):
    if num == 1:
        return '"'
    elif num == 2:
        return '","'
    elif num == 3:
        return '"\n'

def cabecalho():
    saida.write( csv(1))
    saida.write("Nome")
    saida.write( csv(2))
    saida.write("CPF")
    saida.write( csv(2))
    saida.write("Exercicio")
    saida.write( csv(2))
    saida.write("Ano_Calend")
    saida.write( csv(2))
    saida.write("Renda_PJ_Titular")
    saida.write( csv(2))
    saida.write("Renda_PJ_Depend")
    saida.write( csv(2))
    saida.write("Renda_PF_Titular")
    saida.write( csv(2))
    saida.write("Renda_PF_Depend")
    saida.write( csv(2))
    saida.write("Renda_Acum_Titular")
    saida.write( csv(2))
    saida.write("Renda_Acum_Depend")
    saida.write( csv(2))
    saida.write("Resultado_Rural")
    saida.write( csv(2))
    saida.write("Renda_Total")
    saida.write( csv(2))
    saida.write("EvoPatr_Bens_Anterior")
    saida.write( csv(2))
    saida.write("EvoPatr_Bens_Atual")
    saida.write( csv(2))
    saida.write("EvoPatr_Divida_Anterior")
    saida.write( csv(2))
    saida.write("EvoPatr_Divida_Atual")
    saida.write( csv(2))
    saida.write("Outras_Renda_Isento")
    saida.write( csv(2))
    saida.write("Outras_Renda_Exclusivo")
    saida.write( csv(2))
    saida.write("Outras_Renda_Tributavel")
    saida.write( csv(3))
    
def modCompleto():    
    saida.write( csv(1))
    saida.write(quadro1[0][0].strip()) #Nome
    saida.write( csv(2))
    saida.write(quadro1[0][1].strip()) #CPF
    saida.write( csv(2))
    saida.write(modelo[0][1].strip()) #Exercicio
    saida.write( csv(2))
    saida.write(modelo[0][2].strip()) #Ano_Calend
    saida.write( csv(2))
    saida.write(quadro2[0][0].strip()) #Renda_PJ_Titular
    saida.write( csv(2))
    saida.write(quadro2[0][1].strip()) #Renda_PJ_Depend
    saida.write( csv(2))
    saida.write(quadro2[0][2].strip()) #Renda_PF_Titular
    saida.write( csv(2))
    saida.write(quadro2[0][3].strip()) #Renda_PF_Depend
    saida.write( csv(2))
    saida.write(quadro2[0][4].strip()) #Renda_Acum_Titular
    saida.write( csv(2))
    saida.write(quadro2[0][5].strip()) #Renda_Acum_Depend
    saida.write( csv(2))
    saida.write(quadro2[0][6].strip()) #Resultado_Rural
    saida.write( csv(2))
    saida.write(quadro2[0][7].strip()) #Renda_Total
    saida.write( csv(2))
    saida.write(quadro3[0][0].strip()) #EvoPatr_Bens_Anterior
    saida.write( csv(2))
    saida.write(quadro3[0][1].strip()) #EvoPatr_Bens_Atual
    saida.write( csv(2))
    saida.write(quadro3[0][2].strip()) #EvoPatr_Divida_Anterior
    saida.write( csv(2))
    saida.write(quadro3[0][3].strip()) #EvoPatr_Divida_Atual
    saida.write( csv(2))
    saida.write(quadro4[0][0].strip()) #Outras_Renda_Isento
    saida.write( csv(2))
    saida.write(quadro4[0][1].strip()) #Outras_Renda_Exclusivo
    saida.write( csv(2))
    saida.write(quadro4[0][2].strip()) #Outras_Renda_Tributavel
    saida.write( csv(3))
    
# obtendo os nomes dos arquivos na pasta de entrada
dirIn  = '/home/labcsjt/dirpf_in/'
dirOut = '/home/labcsjt/dirpf_out/'
listaPdf = os.listdir(dirIn)
relatorio = ''
for indPdf in range(len(listaPdf)):
    arq = listaPdf[indPdf]
    if arq.find(".pdf") < 0:
        continue
    #if arq.find("DEC97634158100_anocal_2014.pdf") < 0:
    #    continue
        
    # Abrindo arquivo de entrada, lendo PDF
    entrada = open( dirIn + arq, 'rb')
    pdf = pdftotext.PDF(entrada)
    texto = "\n\n".join(pdf)
    entrada.close()
    
    # Descobrindo se o arquivo é Declaração de Imposto de Renda de Pessoa Física
    dirpf = re.findall(r'Módulo de Impressão de (.*?) Assinadas.*Tipo (.*?) documento.*', texto, re.M|re.I|re.S)
    try:
        if dirpf[0][0] != 'Declarações' or dirpf[0][1] != 'de':
            continue
    except:
        continue
            
    # Criando arquivo de saida
    saida = open(dirOut + arq[0:arq.find('.')] + '.txt', 'w')

    # Buscando todos os quadros da DOI
    modelo   = re.findall(r'Modelo:(.*?)\n.*EXERCÍCIO(.*).*Ano-Calendário(.*?)\n.*', texto, re.M|re.I|re.S)
    anoAtual = modelo[0][2].strip()
    anoAnt   = str(int(modelo[0][2].strip()) - 1)
    if modelo[0][0].strip() == 'COMPLETO':
        # RegEx para Modelo Completo
        quadros = re.findall(r'IDENTIFICAÇÃO DO CONTRIBUINTE\n(.*?)\n.?DEPENDENTES.*RESUMO.*RENDIMENTOS TRIBUTÁVEIS\n(.*?)\nDEDUÇÕES.*EVOLUÇÃO PATRIMONIAL\n(.*?)\nOUTRAS INFORMAÇÕES\n(.*?)Depósitos judiciais do imposto', texto, re.M|re.I|re.S)
        quadro1 = re.findall(r'Nome:(.*?)CPF:(.*?)\n', quadros[0][0], re.M|re.I|re.S)
        quadro2 = re.findall(r'Recebidos de Pessoa Jurídica pelo titular(.*?)\n.*Recebidos de Pessoa Jurídica pelos dependentes(.*?)\n.*Recebidos de Pessoa Física/Exterior pelo titular(.*?)\n.*Recebidos de Pessoa Física/Exterior pelos dependentes(.*?)\n.*Recebidos acumuladamente pelo titular(.*?)\n.*Recebidos acumuladamente pelos dependentes(.*?)\n.*Resultado tributável da Atividade Rural(.*?)\n.*TOTAL(.*?)$', quadros[0][1], re.M|re.I|re.S)
        quadro3 = re.findall(r'Bens e direitos em 31/12/'+anoAnt+'(.*?)\n.*Bens e direitos em 31/12/'+anoAtual+'(.*?)\n.*Dívidas e ônus reais em 31/12/'+anoAnt+'(.*?)\n.*Dívidas e ônus reais em 31/12/'+anoAtual+'(.*?)$', quadros[0][2], re.M|re.I|re.S)
        quadro4 = re.findall(r'Rendimentos isentos e não.tributáveis(.*?)\n.*Rendimentos sujeitos à tributação exclusiva/definitiva(.*?)\n.*Rendimentos tributáveis - imposto com exigibilidade suspensa(.*?)$', quadros[0][3], re.M|re.I|re.S)
    else:
        # RegEx para modelo Simplificado
        quadros = re.findall(r'IDENTIFICAÇÃO DO CONTRIBUINTE\n(.*?)\n.?DEPENDENTES.*RESUMO.*RENDIMENTOS TRIBUTÁVEIS E DESCONTO SIMPLIFICADO\n(.*)\n.*Desconto Simplificado.*EVOLUÇÃO PATRIMONIAL\n(.*)\n.*OUTRAS INFORMAÇÕES\n(.*)\n.*Depósitos judiciais do imposto', texto, re.M|re.I|re.S)
        quadro1 = re.findall(r'Nome:(.*?)CPF:(.*?)\n', quadros[0][0], re.M|re.I|re.S)
        quadro2 = re.findall(r'Recebidos de Pessoa Jurídica pelo titular(.*?)\n.*Recebidos de Pessoa Jurídica pelos dependentes(.*?)\n.*Recebidos de Pessoa Física/Exterior pelo titular(.*?)\n.*Recebidos de Pessoa Física/Exterior pelos dependentes(.*?)\n.*Recebidos acumuladamente pelo titular(.*?)\n.*Recebidos acumuladamente pelos dependentes(.*?)\n.*Resultado tributável da Atividade Rural(.*?)\n.*TOTAL DE RENDIMENTOS TRIBUTÁVEIS(.*?)$', quadros[0][1], re.M|re.I|re.S)
        quadro3 = re.findall(r'Bens e direitos em 31/12/'+anoAnt+'(.*?)\n.*Bens e direitos em 31/12/'+anoAtual+'(.*?)\n.*Dívidas e ônus reais em 31/12/'+anoAnt+'(.*?)\n.*Dívidas e ônus reais em 31/12/'+anoAtual+'(.*?)$', quadros[0][2], re.M|re.I|re.S)
        quadro4 = re.findall(r'Rendimentos isentos e não.tributáveis(.*?)\n.*Rendimentos sujeitos à tributação exclusiva/definitiva(.*?)\n.*Rendimentos tributáveis - imposto com exigibilidade suspensa(.*?)$', quadros[0][3], re.M|re.I|re.S)

    cabecalho()
    modCompleto()
      
    saida.close()
    relatorio = relatorio + arq + ' processadas ' + str(len(quadros)) + ' DIRPFs -'

relatorio
