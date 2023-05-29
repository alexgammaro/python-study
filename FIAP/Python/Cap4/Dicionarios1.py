usuarios = {}
usuarios = {
    "Chaves":["Chaves do 8","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
}
print(usuarios)

usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
print(usuarios)

print("####################")

print(usuarios.get("Chaves"))