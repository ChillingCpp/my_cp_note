# Dynamic Programming on Tree

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/dp/tree/dp_tree_basic.cpp)

## Hai kiểu chuyển trạng thái chính
### 1. Preorder DP
- Tính trước khi đi xuống con.
- Dùng khi con phụ thuộc trực tiếp thông tin từ cha.

### 2. Postorder DP
- Tính sau khi xử lý xong các con.
- Dùng khi cha cần tổng hợp từ toàn bộ subtree con.

## Quy tắc chọn nhanh
- Cần thông tin từ tổ tiên -> con: nghĩ preorder.
- Cần thông tin từ con -> cha: nghĩ postorder.
- Cần cả hai chiều cho mọi root: nghĩ thêm rerooting.

## Liên kết
- [[DP rerooting]]

## Công thức check nhanh
- Invariant cơ bản của subtree: `sz[u] = 1 + \sum sz[v]` với `v` là con trực tiếp của `u`.
- Với bài postorder, `dp[u]` chỉ được merge từ `v != parent[u]`.
- Với bài preorder truyền từ cha xuống con: `depth[v] = depth[u] + 1` và trạng thái con phải được tạo từ trạng thái cha qua đúng 1 cạnh.
- Với toàn cây: tổng bậc luôn là `\sum degree[u] = 2*(n-1)`.
- Debug nhanh: brute force cây nhỏ (`n <= 15`) để đối chiếu `dp[root]` hoặc `ans[u]`.

