# DP Rerooting

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/dp/tree/dp_tree_rerooting.cpp)

## Mục tiêu
- Tính đáp án cho mọi node khi node đó được chọn làm root.

## Quy trình 2 DFS
1. `dfs1`: tính thông tin cục bộ/subtree khi root cố định (thường là 1).
2. `dfs2`: chuyển gốc từ `u` sang từng con `v` để suy ra đáp án toàn cục.

## Khung thao tác khi chuyển `u -> v`
1. `backup(u, v)`.
2. `exclude(u, v)` nếu cần loại ảnh hưởng cây con `v` khỏi `u`. ( có thể không cần )
3. `include(v, u)` để thêm ảnh hưởng phần còn lại vào `v`.
4. Gọi `dfs2(v, u)`.
5. `restore(u, v)`.

## Lưu ý
- Tránh sửa trực tiếp rồi quên hoàn tác.
- Tách rõ hàm merge/exclude để dễ debug.

## Công thức check nhanh
- Sau `dfs1`: `sub[u] = 1 + \sum sub[v]` (với `v` là con), và `sub[root] = n`.
- Mẫu kinh điển (tổng khoảng cách từ mỗi node):
  - `down[u] = \sum (down[v] + sub[v])`.
  - `ans[root] = down[root]`.
  - Với con `v` của `u`: `ans[v] = ans[u] + n - 2*sub[v]`.
- Nếu `ans[u]` là tổng khoảng cách từ `u` tới mọi node:
  - `\sum ans[u] = 2 * \sum_{i<j} dist(i, j)` (để check toàn cục).
- Khi chuyển gốc `u -> v`, trạng thái phải được khôi phục y hệt sau khi quay lui.
