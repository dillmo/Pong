import sfml as sf
import random as rng

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "Pong"

rng.seed(a=None, version=2)

class Ball():
    def __init__(self):
        self.size = 10
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.vx = rng.randint(-5, 5)
        self.vy = rng.randint(-5, 5)
        self.sprite = sf.RectangleShape(sf.Vector2(self.size, self.size))

    def update(self):
        # Bouncing
        if self.x <= 0 or self.x >= WINDOW_WIDTH - self.size:
            # Reset if I run into either vertical window border
            self.__init__()
        else:
            if self.y <= 0 or self.y >= WINDOW_HEIGHT - self.size:
                self.vy = -self.vy
            if self.x <= paddle1.x + paddle1.width:
                if self.y <= paddle1.y + paddle1.height and self.y >= paddle1.y:
                    self.vx = abs(self.vx)
                    self.vy += paddle1.velocity
            if self.x >= paddle2.x - self.size:
                if self.y <= paddle2.y + paddle2.height and self.y >= paddle2.y:
                    self.vx = -abs(self.vx)
                    self.vy += paddle2.velocity
        # Update position
        self.x += self.vx
        self.y += self.vy
        self.sprite.position = (self.x, self.y)

class Paddle():
    def __init__(self, isPlayer, side):
        self.isPlayer = isPlayer
        self.width = 10
        self.height = 100
        self.velocity = 0
        self.maxVelocity = 3
        self.moveRate = 1
        if side == "left":
            self.x = 0
        else:
            self.x = WINDOW_WIDTH - self.width
        self.y = WINDOW_HEIGHT / 2 - self.height / 2
        self.sprite = sf.RectangleShape(sf.Vector2(self.width, self.height))

    def goUp(self):
        self.velocity -= self.moveRate
        if self.velocity < -self.maxVelocity:
            self.velocity = -self.maxVelocity
    def goDown(self):
        self.velocity += self.moveRate
        if self.velocity > self.maxVelocity:
            self.velocity = self.maxVelocity

    def update(self):
        # Movement
        if self.isPlayer:
            # Handle keypresses
            if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
                self.goUp()
            elif sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
                self.goDown()
            else:
                # Slow down over time
                if self.velocity > 0:
                    self.velocity -= self.moveRate
                elif self.velocity < 0:
                    self.velocity += self.moveRate
        else:
            if self.y < ball.y:
                self.goDown()
            elif self.y > ball.y:
                self.goUp()
        # Update position
        # Detect collisions with the window borders
        if self.y <= 0:
            self.velocity = abs(self.velocity)
        elif self.y >= WINDOW_HEIGHT - self.height:
            self.velocity = -abs(self.velocity)
        self.y += self.velocity
        self.sprite.position = (self.x, self.y)

window = sf.RenderWindow(sf.VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_TITLE)
ball = Ball()
paddle1 = Paddle(isPlayer=True, side="left")
paddle2 = Paddle(isPlayer=False, side="right")

# Changes the properties of sprites each tick
def update():
    ball.update()
    paddle1.update()
    paddle2.update()

# Draws sprites each tick
def draw():
    window.draw(ball.sprite)
    window.draw(paddle1.sprite)
    window.draw(paddle2.sprite)

# Game loop
while window.is_open:
    # Process events
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
    # Update the window
    update()
    window.clear()
    draw()
    window.display()
