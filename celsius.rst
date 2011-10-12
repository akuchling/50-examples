
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

Here we will dive further into the code, discussing particularly
interesting sections of code, programming techniques, or larger
issues.

The conversion to Celsius done by the :func:`convert_f2c` function is
a straightforward calculation.  An input string is converted to
a floating-point value.  If there's a problem, the resulting :exc:`ValueError`
exception is not handled here but instead is left for the caller to catch.  

Notice that the :func:`main` function tries to print a helpful message 
when no command-line arguments are provided, and it also 
catches the :exc:`ValueError`.  For pedagogical programs like this, I will
try to ensure the error handling is helpful to a user experimenting with 
the script.


Lessons Learned
========================================

Finally, does this program demonstrate any interesting themes 
about Python, about programming in general, or about its subject matter?

For this celsius example, I'll discuss Python's string :meth:`format`
method and the mini-language it uses, since it will be used throughout
our example programs.

The strings used with the :meth:`format` method will
contain a replacement field specification inside curly brackets (``{ }``).
It's possible to leave the specification empty (just ``{}``)
but we can also specify the position and type of the argument to use
and how the resulting value should be rendered.  A few examples::

    '{!r}'.format(v)     # Equivalent to repr(v)
    '{!s}'.format(v)	 # Equivalent to str(v)

    # Explicitly give the position of the argument to use for
    # each field. Results in the string "arg2 arg1"
    '{1} {0}'.format('arg1', 'arg2')  

We can also specify formatting details such as the number of decimal
places, style of numeric display, and left- or right-alignment.  This
comes within the curly brackets and following a ``:`` character.  

We can left-align, right-align, or center a string within 
a desired output width, optionally giving the character to be used 
for padding:
  
    >>> '{0:<15}'.format('left-justify')
    'left-justify   '
    >>> '{0:>15}'.format('right-justify')
    '  right-justify'
    >>> '{0:*^15}'.format('centered')
    '***centered****'

We can output a value in binary, octal, decimal, or hexadecimal::

    >>> '{0:b}'.format(1972)
    '11110110100'
    >>> '{0:o}'.format(1972)
    '3664'
    >>> '{0:d}'.format(1972)
    '1972'
    >>> '{0:x}'.format(1972)
    '7b4'

We can request rounding to a specific number of decimal places, 
exponential notation, or displaying as a percentage::

    >>> '{0:d}'.format(2**32)
    '4294967296'
    >>> '{0:e}'.format(2**32)
    '4.294967e+09'
    >>> '{0:%}'.format( 45 / 70 )
    '64.285714%'
    >>> '{0:.2%}'.format( 45 / 70 )
    '64.29%'
    
The complete syntax for format strings is documented in
the Python Library Reference at 
<http://docs.python.org/library/string.html#format-string-syntax>.


References
========================================

The references in each section will be to 
useful web pages, Wikipedia entries, software libraries,
and books.  Generally each reference is annotated with a short
explanation of what's in it and why it might be of interest, to help
you in deciding which references to pursue.

http://books.google.com/books?id=lnmrSAAACAAJ
  "A Matter of Degrees: What Temperature Reveals About the Past and
  Future of Our Species, Planet and Universe", by Gino Segré, is an
  entertaining tour through science using the concept of temperature
  as the connecting thread, including: biological aspects such as the
  regulation of body temperature and the thermophile species that
  cluster around deep-sea superheated vents; the theoretical arguments
  underlying global warming; the discovery of the laws of
  thermodynamics; low-temperature phenomena such as superconductivity
  and helium's superfluidity; and the temperature of the
  cosmic microwave background.
