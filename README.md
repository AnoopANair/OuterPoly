# OuterPoly
Python module to find outer polygons of any 2d geometry

There are two methods :

Consider **(x1,y1)**, **(x2,y2)** and **(x3,y3)** as the three points and **outerx2** and **outery2** be the points corresponding to the inner **x2,y2**. Then for a given **separation** the outer coordinates are found.

> outerx2, outery2 = angle(x1,y1,x2,y2,x3,y3,separation)

Given the array of coordinates for the inner polygon **(Polygoncoords)** and a **separation**, the outer polygon coordinates are found (outerarray)

> outerarray = oordsOuter(Polygoncoords,separation)
