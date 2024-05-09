import urllib
import urllib.error
import urllib.request
try:
    site= urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw')
except urllib.error.URLError:
    print('\033[31mNão consegui acessar o site do pudim')
else:
    print('\033[32mConsegui acessar o site do pudim\033[m')
finally:
    print('Você gosta de pudim?')