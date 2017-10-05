# -*- coding: utf-8 -*-
"""
Created on Sun May 28 07:47:25 2017

@author: HP-PC
"""
import numpy

def clk(P) :
    total_points=len(P)
    sumx=0
    sumy=0
    for i in range(total_points):
        sumx=sumx+P[i][0]
        sumy=sumy+P[i][1]
    
    avgx=sumx/total_points
    avgy=sumy/total_points
    nP=numpy.zeros((total_points,2))
    for i in range(total_points):
        nP[i][0]=P[i][0]-avgx
        nP[i][1]=P[i][1]-avgy
    
    THETA=numpy.zeros((total_points,2)).tolist()
    for i in range(total_points):
        THETA[i][0]=numpy.arctan2(nP[i][1],nP[i][0])*180/numpy.pi
        THETA[i][1]=i
    
    for i in range(total_points):
        for j in range(i+1,total_points):
            if THETA[i][0]<THETA[j][0]:
               temp=THETA[j][0]
               tem=int(THETA[j][1])
               THETA[j][0]=THETA[i][0]
               THETA[j][1]=int(THETA[i][1])
               THETA[i][0]=temp
               THETA[i][1]=tem
    for i in range(total_points):
        nP[i][0]=P[int(THETA[i][1])][0]
        nP[i][1]=P[int(THETA[i][1])][1]
    return[nP]
    
def aclk(P) :
    total_points=len(P)
    sumx=0
    sumy=0
    for i in range(total_points):
        sumx=sumx+P[i][0]
        sumy=sumy+P[i][1]
    
    avgx=sumx/total_points
    avgy=sumy/total_points
    nP=numpy.zeros((total_points,2))
    for i in range(total_points):
        nP[i][0]=P[i][0]-avgx
        nP[i][1]=P[i][1]-avgy
    
    THETA=numpy.zeros((total_points,2)).tolist()
    for i in range(total_points):
        THETA[i][0]=numpy.arctan2(nP[i][1],nP[i][0])*180/numpy.pi
        THETA[i][1]=i
    
    for i in range(total_points):
        for j in range(i+1,total_points):
            if THETA[i][0]<THETA[j][0]:
               temp=THETA[j][0]
               tem=int(THETA[j][1])
               THETA[j][0]=THETA[i][0]
               THETA[j][1]=int(THETA[i][1])
               THETA[i][0]=temp
               THETA[i][1]=tem
    for i in range(total_points):
        nP[i][0]=P[int(THETA[i][1])][0]
        nP[i][1]=P[int(THETA[i][1])][1]
    return nP
    
def intersection1(P,pn1,pn2):
    P=list(clk(P))
    P=numpy.ndarray.tolist(P[0])
    m=(pn1[1]-pn2[1])/(pn1[0]-pn2[0])
    c=pn1[1]-m*pn1[0]
    IM=[]
    
    for i in range(len(P)):
        a=(P[i][1]-m*P[i][0]-c)
        if a>0:
            IM.append([1,i])
        elif a<0:
            IM.append([-1,i])
        else:
            IM.append([0,i])
    temp=0
    for i in range(len(IM)-1):
        if IM[i][0]*IM[i+1][0]<=0:
            p1=P[i]
            p2=P[i+1]
            ip=lineint(p1,p2,pn1,pn2)
            if IM[i][0]*IM[i+1][0]==0:
                i=i+1
            break
    for j in range(i+1,len(IM)-1):
        if IM[j][0]*IM[j+1][0]<0:
            p3=P[j]
            p4=P[j+1]
            ip1=lineint(p3,p4,pn1,pn2)
            temp=1
            break
    if not temp==1:
        p3=P[0]
        p4=P[-1]
        ip1=lineint(p3,p4,pn1,pn2)
        
    pp=[]
    np=[]
    for i in range(len(IM)):
        if IM[i][0]>0:
            pp.append(P[i])
        elif IM[i][0]<0:
            np.append(P[i])
            
    pp.append(ip)
    np.append(ip)
    pp.append(ip1)
    np.append(ip1)
    
    if abs(ip[0]-pn1[0])>0.001 or abs(ip[1]-pn1[1])>0.001:
        E=ip
    else:
        E=ip1
    return [[pn1,E],pp,np]

    

def intersection2(P,pn1,pn2):
    IM=[]
    for i in range(len(P)):
        if P[i][0]>pn1[0]:
            IM.append([1,i])
        else:
            IM.append([-1,i])
    temp=0
    for i in range(len(IM)-1):
        if IM[i][0]*IM[i+1][0]<=0:
            p1=P[i]
            p2=P[i+1]
            ip=lineint(p1,p2,pn1,pn2)
            if IM[i][0]*IM[i+1][0]==0:
                i=i+1
            break
    for j in range(i+1,len(IM)-1):
        if IM[j][0]*IM[j+1][0]<0:
            p3=P[j]
            p4=P[j+1]
            ip1=lineint(p3,p4,pn1,pn2)
            temp=1
            break
    if not temp==1:
        p3=P[0]
        p4=P[-1]
        ip1=lineint(p3,p4,pn1,pn2)
        
    pp=[]
    np=[]
    for i in range(len(IM)):
        if IM[i][0]>0:
            pp.append(P[i])
        elif IM[i][0]<0:
            np.append(P[i])
            
    pp.append(ip)
    np.append(ip)
    pp.append(ip1)
    np.append(ip1)
    
    if abs(pn1[0]-ip[0])>0.001 or abs(pn1[1]-ip[1])>0.001:
        E=ip
    else:
        E=ip1
    return [[pn1,E],pp,np]

def intersection(P,pn1,pn2):
    if pn1[0]-pn2[0] is not 0:
        [[pn1,E],pp,np]=intersection1(P,pn1,pn2)
    else:
        [[pn1,E],pp,np]=intersection2(P,pn1,pn2)
    return [[pn1,E],pp,np]
    
def area(P):
    P=clk(P)
    P=numpy.ndarray.tolist(P[0])
    A=[]
    for i in range(len(P)-1):
        A.append(P[i][0]*P[i+1][1]-P[i+1][0]*P[i][1])
    A.append(P[-1][0]*P[0][1]-P[0][0]*P[-1][1])
    
    return abs(0.5*sum(A))
    
def radius(r,p1,p2):
    a1=area(p1)
    a2=area(p2)
    x=a1/(a1+a2)
    k=((1-x)/x)**(1/3)
    r1=r/(1+k**3)**(1/3)
    r2=k*r1
    return [r1,r2]

def com(p):
    p=list(clk(p))
    p=numpy.ndarray.tolist(p[0])
    a=area(p)
    cx=[]
    cy=[]
    for i in range(len(p)-1):
        cx.append((p[i][0]+p[i+1][0])*(-p[i][0]*p[i+1][1]+p[i+1][0]*p[i][1]))
        cy.append((p[i][1]+p[i+1][1])*(-p[i][0]*p[i+1][1]+p[i+1][0]*p[i][1]))
    cx.append((p[len(p)-1][0]+p[0][0])*(-p[len(p)-1][0]*p[0][1]+p[0][0]*p[len(p)-1][1]))
    cy.append((p[len(p)-1][1]+p[0][1])*(-p[len(p)-1][0]*p[0][1]+p[0][0]*p[len(p)-1][1])) 
    cx=sum(cx)
    cy=sum(cy)
    cx=cx/6/a
    cy=cy/6/a
        
        
    return[cx,cy]

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def lineint1(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return [x,y]
    else:
        return False
def lineint(p1,p2,p3,p4):
    L1 = line(p1, p2)
    L2 = line(p3, p4)
    R = lineint1(L1, L2)
    
    return R