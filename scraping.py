import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do Google que você deseja raspar
URL = "https://www.google.com/search?sca_esv=5ad93beeef71fbb7&rlz=1C1CHBF_pt-PTBR1088BR1088&tbm=shop&sxsrf=ACQVn0_0gfTduOXZCaIqEDcgEBUfsv9IFg:1712062000918&q=livros+mais+vendidos&prmd=sivnbmtz&tbs=vw:g,mr:1,merchagg:g134886126%7Cg103278022%7Cg104823487%7Cg8670533%7Cm134942054%7Cm134880504%7Cm121281735%7Cm267764863%7Cm111569157%7Cm112295332%7Cm5305103289%7Cm441351849%7Cm546649349%7Cm282570203%7Cm478855842%7Cm553660352%7Cm735128188%7Cm735125422%7Cm735128761%7Cm735098639%7Cm735098660&sa=X&ved=0ahUKEwjA-Jb7x6OFAxWfpZUCHVH_AmsQsysI5gkoBQ&biw=1146&bih=835&dpr=1.1"

# Cabeçalhos para simular um navegador real
HEADERS = {
    'User-Agent': ''
}

# Fazendo a solicitação HTTP
webpage = requests.get(URL, headers=HEADERS)
print(webpage)

# Convertendo o conteúdo da página em HTML
soup = BeautifulSoup(webpage.content, "html.parser")

titles = soup.find_all('h3', {'class': 'tAxDx'})
prices = soup.find_all('span', {'class': 'a8Pemb OFFNJ'})
sellers = soup.find_all('div', {'class': 'aULzUe IuHnof'})

# Criar um DataFrame com os dados
data = {'Produto': [title.text for title in titles],
        'Preço': [price.text for price in prices],
        'Vendedor': [seller.text for seller in sellers]}


df = pd.DataFrame(data)

# Escrever o DataFrame em um arquivo CSV
df.to_csv('livros.csv', index=False)

print("Dados gravados no arquivo livros.csv")


