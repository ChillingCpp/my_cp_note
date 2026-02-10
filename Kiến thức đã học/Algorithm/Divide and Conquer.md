

- Sử dụng trong Merge sort và count inversion
- Dùng để tối ưu hóa 1 số bài toán có độ phức tạp O(n^2), tối ưu hóa Quy hoạch động
- Đặc điểm nhận biết :
	- các bài toán con độc lập với nhau, giải bài toán A thì không ảnh hướng đến bài toàn B và không ảnh hưởng tới kết quả của giải bài toán lớn có cả A và B
	- các bài toán con có cùng lời giải với bài toán gốc
		- ví dụ giải bài toán độ dài N thì có thể giải với N/2, N/4....
	- Các bài toán độc lập sau khi giải có thể ghép lại bài toán lớn đó và vẫn đúng khi giải bài toán lớn đó
		- ví dụ : bài toán A là bài toán gốc được phân thành 2 bài toán con B và C, ta có tính chất như sau : $solve(A) == combine(solve(B) \cup solve(C))$.