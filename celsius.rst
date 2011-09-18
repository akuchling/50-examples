
Convert Fahrenheit to Celsius
--------------------------------------------------

We'll begin with a very simple example to illustrate the format used 
for each example.  Each section will start with a discussion of the 
problem being solved, giving its requirements and sometimes a brief
discussion of its history.

Most of the world uses the Celsius scale to indicate temperatures, but
the United States still uses the Fahrenheit scale.  We'll write a
little script that takes Fahrenheit temperatures and prints their
corresponding values in Celsius.  (The author, who's a Canadian living
in the United States, first wrote this script because he could never
remember if 85 degrees Fahrenheit is pleasantly warm or scorchingly
hot while listening to the weather report.)


Approach
========================================

Here we'll discuss the algorithm or approach taken to solving the
problem.

The calculation for the temperature conversion is straightforward and
references can be found all over the place.  Celsius and Fahrenheit
have different zero points -- 0 degrees Celsius is 32 degrees
Fahrenheit -- so we need to subtract 32 from the Fahrenheit
temperature.

The size of the units are also different.  Celsius divides the
temperature span between the freezing and boiling points of water into
100 degrees, while Fahrenheit divides this range into 180 degrees, so
we need to multiply the value by 5/9 to turn 180 degrees into 100.


Solution
========================================

Next we'll present the complete program listing.  The source code for
this book also includes test suites for each program, but the test
suites won't be shown in the book.

.. literalinclude:: /code/to_celsius.py
   :linenos:


Code Discussion
========================================

Explore interesting aspects of the code

Lessons Learned
========================================

Does this program demonstrate any interesting themes 
about programming or about its subject matter?


References
========================================

Relevant web pages, books, with an annotation about why it's notable
or worthwhile.


