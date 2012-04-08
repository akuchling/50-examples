Background: Measuring Complexity
-----------------------------------------

It's obviously most important that an algorithm solves a
given problem correctly.  How much time an algorithm will take to solve
a problem is only slightly less important.  All algorithms must
terminate eventually, because they wouldn't be algorithms if they
didn't, but they might run for billions of years before terminating.
In order to compare algorithms, we need a way to measure the time
required by an algorithm.

To characterize an algorithm, we really need to know how its running
time changes in relation to the size of a problem.  If we solve a
problem that's ten times as large, how does the running time change?
If we run :func:`find_max` on a list that's a thousand elements long
instead of a hundred elements, does it take the same amount of time?
Does it take 10 times as long to run, 100 times, or 5 times?  This is
called the algorithm's *time complexity* or, occasionally, its
*scalability*.

To measure the time complexity, we could simply implement an algorithm
on a computer and time it on problems of different sizes.  For
example, we could run :func:`find_max` on lists from lengths ranging from
1 to 1000 and graph the results.
This is unsatisfactory  for two reasons:

* Computers perform different operations at different speeds:
  addition may be very fast and division very slow.  Different
  computers may have different specialities. One machine may
  have very fast math but slow string operations while another
  might do math very slowly.  Machines also vary in memory size
  and processor, memory, and disk speeds.  Researchers would
  find it difficult to compare results measured on different machines.

* Measuring performance within a given range doesn't
  tell us if the algorithm continues to scale outside of the range.
  Perhaps it runs very well for problem sizes up to 1000,
  but at some larger size it began to run too slowly.

Instead, the measurement is done more abstractly by counting the
number of basic operations required to run the algorithm, after
defining what is counted as an operation.  For example, if you
wanted to measure the time complexity of computing a sine function,
you might assume that only addition, subtraction, multiplication, and
division are basic operations.  On the other hand, if you were
measuring the time to draw a circle, you might include sine as a basic
operation.

Complexity is expressed using *big-O notation*.  The complexity is
written as O(<some function>), meaning that the number of operations
is proportional to the given function multiplied by some constant
factor.  For example, if an algorithm takes 2*(n**2) operations, the
complexity is written as O(n**2), dropping the constant multiplier of 2.

Some of the most commonly seen complexities are:

* O(1) is *constant-time* complexity.  The number of operations
  for the algorithm doesn't actually change as the
  problem size increases.

* O(log n) is *logarithmic* complexity. The base used to take the
  logarithm makes no difference, since it just multiplies the
  operation count by a constant factor.  The most common base is base
  2, written as :math:`log_2` or :math:`lg`.

  Algorithms with logarithmic complexity cope quite well with
  increasingly large problems.  Doubling the problem size
  requires adding a fixed number of new operations, perhaps
  just one or two additional steps.

* O(n) time complexity means that an algorithm is *linear*;
  doubling the problem size also doubles the number of operations required.
* O(n**2) is *quadratic* complexity.  Doubling the problem size
  multiplies the operation count by four.  A problem 10 times
  larger takes 100 times more work.
* O(n**3), O(n**4), O(n**5), etc. are *polynomial* complexity.
* O(2**n) is *exponential* complexity.  Increasing the problem
  size by 1 unit doubles the work.  Doubling the problem size
  squares the work.  The work increases so quickly that only
  the very smallest problem sizes are feasible.

The following graph compares the growth rates of various time
complexities.

.. XXX add graph here

When writing down big-O notation, we can keep only the fastest-growing
term and drop slower-growing terms.  For example, instead of writing
O(n**2 + 10n + 5), we drop the lower terms and write only O(n**2).
The smaller terms don't contribute very much to the growth of the
function as ``n`` increases.  If ``n`` increases by a factor of 100,
the ``n**2`` term increases the work by a factor of 10,000.  The
increase of 1000 operations from the ``10n`` term dwindles to
insignificance.

After correctness, time complexity is usually the most interesting
property of an algorithm, but in certain cases the amount of memory or
storage space required by an algorithm is also of interest.  These
quantities are also expressed using big-O notation.  For example, one
algorithm might have O(n) time and use no extra memory while another
algorithm might take only O(1) time by using O(n) extra storage space.
In this case, the best algorithm to use will vary depending on the
environment where you're going to be running it.  A cellphone has very
little memory, so you might choose the first algorithm in order to use
as little memory as possible, even if it's slower.  Current desktop
computers usually have gigabytes of memory, so you might choose the
second algorithm for greater speed and live with using more memory.

Big-O notation is an upper bound, expressing the worst-case time
required to run an algorithm on various inputs.  Certain inputs,
however, may let the algorithm run more quickly.  For example, an
algorithm to search for a particular item in a list may be lucky and
find a match on the very first item it tries.  The work required in
the best-case speed may therefore be much less than that required in
the worst case.

Another notation is used for the best-case time, *big-omega notation*.
If an algorithm is Omega(<some function>), the best-case time
is proportional to the function multiplied by some constant factor.
For example, the quicksort
algorithm discussed later in this book is Omega(n lg n) and O(n**2).
For most inputs quicksort requires time proportional to ``n lg n``,
but for certain inputs time proportional to ``n**2`` will be
necessary.

*Big-theta notation* combines both upper and lower bounds; if an
algorithm is both O(function) and Omega(function), it is also
Theta(function).  The function is therefore a tight bound on both the
upper and lower limits of the running time.

.. XXX need a way to write Omega symbols (Unicode?)

Usually the worst case is what we're interested in.  It's important
that we know the longest possible time an algorithm might take so that
we can determine if we can solve problems within a reasonable time.
Occasionally encountering a particular input that can be solved more
quickly may be lucky when it happens, but it can't be relied upon, so
the best-case time usually isn't very relevant.  For most of the
algorithms in this book, only the O() bound will discussed.

.. XXX finish writing this

  * Time complexity of various Python built-in operations (dicts, lists)
    * Lists: access O(1), removing from the end/appending O(1),
      inserting at the beginning O(n), searching O(n/2) == O(n)
    * Dicts: access is O(1), keys()/items() O(n),

.. XXX * Time complexity of various Python built-in operations (dicts, lists)


.. Not sure whether to have exercises.

	Exercises
	-----------------------


	* Write down a series of steps for finding a lost item.
	  Is this an algorithm?

	* In the problem statement for :alg:`find_max`, why does it
	  require that all the numbers are positive?
	  Is this condition necessary for the recursive formulation?


References
==================================================

XXX
