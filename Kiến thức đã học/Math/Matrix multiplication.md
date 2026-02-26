[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/math/matmul.cpp)

## Tính chất ứng dụng giải bài

- Thường sử dụng cho tối ưu hóa quy hoạch động
- Dùng khi trạng thái chuyển tuyến tính: `state_{t+1} = M * state_t`.
- Dùng cho truy hồi tuyến tính bậc `k` với số bước rất lớn (`n` lớn): nâng lũy thừa ma trận.
- Dùng để đếm số đường đi đúng `k` bước (adjacency matrix exponentiation).
- Dùng khi cần gộp nhiều phép biến đổi tuyến tính liên tiếp bằng phép nhân ma trận.
- Keyword nhận diện: `k-th step`, `linear recurrence`, `transition matrix`, `count walks length k`.
- Không phù hợp khi chuyển trạng thái không tuyến tính hoặc số chiều trạng thái quá lớn.
