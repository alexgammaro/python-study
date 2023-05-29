# open("arquivo.txt", "r") # read
# open("arquivo.txt", "w") # write
# open("arquivo.txt", "r+") # read e write
# open("arquivo.txt", "a") # append
# open("arquivo.txt", "b") # bytes

arquivo = open("arquivo.txt", "r+")
type(print(arquivo))
print(type(arquivo))
print(arquivo)

for i in range(1, 1001):
    arquivo.write("aaa "+str(i)+"\n")

print(arquivo.read())