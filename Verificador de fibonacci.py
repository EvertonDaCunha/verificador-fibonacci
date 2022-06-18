num=int(input("Digite um número para ver se ele faz parte da sequência de fibonacci: "))
t1=0
t2=1
t3=0
print("{} - {} -".format(t1,t2), end=' ')
while t3<num:
    t3=t1+t2
    print("{} -".format(t3), end=' ')
    t1=t2
    t2=t3

if t3==num:print("Esse número pertence a sequência.")
if t3!=num:print("Esse número não pertence a sequência.")