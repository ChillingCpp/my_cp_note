

- bài viết này cho negative cycle, positive cycle tương tự chỉ đổi dấu > thành <
- Sử dụng SPFA hoặc floyd warshall
- SPFA
	- nếu relax $cnt[v] > n$ thì ta biết được có 1 hành trình dạng : 1 -> cycle -> v
	- cách tìm negative cycle từ s ->t ( s và t cố định được đề bài cho trước )
		- sau khi relax $cnt[v] > n$ thì sẽ chưa dừng, gán $cycle[v] = true$, cho relax tiếp cho tới khi $cnt[v]> n +5$ thì dừng
		- lan truyền $cycle[v] \; |= cycle[u]$ khi $d[v] > d[u] + w$