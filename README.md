Random Walk can have several practical uses across different fields, both in research and applied contexts.

This is a Simple Random Walk Program made with matplotlib, there is nothing in special in this specific program whatsoever

* How it works *

A point is generated in the graph at (0,0),
in the code there is the function get_step, where there is the direction and distance variables, the direction variable choose randomly 1 or -1, if it is chosen 1, the next point will be to the right(towards the positive side of the axis), 
if -1, go to the negative direction, the distance variable choose a random number in a custom size list given by the set_distance function that have a minDistance and maxDistance as parameters, so it will choose between a number in range of these values
when you have these two values, it will be multiplied by each other giving a direction to move and how much to, this happens for each axis, for example, starting in (0,0) getting the direction -1 and 5 distance for x-axis, 1 and 2 for y-axis, will get the next 
point to (-5,2), which will be drawn a point to mark the position, the next point will be in reference to the (-5,2) point, moving x and y steps but starting in (-5,2), and so goes on until the total number of points reach the num_points variable in the init function,
which also can be set.

Here is some videos about Random Walk Theory:
https://www.youtube.com/watch?v=zRLhixHmI7Q
https://www.youtube.com/watch?v=stgYW6M5o4k
