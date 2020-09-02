import json
import webbrowser
from os import linesep
import os


def reporte():
   
    archivo = open("archivo1.json")
    registro = json.load(archivo)
    
    report = open("reporte.html","w")
    report.write("<!DOCTYPE html>"
+"<html>"
    +"<head>"
        +"<title>REPORTE</title>"
         + "<meta charset=\"utf-8\">"
          +"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
          +"<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css\"> "
          +"<style>"
    
    +"body {"
        +"background-color: Slategray;"
    +"}"
+"</style>"
    +"</head>"
    +"<body>"
        +"<div class=\"container\">"
  +"<h1>REPORTE  </h1>"
  
  +"<table class=\"table\">"
    +"<thead>"
      +"<tr>"
        +"<th>Nombre</th>"
        +"<th>Edad</th>"
        +"<th>Activo</th>"
        +"<th>Saldo </th>"
      +"</tr>"
    +"</thead>"
    +"<tbody>      "+linesep
            
            )
    cont_alternacion = 0
    for x in registro:
    
        clasetr = ""
        if cont_alternacion == 0:
            clasetr = "<tr class=\"table-primary\">"
            cont_alternacion += 1
        elif cont_alternacion == 1:
            clasetr = "<tr class=\"table-success\">"
            cont_alternacion += 1
        elif cont_alternacion == 2:
            clasetr = "<tr class=\"table-danger\">"
            cont_alternacion +=1

        elif cont_alternacion == 3:
            clasetr = "<tr class=\"table-info\">"
            cont_alternacion = 0



        report.write(clasetr  + "\n"
    + "<td>"+x["nombre"]+"</td>"   
    + "<td>"+str(x["edad"])+"</td>"   
    + "<td>"+x["activo"]+"</td>"   
    + "<td>"+str(x["saldo"])+"</td>"   
        
      +"</tr>"
    + linesep
    
        
    )

    report.write(
          "</tbody>"
  +"</table>"
+"</div>"


    +"</body>"
+"</html>"
    ) 

reporte()
os.system("reporte.html")

    


    



