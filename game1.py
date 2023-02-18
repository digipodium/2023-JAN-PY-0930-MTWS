import pgzrun

# add bgm music
music.play('bg')

# b = Rect((50,50), (100,50))
b =  Actor('img1', (300,300))
vx, vy = 3, 5     # global variable

def draw():
    screen.fill('black')
    # screen.draw.filled_rect(b, 'yellow')
    b.draw()

def update():
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
        sounds.s1.play()
    if b.bottom > 600 or b.top < 0:
        vy = -vy
        sounds.s1.play()

pgzrun.go()

