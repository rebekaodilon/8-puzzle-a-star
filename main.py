from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from RBFS_search import recursive_best_first_search
from puzzle import Puzzle


state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5]]

for i in range(0,3):
    Puzzle.num_of_instances=0
    
    Puzzle.num_of_instances = 0
    t0 = time()
    astar = Astar_search(state[i])
    t1 = time() - t0
    print('A*:',astar)
    print('movimentos:', Puzzle.num_of_instances)
    print('tempo de execuçao:', t1)
    print()


    print('------------------------------------------')