from googletrans import Translator

# Crea una instancia del traductor
translator = Translator()

# Define el texto que deseas traducir
texto_a_traducir = "Hello, world!"

# Utiliza el traductor para traducir el texto al español
texto_traducido = translator.translate(texto_a_traducir, dest='es').text

# Imprime el texto traducido
print(texto_traducido)
