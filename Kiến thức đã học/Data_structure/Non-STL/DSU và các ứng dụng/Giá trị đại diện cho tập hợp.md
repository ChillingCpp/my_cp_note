# Giá trị đại diện cho tập hợp (DSU + Aggregate)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dsu/Dsu.cpp)

## Mục tiêu
- Duy trì thông tin tổng hợp cho mỗi component.

## Các dạng thông tin thường lưu ở root
- `size`, `sum`, `min`, `max`.
- Thông tin tương đối: weighted/parity/xor distance.

## Nguyên tắc
- Chỉ cập nhật aggregate tại root sau mỗi lần merge.
- Nếu cần truy vấn theo quan hệ giữa 2 node, dùng DSU có trọng số/parity.

## Liên kết
- [[DSU lý thuyết]]
- [[DSU bipartite]]

