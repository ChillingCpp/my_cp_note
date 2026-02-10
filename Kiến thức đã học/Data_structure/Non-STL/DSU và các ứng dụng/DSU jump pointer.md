
[[Neighbor-linked array ~ DSU]]
- **DSU next pointer chỉ dùng được khi thỏa mãn đồng thời 3 điều kiện, thiếu thì không dùng:**
	1. **Có thể áp đặt một thứ tự tuyến tính cố định (total order)**
	2. **Mỗi phần tử chỉ bị “xử lý / loại bỏ” đúng 1 lần (one-shot, đơn điệu)**
	3. **Không bao giờ cần quay lại hay khôi phục phần tử đã xử lý**
- Không thể dùng DSU next pointer nếu có 1 trong trường hợp sau :
	- Phần tử **có thể bị xử lý lại**
	- Có **rollback / undo**
	- Có **split + merge**
	- Trạng thái **không đơn điệu**
	- Không xác định được “next” duy nhất
- Ví dụ:
	- nhân viên đổi phòng nhiều lần
	- interval động
	- dynamic graph
	- range update + query
- Danh sách dạng cấu trúc nếu đề bài thỏa mãn 3 điều kiện ở trên

| Cấu trúc        | DSU next pointer sử dụng                                                    |
| --------------- | --------------------------------------------------------------------------- |
| Mảng 1D         | luôn có thể                                                                 |
| Tree            | Euler tour loại 3 + one-shot                                                |
| DAG             | Topo order + one-shot                                                       |
| Graph tổng quát | node không xử lí lại lần nữa. Nối node đã xử lí vào node kề chưa được xử lí |
| Mảng 2D         | ép về 1D, đơn điệu                                                          |

