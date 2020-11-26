# OuterPoly
Python module to find outer polygons of any 2d geometry

There are two methods :

Consider **(x1,y1)**, **(x2,y2)** and **(x3,y3)** as the three points and **outerx2** and **outery2** be the points corresponding to the inner **x2,y2**. Then for a given **separation** the outer coordinates are found.

> outerx2, outery2 = angle(x1,y1,x2,y2,x3,y3,separation)

Given the array of coordinates for the inner polygon **(Polygoncoords)** and a **separation**, the outer polygon coordinates are found (outerarray)

> outerarray = CoordsOuter(Polygoncoords,separation)

You can install it using :

> pip install OuterPoly

and can be called in your file via:

> import OuterPoly as op

The PyPI repo is found at : https://pypi.org/project/OuterPoly/


You could cite the code using: 

[![DOI](https://zenodo.org/badge/316223024.svg)](https://zenodo.org/badge/latestdoi/316223024)

