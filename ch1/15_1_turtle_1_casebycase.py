# turtle 모듈을 이용한 다각형 생성코드

import turtle as t
from random import choice

color = ['darkred','sienna','ivory','lightgreen','gold','fuchsia','deeppink',
'crimson','olive','lime','midnightblue','lavender','blueviolet',
'plum','m','tan','darkorange','y','springgreen',
'coral','indianred','rosybrown','darkgray','teal']

t.shape('turtle')
t.pensize(5)

t.circle(20, steps=3)
t.color(choice(color))
t.circle(30, steps=4)
t.color(choice(color))
t.circle(40, steps=5)
t.color(choice(color))
