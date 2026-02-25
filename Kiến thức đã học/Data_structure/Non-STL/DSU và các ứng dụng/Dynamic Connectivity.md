[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dynamic_connectivity/DSU_rollback.cpp)

## Tính chất ứng dụng giải bài

- Dùng khi có chuỗi thao tác thêm/xóa cạnh và query connectivity theo thời gian.
- Bản offline chuẩn: `DSU rollback + segment tree theo trục thời gian`.
- Điều kiện phù hợp:
  - query chủ yếu là `same(u, v)` hoặc thuộc tính component dễ merge/rollback,
  - không yêu cầu online realtime nghiêm ngặt.
- Keyword nhận diện: `edge add/remove`, `connectivity over time`, `offline dynamic connectivity`.
- Không phù hợp nếu cần đường đi chi tiết online sau mỗi thao tác.
