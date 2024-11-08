# this code uses code from this link: https://github.com/tfx2001/python-turtle-draw-svg/blob/master/main.py 
# attribution: 

# -*- coding: utf-8 -*-
# Author: tfx2001
# License: GNU GPLv3
# Time: 2018-08-09 18:27



import turtle 

import turtlethread 
from bs4 import BeautifulSoup


from PIL import Image

import fitz
from svglib import svglib
from reportlab.graphics import renderPDF

from concurrent.futures import ThreadPoolExecutor # to speed up computation 

import numpy as np 

import tempfile 

WriteStep = 15  # 贝塞尔函数的取样次数
Xh = 0  # 记录前一个贝塞尔函数的手柄
Yh = 0
scale = (1, 1)
first = True
K = 32


def Bezier(p1, p2, t):  # 一阶贝塞尔函数
    return p1 * (1 - t) + p2 * t


def Bezier_2(te, x1, y1, x2, y2, x3, y3):  # 二阶贝塞尔函数
    te.goto(x1, y1)
    #te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        te.goto(x, y)
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
    te.goto(x1, y1)
    #te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        te.goto(x, y)
    #te.penup()


def Moveto(te, startx, starty, x, y):  # 移动到svg坐标下（x，y）
    with te.jump_stitch(): 
        te.goto(startx + x, starty - y)


def Moveto_r(te, dx, dy):
    #te.penup()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    #te.pendown()


def line(te, startx, starty, x1, y1, x2, y2):  # 连接svg坐标下两点
    #te.penup()
    te.goto(startx + x1, starty - y1)
    #te.pendown()
    te.goto(startx + x2, starty - y2)
    #te.penup()


def Lineto_r(te, dx, dy):  # 连接当前点和相对坐标（dx，dy）的点
    #te.pendown()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    #te.penup()


def Lineto(te, startx, starty, x, y):  # 连接当前点和svg坐标下（x，y）
    #te.pendown()
    te.goto(startx + x, starty - y)
    #te.penup()


def Curveto(te, startx, starty, x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
    #te.penup()
    X_now = te.xcor() - startx
    Y_now = starty - te.ycor()
    Bezier_3(te, startx, starty, X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def Curveto_r(te, startx, starty, x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
    #te.penup()
    X_now = te.xcor() - startx 
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



def drawSVG(te:turtlethread.Turtle, filename, height, w_color, thickness=1, fill=False): # TODO consider colour 
    # draws an SVG file with the turtle 

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
    te.speed(0)


    s = Height / float(viewbox[3]) 
    scale = [s, s]
    print("SCALE:", scale) 

    startx, starty = float(viewbox[0])*scale[0], float(viewbox[1])*scale[1] 
    addsx, addsy = te.position() 
    startx += addsx 
    starty += addsy 

    print("START:", [startx, starty])


    #te.penup()

    # TODO: DEAL WITH FILL USING ZIGZAG/SATIN STITCH 


    turtle.screensize(Width, Height)
    screen = turtle.Screen() 


    if fill: 
        tpe = ThreadPoolExecutor() 
        future_lines = tpe.submit(svg_get_lines, filename, round(Width), round(Height))
    
    

    # TODO: use satin stitch for thickness 
    with te.running_stitch(99999): # 99999 will make sure we won't have gaps 
        #te.color(w_color) # TODO SWITCH COLOUR OF TEXT 

        def get_position(): 
            posx, posy = te.position() 
            return posx-startx, -posy+starty 

        firstpos = None 

        def set_firstpos(): 
            nonlocal firstpos
            firstpos = list(te.position())
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
                    Y_now = te.ycor() #starty - te.ycor()
                    Bezier_2(te, X_now, Y_now, next(f) * scale[0] + startx, -next(f) * scale[1] + starty, 
                             next(f) * scale[0] + startx, -next(f) * scale[1] + starty) 
                elif i == 'q': 
                    X_now = te.xcor() 
                    Y_now = te.ycor()
                    Bezier_2(te, X_now, Y_now, X_now + next(f) * scale[0], Y_now - next(f) * scale[1], 
                             X_now + next(f) * scale[0], Y_now - next(f) * scale[1],) 
                elif i == 'L':
                    Lineto(te, startx, starty, next(f) * scale[0], next(f) * scale[1])
                elif i == 'l':
                    Lineto_r(te, next(f) * scale[0], next(f) * scale[1])
                    lastI = i
                elif i == 'H': 
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


    # handle fill if needed 
    if fill: 
        #lines = svg_get_lines(filename, round(Width), round(Height)) 
        # get lines - started processing earlier to speed up. 
        lines = future_lines.result() 
        tpe.shutdown() 
        del tpe 

        for p1, p2 in lines: 
            with te.jump_stitch(): 
                te.goto(startx+p1[0], -addsy-p1[1]) 
            with te.running_stitch(99999): 
                te.goto(startx+p2[0], -addsy-p2[1]) 

    with te.jump_stitch(): 
        te.goto(addsx+Width, addsy) 

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
    
    return screen 

    
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

