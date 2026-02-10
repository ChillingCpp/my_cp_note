
- 1 số mảng có trong bài viết này :
	- $d[u]$ : độ sâu của cây
	- $in[u]$ : thời gian đầu tiên đến node u khi chạy euler tour
	- $out[u]$ : thời gian cuối cùng quay lại node u khi chạy euler tour
	- $flat[timer]$ : giá trị của node u khi timer  = $in[u]$ || $out[u]$
	- st : cây phân đoạn truy vấn giá trị

- Euler tour có 3 loại :
	- Euler tour hoàn chỉnh kích thước  $2*n-1$ : dùng cho RMQ, 1 node chứa LCA và các giá trị đại diện, đồng thời các phép toán phải thỏa mãn tính chất của Segment tree
	- Euler tour $2*n$ : mỗi node xuất hiện đúng 2 lần, sử dụng cho thuật toán Mo trên cây
		- node thấy lần đầu : on
		- node thấy lần thứ 2 : off ( node đó không ở trong path u -> v )
		- biến đổi query như sau :
			- nếu lca(u, v) = u || v thì sẽ biến đổi thành đoạn $[in[u], in[v]] \;  với \; h[u] < h[v]$  
			- còn không thì là  $[out[u], in[v]] + lca(u, v)$  