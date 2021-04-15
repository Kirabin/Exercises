# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/solutions/python

class Node:
	def __init__(self):
		self.next = None

# My take not memory efficient
# def loop_size(node):
#     l = []
#     s = set()
#     while 1:
#         l.append(node)
#         s.add(node)
#         node = node.next
        
#         if node in s: 
#             return len(l) - l.index(node)

def loop_size(node): 
	turtle, rabbit = node, node.next

	while turtle != rabbit:
		turtle = turtle.next
		rabbit = rabbit.next.next

	# now turtle and rabbit on the same node if a loop
	# let's find loop size by going through loop one more time
	count = 1 
	rabbit = rabbit.next
	while turtle != rabbit: 
		rabbit = rabbit.next
		count += 1

	return count

# Test 
nodes = [Node() for _ in range(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
assert loop_size(nodes[0]) == 29