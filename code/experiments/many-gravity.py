
# Experiment to see how many objects the simulator can handle
# with reasonable speed.

import gravity

L = []
for i in range(20):
   b = gravity.Body()
   b.name = str(i)
   b.mass = 10**26
   b.px = gravity.AU * (i/25)
   b.vy = ((i % 10) - 5) * 2000
   b.vx = ((i % 4) - 2) * 500
   L.append(b)

gravity.loop(L)
