# Một số mảng thường dùng trong bài Tree

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/dp/tree)

## Mảng cơ bản
- `parent[u]`: cha trực tiếp của `u`.
- `depth[u]` hoặc `h[u]`: độ sâu.
- `sz[u]`: kích thước cây con gốc `u`.
- `in[u]`, `out[u]`: thời điểm vào/ra khi DFS/Euler.

## Công thức hay dùng
- Số cặp đường đi qua cạnh `(u, parent[u])`: `sz[u] * (n - sz[u])`.
- Số node trong subtree `u`: `sz[u] = out[u] - in[u] + 1` (với Euler loại 1 lần).

## Gợi ý
- Nếu truy vấn subtree nhiều: ưu tiên [[Euler tour flatten]]
- Nếu truy vấn tổ tiên/LCA: [[binary lifting]]


