# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List
# import util
# from collections import Stack
from util import*


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) :
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) :
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
   
    fringe = Stack()
    current_state = problem.getStartState()
    current_path = []
    fringe.push( (current_state,current_path) )
    visited = set()
    while not fringe.isEmpty():
        current_state, current_path = fringe.pop() 
        if problem.isGoalState(current_state):
            return current_path
        
        visited.add(current_state)
        successors = problem.getSuccessors(current_state)
        for node in successors:
            if node[0] not in visited:
                fringe.push( (node[0],current_path + [node[1]]) )
    return []  

    

def breadthFirstSearch(problem: SearchProblem) :
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = Queue()
    current_state = problem.getStartState()
    current_path = []
    fringe.push( (current_state,current_path) )
    visited = set()
    while not fringe.isEmpty():
        current_state, current_path = fringe.pop()
        if problem.isGoalState(current_state):
            return current_path
        visited.add(current_state)
        successors = problem.getSuccessors(current_state)
        for node,direction,cost in successors:
            if(node not in visited):
               # visited.add(node)
                if node not in (s[0] for s in fringe.list):
                    fringe.push( (node, current_path + [direction]) )
    return []
    # util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) :
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    fringe = PriorityQueue()
    current_state = problem.getStartState()
    current_path = []
    fringe.push( (current_state,current_path), 0 )
    visited = set()
    while not fringe.isEmpty():
        current_state, current_path  = fringe.pop()
        if current_state in visited :
            continue
        if problem.isGoalState(current_state):
            return current_path
        visited.add(current_state)
        successors = problem.getSuccessors(current_state)
        for node,direction,c in successors:
            c_path = current_path + [direction]
            cost = problem.getCostOfActions(c_path)
            if node not in visited:
                fringe.push((node,c_path),cost)
    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) :
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    fringe = PriorityQueue()
    current_state = problem.getStartState()
    current_path = []
    fringe.push( (current_state,current_path), 0 )
    visited = {}
    while not fringe.isEmpty():
        current_state, current_path  = fringe.pop()
        if current_state in visited and visited[current_state]<=problem.getCostOfActions(current_path):
            continue
        if problem.isGoalState(current_state):
            return current_path
        visited[current_state] = problem.getCostOfActions(current_path)
        successors = problem.getSuccessors(current_state)
        for node,direction,c in successors:
            c_path = current_path + [direction]
            cost = problem.getCostOfActions(c_path) + heuristic(node,problem)
            # if node not in visited:
            fringe.push((node,c_path),cost)
    return []
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
