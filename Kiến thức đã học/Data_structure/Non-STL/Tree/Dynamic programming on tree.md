
- Dynamic programming trên cây bao gồm 2 loại tính chất sau đây : 
	- preorder : tính trước khi gọi đệ quy hoặc vòng lặp dfs
		- sử dụng khi kết quả của node con có thể tính ngay lập tức hoặc phụ thuộc node cha
	- postorder : tính sau khi gọi đệ quy dfs
		- sử dụng khi node cha phụ thuộc vào cây con gốc cha