[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/Searching/Binary_Search.cpp)

## Tính chất ứng dụng giải bài

- Dùng khi miền tìm kiếm có thứ tự và có thể cắt nửa sau mỗi lần.
- Có 2 nhánh chính:
  - `Binary search on array/set`: dữ liệu đã sort hoặc ordered container (`set/map`), mục tiêu là `first/last`, `lower_bound/upper_bound`.
  - `Binary search on answer`: không tìm trên mảng mà tìm trên miền đáp án, cần `check(x)` đơn điệu.
- Keyword nhận diện mạnh: `first >= x`, `last <= x`, `k-th`, `min x thỏa`, `max x thỏa`.
- Không dùng khi không có thứ tự hoặc predicate không đơn điệu.

[[Binary search on answer]]
[[Binary search on array or set]]
