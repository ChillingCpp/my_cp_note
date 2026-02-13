

- State Space Search là thuật toán tham lam trên đồ thị sử dụng thuật toán Djikstra/BFS, lan truyền như DP nhưng chỉ lấy tốt nhất và không brute force
- Cách hoạt động : 
	- Mỗi Node chứa trạng thái $(u, state1, state2,...)$ với các rằng buộc khác nhau và trạng thái đó phải lan truyền được
	- Duy trì ```vector<Node> state(n)``` 
	- Cách lan truyền : 
		- gọi $state[u]$ là trạng thái tốt nhất của u
		- gọi $state(u, v)$ là trạng thái chuyển trực tiếp của u -> v ban đầu 
		- if $state[v]$ not optimal than  $combine(state(u), original(u, v))$ then 
			- $state[v]$ =  $combine(state(u), original(u, v))$
- Sử dụng khi :
	- Đề cho rằng buộc và yêu cầu phải có đường đi tốt ưu nhất, hoặc k đường đi tối ưu nhất cho phép lặp đỉnh