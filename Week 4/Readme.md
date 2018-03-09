# Problem Statement
Given a set of simple (convex) obstacle polygons in 2D workspace, build a visibility graph and find the shortest path between the initial and final positions of the robot tool R. The tool R should not be rotated while translating it to the goal position.

The obstacle polygons: 
P1: [(1,3);(1,4);(2,5);(3,4);(3,3);(2,2)]
P2: [(4,5);(5,6);(5,4)]
P3: [(3,2);(6,2);(5,1)]

Robot to be moved:
Anchor_init: (0,1)
Anchor_goal: (6,6)
R: [(0,1);(1,2);(1,1)]

Step 1: Write a small routine to create a visibility graph given the polygonal obstacles and shape of the robot.
Step 2: Implement A* to find the shortest path.
