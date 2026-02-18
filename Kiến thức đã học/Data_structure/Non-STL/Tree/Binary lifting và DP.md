# Binary Lifting + DP trên cây

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/GraphTree/binlift.cpp)

## 1. Ý tưởng chính
- Binary lifting lưu tổ tiên theo lũy thừa của 2:
  - `up[u][i]` = tổ tiên thứ `2^i` của node `u`.
- Nếu cần truy vấn giá trị trên đường đi, ta nâng cấp thêm:
  - `dp[u][i]` = kết quả gộp trên đoạn đường đi từ `u` lên `up[u][i]`.

## 2. Công thức cốt lõi
- Quan hệ tổ tiên:
  - $up[u][i] = up[up[u][i-1]][i-1]$
- Nhảy `k` bước từ `u`:
  - Duyệt bit của `k`, nếu bit `i` bật thì `u = up[u][i]`.
- DP khi nâng node:
  - $dp[u][i] = combine(dp[u][i-1], dp[up[u][i-1]][i-1])$

## 3. Điều kiện của hàm `combine`
- Bắt buộc có tính **kết hợp** (associative).
- Không bắt buộc giao hoán trong nhiều bài:
  - Ví dụ lưu `(prefix, suffix)`, rolling hash chuỗi.

## 4. Công thức đường đi bằng LCA
- Gọi `f(x)` là giá trị từ `root -> x`, khi đó:
  - $f(u, v) = f(u) + f(v) - 2 \cdot f(lca(u, v))$

## 5. Ghi nhớ nhanh
- `up` dùng cho truy vấn tổ tiên / LCA.
- `up + dp` dùng cho truy vấn giá trị trên đường đi theo kiểu "nhảy bit".
- Khi thiết kế `dp`, kiểm tra trước:
  - identity element (phần tử đơn vị),
  - hướng gộp trái/phải có ảnh hưởng hay không.

