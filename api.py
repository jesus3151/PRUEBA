import requests

# 1. La URL de la API a la que le vamos a hacer la petición (nuestro "mesero")
url = "https://jsonplaceholder.typicode.com/users/1"

# 2. Le pedimos los datos al servidor externo
respuesta = requests.get(url)

usuario = input("Ingrese el nombre del usuario: ")
print(usuario)

# 3. Convertimos la respuesta en un formato que Python entienda (un diccionario)
datos = respuesta.json()

# 4. Usamos la información en nuestro código como si fuera nuestra
print("¡Datos obtenidos de la API con éxito!")
print(f"Nombre del usuario: {datos['name']}")
print(f"Correo electrónico: {datos['email']}")
print(f"Ciudad donde vive: {datos['address']['city']}")