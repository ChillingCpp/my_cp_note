# DSU Bipartite (Parity DSU)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dsu/Dsu.cpp)

## Mục tiêu
- Duy trì quan hệ 2 phía (2-color) trong từng component.
- Phát hiện mâu thuẫn khi thêm ràng buộc `u` và `v` khác màu.

## Ý tưởng cốt lõi
- Lưu `parity[x]`: parity từ `x` tới root.
- `find(x)` trả về `(root, parity_to_root)`.
- Khi `union(u, v, w)` với `w` là parity mong muốn giữa `u` và `v`:
  - Nếu khác root: nối 2 root và cập nhật parity root con.
  - Nếu cùng root: kiểm tra mâu thuẫn bằng parity hiện có.

## Công thức thường dùng
- `parity(root_v -> root_u) = parity[u] XOR parity[v] XOR w`.
- Bài bipartite chuẩn: `w = 1` (u và v khác màu).

## Lưu ý
- Phép gộp không giao hoán, nhưng vẫn đúng vì lưu thông tin theo hướng.
- Nên dùng union by size/rank + path compression.

## Liên kết
- [DSU lý thuyết](<DSU lý thuyết.md>)
- [Giá trị đại diện cho tập hợp](<Giá trị đại diện cho tập hợp.md>)

