## 1. Tổng Quan
Heavy Light Decomposition (HLD) là kỹ thuật phân rã cây thành nhiều heavy path để biến path query trên cây thành các đoạn liên tiếp trên mảng, từ đó xử lý bằng Segment Tree

## 2. Khi Nào Dùng
- Cây tĩnh, không thêm hoặc xóa cạnh trong quá trình query.
- Có truy vấn update giá trị Node/Edge/subtree/path
- Nhiều truy vấn đường đi giữa hai đỉnh.
- Hàm gộp có tính kết hợp như sum, min, max, xor, gcd.

## 3. Thuật Ngữ
- Heavy edge: cạnh nối từ một đỉnh xuống con có subtree lớn nhất.
- Light edge: cạnh còn lại.
- Heavy path (chain): dãy đỉnh nối bằng heavy edge.

## 4. Tính Chất Quan Trọng
Mỗi đường từ gốc đến lá đi qua không quá `O(log n)` cạnh light, nên đường đi giữa hai đỉnh được chia thành `O(log n)` đoạn chain.

## 5. Dữ Liệu Lưu Trữ
- `parent[u]`: cha của `u`.
- `depth[u]`: độ sâu.
- `sz[u]`: kích thước subtree.
- `head[u]`: đỉnh đầu của chain chứa `u`.
- `pos[u]`: vị trí của `u` trên mảng `base`.
- `value[pos[u]]`: giá trị của đỉnh `u` hoặc cạnh `(parent[u], u)`.
- gán `head[1] = 1` cho base case


## 6. Truy Vấn Đường Đi Trên Đỉnh
1. Khi `head[u] != head[v]`, luôn đưa đỉnh có `head` sâu hơn lên.
2. Cộng kết quả trên đoạn `[pos[head[u]], pos[u]]`, rồi gán `u = parent[head[u]]`.
3. Khi cùng chain, query đoạn `[pos[u], pos[v]]` với `u` là đỉnh nông hơn.

## 7. Truy Vấn Đường Đi Trên Cạnh
- Tương tự truy vấn đường đi trên đỉnh, khác xử lí phần cùng chain
- Khi cùng chain, query đoạn `[pos[u] + 1, pos[v]]`

## 8. Cập Nhật
- Cập nhật đỉnh: `update(pos[u], newValue)`.
- Cập nhật cạnh `(u, v)`: cập nhật ở vị trí của đỉnh sâu hơn.

## 9. Độ Phức Tạp
- Tiền xử lý: `O(n)`.
- Mỗi query: `O(log^2 n)` vì `O(log n)` đoạn, mỗi đoạn `O(log n)`.
- Node/Edge/subtree/path update: `O(log n)`.

## 10. Dạng Bài Ứng Dụng
- Node/Edge/subtree/path update + Node/Edge/subtree/path query
- Đối với path/subtree update thì sử dụng lazy segment tree
- Đếm số đỉnh theo màu trên path/subtree.
- K-th smallest trên path/subtree bằng persistent segment tree.
- Truy vấn kết hợp path và subtree
- Truy vấn động yêu cầu đổi root nhưng cây vẫn tĩnh.
- Sử dụng cùng với ODT nếu như subtree/path update phức tạp và chỉ có Node/Edge query

## 11. Lỗi Thường Gặp
- Quên loại bỏ `pos[LCA]` khi query theo cạnh.
- So sánh sai độ sâu giữa `head[u]` và `head[v]`.
- Sai chỉ số mảng `base` giữa 1-index và 0-index.
- Không gán `heavy[u] = -1` ban đầu hoặc chọn heavy sai.
- Dùng giá trị trung hòa không phù hợp với hàm gộp.
