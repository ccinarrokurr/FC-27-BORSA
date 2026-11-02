import requests
from bs4 import BeautifulSoup

def update_player_price(player_id, new_price):
    url = "https://ccinarrokurr.github.io/FC-27-BORSA/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        player_div = soup.find('div', {'id': player_id})
        
        if player_div:
            price_span = player_div.find('span', {'class': 'price'})
            if price_span:
                price_span.string = new_price
                
                with open('index.html', 'w', encoding='utf-8') as file:
                    file.write(str(soup))
                print(f"Price updated for {player_id}")
            else:
                print("Price span not found")
        else:
            print("Player div not found")
    else:
        print("Failed to access the website")

update_player_price('mbappe', '2,500,000')
