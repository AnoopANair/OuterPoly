import cv2
import numpy as np
import math

def angle(x1,y1,x2,y2,x3,y3,separation):
    # distance of the outer polygon from the inner polygon
    distance = separation
    # dot and cross products of vector1  with  [1,0]  vector
    dot_value1 = (x1-x2) 
    cross_value1 = (y1-y2)
    # norm of the vector1 and [1,0] vector.
    norm11 = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    norm21 = 1
    # finding the quadrant based on the cross and dot products of vector 1 with [1,0] vector
    if cross_value1 >  0 :
        theta = math.acos(dot_value1/(norm11*norm21))
    elif cross_value1 < 0 :
        theta = - math.acos(dot_value1/(norm11*norm21))
    elif cross_value1 == 0:
      if (x1 - x2)  > 0:
        theta = 0
      if (x1 - x2) < 0:
        theta = math.pi
    # cross and dot products of vector1 and vector2
    dot_value = (x1-x2)*(x3-x2) + (y1-y2)*(y3-y2)
    cross_value = (x1-x2)*(y3-y2) - (y1-y2)*(x3-x2)
    # norm of vector 1 and vector 2
    norm1 = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    norm2 = ((x3-x2)**2 + (y3-y2)**2)**(0.5)


    # finding the external angle based on cross and dot products
    if cross_value >  0 :
        inner_theta = math.acos(dot_value/(norm1*norm2))
    elif cross_value < 0 :
        inner_theta = 2*math.pi - math.acos(dot_value/(norm1*norm2))

    # finding the bisection of the angle between vector1 and vector 2 
    if inner_theta < math.pi : 
      bi_theta = inner_theta/2.0
      x_inner = distance/math.tan(bi_theta)
      y_inner = distance

    elif inner_theta > math.pi : 
      bi_theta = (inner_theta - math.pi)/2.0
      x_inner = - distance*math.tan(bi_theta)
      y_inner = distance

    # coordinate transform to get the x,y positons relative to point 2 based on [1,0] and [0,1] basis
    x_inner_trans = math.cos(theta)*x_inner - math.sin(theta)*y_inner
    y_inner_trans = math.sin(theta)*x_inner + math.cos(theta)*y_inner
    # shifting with respect to point 2
    x_outer = x_inner_trans + x2
    y_outer = y_inner_trans + y2

    return round(x_outer,0),round(y_outer,0)


# function to find the outer cooords
def CoordsOuter(Polygoncoords,separation)

    Polygoncoords = np.array(Polygoncoords)
    Polygoncoords_new = np.vstack((Polygoncoords,Polygoncoords[0],Polygoncoords[1]))

    angle(x1,y1,x2,y2,x3,y3,separation)
    Outercoords = []
    for i in range(len(Polygoncoords[1:])):
            x1,y1 = Polygoncoords_new[i]
            x2,y2 = Polygoncoords_new[i+1]
            x3,y3 = Polygoncoords_new[i+2]
            Outercoord = angle(x1,y1,x2,y2,x3,y3,separation)
            Outercoords.append(Outercoord)

    Outercoords = np.array(Outercoords)
    return Outercoords
