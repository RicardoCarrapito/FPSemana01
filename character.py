
print("Raul")

raulatq= int(input())
rauldef= int(input())

print("Maria")

mariaatq= int(input())
mariadef= int(input())

print("Carlos")

carlosatq= int(input())
carlosdef= int(input())

raulstats=(raulatq,rauldef)

mariastatus=(mariaatq,mariadef)

carlosstatus=(carlosatq,carlosdef)

all_status =[
["Raul", raulstats],
["Maria", mariastatus],
["Carlos", carlosstatus]
]
print(all_status)


maior_ataque=[]
maior_defesa= []
y=0
z=0

for personagem in all_status:
    if y < personagem[1][0]:
        y= personagem[1][0]
        maior_ataque = personagem
        

    if z < personagem[1][1]:
        z= personagem[1][1]
        maior_defesa = personagem

print(f"ataque {maior_ataque[0]} {maior_ataque[1][0]}")
print(f"defesa {maior_defesa[0]} {maior_defesa[1][1]}")
        

