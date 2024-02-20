from bs4 import BeautifulSoup

with open("Dan_45-WebScraping_Beautiful_Soup/bs4-start/website.html", encoding="utf-8") as file:
    contents = file.read()


# u zavisnosti od sajta sa koga skidamo podatke koristimo razlicite parsere
# mozemo koristiti i lxml parser, ali mora onda i gore da se importuje
soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

# # trazenje title elementa
# print(soup.title)
# # trazenja teksta u title elementu
# print(soup.title.string)
# # trazenje naziva elementa
# print(soup.title.name)
# # trazenje prvog linka
# print(soup.a)
# # trazenje svih elemenata
# #info funkcija find_all()
# print(soup.find_all(name = "a"))
# all_anchor_tags = soup.find_all(name = "a")
# # ako hocemo samo tekst iz svih linkova onda koristimo for i getText()
# #info FOR petlja i funkcija "getText()" ili "get()"
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# trazenje po nazivima atributa
heading = soup.find(name = "h1", id = "name")
section_heading = soup.find(name = "h3", class_ = "heading") # --> mora da stoji "class_" jer je samo "class" rezervisano kada pravimo klase
print(heading, section_heading.getText())

company_url = soup.select_one(selector="p a") # --> selektori su isto kao i za css # je id . je class
print(company_url.get('href'))

#! find returns the first matching element as a single element, while select returns all matching elements as a list. Additionally, select allows for more complex CSS selector patterns, offering more flexibility in selecting elements.