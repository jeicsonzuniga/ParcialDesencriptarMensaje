"""MY NAME IS MAXIMUS DECIMUS MERIDIUS COMMANDER OF THE ARMIES OF THE NORTH GENERAL OF THE FELIX LEGIONS AND LOYAL SERVANT TO THE TRUE EMPEROR MARCUS AURELIUS FATHER TO A MURDERED SON HUSBAND TO A MURDERED WIFE AND I WILL HAVE MY VENGEANCE IN THIS LIFE OR THE NEXT"""
import itertools
#--------------------------------------------------------------------------------------------
def encontrarPalabraClave(abecedarioPermutado,mensajeCifrado,palabraDicionario,abecedario):
  print("--------------------------------------------------------------------------------")
  iterador=0
  posicionesClave=[]
  posiblePalabra=[]
  posiblePalabraString=""
  print("abecedario para el for: ",abecedario)
  for letra in palabraDicionario:
    posicionesClave.append(abecedario.index(letra))
    print("letra: ",letra)
  print(posicionesClave)
  for i in posicionesClave:
    posiblePalabra.append(abecedarioPermutado[i])
    posiblePalabraString=posiblePalabraString+abecedarioPermutado[i]
  print("abecedario normal: ",abecedario)
  print("abecedarioPermutado:",abecedarioPermutado)
  print("posiblePalabra:",posiblePalabra)
  print("posiblePalabraString:",posiblePalabraString)
  print("--------------------------------------------------------------------------------")
  if posiblePalabraString in mensajeCifrado:
    print("encontro la palabra en el dicionario y esta en la permutacion: ",abecedarioPermutado)
    return abecedarioPermutado
  else:
    return False
#--------------------------------------------------------------------------------------------
#m=z
#y=c
#n=h
#a=d
mensajeCifrado="zchdzqtrzdytzirgqstzirzqltgtirsezzdhgqleanmqdlztqreanmqhelnmfqhqldueanmqaqutyuqftehrdhguecdurqlodhnnenmqnliqqzvqlelzdlsirdilqutiradnmqlnedzilgqlqgrehmirbdhgnedzilgqlqgktaqdhgtktuumdoqzcoqhfqdhsqthnmtrutaqelnmqhqyn"
#mensajeCifrado="cbagfg"
#abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#abecedario=["a","b","c","d","e","f","g","h","i","j","k","l"]
#abecedario=["a","b","c","d","e","f","g","h","i","j","k"]
abecedario=["a","b","c","d","e","f","g","h","i"]
#palabraDicionario="bacefe"
palabraDicionario="deci"
abecedariosPermutados=list(itertools.permutations(abecedario))
print("Lista abecedario: --->",abecedario)
#print("Lista permutada: ",permutada)
print("len(permutada): --->",len(abecedariosPermutados))
print("Inicia el ciclo for")
c=0
posiblesLlavesPermutadas=[]
for abecedarioPermutado in abecedariosPermutados:
    print("Abecesario permutado Nro: ",c)
    print(abecedarioPermutado)
    resultado=encontrarPalabraClave(abecedarioPermutado,mensajeCifrado,palabraDicionario,abecedario)
    if resultado is not False:
      posiblesLlavesPermutadas.append(resultado)
    c+=1
print("Termina el ciclo for")
print("posiblesLlavesPermutadas")
for posibleLlave in posiblesLlavesPermutadas:
  print(posibleLlave)
print("posiblesLlavesPermutadas")
#-------------------------------------------
#mynameismaximusdecimusmeridius
#abcdefghijklmnopqrstuvwxyz
#zchdzqtrzdytzirgqstzirzqltgtirsezzdh
#2_primeras
#m=z
#y=c
#n=h
#a=d