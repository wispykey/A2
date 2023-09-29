"""
The main search program
"""
class Search():
    def __init__(self):
        pass

    def search(self, node, goal_fn, select_fn):
        frontier = [[node]]
        print("Expanding...")
        while frontier:
            path = select_fn(frontier)
            n_k = path[-1]
            print(n_k.value,end="")
            if goal_fn(n_k):
                self.print_solution(path)
                return path
            for arc in n_k.neighbors:
                new_path = path[:]
                new_path.append(arc.node)
                frontier.append(new_path)
        print("\nNo solution found.")
        return None
    
    def print_solution(self, path):
        print("\nSolution found!")
        print("Path: ", end="")
        for path_node in path:
            print(path_node.value, end="")
        print("")

    def ids_wrapper(self, node, max_depth, goal_fn):
        depth = 1
        def select_last_in_at_depth(frontier):
            next_path = frontier.pop()
            while len(next_path) > depth and len(frontier) > 0:
                next_path = frontier.pop()
            if (len(next_path) <= depth):
                return next_path
            else:
                return [Node("", 0, [])]
        while depth <= max_depth:
            print("\nDepth:" + str(depth))
            if (self.search(node, goal_fn, select_last_in_at_depth)):
                return
            else:
                depth += 1
            
"""
Functions passed into select_fn pointer
"""
def select_last_in(frontier):
    return frontier.pop()   

def select_first_in(frontier):
    return frontier.pop(0)


"""
Functions passed into goal_fn pointer
"""
def is_value_Z(node):
    return node.value == "Z"

def is_value_X(node):
    return node.value == "X"

"""
Hard-coded representation of Q1 graph
"""
class Node():
    def __init__(self, value, heuristic, neighbors):
        self.value = value
        self.heuristic = heuristic
        self.neighbors = neighbors

class Arc():
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
        
nodeZ = Node("Z", 0.0, [])
nodeH = Node("H", 6.0, [Arc(nodeZ, 6.0)])
nodeG = Node("G", 4.0, [Arc(nodeZ, 9.0)])
nodeF = Node("F", 12.0, [Arc(nodeG, 8.0), Arc(nodeH, 7.0), Arc(nodeZ, 18.0)])
nodeE = Node("E", 11.0, [Arc(nodeF, 7.0)])
nodeD = Node("D", 9.0, [Arc(nodeF, 5.0)])
nodeC = Node("C", 19.0, [Arc(nodeD, 5.0), Arc(nodeE, 4.0), Arc(nodeF, 8.0)])
nodeB = Node("B", 19.0, [Arc(nodeC, 13.0)])
nodeA = Node("A", 21.0, [Arc(nodeC, 2.0)])
nodeS = Node("S", 24.0, [Arc(nodeA, 3.0), Arc(nodeB, 9.0), Arc(nodeC, 4.0)])

"""
Calls to search function
"""
search = Search()

# DFS 
search.search(nodeS, is_value_Z, select_last_in)
search.search(nodeS, is_value_X, select_last_in)

# BFS
search.search(nodeS, is_value_Z, select_first_in)
search.search(nodeS, is_value_X, select_first_in)

# IDS
search.ids_wrapper(nodeS, 4, is_value_Z)
search.ids_wrapper(nodeS, 4, is_value_X)