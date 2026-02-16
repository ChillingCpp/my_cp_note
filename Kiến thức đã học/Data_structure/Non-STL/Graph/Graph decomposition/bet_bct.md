# Graph Decomposition: BET và BCT (Gộp Theo Đề Mục)

## 1) Định nghĩa
- `Bridge-Edge Tree (BET)`:
  - Nén theo `2-edge-connected component`.
  - Mỗi cạnh trong cây nén tương ứng một `bridge`.
- `Block-Cut Tree (BCT)`:
  - Nén theo `biconnected component (theo đỉnh)` + `articulation point`.
  - Là cây hai phía: `BCC-node` và `AP-node`.

## 2) Bài toán phù hợp
- `BET`:
  - điểm nghẽn theo **cạnh**
  - đếm số bridge trên đường đi
  - tăng độ bền kết nối theo cạnh
- `BCT`:
  - điểm nghẽn theo **đỉnh**
  - đếm AP bắt buộc trên đường đi
  - phân cụm ổn định theo đỉnh khớp

## 3) Cách build
- Bước chung:
  1. Chạy Tarjan lấy `tin/low`.
  2. Nén đồ thị thành cây/forest.
- Riêng `BET`:
  - đánh dấu bridge bằng điều kiện `low[v] > tin[u]`
  - bỏ bridge, tô `comp[u]`, rồi nối các component bằng bridge
- Riêng `BCT`:
  - tách BCC bằng stack cạnh với điều kiện `low[v] >= tin[u]`
  - tạo node BCC + node AP, rồi nối AP-node với các BCC chứa nó

## 4) Tính chất quan trọng
- Điểm chung:
  - sau nén đều là `tree` nếu đồ thị gốc liên thông, ngược lại là `forest`
  - query đường đi đều có thể dùng `LCA/HLD`
- `BET`:
  - số cạnh trên path nén = số bridge bắt buộc đi qua
- `BCT`:
  - AP xuất hiện thành node riêng, nên dễ kiểm tra "đi qua đỉnh bắt buộc"

## 5) Độ phức tạp
- Build Tarjan + nén: `O(n + m)` cho cả hai.
- Nếu có nhiều query path:
  - preprocess LCA: `O(Nc log Nc)`
  - mỗi query: `O(log Nc)`
  - `Nc` là số node của cây nén tương ứng.

## 6) Mẹo triển khai
- `BET`:
  - luôn lưu `edge_id` để tránh lỗi multi-edge
  - query bridge count: dùng `depth + lca`
- `BCT`:
  - lưu map từ đỉnh gốc sang node cây nén (`comps_of_vertex[u]`)
  - xử lý riêng trường hợp đồ thị không liên thông

## 7) Chọn nhanh
- Nút thắt theo **cạnh** -> `BET`
- Nút thắt theo **đỉnh** -> `BCT`

## 8) Lỗi hay gặp
- Nhầm điều kiện `>` và `>=` khi tách cấu trúc.
- Quên xử lý đồ thị nhiều component.
- Nhầm bản chất:
  - `BET`: edge-connectivity
  - `BCT`: vertex-connectivity

## Đường dẫn
- [[bridge and ap]]
- [[advance_span_tree_forest]]
- [[dfs_cactus]]
