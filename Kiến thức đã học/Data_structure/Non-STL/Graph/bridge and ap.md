# Bridge và Articulation Point (Cut Vertex)

## 1) Định nghĩa
- `Bridge` (cầu): cạnh mà khi xóa đi làm tăng số thành phần liên thông.
- `Articulation point` (AP, đỉnh khớp): đỉnh mà khi xóa đi (kèm cạnh kề) làm tăng số thành phần liên thông.
- Áp dụng cho đồ thị vô hướng.

## 2) Ý tưởng cốt lõi: DFS time + low-link ~ thuật toán tarjan
- `tin[u]`: thời điểm DFS thăm `u`.
- `low[u]`: thời điểm nhỏ nhất có thể quay về từ `u` (đi xuống cây DFS rồi dùng tối đa 1 back-edge).
- Công thức cập nhật:
  - Nếu `v` chưa thăm: DFS `v`, rồi `low[u] = min(low[u], low[v])`
  - Nếu `v` đã thăm và `v != parent`: `low[u] = min(low[u], tin[v])`

## 3) Điều kiện nhận diện
- Bridge `(u, v)` với `u` là cha của `v` trong DFS:
  - `low[v] > tin[u]`
- AP:
  - Nếu `u` không phải root DFS : `p != -1`: tồn tại con `v` sao cho `low[v] >= tin[u]`
  - Nếu `u` là root DFS : `p == -1` : có từ 2 con DFS trở lên

## 4) Độ phức tạp
- `O(n + m)` cho một lần DFS toàn đồ thị.

## 7) Ứng dụng
- Tìm các cạnh/yếu tố "điểm nghẽn" của mạng.
- Build `Bridge-Edge Tree` (nén theo 2-edge-connected components).
- Build `Block-Cut Tree` (nén theo biconnected components theo đỉnh).

## Đường dẫn
- [[block_cut_tree]]
- [[Bridge_edge_tree]]
