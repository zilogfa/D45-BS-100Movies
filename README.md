# Web Data Scraping with Beautiful Soup

A Python script utilizing Beautiful Soup for scraping the top 100 movie titles from an archived webpage and storing them in a text file. Additionally, it can randomly select a movie title from this list.

## Features

- **Data Scraping**: Extracts content from a given web archive URL using Beautiful Soup.
- **Text File Storage**: Saves the scraped movie titles into `movies.txt`.
- **Random Movie Selector**: Picks a random movie title from the stored list.

## Dependencies

- **Beautiful Soup**: For parsing HTML and XML documents.
- **Requests**: For making HTTP requests to web pages.

## Setup

1. Install Python 3.x on your system.
2. Install the required libraries using pip:

```
pip install beautifulsoup4 requests
```

3. Clone this repository or copy the `main.py` script to your local machine.
4. Run the script with `python main.py`.

## Usage

- Simply run the script. It will fetch the list of movies and save them into `movies.txt`.
- When prompted, it will also print out a randomly selected movie title from the list.


