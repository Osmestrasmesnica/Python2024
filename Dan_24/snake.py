from turtle import Turtle

# Varijable/Konstante
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STARTING_POSITION = [(0,0), (-20,0), (-40,0)] #konstanta se pise velikim slovima, ovo je bolji metod od for i sto sam ja pisao prvo
MOVE_DISTANCE = 20 # konstanta kojom se zmija krece, jer ako hocemo da se pomera brze onda samo ovo menjamo

class Snake:
    """Napraviti telo Snake"""
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        # pravi telo od snake
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        body_part = Turtle("square")
        body_part.penup()
        body_part.color('red')
        body_part.goto(position)
        self.snake_body.append(body_part)

    def extend(self):
        """add a new segment to the snake. [-1] ti u listi daje poslednju stvar u listi"""
        self.add_segment(self.snake_body[-1].position())
    
    def move(self):
        """Make Snake Move, and make tail follow head position"""
        for segment_number in range(len(self.snake_body)-1, 0, -1): # START, STOP, STEP.. ako hocemo range 123, onda je start 1, stop 3, step 1, a ako hocemo 321 onda je start 3, stop 1, segment-1, ali zato sto prolazimo kroz listu, a ona pocinje sa 0, a zavrsava se sa n-1 onda krecemo od 2 a zavrsavamo na 0
            new_x = self.snake_body[segment_number-1].xcor() # pozivija x ose pretposlednjeg segmenta
            new_y = self.snake_body[segment_number-1].ycor() # pozivija y ose pretposlednjeg segmenta
            self.snake_body[segment_number].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE) # zelimo da napravimo konstantu kojom se zmija krece zato ovo menjamo ovako

    # napomena da ne mozes da ako ides levo da stisnes desno i da zmija krene desno, ako ides gode ne moze na dole da krene    
    def up(self):
        """Skretanje na gore"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        """Skretanje na dole"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Skretanje na levo"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Skretanje na desno"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def cheat(self):
        self.snake_body[0].goto(0,0)

    def reset(self):
        """Resetujemo zmiju kao na pocetku kada je __init__"""
        for segment in self.snake_body:
            segment.goto(1000, 1000)
            segment.hideturtle()
        self.snake_body.clear() # clear the list
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.showturtle()
        

