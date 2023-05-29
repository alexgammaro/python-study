conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)
print("União: {}".format(conjunto_uniao))
conjunto_intersecao = conjunto1.intersection(conjunto2)
print("Interseção: {}".format(conjunto_intersecao))
conjunto_diferenca1 = conjunto1.difference(conjunto2)
print("Diferença do conjunto 1: {}".format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print("Diferença do conjunto 2: {}".format(conjunto_diferenca2))
conjunto_dif_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferença simétrica: {}".format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset_a = conjunto_a.issubset(conjunto_b)
print("Conjunto A é subconjunto do Conjunto B? {}".format(conjunto_subset_a))
conjunto_subset_b = conjunto_b.issubset(conjunto_a)
print("Conjunto B é subconjunto do Conjunto A? {}".format(conjunto_subset_b))
conjunto_superset_a = conjunto_a.issuperset(conjunto_b)
print("Conjunto A é superconjunto do Conjunto B? {}".format(conjunto_superset_a))
conjunto_superset_b = conjunto_b.issuperset(conjunto_a)
print("Conjunto B é superconjunto do Conjunto A? {}".format(conjunto_superset_b))

lista = ["cachorro", "cachorro", "gato", "gato", "elefante"]
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

# conjunto = {1, 2, 3, 4, 4, 2, 3}
# conjunto.add(5)
# conjunto.discard(3)
# print(type(conjunto))
# print(conjunto)