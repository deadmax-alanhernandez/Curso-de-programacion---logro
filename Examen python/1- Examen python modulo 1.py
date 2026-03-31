#1.-Contador de Vocales y Consonantes
print("Contandor de Vocales y Consonantes")

contador1 = 0
contador2 = 0
vocales = "aeiouáéíóú"
consonante = "b,c,d,f,g,h,j,k,l,m,n,ñ,p,q,r,s,t,v,w,x,y,z"
frase = input("Ingrese una frase: ")

for cantidad in frase.lower():
    if cantidad in vocales:
            contador1 += 1
    elif cantidad in consonante:
          contador2 += 1

print(f"La frase {frase} contiene {contador1} vocales y {contador2} consonantes")



