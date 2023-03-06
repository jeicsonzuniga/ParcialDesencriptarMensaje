"""MY NAME IS MAXIMUS DECIMUS MERIDIUS COMMANDER OF THE ARMIES OF THE NORTH GENERAL OF THE FELIX LEGIONS AND LOYAL SERVANT TO THE TRUE EMPEROR MARCUS AURELIUS FATHER TO A MURDERED SON HUSBAND TO A MURDERED WIFE AND I WILL HAVE MY VENGEANCE IN THIS LIFE OR THE NEXT"""
#mynameismaximusdecimusmeridiuscommanderofthearmiesofthenorthgeneralofthefelixlegionsandloyalservanttothetrueemperormarcusaureliusfathertoamurderedsonhusbandtoamurderedwifeandiwillhavemyvengeanceinthislifeorthenext
#zchdzqtrzdytzirgqstzirzqltgtirsezzdhgqleanmqdlztqreanmqhelnmfqhqldueanmqaqutyuqftehrdhguecdurqlodhnnenmqnliqqzvqlelzdlsirdilqutiradnmqlnedzilgqlqgrehmirbdhgnedzilgqlqgktaqdhgtktuumdoqzcoqhfqdhsqthnmtrutaqelnmqhqyn
import itertools
#La posible llave parcial es :nmq
#La posible llave parcial es :reh
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--->:[m][y][n]
#--><--
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
def productoCartesiano(abecedario,palabraDicionario,mensajeCifrado,palabraDicionarioEntre):
  combinaciones=[]
  encontradas=[]
  c=0
  for i in itertools.product(abecedario, repeat=len(palabraDicionario)):
    #print("itertools.product(abecedario, repeat=3): ",i)
    concatenar=""
    for j in i:
      concatenar=concatenar+j
    combinaciones.append(concatenar)
  for i in combinaciones:
    if i in mensajeCifrado:
      #print("-----------------------------------")
      #print("La posible llave parcial es :"+i)
      #print("Posible descifrado --->:",mensajeCifrado.replace(i,"-->"+palabraDicionario+"<--"))
      #print("-----------------------------------")
      d=0
      reemplazado=mensajeCifrado
      #residual=mensajeCifrado
      for j in palabraDicionario:
        reemplazado=reemplazado.replace(i[d],"["+j+"]")
        #residual=residual.replace(i[d],"")
        d+=1
      #print("Reemplazado: ",reemplazado)
      c+=1
      if palabraDicionarioEntre[0] in reemplazado:
        encontradas.append(reemplazado)
  #print("-----------------------------------")
  #print("-----------------------------------")
  #print("-----------------------------------")
  return encontradas,c#,abecedarioResidual
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
def productoCartesiano2(abecedario,palabraDicionario,mensajeCifrado,palabraDicionarioEntre):
  #if mensajeCifrado[0:9] == "[m][y][n]":
  print("<->:",mensajeCifrado)
  combinaciones=[]
  encontradas=[]
  abecedarioResidual=[]
  c=0
  for i in itertools.product(abecedario, repeat=len(palabraDicionario)):
    #print("itertools.product(abecedario, repeat=3): ",i)
    concatenar=""
    for j in i:
      concatenar=concatenar+j
    combinaciones.append(concatenar)
  #--------------------------------------------------------------------
  f = open ('salida.txt','a')
  for i in combinaciones:
    if i in mensajeCifrado and validarPalabrasContenidas(palabraDicionarioEntre,mensajeCifrado):
      """
      f.write("\n")
      f.write(palabraDicionarioEntre[0])
      f.write("\n")
      f.write(mensajeCifrado)
      f.write("\n")
      """
      print("-----------------------------------")
      print("La posible llave parcial es :"+i)
      print("Posible descifrado --->:",mensajeCifrado.replace(i,"-->"+palabraDicionario+"<--"))
      print("-----------------------------------")
      print(i)
      print(mensajeCifrado)
      f.write("\n")
      f.write("-----------------------------------")
      f.write("\n")
      f.write("La posible llave parcial es :"+i)
      f.write("\n")
      f.write("Posible descifrado --->:"+mensajeCifrado.replace(i,"-->"+palabraDicionario+"<--"))
      f.write("\n")
      f.write("-----------------------------------")
      f.write("\n")
      f.write(i)
      f.write("\n")
      d=0
      reemplazado=mensajeCifrado
      residual=mensajeCifrado
      for j in palabraDicionario:
        reemplazado=reemplazado.replace(i[d],"["+j+"]")
        reemplazado=reemplazado.replace("[["+j+"]]","["+i[d]+"]")#que chistoso esto jajaja, si se quita pailas jajaja
        #residual=residual.replace(i[d],"")
        d+=1
      f.write("Reemplazado: "+reemplazado)
      f.write("\n")
      #f.write("Residual: "+residual)
      #f.write("\n")
      c+=1
      esta=0
      for palabra in palabraDicionarioEntre:
        if palabra in reemplazado:
          esta+=1
      if esta==len(palabraDicionarioEntre):
        encontradas.append(reemplazado)
  f.close()
  print("-----------------------------------")
  print("-----------------------------------")
  print("-----------------------------------")
  return encontradas,c#,abecedarioResidual
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
def validarPalabrasContenidas(palabraDicionarioEntre,mensajeCifrado):
  c=0
  for palabra in palabraDicionarioEntre:
    if palabra in mensajeCifrado:
      c+=1
  if c>0:
    return True
  else:
    return False
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
"""MY NAME IS MAXIMUS DECIMUS MERIDIUS COMMANDER OF THE ARMIES OF THE NORTH GENERAL OF THE FELIX LEGIONS AND LOYAL SERVANT TO THE TRUE EMPEROR MARCUS AURELIUS FATHER TO A MURDERED SON HUSBAND TO A MURDERED WIFE AND I WILL HAVE MY VENGEANCE IN THIS LIFE OR THE NEXT"""
mensajeCifrado="zchdzqtrzdytzirgqstzirzqltgtirsezzdhgqleanmqdlztqreanmqhelnmfqhqldueanmqaqutyuqftehrdhguecdurqlodhnnenmqnliqqzvqlelzdlsirdilqutiradnmqlnedzilgqlqgrehmirbdhgnedzilgqlqgktaqdhgtktuumdoqzcoqhfqdhsqthnmtrutaqelnmqhqyn"
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#abecedario=["a","b","c","d","e","f","g","h","i","j","k","l"]
#abecedario=["a","b","c","d","e","f","g","h","i","j","k"]
palabraDicionario="myname"
palabraDicionarioEntreResidual="[m],[y],[n],[a],[m],[e]"
#--------------------------------------------------------------------------------------------
palabraDicionario2="of"
palabraDicionarioEntreResidual2="[o],[f]"
#--------------------------------------------------------------------------------------------
palabraDicionario3="rth"
palabraDicionarioEntreResidual3="[r],[t],[h]"
#--------------------------------------------------------------------------------------------
dicionarioClave=[palabraDicionarioEntreResidual.replace(",",""),palabraDicionarioEntreResidual2.replace(",",""),palabraDicionarioEntreResidual3.replace(",","")]
palabraDicionarioEntre=[]
palabraDicionarioEntre.append(dicionarioClave[0])
#--------------------------------------------------------------------------------------------
totalAltaPosibilidad=0
encontradas,c=productoCartesiano(abecedario,palabraDicionario,mensajeCifrado,palabraDicionarioEntre)
for i in encontradas:
  #print("-----------------------------------")
  #print("Alta posibilidad de ser el mensaje: ")
  #print("-->",i)
  depurado=i
  for l in palabraDicionarioEntreResidual.split(","):
    depurado=depurado.replace(l,"")
  #print("Dicionario letras retiradas: -->",depurado)
  lista=list(depurado)
  #print("Dicionario letras retiradas sin duplicados lista: -->",set(lista))
  #print("Total encontradas: ",i.count("["))
  #print("Total faltantes: ",(len(mensajeCifrado)-i.count("[")))
  #print("Total letras sin duplicar: ",len(set(lista)))
  totalAltaPosibilidad+=1
  #print("-----------------------------------")
  #print("-----------------------------------")
  #print("-------------Sesion 2--------------")
  #print("-----------------------------------")
  #print("-----------------------------------")
  encontradas2,c2=productoCartesiano2(set(lista),palabraDicionario2,i,palabraDicionarioEntre)
#--------------------------------------------------------------------------------------------  
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
for i in encontradas2:
    #print("-----------------------------------")
    #print("Alta posibilidad de ser el mensaje: ")
    #print("-->",i)
    depurado=i
    for l in palabraDicionarioEntreResidual3.split(","):
      depurado=depurado.replace(l,"")
    #print("Dicionario letras retiradas: -->",depurado)
    lista=list(depurado)
    #print("Dicionario letras retiradas sin duplicados lista: -->",set(lista))
    #print("Total encontradas: ",i.count("["))
    #print("Total faltantes: ",(len(mensajeCifrado)-i.count("[")))
    #print("Total letras sin duplicar: ",len(set(lista)))
    totalAltaPosibilidad+=1
    #print("-----------------------------------")
    #print("-----------------------------------")
    #print("-------------Sesion 2--------------")
    #print("-----------------------------------")
    #print("-----------------------------------")
    palabraDicionarioEntre.append(dicionarioClave[1])
    productoCartesiano2(set(lista),palabraDicionario3,i,palabraDicionarioEntre)
    #abecedario,palabraDicionario,mensajeCifrado,palabraDicionarioEntre
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
"""
  lista=productoCartesiano2(set(lista),"the",i)
  for j in lista:
    if j[0:9] == "[m][y][n]":
      print(j)
      """
""""
for i in abecedarioResidual:
  print("-----------------------------------")
  print("Residual: ",i)
  print("-----------------------------------")
"""
print("-----------------------------------")
print("-----------------------------------")
print("Total llaves: ",c)
print("mensajeCifrado: ",mensajeCifrado)
print("-----------------------------------")
print("-----------------------------------")
print("totalAltaPosibilidad: ",totalAltaPosibilidad)
print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")