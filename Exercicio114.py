import urllib
import urllib.request


def VerificarSite():

    try:
        url = urllib.request.urlopen("http://www.pudim.com.br")
    except urllib.error.URLError:
        print(f"Ocorreu um erro ao acessar o site!  ")
    else:
        print("O Site esta disponivel para uso :D")
        print(url.read)

VerificarSite()
