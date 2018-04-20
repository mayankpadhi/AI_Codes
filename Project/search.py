import heapq
from collections import deque
import os

class StateSpace:
    n = 0
    
    def __init__(self, action, gval, parent):
        self.action = action
        self.gval = gval
        self.parent = parent
        self.index = StateSpace.n
        StateSpace.n = StateSpace.n + 1

    def print_path(self):
        s = self
        states = []
        while s:
            states.append(s)
            s = s.parent
        states.pop().print_state()
        while states:
            print(" ==> ", end="")
            states.pop().print_state()
        print("")
 
    def has_path_cycle(self):
        '''Returns true if self is equal to a prior state on its path'''
        s = self.parent
        hc = self.hashable_state()
        while s:
            if s.hashable_state() == hc:
                return True
            s = s.parent
        return False

_BEST_FIRST = 2
_ASTAR = 3
_CUSTOM = 5

_SUM_HG = 0
_H = 1
_G = 2
_C = 3

_CC_NONE = 0
_CC_PATH = 1
_CC_FULL = 2

def _zero_hfn(state):
    return 0

def _fval_function(state):
  return state.hval 

class sNode:
    n = 0
    lt_type = _SUM_HG
    
    def __init__(self, state, hval, fval_function):
        self.state = state
        self.hval = hval
        self.gval = state.gval
        self.index = sNode.n
        self.fval_function = fval_function
        sNode.n = sNode.n + 1

    def __lt__(self, other):
                
        if sNode.lt_type == _SUM_HG:
            if (self.gval+self.hval) == (other.gval+other.hval):
                #break ties by greatest gval. 
                return self.gval > other.gval
            else: return ((self.gval+self.hval) < (other.gval+other.hval))
        if sNode.lt_type == _G:
            return self.gval < other.gval
        if sNode.lt_type == _H:
            return self.hval < other.hval    
        if sNode.lt_type == _C:  
            return self.fval_function(self) <  other.fval_function(other)          
        
        print('sNode class has invalid comparator setting!')
               return self.gval < other.gval

class Open:
    
    def __init__(self, search_strategy):
        if search_strategy == _BEST_FIRST:
            self.open = []
            sNode.lt_type = _H
            self.insert = lambda node: heapq.heappush(self.open, node)
            self.extract = lambda: heapq.heappop(self.open)
        elif search_strategy == _ASTAR:
            self.open = []
            sNode.lt_type = _SUM_HG
            self.insert = lambda node: heapq.heappush(self.open, node)
            self.extract = lambda: heapq.heappop(self.open) 
        elif search_strategy == _CUSTOM:
            #use priority queue for OPEN (first out is node with lowest fval)
            self.open = []
            sNode.lt_type = _C
            self.insert = lambda node: heapq.heappush(self.open, node)
            self.extract = lambda: heapq.heappop(self.open)          

    def empty(self): return not self.open


class SearchEngine:
    def __init__(self, strategy = 'depth_first', cc_level = 'default'):
        self.set_strategy(strategy, cc_level)
        self.trace = 0

    def initStats(self):
        sNode.n = 0
        StateSpace.n = 1    #initial state already generated on call so search
        self.cycle_check_pruned = 0
        self.cost_bound_pruned = 0

    def trace_on(self, level = 1):
        '''For debugging, set tracking level 1 or 2'''
        self.trace = level

    def trace_off(self):
        '''Turn off tracing'''
        self.trace = 0

    def set_strategy(self, s, cc = 'default'):
        if not s in ['depth_first', 'breadth_first', 'ucs', 'best_first', 'astar', 'custom']:
            print('Unknown search strategy specified:', s)
            print("Must be one of 'depth_first', 'ucs', 'breadth_first', 'best_first', 'custom' or 'astar'")
        elif not cc in ['default', 'none', 'path', 'full']:
            print('Unknown cycle check level', cc)
            print( "Must be one of ['default', 'none', 'path', 'full']")

        else:
            if cc == 'default' :
                if s == 'depth_first' :
                    self.cycle_check = _CC_PATH
                else:
                    self.cycle_check = _CC_FULL
            elif cc == 'none': self.cycle_check = _CC_NONE
            elif cc == 'path': self.cycle_check = _CC_PATH
            elif cc == 'full': self.cycle_check = _CC_FULL

            if  s == 'best_first'   : self.strategy = _BEST_FIRST
            elif s == 'astar'        : self.strategy = _ASTAR       
            elif s == 'custom' : self.strategy = _CUSTOM             

    def get_strategy(self):
        if   self.strategy == _BEST_FIRST     : rval = 'best_first' 
        elif self.strategy == _ASTAR          : rval = 'astar'      
        elif self.strategy == _CUSTOM          : rval = 'custom'   
  
        rval = rval + ' with '

        if   self.cycle_check == _CC_NONE : rval = rval + 'no cycle checking'
        elif self.cycle_check == _CC_PATH : rval = rval + 'path checking'
        elif self.cycle_check == _CC_FULL : rval = rval + 'full cycle checking'

        return rval

    def init_search(self, initState, goal_fn, heur_fn=_zero_hfn, fval_function=_fval_function):
        self.initStats()

        if self.trace:
            print("   TRACE: Search Strategy: ", self.get_strategy())
            print("   TRACE: Initial State:", end="")
            initState.print_state()
        self.open = Open(self.strategy)

        node = sNode(initState, heur_fn(initState), fval_function)      

        if self.cycle_check == _CC_FULL:
            self.cc_dictionary = dict() 
            self.cc_dictionary[initState.hashable_state()] = initState.gval
        
        self.open.insert(node)
        self.fval_function = fval_function
        self.goal_fn = goal_fn
        self.heur_fn = heur_fn

    def search(self, timebound=10, costbound=None):
        goal_node = []

        self.search_start_time = os.times()[0]
        self.search_stop_time = None
        if timebound:
            self.search_stop_time = self.search_start_time + timebound
        goal_node = self._searchOpen(self.goal_fn, self.heur_fn, self.fval_function, costbound)

        if goal_node:
            total_search_time = os.times()[0] - self.search_start_time
            print("Solution Found with cost of {} in search time of {} sec".format(goal_node.gval, total_search_time))
            print("Nodes expanded = {}, states generated = {}, states cycle check pruned = {}, states cost bound pruned = {}".format(
                sNode.n, StateSpace.n, self.cycle_check_pruned, self.cost_bound_pruned))
            return goal_node.state
        else:
            #exited the while without finding goal---search failed
            total_search_time = os.times()[0] - self.search_start_time            
            print("Search Failed! No solution found.")
            print("Nodes expanded = {}, states generated = {}, states cycle check pruned = {}, states cost bound pruned = {}".format(
                sNode.n, StateSpace.n, self.cycle_check_pruned, self.cost_bound_pruned))
            return False

    def _searchOpen(self, goal_fn, heur_fn, fval_function, costbound):
        if self.trace:
            print("   TRACE: Initial OPEN: ", self.open.print_open())
            if self.cycle_check == _CC_FULL:
                print("   TRACE: Initial CC_Dict:", self.cc_dictionary)
        while not self.open.empty():
            node = self.open.extract()

            if self.trace:
                print("   TRACE: Next State to expand: <S{}:{}:{}, g={}, h={}, f=g+h={}>".format(
                    node.state.index, node.state.action, node.state.hashable_state(), node.gval, node.hval, node.gval + node.hval))
                if node.state.gval != node.gval:
                    print("ERROR: Node gval not equal to state gval!")
                        
            if goal_fn(node.state):
              return node

            if self.search_stop_time: #timebound check
              if os.times()[0] > self.search_stop_time:                
                print("TRACE: Search has exceeeded the time bound provided.")
                return False

            successors = node.state.successors()

            for succ in successors:
                hash_state = succ.hashable_state()
                if self.trace > 1: 
                  if self.cycle_check == _CC_FULL and hash_state in self.cc_dictionary:
                      print("   TRACE: Already in CC_dict, CC_dict gval={}, successor state gval={}".format(
                        self.cc_dictionary[hash_state], succ.gval))   

                if self.trace > 1:
                    print("   TRACE: Successor State:", end="")
                    succ.print_state()
                    print("   TRACE: Heuristic Value:", heur_fn(succ))

                    if self.cycle_check == _CC_FULL and hash_state in self.cc_dictionary:
                        print("   TRACE: Already in CC_dict, CC_dict gval={}, successor state gval={}".format(
                            self.cc_dictionary[hash_state], succ.gval))

                    if self.cycle_check == _CC_PATH and succ.has_path_cycle():
                        print("   TRACE: On cyclic path")

                prune_succ = (self.cycle_check == _CC_FULL and
                              hash_state in self.cc_dictionary and
                              succ.gval > self.cc_dictionary[hash_state]
                             ) or (
                              self.cycle_check == _CC_PATH and
                              succ.has_path_cycle()
                             )

                if prune_succ :
                    self.cycle_check_pruned = self.cycle_check_pruned + 1
                    if self.trace > 1:
                        print(" TRACE: Successor State pruned by cycle checking")
                        print("\n")                        
                    continue

                succ_hval = heur_fn(succ)
                if costbound is not None and (succ.gval > costbound[0] or
                                              succ_hval > costbound[1] or
                                              succ.gval + succ_hval > costbound[2]) : 
                    self.cost_bound_pruned = self.cost_bound_pruned + 1
                    if self.trace > 1:
                      print(" TRACE: Successor State pruned, over current cost bound of {}", costbound)
                      print("\n") 
                    continue                    

                self.open.insert(sNode(succ, succ_hval, node.fval_function))

                if self.trace > 1:
                    print(" TRACE: Successor State added to OPEN")
                    print("\n")

                if self.cycle_check == _CC_FULL:
                    self.cc_dictionary[hash_state] = succ.gval

        return False

