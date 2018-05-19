from graphics import *
import numpy as np
import time

P=[[300,600],[225,650],[150,650],[100,550],[200,350],[300,250],[500,250],[600,350],[700,550],[650,650],[575,650],[500,600]] #area_for_filling
coc=[]            #array to store of Point objects which will be used further to plot the polygon
start=[400,650]   #starting point of the fractal
end=[400,600]     #this point is used for giving the direction for the first branch
c=0.3

for i in range(len(P)):
    coc.append(Point(P[i][0],P[i][1]))

P=clk(P)                               #arrange the points of polygon in clockwise order
P=numpy.ndarray.tolist(P[0])


tree=[]                                #stores branch and its radius #later value is predicted by using murray law
tree1=[[start, end, P,1]]              #stores branch, its direction, polygon which the branch will divide and the radius of branch

    
def branch(start, end, P,r):
    [[start,end],p1,p2]=intersection(P,start,end)            #returns starting point of next branch and two newly formed polygon due to divison of bigger polygon
    a1=area(p1)
    com1=com(p1)                                             #center of mass/area of newly form polygon p1
    a2=area(p2)
    R=radius(r,p1,p2)
    com2=com(p2)                                             #center of mass/area of newly form polygon p2
    branch_end=[start[0]+c*(end[0]-start[0]),start[1]+c*(end[1]-start[1])]
    branch1_end=[branch_end[0]+(com1[0]-branch_end[0]),branch_end[1]+(com1[1]-branch_end[1])]
    branch2_end=[branch_end[0]+(com2[0]-branch_end[0]),branch_end[1]+(com2[1]-branch_end[1])]
    tree1.append([branch_end,branch1_end,p1,R[0],R[0]**2/(R[1]**2)])
    tree1.append([branch_end,branch2_end,p2,R[1],R[1]**2/R[0]**2])
    tree.append([branch_end,start,r])


for i in range(255):                     #tree will have 255 nodes #for full balanced tree total node must be 2^n-1
    branch(tree1[i][0],tree1[i][1],tree1[i][2],tree1[i][3])


win = GraphWin('Face',800, 800)
win.setBackground('white')
triangle = Polygon(coc)
triangle.setFill('light gray')
triangle.setOutline('light grey')
triangle.draw(win)



for i in range(len(tree)):
    f=tree[i]
    f1=Point(f[0][0],f[0][1])
    f2=Point(f[1][0],f[1][1])
    ln=Line(f1,f2)
    ln.setWidth(2)
    ln.setFill('black')
    ln.draw(win)
    #time.sleep(0.005)


win.getMouse()
win.close()
