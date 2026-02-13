

- State Space Search là thuật toán tham lam trên đồ thị sử dụng thuật toán Djikstra/BFS, lan truyền như DP nhưng chỉ lấy tốt nhất và không brute force
- Cách hoạt động : 
	- Định nghĩa trạng thái tương tự DP và trạng thái đó phải lan truyền được
	- Mỗi Node chứa trạng thái $(u, state1, state2,...)$ với các rằng buộc khác nhau
	- Khi duyệt BFS/Dijstra thì state được pop ra từ heap/queue thì đó là state tốt nhất hiện tại và ta chỉ được phép dùng state đó để lan truyền
	- Sau đó sử dụng thuật toán để lan truyền thông qua duyệt ```for auto v in a[u]``` 
- Sử dụng khi :
	- Đề cho rằng buộc và yêu cầu phải có đường đi tốt ưu nhất, hoặc k đường đi tối ưu nhất cho phép lặp đỉnh