import pygame
import play
from random import randint


play.screen.width = 994
play.screen.height = 492


fone = play.new_image (image = 'fone.png', size = 33)


truba_list = []


status = 1



bird = play.new_image(image = 'bird0.png', x = - 350, y = 200)
total_score = play.new_image(image = 'score.png', x = - 455, y = 235, size = 150)


sound_jump = pygame.mixer.Sound('qwerty.ogg')


restart_button = play.new_image(image = 'restart.png', x =- 250, y = -150)
exit_button = play.new_image(image = 'exit.png', x = 250, y = -150)
restart_button.hide()
exit_button.hide()


# one = play.new_image (image = 'one.png')
# two = play.new_image (image = 'two.png')
# three = play.new_image (image = 'three.png')
# five = play.new_image (image = 'five.png')
# six = play.new_image (image = 'six.png')
# seven = play.new_image (image = 'seven.png')
# eight = play.new_image (image = 'eight.png')
# nine = play.new_image (image = 'nine.png')
# zero = play.new_image (image = 'zero.png')

def draw_truba(y, delta):
    x_cor = 510
    # truba1=play.new_image(image='truba.png', x=x_cor, y=y, size=20)
    # truba3=play.new_image(image='truba.png', x=x_cor, y=y+460+delta, angle= 180, size=20)
    
    truba = play.new_box (height = 462, width = 65, x = x_cor, y = y, transparency = 50)
    truba2=play.new_box (height = 462, width = 65, x = x_cor, y = y + 460 + delta, angle = 180, transparency = 50)
    return truba, truba2


@play.repeat_forever
def go_bird ():
    if play.key_is_pressed ('space') : 
        bird.y = bird.y + 3
    else:
        bird.y -= 3


@play.repeat_forever
async  def vois_bird () :
    global status
    if status == 1 :
        if play.key_is_pressed ('space') :
            sound_jump.play ()
            await play.timer (2)


@play.repeat_forever
async def made () :
    global status
    if status == 1:
        y = randint (- 350, - 200)
        delta = randint (100, 200)
        sprites = draw_truba (y, delta)
        truba_list.append (sprites)
        await play.timer (seconds = 5)
    

@play.repeat_forever
def move () :
    for truba in truba_list :
        truba[0].x -= 5
        truba[1].x -= 5
        if truba[0].x < - 497 :
                truba[0].remove ()
                truba[1].remove ()
                truba_list.remove (truba)


def all_hide (truba_list) :
    for truba in truba_list :
        truba[0].hide ()
        truba[1].hide ()
                         
    
@play.repeat_forever
def lose () :
    global status
    for truba in truba_list :
        if bird.is_touching (truba[0]) or bird.is_touching (truba[1]) :
            status = 0
            all_hide (truba_list)
            bird.stop_physics()
            bird.hide () 
            lose = play.new_text (words = 'LOSER', x = 0, y = 100, font_size = 200)
            restart_button.show()
            exit_button.show()


@play.repeat_forever
async def scoree () :
    for truba in truba_list:
        if truba[0].x < - 497 :
            score =+ 1
            await play.timer (seconds = 5)
            #score = play.new_text (words = score, font_size = 100, x = - 400 , y = 235 )


@restart_button.when_clicked
def restart () :
    global status
    status = 0


@exit_button.when_clicked
def exit () :
    exit()












play.start_program()
