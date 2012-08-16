Background: Algorithms
--------------------------------------------------

An *algorithm* specifies a series of steps that perform a particular
computation or task.  Algorithms were originally born as part of
mathematics -- the word "algorithm" comes from the Arabic writer 
Muḥammad ibn Mūsā al-Khwārizmī, -- but currently the word is strongly 
associated with computer science.  Throughout this book we'll examine 
a number of different algorithms to perform a variety of tasks.

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
