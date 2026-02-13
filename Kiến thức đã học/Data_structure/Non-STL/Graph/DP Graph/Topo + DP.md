
- Chỉ áp dụng cho đồ thị có hướng
- DP + topo sort
	- nếu graph là DAG thì có thể sử dụng topo sort
	- nếu graph không là DAG thì có thể sử dụng condensation graph nhưng cần phải thỏa mãn tính chất sau :
		- bài toán cho phép lặp đỉnh, lặp đỉnh thì chỉ lấy giá trị của lần đầu tiên tới đỉnh đó