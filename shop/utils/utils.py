from urllib.parse import urlparse

def validateUrl(url):
    try:
        resultado = urlparse(url)
        return all([resultado.scheme, resultado.netloc])
    except ValueError:
        return False

def contiene_palabra(texto, palabra):
    # Convertir los textos a minúsculas para que la comparación no distinga entre mayúsculas y minúsculas
    texto = texto.lower()
    palabra = palabra.lower()

    # Verificar si la palabra está presente en el texto
    return palabra in texto