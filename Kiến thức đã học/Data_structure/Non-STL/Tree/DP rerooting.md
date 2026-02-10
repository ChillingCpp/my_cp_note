

- Dp rerooting là dạng dp dùng khi phải tính đáp án cho toàn bộ n node khi chúng làm root
- Dp rerooting có 2 quá trình sau :
	- dfs lần 1 để tính kết quả cho node 1
	- dfs lần 2 là kỹ thuật chuyển gốc :
		- thường thì trước vòng lặp dfs $ans[u] = dp[u]$
		- trong vòng lặp dfs xảy ra các quá trình sau với 2 node u và v:
			 - backup() : lưu lại trạng thái của node u và v
			 - process() : thực hiện quá trình chuyển root :
				- exclude(u, v) : loại bỏ cây con gốc v ra khỏi root u ( 1 số bài không có đoạn này )
				- include(v, u) : tính toán lại giá trị khi v là root và cây con gốc u là cây con của v với u nối trực tiếp với v
			- dfs2(v, u) : gọi đệ quy dfs của reroot
			- restore() : phục hồi lại giá trị DP cho node u và node v, gán lại u là root và v là cây con gốc u.
				