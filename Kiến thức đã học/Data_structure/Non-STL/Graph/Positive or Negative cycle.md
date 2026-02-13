

- bài viết này cho negative cycle, positive cycle tương tự chỉ đổi dấu > thành <
- Sử dụng SPFA hoặc floyd warshall
- SPFA
	- nếu relax $cnt[v] > n$ thì ta biết được có 1 hành trình dạng : 1 -> cycle -> v
	- cách tìm negative cycle từ s ->t ( s và t cố định được đề bài cho trước )
		- sau khi relax $cnt[v] > n$ thì sẽ chưa dừng, gán $cycle[v] = true$, cho relax  tới $cnt[v]> n +5$ 
		- việc lan truyền cycle thực hiện ưu tiên trước và không đồng thời với $d[v] > d[u] + w$ 
		- nếu $cycle[t]$ = 1 thi từ s -> t có 1 negative cycle
	- Cách tìm random negative cycle :
		- sử dụng [[Kĩ thuật traceback]] để biết cách làm. thực hiện inline ở SPFA và cho relax tới $cnt[v]> n +5$ để kiếm được cycle