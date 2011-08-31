
Simulating Planetary Orbits
--------------------------------------------------

According to Isaac Newton, the force of gravitational attraction
between two objects is given by:

.. math::

  F = G\frac{m_1m_2}{d^2}

where :math:`G` is the gravitational constant, :math:`m_1` and
:math:`m_2` are the masses of the two objects, and :math:`d` is the
distance between them.  In SI units, :math:`G` has the value
:math:`6.67428 \times 10^{-11} N(m/kg)^2`,
so :math:`d` is measured in meters, the masses are measured in kilograms,
and the resulting :math:`F` is in newtons.

Using this equation, Newton determined a formula for calculating how
long it took an object to complete an orbit around a central mass.
However, when dealing with three or more objects, it's generally not possible
to find a tidy formula to calculate what the three bodies will do.

Instead, such problems are tackled by numeric integration, a
brute-force approach where you take all the object positions and
velocities at time :math:`T`, calculate the forces they exert on each
other, update the velocities, and calculate the new positions at time
:math:`T+\epsilon`.  Then you repeat this in a
loop, stepping forward through time, and output or plot the results.


Approach
========================================

To implement this in Python, we'll use the :mod:`turtle` module to
provide a graphical display, subclassing the :class:`Turtle` class to
create a :class:`Body` class that will have
additional attributes:
:attr:`mass` for the object's mass,
:attr:`vx` and :attr:`vy` for its velocity,
and :attr:`px` and :attr:`py` for its position.

An added method on :class:`Body`, :meth:`attraction`, will
take another :class:`Body` instance
and return the X and Y components of the force exerted
by the other body.


Solution
========================================

.. literalinclude:: /code/gravity.py
   :linenos:


Code Discussion
========================================

The system described in the code consists of the Sun, Earth, and
Venus, so the :func:`main` function creates three :class:`Body`
instances for each body and passed to the :func:`loop` function.

The :func:`loop` function is the heart of the simulation, taking a
list of :class:`Body` instances and then performing simulation steps
forever.  The time step chosen is one day, which works well for our
Sun/Earth/Venus example.  When you run the program, you can see how
long it takes for the plot to complete an entire orbit; for Earth it's
the expected 365 days and for Venus it's 224 days.

Lessons Learned
========================================

Each simulation step requires calculating :math:`N * (N-1)` distances
and attractions, so the time complexity is :math:`O(N^2)`.  On a
laptop or desktop, the display will be visible changing
up to around 20 objects.  More efficient coding would let us
handle more objects; we could rewrite the calculations in C or
parallelize the code to divide the work in each step among multiple
threads or CPUs.  You could also adjust the timestep dynamically: if
objects are far apart, a larger timestep would introduce less error,
and the timestep could be shortened when objects are interacting
more closely.

These techniques would increase our practical limit to hundreds
(:math:`10^3`) or thousands (:math:`10^4`) of objects, but this means
we can't simulate even a small galaxy, which might contain tens of
millions of stars (:math:`10^7`).  (Our galaxy is estimated to have
around 200 billion stars, :math:`2 \times 10^{11}`.)  Entirely
different approaches need to be taken for that problem size; for
example, the attraction of distant particles is approximated and only
nearby particles are calculated exactly.  The references include a
survey by Drs. Trenti and Hut that describes the techniques used for
larger simulations.


References
========================================


http://www.scholarpedia.org/article/N-body_simulations
  This survey, by Dr. Michele Trenti and Dr. Piet Hut, describes
  how the serious scientific N-body simulators work, using trees
  to approximate the attraction at great distances.  Such programs are able
  to run in :math:`O(N log(N))` time.

http://ssd.jpl.nasa.gov/horizons.cgi
  NASA's Jet Propulsion Laboratory provides a system called HORIZONS
  that returns accurate positions and velocities for objects within
  the solar system.  In the example code, the values used are only
  rough approximations; the orbital distances and planet velocities
  are set to the mean distances and their relative positions don't
  correspond to any actual point in time -- but they produce
  reasonable output.
