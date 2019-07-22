# -*- coding: utf-8 -*-
# Objetivo: Ler arquivos DOI.PDF e gravar arquivo .csv para leitura pelo Qlik Sense
# Lê todos os arquivos da pasta dirIn e grava o txt em dirOut
# dirIn e dirOut precisam refletir o ambiente de instalação
# versão 1.1 de 17/07/2019

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
    
def csv_cabecalho():
    saida.write( csv(1))
    saida.write("Matricula")
    saida.write( csv(2))
    saida.write("Data_Lavratura")
    saida.write( csv(2))
    saida.write("Data_Alienacao")
    saida.write( csv(2))
    saida.write("Tipo_Imovel")
    saida.write( csv(2))
    saida.write("Tipo_Transacao")
    saida.write( csv(2))
    saida.write("Forma_Alienacao")
    saida.write( csv(2))
    saida.write("Valor_Alienacao")
    saida.write( csv(2))
    saida.write("Valor_Base_Calculo")
    saida.write( csv(2))
    saida.write("CPF_CNPJ")
    saida.write( csv(2))
    saida.write("Nome")
    saida.write( csv(2))
    saida.write("%_Participacao")
    saida.write( csv(2))
    saida.write("Inferido")
    saida.write( csv(2))
    saida.write("Categoria")
    saida.write( csv(3))
    
def csv_dadosGerais():    
    saida.write( csv(1))
    if quadro2[0][3].strip() == '' or float(quadro2[0][3].strip()) == 0: #Matricula
        saida.write("ND")
        saida.write(quadro2[0][1])
    else:
        saida.write(quadro2[0][3])
    saida.write( csv(2))
    saida.write(quadro2[0][0]) #Data_Lavratura
    saida.write( csv(2))
    saida.write(quadro5[0][1]) #Data_Alienacao
    saida.write( csv(2))
    saida.write(quadro6[0][0].strip()) #Tipo_Imovel
    saida.write( csv(2))
    saida.write(quadro5[0][0].strip()) #Tipo_Transacao
    saida.write( csv(2))
    saida.write(quadro5[0][2].strip()) #Forma_Alienacao
    saida.write( csv(2))
    saida.write(quadro5[0][3].strip()) #Valor_Alienacao
    saida.write( csv(2))
    saida.write(quadro5[0][4].strip()) #Valor_Base_Calculo
    saida.write( csv(2))
    
def infereParticipacao(quadro):
    #part = print(f'{(100/len(quadro)):6.2f}')
    part = str(100/len(quadro))
    part = part.replace(".",",")
    return (part)
    
# obtendo os nomes dos arquivos na pasta de entrada
dirIn  = '/home/labcsjt/doi_in/'
dirOut = '/home/labcsjt/doi_out/'
listaPdf = os.listdir(dirIn)
relatorio = ''
for indPdf in range(len(listaPdf)):
    arq = listaPdf[indPdf]
    if arq.find('.pdf') < 0:
        continue
    # Abrindo arquivo de entrada, lendo PDF
    entrada = open( dirIn + arq, 'rb')
    pdf = pdftotext.PDF(entrada)
    texto = "\n\n".join(pdf)
    entrada.close()

    # Descobrindo se o arquivo é DOI
    doi = re.findall(r'DOI - Declaração (.*?) Operações Imobiliárias', texto, re.M|re.I|re.S)
    if doi[0] != 'sobre':
        continue

    # Criando arquivo de saida
    saida = open(dirOut + arq[0:arq.find('.')] + '.txt', 'w')

    # Buscando todos os quadros da DOI
    quadros = re.findall(r'01 Identificação do Cartório(.*?)02 Identificação da Operação(.*?)03 Identificação do\(s\) Alienante\(s\)(.*?)04 Identificação do\(s\) Adquirente\(s\)(.*?)05 Informações sobre a Alienação(.*?)06 Informações sobre o Imóvel(.*?)Página', texto, re.M|re.I|re.S)

    csv_cabecalho()

    for listInd0 in range(len(quadros)):
        quadro2 = re.findall( r'(\d{2}\/\d{2}\/\d{4}).*?(\d{1,6}\/\d{2}).*?(.*?)\nMatr.*?Situação\n(.*?)[ ](.*?)\n', quadros[listInd0][1], re.M|re.I|re.S)
        quadro3 = re.findall( r'(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}|\d{3}\.\d{3}\.\d{3}-\d{2})[ ](.*?)\n', quadros[listInd0][2], re.M|re.I|re.S)
        quadro4 = re.findall( r'(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}|\d{3}\.\d{3}\.\d{3}-\d{2})[ ](.*?)\n', quadros[listInd0][3], re.M|re.I|re.S)
        quadro5 = re.findall( r'Transação(.*?)\nData.*?(\d{2}\/\d{2}\/\d{4})(.*?)\nValor da Alienação.*?\n(.*?)[ ](.*?)\n', quadros[listInd0][4], re.M|re.I|re.S)
        quadro6 = re.findall( r'Municipal\n(.*?)[ ](.*)[ ](.*?)\nÁrea.*Número\n(.*?)\nComplemento.*?CEP\n(.*?)\nMuni.*?UF\n(.*)(RS|SC|PR|SP|RJ|ES|MG|GO|MS|DF|MT|BA|AL|SE|PE|PB|RN|PI|CE|MA|PA|AP|AM|RR|RR|AC)', quadros[listInd0][5], re.M|re.I|re.S)
    
        # Gravar dados do Alienante
        for listInd in range(len(quadro3)):
            # Se quadro32 (Participação) estiver preenchido retirar a Participação do quadro31 e gravar em Nome
            # Se quadro32 (Participação) estiver em branco gravar quadro31 em nome e "NI" em participação
            quadro31 = re.findall( r'(.*)', quadro3[listInd][1], re.M|re.I|re.S)            # Busca os campos Nome e Participação 
            quadro32 = re.findall( r'(\d{1,3},\d{2})', quadro3[listInd][1], re.M|re.I|re.S) # Busca o campo Participação

            csv_dadosGerais()
            saida.write(quadro3[listInd][0]) #CPF_CNPJ
            saida.write( csv(2))
            if len(quadro32) > 0:
                saida.write(quadro31[0].replace(quadro32[0],"").strip()) #Nome
                saida.write( csv(2))
                saida.write(quadro32[0]) #%_Participacao
                saida.write( csv(2))
                saida.write("N") #Inferido
            else:
                saida.write(quadro31[0].strip()) #Nome
                saida.write( csv(2))
                saida.write(infereParticipacao(quadro3)) #%_Participacao
                saida.write( csv(2))
                saida.write("S") #Inferido
            saida.write( csv(2))
            saida.write("Alienante") #Categoria
            saida.write( csv(3))

        # Gravar dados do Adquirente
        for listInd in range(len(quadro4)):
            # Se quadro42 (Participação) estiver preenchido retirar a Participação do quadro41 e gravar em Nome
            # Se quadro42 (Participação) estiver em branco gravar quadro41 em nome e "NI" em participação
            quadro41 = re.findall( r'(.*)', quadro4[listInd][1], re.M|re.I|re.S)            # Busca os campos Nome e Participação 
            quadro42 = re.findall( r'(\d{1,3},\d{2})', quadro4[listInd][1], re.M|re.I|re.S) # Busca o campo Participação

            csv_dadosGerais()
            saida.write(quadro4[listInd][0]) #CPF_CNPJ
            saida.write( csv(2))
            if len(quadro42) > 0:
                saida.write(quadro41[0].replace(quadro42[0],"").strip()) #Nome
                saida.write( csv(2))
                saida.write(quadro42[0]) #%_Participacao
                saida.write( csv(2))
                saida.write("N") #Inferido
            else:
                saida.write(quadro41[0].strip()) #Nome
                saida.write( csv(2))
                saida.write(infereParticipacao(quadro4)) #%_Participacao
                saida.write( csv(2))
                saida.write("S") #Inferido
            saida.write( csv(2))
            saida.write("Adquirente") #Categoria
            saida.write( csv(3))
        
    saida.close()
    relatorio = relatorio + arq + ' processadas ' + str(len(quadros)) + ' DOIs -'

relatorio
doi