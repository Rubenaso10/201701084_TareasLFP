def automata(cadenita):

  
  estado_principal = 0 #Estado con el que nos movemos
  

  #cadenita = input("Ingrese Cadenita: ") # __Letra+Numero --->Cadena Valida
  for x in cadenita: # 34AB

      if estado_principal == 0:
          if x == "_" :
            estado_principal=1 
          elif x.isalpha():
            estado_principal = 2
          else:
              break #print("Cadenita invalida")
      

      elif estado_principal==1:
          if x == "_":
              estado_principal=1
          elif x.isalpha():
              estado_principal=3
          else:
              break
              #print("Cadenita invalida")
          

      elif estado_principal==3:
          if x.isdigit():
              estado_principal =4
          else :
              break
              #print("Cadenita Invalida")

        
      elif estado_principal==2:
          if x.isalpha():
              estado_principal=2
          elif x.isdigit():
              estado_principal=4
          else:
               break
            #print("Cadenita invalida")

      elif estado_principal==4:
          estado_principal= 5
          break 

  if estado_principal == 4:
       print("CADENA VALIDA")
  else:
      print("CADENA INVALIDA")


automata("__Servidor1")
automata("Servidor3")
           
          


       

       
          
          




      





