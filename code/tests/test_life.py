#!/usr/bin/env python3

import unittest
import life

class TestLife(unittest.TestCase):
    def setUp(self):
        self.board = life.LifeBoard(10, 10)

    def test_overcrowding(self):
        "Live cell with four neighbors dies."
        # Set up a live cell with four neighbors.
        for (x,y) in [
            (5,5),  # Center cell,
            (4,4),
            (4,6),
            (6,4),
            (6,6),
            ]:
            self.board.set(x,y)

        self.board.step()
        self.assertNotIn((5,5), self.board.state)

    def test_survival_2(self):
        "Live cell with 2 neighbors survives."
        for (x,y) in [
            (5,5),  # Center cell,
            (4,4),
            (6,6),
            ]:
            self.board.set(x,y)

        self.board.step()
        self.assertIn((5,5), self.board.state)

    def test_survival_3(self):
        "Live cell with 3 neighbors survives."
        for (x,y) in [
            (5,5),  # Center cell,
            (4,4),
            (6,6),
            (4,5),
            ]:
            self.board.set(x,y)

        self.board.step()
        self.assertIn((5,5), self.board.state)

    def test_loneliness(self):
        "Live cell with 1 neighbor dies."
        for (x,y) in [
            (5,5),  # Center cell,
            (4,4),
            ]:
            self.board.set(x,y)

        self.board.step()
        self.assertNotIn((5,5), self.board.state)

    def test_birth(self):
        "Empty cell with three neighbors becomes alive"

        # Set up an empty cell with three neighbors.
        for (x,y) in [
            (4,6),
            (6,4),
            (6,6),
            ]:
            self.board.set(x,y)

        self.board.step()
        self.assertIn((5,5), self.board.state)

    def test_inactive(self):
        "Empty cell with two neighbors remains dead"
        for (x,y) in [
            (4,6),
            (6,4),
            ]:
            self.board.set(x,y)

        self.board.step()
        self.assertNotIn((5,5), self.board.state)

    def test_blinker(self):
        "A blinker oscillates correctly"
        # Set up a blinker.
        self.board.set(4, 5)
        self.board.set(5, 5)
        self.board.set(6, 5)

        # Step forward one generation
        self.board.step()

        # Verify that the center cell is still alive.
        self.assertIn((5,5), self.board.state)

        # Verify that the end-point cells are now dead.
        self.assertNotIn((4,5), self.board.state)
        self.assertNotIn((6,5), self.board.state)

        # Verify that two new cells are now live.
        self.assertIn((5,4), self.board.state)
        self.assertIn((5,6), self.board.state)


        
if __name__ == '__main__':
    unittest.main()
