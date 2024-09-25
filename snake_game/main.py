
from turtle import Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)



    

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while game_is_on:
    screen.update()
    
    
    snake.move()
    time.sleep(0.1)
    #detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increasescore()
#detect collision with tail.


    # detect collision with food

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()