
Simulating Planetary Orbits
--------------------------------------------------

According to Isaac Newton, the force of gravitational attraction 
between two objects is given by:

.. math::

  F = G\frac{m_1m_2}/d^2

where :math:`G` is the gravitational constant, :math:`m_1` and
:math:`m_2` are the masses of the two objects, and :math:`d` is the
distance between them.  In SI units, :math:`G` has the value
:math:`6.67428 x 10^{-11} N(m/kg)^2`,
so :math:`d` is measured in meters, the masses are measured in kilograms,
and the resulting :math:`F` is in newtons.

Using this equation, Newton determined a formula for calculating how
long it took an object to complete an orbit around a central mass.
However, when dealing with three or more objects, it's generally not possible
to find a tidy formula to calculate what the three bodies will do.

Instead, such problems are tackled by numeric integration, a
brute-force approach where you take all the object positions and
velocities, at time :math:`T`, calculate the forces they exert on each
other, update the velocities and calculate the new positions at time
:math:`T+\epsilon`, a short interval later.  Then you repeat this in a
loop, stepping forward through time, and output or plot the results.


Approach
========================================

To implement this in Python, we'll use the :mod:`turtle` module to
provide a graphical display, subclassing the :class:`Turtle` class to
create a 

Discuss the general idea underlying the solution.


Solution
========================================

.. literalinclude:: /code/gravity.py
   :linenos:


Code Discussion
========================================


Lessons Learned
========================================


References
========================================

