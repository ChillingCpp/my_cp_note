# Advanced Spanning Tree / Forest

## 1) Ý tưởng
- Build một `spanning tree` (thường là MST), rồi chuyển bài toán trên đồ thị về bài toán truy vấn đường đi trên cây.
- Truy vấn phổ biến: `max edge`, `min edge`, `sum`, `xor` trên đường đi `u -> v`.
- Công cụ chuẩn: `Binary Lifting + Sparse DP`.

## 2) Khi nào dùng
- Có rất nhiều truy vấn trên cạnh không thuộc cây (`non-tree edge`).
- Cần kiểm tra điều kiện thay cạnh vào cây (`exchange argument`).
- Cần bài toán kiểu:
  - `second-best MST`
  - cạnh có thể nằm trong *một MST nào đó*
  - tối ưu chu trình sinh từ `non-tree edge + path(u, v)` trong cây

## 3) Khung build chung
1. Chạy Kruskal/Prim để lấy cây (hoặc forest nếu đồ thị không liên thông).
2. Root từng cây, tiền xử lý:
   - `up[k][u]`: tổ tiên `2^k`
   - `mx[k][u]` hoặc `mn[k][u]`: max/min cạnh trên đoạn đi lên `2^k`
3. Viết `query(u, v)` trả về giá trị trên path.

Độ phức tạp thường dùng:
- Build MST: `O(m log m)` (Kruskal)
- Preprocess LCA: `O(n log n)`
- Mỗi query: `O(log n)`

## 4) Tính chất quan trọng
- Với cạnh ngoài cây `e = (u, v, w)`:
  - Khi thêm `e` vào cây sẽ tạo đúng 1 chu trình.
  - Muốn vẫn là cây, phải bỏ 1 cạnh trên `path(u, v)`.
- Cho MST:
  - `maxEdge(path(u, v)) <= w` là điều kiện cần để thay cạnh không làm giảm tính tối ưu.
  - Ứng viên `second-best`:
    - `W2 = min(Wmst + w - maxEdge(path(u, v)))` với mọi cạnh ngoài cây có `w > maxEdge(...)`.
- Cạnh `(u, v, w)` có thể thuộc ít nhất một MST nếu:
  - `w == maxEdge(path(u, v))` trong một MST đang xét.

- Nếu đồ thị không liên thông, ta có `spanning forest`.
- Lưu mỗi component 1 span tree trong đó
- Query phải kiểm tra `component_id[u] == component_id[v]` để xác cạnh tồn tại trước khi xử lý LCA.
- nếu nối 2 span tree ở 2 component khác nhau bằng cạnh (u, v, w) và có trọng số W thì span tree mới có trọng số là w1 + w2 + w

## 6) Lỗi hay gặp
- Quên xử lý nhiều component nên query sai hoặc crash.
- Dùng `int` thay vì `long long` khi tổng trọng số lớn.
- Sai điều kiện strict/non-strict trong `second-best MST` (`>` vs `>=`).
- Build LCA từ node 1 nhưng đồ thị không liên thông.

## 7) Note triển khai nhanh
- Nên tách:
  - DSU cho Kruskal
  - Cây adjacency cho MST/forest
  - Module LCA + path aggregate
- Nếu cần cả `max` và `second max` trên path (để xử lý cạnh bằng nhau), lưu thêm 2 giá trị tốt nhất trong DP.

## Đường dẫn
- [[basic_spanning_tree_forest]]
- [[Binary lifting và DP]]
- [[Bridge_edge_tree]]
