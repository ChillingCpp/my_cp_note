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


