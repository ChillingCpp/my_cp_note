# Value contribution trên cây

## 1) Tư tưởng
- Thay vì duyệt mọi cặp đỉnh `O(n^2)`, tính số cặp mà một cạnh/giá trị "đại diện".
- Công thức đóng góp thường có dạng:
  - `value * number_of_pairs_affected`.

## 2) Dạng A: mỗi cạnh đóng góp vào mọi đường đi đi qua nó
Áp dụng tốt cho tổng khoảng cách trên cây có trọng số.

- Cắt cạnh `e(u-v)` thì cây tách thành 2 phần có kích thước `sz(u)` và `n - sz(u) = sz(v)`.
- Số cặp đỉnh có đường đi đi qua `e`: `sz(u) * sz(v)`.
- Đóng góp của cạnh:
  - `contrib(e) = w(e) * sz(u) * sz(v)`.
- Tổng:
  - `answer = Σ w(e) * sz(u_e) * sz(v_e)`.

## 3) Dạng B: cực trị trên đường đi mọi cặp (`max/min edge`) bằng DSU
Mục tiêu điển hình:
- `sumMax = Σ maxEdge(u, v)` cho mọi `u < v`.
- `sumMin = Σ minEdge(u, v)` cho mọi `u < v`.
- Hoặc `sum(max - min) = sumMax - sumMin`.

### a) Tính `sumMax`
- Sort cạnh tăng dần theo trọng số.
- Duyệt cạnh `(u, v, w)`:
  - Gọi `ru = find(u)`, `rv = find(v)`, kích thước component là `sz[ru]`, `sz[rv]`.
  - `ans += w * sz[ru] * sz[rv]`.
  - Sau đó union 2 component.

### b) Tính `sumMin`
- Làm tương tự nhưng sort cạnh giảm dần.

## 7) Liên kết
- [DSU lý thuyết](<DSU lý thuyết.md>)
- [Giá trị đại diện cho tập hợp](<Giá trị đại diện cho tập hợp.md>)
