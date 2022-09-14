# turtle 모듈을 이용한 다각형 생성코드

import turtle as t
from random import choice

color = ['darkred','sienna','ivory','lightgreen','gold','fuchsia','deeppink',
'crimson','olive','lime','midnightblue','lavender','blueviolet',
'plum','m','tan','darkorange','y','springgreen',
'coral','indianred','rosybrown','darkgray','teal']

t.shape('turtle')
t.pensize(5)

for i in range(2, 12):
    t.circle(i*10, steps=i+1)
    t.color(choice(color))

t.done()

