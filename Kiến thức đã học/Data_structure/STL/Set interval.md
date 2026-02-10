
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
- 5. Không yêu cầu truy vấn “bên trong đoạn” quá phức tạp

Set interval mạnh về:
- quản lý **cấu trúc đoạn**
- không mạnh về:
    - sum / max / min nội bộ (cái đó giao cho segtree)
👉 Thực tế hay dùng:
> **set interval + segment tree lazy**

---

Nếu **5 điều trên đúng** → set interval dùng được, **bất kể cấu trúc gốc là gì**.