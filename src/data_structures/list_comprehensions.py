#lets build a queue
from collections import deque
queue_list = deque([1, 2, 3, 4, 5])
queue_list.append(6)
queue_list.popleft()

print(queue_list)

#list comprehension
#consists of brackets contaiing an expression followed by a for clause, then zero or more for or if clauses
print([(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x == y])
print([(x, x**2) for x in range(6)])

#tuple
empty = ()
singletup = ('hello',)
print(len(empty))
print(len(singletup))