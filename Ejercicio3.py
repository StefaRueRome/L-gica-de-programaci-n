print("Determinar si un estudiante aprueba o no la asignatura")
n1=float(input("Ingrese la primera nota: "))
nota1=(n1*0.10)
n2=float(input("Ingrese la segunda nota: "))
nota2=(n2*0.15)
n3=float(input("Ingrese la tercer nota: "))
nota3=(n3*0.25)
n4=float(input("Ingrese la cuarta nota: "))
nota4=(n4*0.15)
n5=float(input("Ingrese la quinta nota: "))
nota5=(n5*0.35)

nota_final=(nota1+nota2+nota3+nota4+nota5)
if nota_final>=3:
	if nota_final>4.5:
		print("Felicitaciones aprobó la asignatura, su nota es:", nota_final)
	else:
		print("aprobó, pero debe mejorar, su nota es:", nota_final)
else:
	if nota_final<2.0:
		print("No aprobó, por lo tanto, no puede habilitar la asignatura, su nota es:", nota_final)

