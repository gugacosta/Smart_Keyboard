import string
## Função para ler palavras de um arquivo .txt e armazenar em uma lista
def arquivo_to_list(arquivo_name): 
  """Esta função recebe como entrada um arquivo .txt e retorna uma lista com as palavras contida nele separadas"""

  arq_list = []             
  fin = open(arquivo_name, encoding='utf-8')   #Lê o arquivo .txt na mesma pasta do código

  for line in fin:                        #Separa cada linha e retorna um vetor das palavras
    line = line.strip(string.whitespace)
    line = line.split()
    
    if len(line)>1:  #Este programa ainda é case sensitive, por isso transforma todas as palavras em minusculas 
      for word in line:
        word = word.lower()
        word = word.strip(string.punctuation)        
        arq_list.append(word)  #Soma todas as listas das linhas em uma lista geral

    else:           #Para a excessão da linha vazia
      if line==[]:
        line = '\n'
      line = str(line)   
      arq_list.append(line)
    
  fin.close()

  return arq_list   #Retorna a lista geral com todas as palvras de todas as linhas

def markov_analyses(list_words,markov_dict):
  """Esta função recebe como entrada uma lista de palavras em sequencia e retorna um dict os possíveis sufixos de acordo com a frequência"""

  for x in range(0,len(list_words)-1):    #Caso a palavra ainda não tenha sido analisada  
    if list_words[x] not in markov_dict:  #Cria o dict {Key = palavra, value = Lista[frequencia, palavra]}
        markov_dict[list_words[x]] = [[1,list_words[x+1]]]

    else:
        flag = False
        for sufix in markov_dict[list_words[x]][:100]: #Caso a palavra já exista só adiciona o novo sufixo
            if sufix[1] == list_words[x+1]:
                sufix[0] = sufix[0] + 1   #Aumenta a frequência do sufixo
                flag = True
            
        if flag == False:   #Se o sufixo não existir cria um novo
            markov_dict[list_words[x]].append([1,list_words[x+1]])
            
        markov_dict[list_words[x]].sort(reverse=True) #Ordena os sufixos pela frequência
  
  return markov_dict



palavras = arquivo_to_list("engenhariadedados.txt")
markov_dict = {}
markov_dict = markov_analyses(palavras,markov_dict)
frase = ""
while frase != []:
    frase = str(input("Escreva um pouco sobre algo para que eu possa aprender sua forma de escrita \n"))
    frase = frase.strip(string.whitespace)
    frase = frase.strip(string.punctuation)
    frase = frase.lower()   #Converte todas palavras para minusculas, caso não sensitivo.
    frase = frase.split()
    markov_dict = markov_analyses(frase,markov_dict)  
    try:
        for list in markov_dict[frase[len(frase)-1]][:4]:  #Imprime o sufixo da última para da frase
            print(list[1], end = ' | ')       
    except:
        print("Sem sugestões", end ='')

    print('')
