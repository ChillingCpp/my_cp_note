
- 1. Có thể áp đặt **một thứ tự tuyến tính**
	- Thứ tự **không cần là tự nhiên**, chỉ cần :
	    - so sánh được
	    - duyệt được bằng `lower_bound`
- 2. Trạng thái **đồng nhất trên đoạn**
	- nhiều phần tử liên tiếp **có cùng trạng thái logic**
	- bạn có thể gộp chúng thành `[l, r]`
- 3. Cần **split + merge động nhiều lần**
	- truy vấn có thể :
	    - cắt/chia đoạn
	    - gộp lại
	    - thay đổi
- 4. Phần tử **có thể bị xử lý lại nhiều lần** 
- 5. Kết hợp với lazy segment tree nếu yêu cầu update giá trị trong interval $[l, r]$

# Bảng tóm tắt: Set interval trên các cấu trúc khác nhau
| Cấu trúc gốc          | Linearization                | Set interval dùng khi               | Ghi chú                        |
| --------------------- | ---------------------------- | ----------------------------------- | ------------------------------ |
| **Mảng 1D**           | Index tự nhiên               | Luôn dùng được                      | Case chuẩn                     |
| **Tree**              | Euler tour (tin)             | Trạng thái động trên subtree / path | Interval = đoạn Euler          |
| **DAG**               | Topological order            | Trạng thái node đổi nhiều lần       | Topo phải cố định              |
| **Graph (cycle)**     | Thứ tự ngoài (id, thời gian) | Node có state động                  | Không theo cấu trúc graph      |
| **Grid 2D**           | Quét hàng / cột              | Đơn điệu theo 1 chiều               | Không xử lý hình chữ nhật động |
| **Nhiều tập độc lập** | Mỗi tập 1 set                | Trạng thái độc lập                  | Ví dụ: mỗi row 1 set           |

# Những trường hợp KHÔNG nên dùng set interval
| Trường hợp                 | Lý do                     |
| -------------------------- | ------------------------- |
| One-shot (xử lý xong bỏ)   | DSU next nhanh hơn        |
| Không gom được thành đoạn  | Set không có lợi thế      |
| Không có thứ tự ổn định    | Set không định nghĩa được |
