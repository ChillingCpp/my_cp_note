# DSU lý thuyết

## 1. Khi nào dùng DSU
- Duy trì phân hoạch các phần tử thành component.
- Thao tác chính: `merge(a, b)` và `same(a, b)`.
- Không cần truy vết đường đi cụ thể trong graph.

## 2. Độ phức tạp
- Với path compression + union by size/rank: gần như `O(alpha(n))` mỗi thao tác.

## 3. DSU merge giá trị
### Điều kiện của phép gộp
- Bắt buộc: kết hợp (associative).
- Khuyến nghị: giao hoán (commutative).

### Phép gộp hợp lệ
- `sum`, `min`, `max`, `gcd`, `xor`, `and`, `or`, `count`.

### Không hợp lệ trực tiếp
- Trừ, chia.
- Trung bình nếu không lưu `sum + count`.

## 4. DSU với quan hệ có hướng / tương đối
- Vẫn dùng được dù không giao hoán nếu lưu thông tin theo hướng.
- Ví dụ: parity DSU, weighted DSU, xor-distance DSU.

## 5. Mẫu biến thể thường gặp
### DSU danh sách phần tử theo root
- Dùng small-to-large để chuyển phần tử từ component nhỏ sang lớn.
- Hữu ích khi cần liệt kê toàn bộ phần tử mỗi component.

### DSU rollback cho offline dynamic connectivity
- Dùng khi có add/remove edge theo thời gian và truy vấn offline.
- Thường kết hợp segment tree trên trục thời gian.

### DSU trong Kruskal
- DSU chỉ để kiểm tra chu trình và nối component.

## 6. Nhận diện nhanh DSU
### Dấu hiệu mạnh
- Quan hệ tương đương (same group/component).
- Chỉ cần biết cùng nhóm hay không.
- Nhiều thao tác merge.

### Dấu hiệu cần DSU + phụ trợ
- Có ràng buộc tương đối: parity, difference, xor.
- Cần phát hiện contradiction khi thêm ràng buộc.

### Dấu hiệu offline
- Connectivity thay đổi theo thời gian, được phép xử lý offline.

## 7. Checklist trước khi chốt DSU
- Không cần đường đi cụ thể.
- Có tính bắc cầu theo component.
- Thao tác merge là trung tâm.
- Không cần thứ tự xử lý phức tạp (hoặc đã offline hóa).

## Liên kết
- [[DSU bipartite]]
- [[Giá trị đại diện cho tập hợp]]
- [[MST Kruskal]]
- [[DSU problemset]]
