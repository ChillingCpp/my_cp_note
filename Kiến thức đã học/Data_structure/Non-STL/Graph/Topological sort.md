

- Bản chất của Topological sort :
	- Mọi thứ tự topo hợp lệ nếu và chỉ nếu với mọi cạnh u -> v thì u đứng trước v
		- Nếu không tồn tại cạnh u -> v thì v có thể đứng trước u trong thứ tự topo
- 2 thuật toán cơ bản :
	- DFS
	- thuật toán Kahn
- nếu như yêu cầu lexicographically order : 
	- sử dụng thuật toán Kahn nhưng thay vì dùng queue thì dùng min-heap