from mazelib import Maze
from mazelib.generate.Prims import Prims

m = Maze()
m.generator = Prims(27, 34)
m.generator.generate()
from mazelib.solve.BacktrackingSolver import BacktrackingSolver
m.solver = BacktrackingSolver()
m.generate_entrances()
m.solve()