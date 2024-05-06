import requests
from bs4 import BeautifulSoup


def fetch_tech_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP issues
        soup = BeautifulSoup(response.text, 'html.parser')

        # Modify this to suit the structure of the website you are scraping
        headlines = soup.find_all('h2')  # Assuming headlines are in <h2> tags
        return [headline.get_text().strip() for headline in headlines]
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []


def main():
    # Mapping of URLs to their names for easy reference
    websites = {
        'https://techcrunch.com': 'TechCrunch',
        'https://www.theverge.com': 'The Verge',
        'https://www.wired.com': 'Wired'
    }

    # Dictionary to store results
    news_by_website = {}

    for url, name in websites.items():
        headlines = fetch_tech_news(url)
        news_by_website[name] = headlines

    # Display the results organized by website
    for website, headlines in news_by_website.items():
        print(f"News from {website}:")
        for headline in headlines:
            print(f" - {headline}")
        print("\n")


if __name__ == "__main__":
    main()
