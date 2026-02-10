
[[Neighbor-linked array ~ DSU]]
- "Node gần nhất bên trái/phải" hoặc "Node kế tiếp chưa được xử lí":
    - DSU giúp bỏ qua các phần tử đã bị xử lí
    - DSU + path compression + max
    - reverse order
- **CHỈ ÁP DỤNG ĐỐI VỚI NHỮNG PHẦN TỬ ĐÃ XỬ LÍ HOẶC NHỮNG PHẦN TỬ KHI PROCESS TỪ REVERSE ORDER THÌ KHÔNG CẦN PHẢI ĐỤNG TỚI NỮA**
	- nếu bài toán có phần tử có thể bị xử lí lại nhiều lần : dùng [[Set interval]]