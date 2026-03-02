# Giá trị đại diện cho tập hợp (DSU + Aggregate)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dsu/Dsu.cpp)

## Mục tiêu
- Duy trì thông tin tổng hợp cho mỗi component.

## Các dạng thông tin thường lưu ở root
- `size`, `sum`, `min`, `max`.
- Thông tin theo hệ tương đối: weighted/parity/xor distance.

## Nguyên tắc
- Cách tính đối với dạng hệ tương đối : sử dụng find(u) có thể tính toán được giá trị từ root -> u
- Chỉ cập nhật aggregate tại root sau mỗi lần merge.
- Nếu cần truy vấn theo quan hệ giữa 2 node, dùng DSU có trọng số/parity.

## Liên kết
- [DSU lý thuyết](<DSU lý thuyết.md>)
- [DSU bipartite](<DSU bipartite.md>)

