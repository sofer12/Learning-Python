# Learning-Python
Repositorio de scripts en lenguaje de programación Python 

# proceso de estaging:

Primer comando: Enviar paquete a staging o a la cola
$git add . /$git add --all / git add FILE_NAME.ext / git add FOLDER_NAME

Segundo comando: Anexar mensaje - ¿Que contiene el paquerte? 
$git commit -m "AQUI VA EL MENSAJE"  //-m significa message

Tercer comando: Enviar el paquete o desplegar hacia su destino (RAMA).
$git push origin NOMBRE_RAMA/BRANCH_NAME /$git push

# Comando para hacer seguimiento para hacer seguimiento (archivos color rojo no estan craquados .. son intrusos..git no toma encuenta directorios vacios)
$git status

$ git reset (para quitar el envio)
$ git rstore --staged FILE_NAME.ext
$ git log (Ver cambios realizados)
