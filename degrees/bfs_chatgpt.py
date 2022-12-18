from collections import deque

def breadth_first_search(root):
  # Create a queue to hold the nodes at each depth level
  queue = deque([root])
  
  # Create a set to keep track of visited nodes
  visited = set()
  
  # While there are nodes in the queue
  while queue:
    # Get the next node in the queue
    node = queue.popleft()
    
    # If the node has not been visited yet
    if node not in visited:
      # Mark the node as visited
      visited.add(node)
      
      # Add the node's children to the queue
      for child in node.children:
        queue.append(child)
        
  # Return the set of visited nodes
  return visited
