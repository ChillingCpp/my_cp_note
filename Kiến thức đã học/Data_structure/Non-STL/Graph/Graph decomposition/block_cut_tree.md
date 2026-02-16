# Block-Cut Tree

## 1) Định nghĩa
- Trên đồ thị vô hướng:
  - `articulation point (AP)`: đỉnh xóa đi làm tăng số thành phần liên thông.
  - `biconnected component (BCC)` theo đỉnh: thành phần không bị tách bởi 1 đỉnh đơn lẻ.
- `Block-Cut Tree` là đồ thị 2 phía:
  - Một phía là node BCC
  - Một phía là node AP
  - AP nối tới BCC nếu AP nằm trong BCC đó

## 2) Khi nào dùng
- Cần phân tích cấu trúc "điểm nghẽn theo đỉnh".
- Query đường đi có đi qua AP nào bắt buộc.
- Tách đồ thị lớn thành cụm ổn định để làm DP/query.

## 3) Cách build
1. Tarjan DFS tìm `tin`, `low`, đồng thời dùng stack cạnh.
2. Khi gặp điều kiện tách BCC (`low[v] >= tin[u]`), pop stack để tạo một BCC.
3. Đánh số:
   - Node `1..bcc_cnt` cho BCC
   - Node tiếp theo cho từng AP
4. Nối AP-node với các BCC-node chứa nó.

## 4) Tính chất quan trọng
- Block-cut graph luôn là tree nếu đồ thị gốc liên thông; ngược lại là forest.
- Đường đi giữa 2 đỉnh trong đồ thị gốc tương ứng đường đi trên block-cut tree.
- AP xuất hiện như "điểm bắt buộc" trên một số path.

## 5) Ứng dụng điển hình
- Đếm số AP nằm giữa 2 đỉnh.
- Kiểm tra một đỉnh có bắt buộc phải đi qua khi di chuyển từ `u` đến `v`.
- Bài toán thêm cạnh để giảm số điểm cắt.
## 7) Ghi chú triển khai
- Cần lưu `vector<int> comps_of_vertex[u]` nếu muốn map query từ đỉnh gốc sang node cây.
- Nếu query nhiều, xây LCA trên block-cut tree.

## Đường dẫn
- [[bridge and ap]]
- [[Bridge_edge_tree]]
