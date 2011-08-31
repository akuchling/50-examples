
Problem: Drawing Graphics
--------------------------------------------------

Throughout the rest of this book, we'll need to display graphical
output.  There are many different graphical toolkits available for
Python; the :ref:`turtle-references` section lists some of them.  
For this book I chose one of the simplest: the :mod:`turtle` module.

My reasons for selecting it are:

* :mod:`turtle` is included in the binary installers downloadable from 
  python.org.

* :mod:`turtle` can be used for drawing with Cartesian coordinates
  by calling the :meth:`setposition` method, but the turtle primitives
  are also useful for constructing interesting examples.  Most toolkits
  only support Cartesian plotting.

Unfortunately the module doesn't support printed output,
but I think that isn't much of a disadvantage because interactive
graphics are more interesting.


Approach
========================================

The :mod:`turtle` module:

* display a canvas on which turtles run around.
* turtles have various methods: (pick a fixed subset)
* forward/backward/right/left/speed
* position()/ycor/xcord/heading
* pen/penup/pendown
* hideturtle/showturtle
* home/setpos/setheading
* dot/stamp/clearstamp/reset

XXX write a reference card of methods


Solution
========================================

Large example: 
* draw a border around the canvas
* draw a set of nested squares, varying the color
* draw a sine curve

Code Discussion
========================================


.. _turtle-references:

References
========================================

http://cairographics.org/
  Cairo is a 2D graphics library with a Python API that supports both
  screen and printed output.

"Turtle Geometry: The Computer as a Medium for Exploring Mathematics"
  By Harold Abelson and Andrea diSessa.
  A 1981 textbook that begins with polygons and ends with the
  curved spacetime of general relativity, using turtle graphics
  both to draw illustrative examples and as a conceptual model.
  ISBN 978-0-262-01063-4 (ISBN 978-0-262-51037-0 for the paperback).

  
