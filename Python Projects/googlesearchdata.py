import requests, webbrowser
from bs4 import BeautifulSoup


user_input = input("enter something to search...")
print("googling...")
header = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

google_search = requests.get("https://www.google.com/search?q="+user_input, headers=header)
#soup = BeautifulSoup(google_search.text, 'html.parser')
soup1 = BeautifulSoup(google_search.text, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')


#print(soup2.prettify())
search_results = soup2.select('.r a')
print(search_results)
#print(search_results)
for link in search_results[0:2]:
    actual_link= link.get_text('herf')
    webbrowser.open(actual_link)
    print("Haa...Ho gaya")

