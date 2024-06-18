import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"

def get_quotes():
    quotes_list = []
    authors_dict = {}
    page = 1

    while True:
        response = requests.get(f"{BASE_URL}/page/{page}/")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            break

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            quotes_list.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

            author_url = BASE_URL + quote.find("a")["href"]
            if author not in authors_dict:
                author_info = get_author_info(author_url)
                authors_dict[author] = author_info

        page += 1

    return quotes_list, authors_dict

def get_author_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    author_name = soup.find("h3", class_="author-title").text.strip()
    born_date = soup.find("span", class_="author-born-date").text.strip()
    born_location = soup.find("span", class_="author-born-location").text.strip()
    description = soup.find("div", class_="author-description").text.strip()

    return {
        "fullname": author_name,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    quotes, authors = get_quotes()
    
    save_to_json(quotes, 'quotes.json')
    save_to_json(list(authors.values()), 'authors.json')

if __name__ == "__main__":
    main()
