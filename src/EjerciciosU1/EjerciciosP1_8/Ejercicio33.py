#PSEUDOCÓDIGO
"""
Inicio
	Escribe "Dame 3 números: "
	Lee n1
	Lee n2
	Lee n3
	
	Si (n1 < n2 and n1 < n3) entonces
		Si (n2 < n3) entonces
			Escribe n1 + " " + n2 + " " + n3
		Sino
			Escribe n1 + " " + n3 + " " + n2
	Sino
		Si (n2 < n1 and n2 < n3) entonces
			Si (n1 < n3) entonces
				Escribe n2 + " " + n1 + " " + n3
			Sino
				Escribe n2 + " " + n3 + " " + n1
		Sino
			Si (n3 < n1 and n3 < n2) entonces
				Si (n1 < n2) entonces
					Escribe n3 + " " + n1 + " " + n2
				Sino
					Escribe n3 + " " + n2 + " " + n1
Fin
"""

print("Dame tres números: ")
n1=int(input())
n2=int(input())
n3=int(input())

if(n1<n2 and n1<n3):
    if(n2<n3):
        print(n1,"",n2,"",n3)
    else:
        print(n1,"",n3,"",n2)
else:
    if(n2<n1 and n2<n3):
        if(n1<n3):
            print(n2,"",n1,"",n3)
        else:
            print(n2,"",n3,"",n1)
    else:
        if(n3<n1 and n3<n2):
            if(n1<n2):
                print(n3,"",n1,"",n2)
            else:
                print(n3,"",n2,"",n1)