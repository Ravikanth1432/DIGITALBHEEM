import turtle
import random
import time

# Set up the game screen
game_screen = turtle.Screen()
game_screen.title("Colorful Snake Game")
game_screen.setup(width=700, height=700)
game_screen.tracer(0)
game_screen.bgcolor("#5F98A6")

# Draw colorful boundaries
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.pensize(4)
border_pen.penup()
border_pen.goto(-350, 357)
border_pen.pendown()
colors = ["#FF5733", "#FFD633", "#33FF57", "#337BFF"]
for color in colors:
    border_pen.color(color)
    border_pen.forward(700)
    border_pen.right(90)
border_pen.hideturtle()

# Initialize the game
score = 0
delay = 0.1
food_collection = []

# Create a vibrant snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("#FF5733")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Create colorful food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#FFD633")
food.penup()
food.goto(30, 30)

# Display a dynamic score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("#33FF57")
score_display.penup()
score_display.hideturtle()
score_display.goto(-240, 290)
score_display.write("Score: ", align="center", font=("Arial", 25, "bold"))

# Movements
def move_up():
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    if snake.direction != "up":
        snake.direction = "down"

def move_left():
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)

# User input
game_screen.listen()
game_screen.onkeypress(move_up, "Up")
game_screen.onkeypress(move_down, "Down")
game_screen.onkeypress(move_left, "Left")
game_screen.onkeypress(move_right, "Right")

# Game loop
while True:
    game_screen.update()

    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        score += 1
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Arial", 25, "bold"))
        delay -= 0.001

        # Add new colorful food to the collection
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("#33FF57")
        new_food.penup()
        food_collection.append(new_food)

    # Move snake's body
    for index in range(len(food_collection) - 1, 0, -1):
        food_collection[index].goto(food_collection[index - 1].pos())

    # Move the first body segment to where the head is
    if len(food_collection) > 0:
        food_collection[0].goto(snake.pos())

    # Move the snake
    snake_move()

    # Collision detection and game over
    if (
        snake.xcor() > 340
        or snake.xcor() < -340
        or snake.ycor() > 340
        or snake.ycor() < -340
    ):
        time.sleep(1)
        game_screen.clear()
        game_screen.bgcolor("#330033")
        score_display.goto(0, 0)
        score_display.write(
            "Game Over\nYour Score: {}".format(score),
            align="center",
            font=("Arial", 30, "bold"),
        )
        break

    # Check for collision with the snake's body
    for foods in food_collection:
        if foods.distance(snake) < 20:
            time.sleep(1)
            game_screen.clear()
            game_screen.bgcolor("#003366")
            score_display.goto(0, 0)
            score_display.write(
                "Game Over\nYour Score: {}".format(score),
                align="center",
                font=("Arial", 30, "bold"),
            )
            break

    time.sleep(delay)

# Cleanup
turtle.bye()