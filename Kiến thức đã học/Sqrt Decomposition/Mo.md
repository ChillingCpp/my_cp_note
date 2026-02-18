# Mo's Algorithm

## Tư tưởng
- Mo là kỹ thuật xử lý truy vấn đoạn `query(l, r)` theo kiểu offline.
- Biến đổi cặp giá trị (l, r) thành 1 giá trị hilbert order
- Sort truy vấn tăng dần theo giá trị đó
- Duy trì cấu trúc trạng thái cho cửa sổ hiện tại bằng 3 thao tác:
    - `add(pos)`
    - `remove(pos)`
    - `get_answer()`

## Khi nào dùng
- offline query
- Sử dụng với các phép toán tổng quát có độ phức tạp thực hiện là O(1) 
- point update range query
- tree path/subtree query

## Hilbert order
[Source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/MO_algorithm/hilbert_order.cpp)

## Độ phức tạp
- Sort query: `O(q log q)`.
- $O(n \sqrt{q})$ cho Mo.

## Code mẫu
[Mo bình thường](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/MO_algorithm/Mo.cpp)
[Mo trên cây](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/MO_algorithm/MoTree.cpp)
[Mo point update](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/MO_algorithm/MoUpdate.cpp)

## Biến thể
- Mo point update : thêm chiều thời gian `t` để advance và rollback.
- Mo on tree: kết hợp Euler Tour để đưa về đoạn mảng.

## Đường dẫn
- [[Tư tưởng]]
- [[Harmonic Number]]
- [[Euler tour flatten]]
