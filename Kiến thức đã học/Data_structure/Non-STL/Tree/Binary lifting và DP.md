# Binary Lifting + DP trên cây

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/GraphTree/binlift.cpp)

## 1. Ý tưởng chính
- Binary lifting lưu tổ tiên theo lũy thừa của 2:
    - `up[u][i]` = tổ tiên thứ `2^i` của node `u`.
- Nếu cần truy vấn giá trị trên đường đi, ta nâng cấp thêm:
    - `dp[u][i]` = kết quả gộp trên đoạn đường đi từ `u` lên `up[u][i]` bằng hàm `combine`.
        - Bắt buộc có tính **kết hợp** (associative).
        - Không bắt buộc giao hoán trong nhiều bài:
            - Ví dụ lưu `(prefix, suffix)`, rolling hash chuỗi.

## 2. Công thức cơ bản
- Quan hệ tổ tiên:
    - $up[u][i] = up[up[u][i-1]][i-1]$
- DP khi nâng node:
    - $dp[u][i] = combine(dp[u][i-1], dp[up[u][i-1]][i-1])$
- Gọi `f(x)` là giá trị từ `root -> x`, khi đó:
    - $f(u, v) = f(u) + f(v) - 2 \cdot f(lca(u, v))$
- `vertex\_cnt(u, v) = dist(u, v) + 1`.
- `is_ancestor(u, v) :  in[u] < in[v] && out[v] <= out[u]`
- `x` nằm trên path `u-v` khi và chỉ khi:
    - `dist(u, x) + dist(x, v) = dist(u, v)`.
## 3. Hàm cốt lõi về đỉnh trên cây
- `kth_ancestor(u, k)`:
    - Ý nghĩa: đỉnh cách `u` đúng `k` cạnh theo hướng đi lên cha.
    - Miền hợp lệ: `0 <= k <= depth[u]` (nếu vượt miền, xử lý theo convention: trả `0` hoặc `root`).
    - Cách tính: duyệt bit của `k`, bit `i` bật thì `u = up[u][i]`.
- `kth_node(u, v, k)` (0-index từ `u` trên path `u -> v`):
    - Đặt `w = lca(u, v)`, `a = depth[u] - depth[w]`, `D = dist(u, v)`.
    - Miền hợp lệ: `0 <= k <= D`.
    - Nếu `k <= a`: `kth_node(u, v, k) = kth_ancestor(u, k)`.
    - Nếu `k > a`: `kth_node(u, v, k) = kth_ancestor(v, D - k)`.
- `next_on_path(u, v)` (đỉnh đi tiếp từ `u` về phía `v`):
    - Nếu `u == v`: không tồn tại.
    - Nếu `u != v`: `next_on_path(u, v) = kth_node(u, v, 1)`.

## 4. Ghi nhớ nhanh
- `up` dùng cho truy vấn tổ tiên / LCA.
- `up + dp` dùng cho truy vấn giá trị trên đường đi theo kiểu "nhảy bit".
- Khi thiết kế `dp`, kiểm tra trước:
    - identity element (phần tử đơn vị),
    - hướng gộp trái/phải có ảnh hưởng hay không.

