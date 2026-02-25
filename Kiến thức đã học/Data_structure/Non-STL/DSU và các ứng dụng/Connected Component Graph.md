[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dsu/Dsu.cpp)

## Tính chất ứng dụng giải bài

- Dùng khi cần co các đỉnh cùng component thành siêu đỉnh để giảm bài toán.
- Hợp với bài xử lý theo 2 pha:
  - pha 1: DSU gộp component,
  - pha 2: build graph giữa các component rồi chạy BFS/DP/topo trên graph nén.
- Phù hợp khi query/thuộc tính cần ở cấp component, không cần đường đi chi tiết bên trong mỗi component.
- Keyword nhận diện: `compress component`, `graph of components`, `nén thành cụm`, `xử lý sau khi gộp`.
