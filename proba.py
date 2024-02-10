import requests


response = requests.get(url="https://opentdb.com/api_category.php")
response.raise_for_status()
data = response.json()
kategorije = data["trivia_categories"]
# print(kategorije)


# from this {'id': 30, 'name': 'Science: Gadgets'} want to make this {30:Science: Gadgets}
new_dict = {dict["id"]:dict["name"] for dict in kategorije}
string_representation = ", ".join([f"{value} ({key})" for key, value in new_dict.items()])
print(string_representation)
