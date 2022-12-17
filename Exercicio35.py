print('-='*16)
print("Analisador de triangulos!")
print("-="*16)
l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos PODEM FORMAR um triangulo!")
else:
    print("Os segmentos NÃO PODEM FORMAR um triangulo!")