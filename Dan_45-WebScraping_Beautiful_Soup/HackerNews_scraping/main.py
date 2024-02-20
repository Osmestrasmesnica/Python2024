from bs4 import BeautifulSoup
import requests
import pandas as pd
 
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
 
yc_web_page = response.text
 
soup = BeautifulSoup(yc_web_page, "html.parser")
 
article_texts = []
article_links = []
article_upvotes = []
 
# Loop through each 'athing' row
for row in soup.find_all('tr', class_='athing'):
    # Find the 'titleline' span and extract title and link
    title_line = row.find('span', class_='titleline')
    if title_line and title_line.a:
        article_texts.append(title_line.a.text)
        article_links.append(title_line.a['href'])
 
        # Find the next sibling row which should contain the upvotes
        next_row = row.find_next_sibling('tr')
        if next_row:
            score = next_row.find('span', class_='score')
            article_upvotes.append(int(score.text.split()[0]) if score else 0)
        else:
            article_upvotes.append(0)  # Default value if no upvote is found
 
# Ensure all lists are of the same length
min_length = min(len(article_texts), len(article_links), len(article_upvotes))
article_texts = article_texts[:min_length]
article_links = article_links[:min_length]
article_upvotes = article_upvotes[:min_length]
 
data = {"titles": article_texts, "links": article_links, "upvotes": article_upvotes}
 
df = pd.DataFrame(data)
 
sorted_df = df.sort_values(by="upvotes", ascending=False)
sorted_df.reset_index(drop=True, inplace=True)  # Remove the index from the DataFrame
print(sorted_df)