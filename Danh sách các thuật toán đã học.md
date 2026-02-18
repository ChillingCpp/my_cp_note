[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)


## 1. Cơ bản
- 2 pointers
- sliding windows
- bit
	- bitwise operation
	- bit contribution
	- bitmask
- binary search
	- binary search on array / set
	- binary search on answer
- Sorting
	- sort element
	- sort by index
- backtracking
- Coordinate compression
- Divide and Conquer
- Meet-in-the-middle
- floyd cycle finding
## 2. Cấu trúc dữ liệu

- stack
	- monotonic stack
		- value contribution
	- normal stack
- queue
- deque
	- monotonic queue : sliding windows min/max
	- normal deque
- set/map
- unordered set/map 
- prefix/suffix array 1d
- prefix sum 2d
- Segment tree ( with and without lazy propagation)
- Sparse table for tree LCA queries
- Disjoint set union for groups
- Neighbor-linked array : a simple DSU without path compression
- matrix 2d/ matric exponent
## 3. Xử lí xâu kí tự
- KMP
- Z
- Rolling hash
- Manacher
- Trie
## 4. Toán học
### 4.1 Lí thuyêt số

- GCD/LCM
- Harmonic number
- binary power
- extended euclid
- Prime number
### 4.2 Xác suất tổ hợp thống kê
- Quy tắc cộng, quy tắc nhân
- Tổ hợp chỉnh hợp hoán vị, hoán vị có lặp
- Xác suất
## 5. Kĩ thuật nâng cao

- Greedy
- Dynamic programming
	- DP 1D
	- DP 2D
	- DP space optimized
	- DP on Tree
	- DP bitmask
	- Classical DP
- Sqrt Decomposition : a set of techniques/thinking reduce time complexity from O($n^2$) to O($n \sqrt n$)
	- often relative to some problem O(n / i) time
- Mo algorithm
## 6. Đồ thị và cây
## 6.1. Đồ thị
- BFS/ DFS
	- Multisource BFS to all destinations
- flood fill
- cycle
	- cycle finding
	- negative weight cycle
	- parity cycle
- Topological sort
- Euler tour/cycle
- Shortest path
	- Dijkstra
		- All pair shortest paths
		- Multisource to all destinations
	- SPFA ( handle negative weight )
	- Floyd warshall ( handle negative weight )
	- Johnson algorithm ( SPFA to get array h and set w(u, v) += h(u) - h(v), based on property that the shortest distance from s to v must be smaller than or equal to the shortest distance from s to u plus the weight of the edge (u, v) )
- Minimum spanning tree
	- Kruskal
	- Prims
- Connected Component
	- Tarjan algorithm
	- Find SCCs
	- Articular point and bridge
	- 2-sat
	- Condensation graph
	- Block cut tree
	- Bridge edge tree
## 6.2. Đồ thị dạng cây

- DP on tree
 - Binary lifting
 - Euler tour
 - Sparse table for LCA and DP on tree
 - LCA and Subtree Queries



