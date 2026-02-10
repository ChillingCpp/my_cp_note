
- Set
	- được sử dụng để truy vấn/thêm/sửa  optimal solution ở mỗi bước vòng lặp, đồng thời bao gồm xóa đi 1 solution nào đó, các operation này chạy trong O(log n)
	- hỗ trợ upper/lower bound tìm kiếm nhị phân trong mảng
	- Dùng trong thuật toán tham lam
- Map
	- thay thế unordered_map vì unordered_map có thể bị hack
	- Sử dụng thay thế mảng tần số, coordinate compression 