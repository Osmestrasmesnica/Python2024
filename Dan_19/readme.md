Dan 19 - 

# 1 -  da pocnes da slusas event, onda unosis listen()
    screen.listen()

# 2 - funkcija da bindujemo dugme da se desi nesto kada se prepozna dugme
    def function_a(something):
        do this with something
        then do this
        finally do this
    def function_b():
        do this
    

# 3 - Pozivanje funkcije unutar funkcije takodje moze da se uradi
#   ovo se jos zove higher order function
#   jedan primer toga je event listening
    function_a(function_b())

# 4 - pozivanje event listener da prepozna akciju i dugme koje smo mu zadali i da onda izvrsi funcija
    screen.onkey(key = "Up", fun = "function_a")
    screen.onkeyrelease(key = "Down", fun = "function_b")

# 5 - 
