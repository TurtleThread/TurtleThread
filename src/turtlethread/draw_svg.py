flip_y = True 
# in this file, everything is in python turtle coordinates, except when directly interfacing with te with .goto or .xcor/.ycor/.position() 


# this code uses code from this link: https://github.com/tfx2001/python-turtle-draw-svg/blob/master/main.py 
# attribution: 

# -*- coding: utf-8 -*-
# Author: tfx2001
# License: GNU GPLv3
# Time: 2018-08-09 18:27





#import turtle 

import turtlethread 
from bs4 import BeautifulSoup


from PIL import Image

import fitz
from svglib import svglib
from reportlab.graphics import renderPDF

from concurrent.futures import ThreadPoolExecutor # to speed up computation 

import numpy as np 

import tempfile

import turtlethread.stitches 

WriteStep = 15  # 贝塞尔函数的取样次数
Xh = 0  # 记录前一个贝塞尔函数的手柄
Yh = 0
scale = (1, 1)
first = True
K = 32

import math 
prev_turtle_pos = None 
prev_end_pos = None #"PREV END POS"
min_turtle_dist = 10 

prev_stitch = None 


def move_turtle_to(te:turtlethread.Turtle, x, y): 
    global prev_stitch 
    global prev_turtle_pos 
    global prev_end_pos 
    #print("STITCH GROUP:", type(te._stitch_group_stack[-1])) 
    #print("(PREVIOUS: {})".format(str(prev_stitch_type))) 
    #print() 

    #print(prev_end_pos) 
    #print(prev_turtle_pos) 
    #print(x, y)

    new_stitch = te._stitch_group_stack[-1] 

    diff_stitch_type = not ( (prev_stitch == None) or isinstance(new_stitch, type(prev_stitch)) ) 
    

    # first handle if we need to finish up the previous stitch as current is jump stitch 
    #print("DIFF STITCH TYPE:", diff_stitch_type)
    if diff_stitch_type: 
        #print("FROM {} TO {}".format(prev_stitch, type(new_stitch)))
        if isinstance(new_stitch, turtlethread.stitches.JumpStitch): 
            #print("DRAWING {} FROM {} TO {}".format(prev_stitch, prev_turtle_pos, prev_end_pos)) 

            with te.use_stitch_group(prev_stitch): 
                # then finish this up first before the jump stitch 
                pex, pey = prev_end_pos 
                if flip_y: 
                    te.goto(pex, -pey)
                else: 
                    te.goto(pex, pey) 
            
            prev_turtle_pos = prev_end_pos
            prev_stitch = new_stitch 


    if isinstance(new_stitch, turtlethread.stitches.JumpStitch): 
        #print("JUMP STITCHING FROM {} TO {}".format(prev_turtle_pos, (x,y)))
        # if it's jump stitch then just go 
        if flip_y: 
            te.goto(x, -y) 
        else: 
            te.goto(x, y) 
        prev_turtle_pos = list( te.position() ) 
        if flip_y: 
            prev_turtle_pos[1] = -prev_turtle_pos[1] 
        prev_stitch = new_stitch 
        prev_end_pos = x, y 
        return 

    # otherwise we need to see 
    currx, curry = prev_turtle_pos 
    xdiff = x-currx 
    ydiff = y-curry 
    mag = math.sqrt((xdiff)**2 + (ydiff)**2) # magnitude of difference vector 
    
    if ( mag >= min_turtle_dist): 
        #print("DRAWING {} CONSIDERING MAG FROM {} TO {} MID STOP AT {}".format(new_stitch, prev_turtle_pos, (x,y), (currx + (min_turtle_dist/mag) * xdiff, (curry + (min_turtle_dist/mag) * ydiff) )))
        # travel that distance first 
        if flip_y: 
            te.goto(currx + (min_turtle_dist/mag) * xdiff, - (curry + (min_turtle_dist/mag) * ydiff) ) 

        else: 
            te.goto(currx + (min_turtle_dist/mag) * xdiff, (curry + (min_turtle_dist/mag) * ydiff) ) 

        # then travel the remaining distance 
        if flip_y: 
            te.goto(x, -y) 
        else: 
            te.goto(x, y) 
        prev_turtle_pos = [x, y]
    
    prev_stitch = new_stitch 
    prev_end_pos = x, y 

    


def Bezier(p1, p2, t):  # 一阶贝塞尔函数
    return p1 * (1 - t) + p2 * t


def Bezier_2(te, x1, y1, x2, y2, x3, y3):  # 二阶贝塞尔函数
    move_turtle_to(te, x1, y1)
    #te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        move_turtle_to(te, x, y)

    ##te.penup()


def Bezier_3(te, startx, starty, x1, y1, x2, y2, x3, y3, x4, y4):  # 三阶贝塞尔函数
    x1 = startx + x1
    y1 = starty - y1
    x2 = startx + x2
    y2 = starty - y2
    x3 = startx + x3
    y3 = starty - y3
    x4 = startx + x4
    y4 = starty - y4  # 坐标变换
    move_turtle_to(te, x1, y1)
    #te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        move_turtle_to(te, x, y)

    #te.penup()


def Moveto(te, startx, starty, x, y):  # 移动到svg坐标下（x，y）
    with te.jump_stitch(): 
        move_turtle_to(te, startx + x, starty - y)


def Moveto_r(te, dx, dy):
    #te.penup()
    with te.jump_stitch(): 
        if flip_y: 
            move_turtle_to(te, te.xcor() + dx, -te.ycor() - dy)
        else: 
            move_turtle_to(te, te.xcor() + dx, te.ycor() - dy)
    #te.pendown()


def line(te, startx, starty, x1, y1, x2, y2):  # 连接svg坐标下两点
    #te.penup()
    with te.jump_stitch(): 
        move_turtle_to(te, startx + x1, starty - y1)
    #te.pendown()
    with te.running_stitch(30): 
        move_turtle_to(te, startx + x2, starty - y2) 
    #te.penup()


def Lineto_r(te, dx, dy):  # 连接当前点和相对坐标（dx，dy）的点
    #te.pendown()
    with te.running_stitch(30): 
        if flip_y: 
            move_turtle_to(te, te.xcor() + dx, -te.ycor() - dy) 
        else: 
            move_turtle_to(te, te.xcor() + dx, te.ycor() - dy) 
    #te.penup()


def Lineto(te, startx, starty, x, y):  # 连接当前点和svg坐标下（x，y）
    #te.pendown()
    with te.running_stitch(30): 
        move_turtle_to(te, startx + x, starty - y) 
    #te.penup()


def Curveto(te, startx, starty, x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
    #te.penup()
    X_now = te.xcor() - startx
    if flip_y: 
        Y_now = starty + te.ycor() 
    else: 
        Y_now = starty - te.ycor()
    Bezier_3(te, startx, starty, X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def Curveto_r(te, startx, starty, x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
    #te.penup()
    X_now = te.xcor() - startx 
    if flip_y: 
        Y_now = starty + te.ycor() 
    else: 
        Y_now = starty - te.ycor()
    Bezier_3(te, startx, starty, X_now, Y_now, X_now + x1, Y_now + y1,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def transform(w_attr):
    funcs = w_attr.split(' ')
    for func in funcs:
        func_name = func[0: func.find('(')]
        if func_name == 'scale':
            global scale
            scale = (float(func[func.find('(') + 1: -1].split(',')[0]),
                     -float(func[func.find('(') + 1: -1].split(',')[1]))


def readPathAttrD(w_attr):
    curr_parse = ''
    for i in w_attr:
        # print("now cmd:", i)
        if i == ' ':
            #print(float(curr_parse)) 
            yield float(curr_parse)
            curr_parse = ""
        elif i.isalpha():
            if (curr_parse):
                #print(float(curr_parse))
                yield float(curr_parse)
                curr_parse = ""
            #print(i) 
            yield i
        else:
            curr_parse += i



def drawSVG(te:turtlethread.Turtle, filename, height, w_color, thickness=1, fill=True, outline=False): # TODO consider colour 
    # draws an SVG file with the turtle 
    #print("HI DRAWING SVG")

    SVGFile = open(filename, 'r')
    SVG = BeautifulSoup(SVGFile.read(), 'lxml')
    viewbox = SVG.svg.attrs['viewbox'].split() # x y width height 
    Height = height #float(SVG.svg.attrs['height'][0: -2])
    Width = height * float(viewbox[2]) / float(viewbox[3]) #float(SVG.svg.attrs['width'][0: -2])
    if (SVG.svg.g and 'transform' in SVG.svg.g.attrs): 
        transform(SVG.svg.g.attrs['transform'])
    #if first:
        #te.setup(height=Height, width=Width)
        #te.setworldcoordinates(-Width / 2, 300, Width -
        #                       Width / 2, -Height + 300)
        #first = False
    #te.tracer(100)
    #te.pensize(1)
    #te.speed(10000)

    #turtle.speed(0) 
    #turtle.tracer(0,0)


    s = Height / float(viewbox[3]) 
    scale = [s, s]
    #print("SCALE:", scale) 

    startx, starty = float(viewbox[0])*scale[0], float(viewbox[1])*scale[1] 
    addsx, addsy = te.position() 

    global prev_turtle_pos 
    prev_turtle_pos = list(te.position()) 
    if flip_y: 
        prev_turtle_pos[1] = -prev_turtle_pos[1] 

    print("INITIAL PREV TURTLE POS", prev_turtle_pos)

    startx += addsx 
    starty += addsy 

    if flip_y: 
        addsy = -addsy 

    if flip_y: 
        scale[1] = -scale[1] 
        starty = -starty 

    print("START:", [startx, starty])


    #te.penup()

    # TODO: DEAL WITH FILL USING ZIGZAG/SATIN STITCH 


    #turtle.screensize(Width, Height)
    #screen = turtle.Screen() 


    # if it's fill 
    if fill: 
        lines = svg_get_lines(filename, round(Width), round(Height)) 

        for p1, p2 in lines: 
            with te.jump_stitch(): 
                #print("WITH JUMP STITCH:", te._stitch_group_stack[-1] )
                move_turtle_to(te, startx+p1[0], addsy+p1[1]) 
            with te.running_stitch(99999): 
                #print("WITH RUNNING STITCH:", te._stitch_group_stack[-1] )
                move_turtle_to(te, startx+p2[0], addsy+p2[1]) 




    # outline 
    # TODO: use satin stitch for thickness 
    if outline: 
        with te.running_stitch(30): # 99999 will make sure we won't have gaps 
            #te.color(w_color) # TODO SWITCH COLOUR OF TEXT 

            def get_position(): 
                posx, posy = te.position() 
                if flip_y: 
                    posy = -posy 
                return posx-startx, -posy+starty 

            firstpos = None 

            def set_firstpos(): 
                nonlocal firstpos
                firstpos = list(te.position())
                if flip_y: 
                    firstpos[1] = -firstpos[1] 
                firstpos[0] -= startx
                firstpos[1] *= -1
                firstpos[1] += starty 

            for i in SVG.find_all('path'):
                attr = i.attrs['d'].replace('\n', ' ')
                f = readPathAttrD(attr)
                lastI = ''
                for i in f:
                    #print(i) 
                    # if i.lower() in ['c', 'q', 'l', 'h' 'v', 'z']: 
                    #     set_firstpos() 
                    
                    if i == 'M':
                        #te.end_fill()
                        Moveto(te, startx, starty, next(f) * scale[0], next(f) * scale[1])
                        #te.begin_fill()
                        set_firstpos() 
                    elif i == 'm':
                        #te.end_fill()
                        Moveto_r(te, startx, starty, next(f) * scale[0], next(f) * scale[1])
                        set_firstpos() 
                        #te.begin_fill()
                    elif i == 'C':
                        Curveto(te, startx, starty, next(f) * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1])
                        lastI = i
                    elif i == 'c':
                        Curveto_r(te, startx, starty, next(f) * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1])
                        lastI = i
                    elif i == 'Q': 
                        X_now = te.xcor() #- startx
                        if flip_y: 
                            Y_now = -te.ycor() #starty - te.ycor()
                        else: 
                            Y_now = te.ycor() 
                        Bezier_2(te, X_now, Y_now, next(f) * scale[0] + startx, -next(f) * scale[1] + starty, 
                                next(f) * scale[0] + startx, -next(f) * scale[1] + starty) 
                    elif i == 'q': 
                        X_now = te.xcor() 
                        if flip_y: 
                            Y_now = -te.ycor() #starty - te.ycor()
                        else: 
                            Y_now = te.ycor() 
                        Bezier_2(te, X_now, Y_now, X_now + next(f) * scale[0], Y_now - next(f) * scale[1], 
                                X_now + next(f) * scale[0], Y_now - next(f) * scale[1],) 
                    elif i == 'L':
                        Lineto(te, startx, starty, next(f) * scale[0], next(f) * scale[1])
                    elif i == 'l':
                        Lineto_r(te, next(f) * scale[0], next(f) * scale[1])
                        lastI = i
                    elif i == 'H': 
                        if flip_y: 
                            Lineto(te, startx, starty, next(f) * scale[0], te.position()[1]+starty)
                        else: 
                            Lineto(te, startx, starty, next(f) * scale[0], -te.position()[1]+starty)
                    elif i == 'h':
                        Lineto_r(te, next(f) * scale[0], 0.0)
                        lastI = i
                    elif i == 'V': 
                        Lineto(te, startx, starty, te.position()[0]-startx, next(f) * scale[1])
                    elif i == 'v':
                        Lineto_r(te, 0.0, next(f) * scale[1])
                        lastI = i
                    elif i == 'Z' or i == 'z': 
                        Lineto(te, startx, starty, *firstpos)
                    elif lastI == 'C':
                        Curveto(te, startx, starty, i * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1])
                    elif lastI == 'c':
                        Curveto_r(te, startx, starty, i * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1],
                                next(f) * scale[0], next(f) * scale[1])
                    elif lastI == 'L':
                        Lineto(te, startx, starty, i * scale[0], next(f) * scale[1])
                    elif lastI == 'l':
                        Lineto_r(te, i * scale[0], next(f) * scale[1])
                    else: 
                        print("ERROR", i)



    with te.jump_stitch(): 
        move_turtle_to(te, addsx+Width, addsy) 

    SVGFile.close()



    # save it somewhere, for testing 
    #te.visualise(done=False, bye=False)
    

    '''
    from pathlib import Path
    savepath = (Path(__file__).parent / "visualise_postscript" / "test_text.eps") 
    print("SAVING TO", savepath)
    screen.getcanvas().postscript(file=savepath)

    import time 
    time.sleep(100)

    for i in range(2):
        try:
            turtle.bye()
        except turtle.Terminator:
            pass'''

    #turtle.update() 
    
    #return screen 

    return 

    
def svg_to_pil(svgname) -> Image.Image : 
    # Convert svg to pdf in memory with svglib+reportlab
    # directly rendering to png does not support transparency nor scaling
    drawing = svglib.svg2rlg(path=svgname)
    pdf = renderPDF.drawToString(drawing)

    # Open pdf with fitz (pyMuPdf) to convert to PNG
    doc = fitz.Document(stream=pdf)
    pix = doc.load_page(0).get_pixmap(alpha=True, dpi=300)

    with tempfile.NamedTemporaryFile(suffix='.png') as tmpf: 
        pix.save(tmpf.name)

        image = Image.open(tmpf.name) 
    #print("FINISHED SVG TO PIL")
    return image 


def svg_get_lines(svgname, width:int, height:int): 
    lines = [] 

    image = svg_to_pil(svgname).resize((width, height)) 
    n = np.array(image) 
    for r in range(width): 
        prev = 0 
        prev1 = -1 
        for c in range(height): 
            if n[c,r,3] > 0: # not transparent 
                if prev == 0: 
                    prev1 = c 
                prev = 1 
            else: 
                if prev == 1: # from non-transparent to transparent 
                    lines.append([(r,prev1), (r,c-1)]) 
                prev = 0
        if prev==1: # end of edge 
            lines.append([(r,prev1), (r,c)]) 

    #print("GOT LINES:", lines)
    
    return lines 

