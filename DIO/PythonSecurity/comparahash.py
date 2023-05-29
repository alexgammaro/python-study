import hashlib

arquivo_a = "a.txt"
arquivo_b = "b.txt"

hash1 = hashlib.new("ripemd160")
hash1.update(open(arquivo_a, "rb").read())

hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo_b, "rb").read())
# print(hash1.digest())
# print(hash2.digest())
if hash1.digest() != hash2.digest():
    print("#" * 60)
    print(f"O arquivo: {arquivo_a} é diferente do arquivo: {arquivo_b}")
    print("O Hash do arquivo \"a.txt\" é:", hash1.hexdigest())
    print("O Hash do arquivo \"b.txt\" é:", hash2.hexdigest())
else:
    print("#" * 60)
    print(f"O arquivo: {arquivo_a} é igual ao arquivo: {arquivo_b}")
    print("O Hash dos arquivos \"a.txt\" e \"b.txt\" são: ", hash1.hexdigest())