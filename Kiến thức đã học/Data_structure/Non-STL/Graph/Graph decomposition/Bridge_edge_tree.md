# Bridge-Edge Tree (Bridge Tree)

## 1) Định nghĩa
- Trên đồ thị vô hướng:
  - `bridge`: cạnh xóa đi làm tăng số thành phần liên thông.
  - `2-edge-connected component`: cụm đỉnh không bị tách bởi một bridge đơn lẻ.
- Nén mỗi `2-edge-connected component` thành 1 node, giữ các bridge thành cạnh.
- Đồ thị sau nén là một `tree` (nếu đồ thị gốc liên thông) hoặc `forest`.

## 2) Khi nào dùng
- Bài toán liên quan tới bridge nhưng cần query nhanh trên cấu trúc dạng cây.
- Đếm số bridge trên đường đi giữa 2 đỉnh.
- Tối ưu số cạnh thêm để tăng độ bền kết nối.

## 3) Cách build
1. DFS Tarjan để tìm `tin[u]`, `low[u]`, đánh dấu bridge (`O(n + m)`).
2. Bỏ các bridge, DFS/BFS để tô màu component `comp[u]`.
3. Với mỗi bridge `(u, v)` thêm cạnh `comp[u] - comp[v]` chỉ khi `u < v && comp[u] != comp[v]` vào tree.
4. [Source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Graph_decompose/bridge_edge_tree.cpp)

## 4) Tính chất quan trọng
- Mỗi cạnh trong bridge-tree tương ứng đúng 1 bridge của đồ thị gốc.
- Số bridge trên path `comp[u] -> comp[v]` = số cạnh phải đi qua để nối `u` và `v`.
- Query đường đi có thể dùng:
  - `LCA` nếu nhiều truy vấn tĩnh
  - `HLD` nếu cần update/query nặng hơn

## 5) Độ phức tạp
- Build bridge + component + tree: `O(n + m)`.
- LCA preprocess: `O(C log C)` với `C` là số component.
- Mỗi query path: `O(log C)`.

## 7) Mẹo triển khai
- Lưu ID cạnh khi DFS để phân biệt cạnh cha thật sự với cạnh song song.
- Nếu chỉ cần đếm bridge giữa `u, v`: có thể dùng `depth + lca` trực tiếp trên bridge-tree.

## Đường dẫn
- [[bridge and ap]]
- [[block_cut_tree]]
- [[advance_span_tree_forest]]
