# PYTHON DAN 34

#! HTML Entities
#info nekad se u tekstu & ili ` pise kao &amp ili #039 i da se izbegane koristimo html, unescape()

# import html
# novi_text = html.unescape(stari_text)

#! TYPE HINTS and ARROWS
#info mozemo da napisemo sa : varijablu da kada drzimo mis preko nje da nam pokaze koji je tip podataka
#info sa -> mozemo da napisemo sta ocekujemo kao povratnu informaciju (return type)

age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")
