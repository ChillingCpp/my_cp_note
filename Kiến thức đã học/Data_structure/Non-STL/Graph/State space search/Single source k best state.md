

- Dựa trên [[Khái niệm]]
- Simple path : Không có trong thi
- Cho phép lặp đỉnh : 
	- Trạng thái của 1 node là ```State```
	- Tập trạng thái của 1 node hiện tại là ```heap<State>```
	- Nhưng ta duy trì ```heap<State>``` để cho việc lan truyền state
	- Duy trì ```vector<heap<State>> state(n)``` để lưu trữ đáp án
	- State được pop ra từ heap là state tối ưu nhất và chỉ được phép sử dụng state đó để lan truyền, không được lan truyền state trong ```heap<State>```
	- Chỉ lan truyền từ u -> v nếu $state[u].size() < k$ 
	- Khi lan truyền thì ta cần 2 điều kiện :
		- gọi $state(u)$ là trạng thái hiện tại của u khi pop ra từ heap
		- gọi $state(u, v)$ là trạng thái chuyển trực tiếp của u -> v ban đầu 
		- nếu $state[v].size() < k$ thì push vào
		- còn nếu $state[v].size() == k \; and \; state[v].top()$ not optimal than $combine(state(u), original(u, v))$
			- thay thế  $state[v].top()$ thành $combine(state(u), original(u, v))$