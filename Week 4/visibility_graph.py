import pyvisgraph as vg
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from shapely.geometry import Polygon as Polygon
from math import pi, sqrt, atan, acos
from pyvisgraph.graph import Point
from pyvisgraph import graph

P1 = [vg.Point(0.5,2.5), vg.Point(0.5,4.5), vg.Point(1.5,5.5),vg.Point(1.5,1.5),vg.Point(2.5,5.5),vg.Point(3.5,4.5),vg.Point(3.5,3.5)]
P2 = [vg.Point(3.5,4.5),vg.Point(3.5,5.5),vg.Point(5.5,6.5),vg.Point(5.5,4.5),vg.Point(4.5,3.5),vg.Point(4.5,6.5)]
P3 = [vg.Point(2.5,1.5),vg.Point(2.5,2.5),vg.Point(4.5,0.5),vg.Point(6.5,2.5)]

polys = [ P1 , P2 , P3 ]

# gets the visibilty graph
g = vg.VisGraph()
g.build(polys)
s1=[]
shortest ,s  = g.shortest_path(vg.Point(0,1), vg.Point(6, 6))
#print(s)
# s is the visibility graph
#y = gets all visible edges in the graph
y = s.get_edges()
for i in y :
    s1.append(i.get_me_edge())
#print(s1)
    #s1 contains all edges in format [(0.5, 2.5),(0.5, 4.5)]

print("SHORTEST PATH")
print(shortest)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,8)
ax.set_ylim(0,8)

#polygon 1 with cyan colour
verts = [
    (0.5, 2.5),
    (0.5, 4.5),
    (1.5, 5.5),
    (2.5, 5.5),
    (3.5,4.5),
    (3.5,3.5),
    (1.5,1.5),
    (0.5,2.5)
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

patch = patches.PathPatch(path, facecolor='cyan', lw=1)
ax.add_patch(patch)
#polygon 2 with cyan colour
verts = [
    (3.5, 4.5),
    (3.5,5.5),
    (4.5, 6.5),
    (5.5,6.5),
    (5.5, 4.5),
    (4.5, 3.5),
    (3.5,4.5)
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

patch = patches.PathPatch(path, facecolor='cyan', lw=1)
ax.add_patch(patch)
#polygon 3 with cyan colour
verts = [
    (2.5, 1.5),
    (2.5,2.5),
    (6.5, 2.5),
    (4.5,0.5),
    (2.5,1.5)
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

patch = patches.PathPatch(path, facecolor='cyan',lw=1)
ax.add_patch(patch)
#adds all the edges in the graph with red colour

codes = [Path.MOVETO,
         Path.LINETO
         ]
for i1 in s1:
    #print("hi")
    #print(i1)

    path = Path(i1, codes)

    patch = patches.PathPatch(path, facecolor='white',color='red' , lw=4)
    ax.add_patch(patch)



plt.show()



