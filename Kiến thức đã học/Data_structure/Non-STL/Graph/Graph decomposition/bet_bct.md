# Graph Decomposition: BET và BCT (Gộp Theo Đề Mục)

## 1) Định nghĩa
- `Bridge-Edge Tree (BET)`:
  - Nén theo `2-edge-connected component`.
  - Mỗi cạnh trong cây nén tương ứng một `bridge`.
- `Block-Cut Tree (BCT)`:
  - Nén theo `biconnected component (theo đỉnh)` + `articulation point`.
  - Là cây hai phía: `BCC-node` và `AP-node`.

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

## 7) Ứng dụng điển hình
- `BET` (Bridge-Edge Tree) - Nút thắt theo **cạnh**:
  - Đếm số bridge trên đường đi giữa hai đỉnh.
  - Kiểm tra hai đỉnh còn liên thông khi xóa một cạnh cầu cụ thể.
  - Tìm số cạnh tối thiểu cần thêm để đồ thị không còn bridge (tăng edge-connectivity).
  - Gom cụm 2-edge-connected để làm DP trên cây nén.
  - Trả lời truy vấn kiểu "bao nhiêu cạnh critical nằm trên tuyến `u-v`?".

- `BCT` (Block-Cut Tree) - Nút thắt theo **đỉnh**:
  - Đếm số articulation point bắt buộc đi qua giữa hai đỉnh.
  - Kiểm tra một đỉnh `x` có phải nút bắt buộc khi đi từ `u` đến `v` không.
  - Tách đồ thị thành các khối BCC để xử lý đường đi/đếm cách theo cụm.
  - Bài toán thêm cạnh để giảm số đỉnh khớp quan trọng.
  - Query độ "mong manh theo đỉnh" của mạng (vertex-failure analysis).

- Pattern chung khi đã nén:
  - Chuyển truy vấn trên đồ thị gốc về truy vấn path trên cây/forest nén.
  - Dùng `LCA/HLD` để trả lời nhiều truy vấn tĩnh/động.
  - Dùng DP trên cây nén để tối ưu toàn cục theo component.

## Đường dẫn
- [[bridge and ap]]
- [[advance_span_tree_forest]]
- [[dfs_cactus]]
