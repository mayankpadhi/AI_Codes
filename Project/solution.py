#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the Sokoban warehouse domain.

#   You may add only standard python imports---i.e., ones that are automatically
#   available on TEACH.CS
#   You may not remove any imports.
#   You may not import or otherwise source any of your own files

# import os for time functions
import os
from search import *
from sokoban import SokobanState, Direction, PROBLEMS, sokoban_goal_state

#SOKOBAN HEURISTICS


def heur_displaced(state):
    '''trivial admissible sokoban heuristic'''
    '''INPUT: a sokoban state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''
    count = 0
    for box in state.boxes:
        if box not in state.storage:
            count += 1
    return count


def heur_manhattan_distance(state):
    #IMPLEMENT
    '''admissible sokoban heuristic: manhattan distance'''
    '''INPUT: a sokoban state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''
    #We want an admissible heuristic, which is an optimistic heuristic.
    #It must always underestimate the cost to get from the current state to the goal.
    #The sum Manhattan distance of the boxes to their closest storage spaces is such a heuristic.
    #When calculating distances, assume there are no obstacles on the grid and that several boxes can fit in one storage bin.
    #You should implement this heuristic function exactly, even if it is tempting to improve it.
    #Your function should return a numeric value; this is the estimate of the distance to the goal.
    result_dist = 0
    for box in state.boxes:
        distances = []
        for goal in state.storage:
            if state.restrictions is None or goal in state.restrictions[state.boxes[box]]:
                distances.append(abs(box[0] - goal[0]) + abs(box[1] - goal[1]))
        if distances:
            result_dist += min(distances)
    return result_dist


"""
#up: y - 1, right: x + 1, down: y + 1, left: x - 1
def trapped(x, y, height, width, obstacles, storage):
    corners = ((0, 0), (0, height - 1), (width - 1, 0), (width - 1, height - 1))
    return ((x, y) in corners) or \
           (x == 0 and (x, y) not in storage) or \
           (y == 0 and (x, y) not in storage) or \
           (x == width - 1 and (x, y) not in storage) or \
           (y == height - 1 and (x, y) not in storage)
"""

def fval_function(sN, weight):
    return sN.gval + weight * sN.hval


def weighted_astar(initial_state, heur_fn, weight=1., timebound=10):
    #IMPLEMENT
    '''Provides an implementation of anytime weighted a-star, as described in the HW1 handout'''
    '''INPUT: a sokoban state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False'''
    se = SearchEngine('custom', 'full')
    se.init_search(initial_state, sokoban_goal_state, heur_fn,
                       lambda sN: fval_function(sN, weight))

    solution = None
    costbound = None

    search_start_time = os.times()[0]
    search_stop_time = search_start_time + timebound
    while os.times()[0] <= search_stop_time:
        final_state = se.search(search_stop_time - os.times()[0], costbound)
        if final_state:
            solution = final_state
            # subtract one so search compares >= for costbound, not >
            costbound = (solution.gval - 1, float('inf'), solution.gval - 1)
        else:
            break
    return solution


if __name__ == "__main__":

    solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 8; #8 second time limit
    print("Running Anytime Weighted A-star")


    print("*************************************")
    print("PROBLEM {}".format(0))

    s0 = PROBLEMS[0] #Problems get harder as i gets bigger
    weight = 10
    final = weighted_astar(s0, heur_fn=heur_displaced, weight=weight, timebound=timebound)

    if final:
        final.print_path()
        solved += 1
    else:
        unsolved.append(i)
    counter += 1

    if counter > 0:
        percent = (solved/counter)*100

    print("*************************************")
    print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))
    print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))
    print("*************************************")



