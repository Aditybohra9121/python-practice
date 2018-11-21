'''
1 Recursive algorithm must have a base case.
2 Recursive algorithm must change its state and move toward the base case.3 Recursive algorithm must call itself, recursively.

 A base case is typically a problem that is small enough to solve directly. In the listsum algorithm the base case is a list of length 1.
First, a base case is the condition that allows the algorithm to stop recursing. A base case is typically a problem that is small enough to solve directly
To obey the second law, we must arrange for a change of state that moves the algorithm toward the base case. A change of state means that some data that the algorithm is using is modified. Usually the data that represents our problem gets smaller in some way. In the listsum algorithm our primary data structure is a list, so we must focus our state-changing efforts on the list. Since the base case is a list of length 1, a natural progression toward the base case is to shorten the list. 

The final law is that the algorithm must call itself. This is the very definition of recursion. Recursion is a confusing concept to many beginning programmers. As a novice programmer, you have learned that functions are good because you can take a large problem and break it up into smaller problems. The smaller problems can be solved by writing a function to solve each problem. When we talk about recursion it may seem that we are talking ourselves in circles. We have a problem to solve with a function, but that function solves the problem by calling itself! But the logic is not circular at all; the logic of recursion is an elegant expression of solving a problem by breaking it down into a smaller and easier problems.

'''
