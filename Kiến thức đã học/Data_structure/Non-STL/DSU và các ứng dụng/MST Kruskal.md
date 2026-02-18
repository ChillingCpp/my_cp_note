# DSU trong Kruskal

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Spanning_Tree/kruskal.cpp)

## Vai trò của DSU
- Kiểm tra cạnh `(u, v)` có tạo chu trình hay không.
- Nếu `find(u) != find(v)` thì chọn cạnh và merge 2 component.

## Quy trình Kruskal
1. Sort cạnh theo trọng số tăng dần.
2. Duyệt từng cạnh theo thứ tự đó.
3. Dùng DSU để quyết định nhận/bỏ cạnh.
4. Dừng khi đủ `n - 1` cạnh (nếu graph liên thông).

## Độ phức tạp
- `O(m log m)` do sort cạnh.
- Phần DSU gần tuyến tính theo `m`.

## Liên kết
- [[DSU lý thuyết]]

