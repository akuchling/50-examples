
Background: Algorithms
--------------------------------------------------

An *algorithm* specifies a series of steps that perform a particular
computation or task.  Algorithms were originally born as part of
mathematics -- the word "algorithm" comes from the Arabic writer XXX,
-- but currently the word is strongly associated with computer
science.  Throughout this book we'll examine a number of different
algorithms to perform a variety of tasks.

Algorithms resemble recipes.  Recipes tell you how to accomplish a
task by performing a number of steps.  For example, to bake a cake the
steps are: preheat the oven; mix flour, sugar, and eggs throughly;
pour into a baking pan; and so forth.

However, "algorithm" is a technical term with a more specific meaning
than "recipe", and calling something an algorithm means that the
following properties are all true:

* An algorithm is an unambiguous description that makes clear what has
  to be implemented.  In a recipe, a step such as "Bake until done" is
  ambiguous because it doesn't explain what "done" means.  A more
  explicit description such as "Bake until the cheese begins to
  bubble" is better.  In a computational algorithm, a step such as
  "Choose a large number" is vague: what is large?  1 million,  1
  billion, or 100?  Does the number have to be different each time, or
  can the same number be used on every run?
* An algorithm expects a defined set of inputs. For example, it might
  require two numbers where both numbers are greater than zero.
  Or it might require a word, or a list of zero or more numbers.
* An algorithm produces a defined set of outputs.  It might output
  the larger of the two numbers, an all-uppercase version of a word,
  or a sorted version of the list of numbers.
* An algorithm is guaranteed to terminate and produce a result,
  always stopping after a finite time.  If an algorithm could potentially
  run forever, it wouldn't be very useful because you
  might never get an answer.
* Most algorithms are guaranteed to produce the correct result.  It's
  rarely useful if an algorithm returns the largest number 99% of the time,
  but 1% of the time the algorithm fails and returns the smallest 
  number instead. [#f1]_

* If an algorithm imposes a requirement on its inputs (called a
  *precondition*), that requirement must be met.  For example, 
  a precondition might be that 
  an algorithm will only accept positive numbers as an input.  If
  preconditions aren't
  met, then the algorithm is allowed to fail by producing the wrong
  answer or never terminating.

Studying algorithms is a fundamental part of computer science.
There are several different characteristics of an algorithm 
that are useful to know:

1. Does an algorithm actually exist to perform a given task?
2. If someone proposes an algorithm to solve a task, 
   are we sure that the algorithm works for all possible inputs?
3. How long does the algorithm take to run?  How much memory space does 
   it require?
4. Once we know it's possible to solve a problem with an algorithm,
   a natural question is whether the algorithm is the best possible one. 
   Can the problem be solved more quickly?

Most of these questions will be discussed for the algorithms covered
in this book.


An Example Algorithm
==================================================

Let's look at a very simple algorithm called :func:`find_max`.  

Problem: Given a list of positive numbers, return the largest number
on the list.

Inputs: A list ``L`` of positive numbers.  This list must contain at least one
number.  (Asking for the largest number in a list of no numbers
is not a meaningful question.)

Outputs: A number ``n``, which will be the largest number of the list.

Algorithm:

1. Set ``max`` to 0.
2. For each number ``x`` in the list ``L``, compare it to ``max``.
   If ``x`` is larger, set ``max`` to ``x``.
3. ``max`` is now set to the largest number in the list.

An implementation in Python::

        def find_max (L):
            max = 0
            for x in L:
                if x > max:
                    max = x
            return max


Does this meet the criteria for being an algorithm?

* *Is it unambiguous?*  Yes.  Each step of the algorithm
  consists of primitive operations, 
  and translating each step into Python code is very easy.
* *Does it have defined inputs and outputs?*  Yes.
* *Is it guaranteed to terminate?*   Yes.   The list ``L`` is of finite length,
  so after looking at every element of the list the algorithm will 
  stop.
* *Does it produce the correct result?*  Yes.  In a formal setting you would
  provide a careful proof of correctness.  In the next section I'll sketch a 
  proof for an alternative solution to this problem.


A Recursive Version of :func:`find_max`
==================================================

There can be many different algorithms for solving the same problem.
Here's an alternative algorithm for :func:`find_max`:

1. If ``L`` is of length 1, return the first item of ``L``.
2. Set ``v1`` to the first item of ``L``.
3. Set ``v2`` to the output of performing :func:`find_max` on the rest of ``L``.
4. If ``v1`` is larger than ``v2``, return ``v1``.  
   Otherwise, return ``v2``.

Implementation::

        def find_max (L):
            if len(L) == 1:
                return L[0]
            v1 = L[0]
            v2 = find_max(L[1:])
            if v1 > v2: 
                return v1
            else:
                return v2

.. XXX explain recursion more?

Let's ask our questions again.

* *Is it unambiguous?*  Yes.  Each step is simple and easily translated into 
  Python.
* *Does it have defined inputs and outputs?*  Yes.
* *Is it guaranteed to terminate?*   Yes.   The algorithm obviously
  terminates
  if ``L`` is of length 1.  If ``L`` has more than one element,
  :func:`find_max` is called with a list that's one element shorter and the result
  is used in a computation. 

  Does the nested call to :func:`find_max` always terminate?  Yes.  Each time,
  :func:`find_max` is called with a list that's shorter by one element,
  so eventually the list will be of length 1 and the nested calls will end.

Finally, *does it produce the correct result?* Yes.  Here's a sketch
of a proof. [#f2]_

Consider a list of length 1.  In this case the largest number is also
the only number on the list.  :func:`find_max` returns this number, so
it's correct for lists of length 1.

Now consider a longer list of length ``N+1``, where ``N`` is some
arbitrary length.  Let's assume that we've
proven that :func:`find_max` is correct for all lists of length ``N``.
The value of ``v2`` will therefore be the largest value in the rest of
the list.   There are two cases to worry about.

* Case 1: ``v1``, the first item of the list, is the largest
  item.  In that case, there are no other values in the list
  greater than ``v1``.  We're assuming :func:`find_max` is
  correct when executed on the rest of the list, so the value
  it returns will be less than ``v1``.  The ``if v1 > v2``
  comparison will therefore be true, so the first branch will
  be taken, returning ``v1``.  This is the largest item in the list,
  so in this case the algorithm is correct.

* Case 2: ``v1``, the first item of the list, is *not* the
  largest item.  In that case, there is at least one value in
  the list that's greater than ``v1``.  :func:`find_max` is
  correct for the shortened version of the rest of the list,
  returning the maximum value it contains, so this value must
  be greater than ``v1``.  The ``if v1 > v2`` comparison will
  therefore be false, so the ``else`` branch will be taken,
  returning ``v2``, the largest value in the rest of the list.
  This case assumes that ``v1`` is not the largest value, so
  ``v2`` is therefore the largest value, and the algorithm is
  also correct in this case.

With these two cases, we've now shown that if :func:`find_max` is correct
for lists of length ``N``, it's also correct for lists of length
``N+1``.  In the first part of our argument, we've shown that
:func:`find_max` is correct for lists of length 1.  Therefore, it's also
correct for lists that are 2 elements long, and 3 elements, and 4, 5,
6, ... up to any number.

This may seem like a trick; we showed that it's correct for the
trivial case of the single-element list, and then showed that it's
correct on a problem of a certain size.  Such proofs are called
*inductive proofs*, and they're a well-known mathematical technique
for proving a theorem.

Carrying out an inductive proof of some property requires two steps.

1. First, you show that the property is true for some simple
   case: an empty list or a list of length 1, an empty set, a single
   point.  Usually this demonstration is very simple; often it's
   obviously true that the property is true.  This is called the 
   *basis case*.

2. Next, you assume the property is true for size N and show that it's
   true for some larger size such as N+1.  This is called the
   *inductive step*, and is usually the more difficult one.

Once you have both demonstrations, you've proven the property is true
for an infinite number of values of N; correctness for N=1 implies
that the N=2 case is also correct, which in turn implies correctness
for N=3, 4, 5, and every other positive integer.  Not every theorem
can be put into a form where an inductive proof can be used.
        
.. XXX factoid: for a sorted list, the algorithm is really easy: return
   L[0]. Is this worth mentioning?


References
==================================================

XXX something on induction

.. rubric:: Footnotes

.. [#f1] There are special situations where algorithms
   that are sometimes wrong can still be useful.  A good example is
   testing whether a number is prime.  There's an algorithm 
   called the Rabin-Miller test that's always correct
   when it reports a number is composite, but has a 25% chance of being 
   wrong when it reports a number is prime.  One test therefore 
   isn't enough to conclude you've found a prime,
   but you can perform repeated tests 
   and reduce the chance of being wrong to as low as you like (but never zero).

.. [#f2] It's possible to write formal proofs of
   correctness for an algorithm, but the resulting proofs are lengthy
   even for short algorithms such as this one.


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

* O(log n) is *logarithmic* complexity.:footnote:`The base used
  to take the logarithm makes no difference, since it just 
  multiplies the operation count by a constant factor.  
  The most common base is base 2, written as log2 or lg.`

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


