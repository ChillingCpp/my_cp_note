# Binary Search on Answer

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/Searching/Binary_Search.cpp)

## 1) Bản chất
- Tìm nhị phân trên miền nghiệm `[L, R]`, không nhất thiết trên mảng đã sort.
- Cần một hàm `check(x)` để quyết định nghiệm nằm bên trái hay bên phải.

## 2) Điều kiện bắt buộc
- `check(x)` phải **đơn điệu** (chỉ đổi từ `false -> true` hoặc `true -> false` đúng 1 lần).
- Hàm mục tiêu không có cực trị ở giữa; nếu có thì chỉ ở biên `L/R`.
- Nếu hàm có 1 cực trị trong miền, ưu tiên `[Ternary search on answer](<../Ternary search/Ternary search on answer.md>)`; nhiều cực trị thì cần kỹ thuật khác.

## 3) Cách tư duy hàm check
- Giả sử đáp án tối ưu là `x*`, xét `x0 < x*` và `x0 > x*`:
    - nếu hai phía cho tính chất khác nhau rõ ràng => có thể tạo `check(x)` đơn điệu.
- Với công thức có mảng, thường check gắn với ràng buộc kiểu `<= k`, `>= k`, số phần tử đạt điều kiện,...

## 4) Các dạng bài phổ biến
- Hàm số trực tiếp: ví dụ `f(x) = 3x + 1`.
- Công thức gắn dữ liệu mảng/ràng buộc.
- Tối ưu `max/min`:
    - tìm `max`: thường dùng predicate dạng `f(x) <= k` (hoặc tương đương).
    - tìm `min`: thường dùng predicate dạng `f(x) >= k` (hoặc tương đương).
- Dạng lồng: `max(min(...))`, `min(max(...))`.
- `k`-th element:
    - Khi nhiều tập đã sort, tổng kích thước quá lớn không thể merge toàn bộ.
    - Không cần biết thứ tự đầy đủ, chỉ cần đếm `count(<= x)` để so với `k`.
    - Hay gặp với dãy có quy luật (cấp số cộng, nhân, bảng nhân, ...).
    - Ví dụ:
        - [Multiplication Table - CSES](https://cses.fi/problemset/task/2422)
        - [CF 1996F](https://codeforces.com/contest/1996/problem/F)
        - [Kth Sum](https://codeforces.com/edu/course/2/lesson/6/5/practice/contest/285084/problem/C)
- Có thể dùng **DP bên trong `check(x)`** nếu greedy fail
    - Digit DP

## 6) Lỗi hay gặp
- `check` không đơn điệu nhưng vẫn dùng binary search.
- Chọn sai miền `[L, R]`.
- Nhầm `first true` và `last true`.
- Tràn số khi tính `mid` hoặc trong công thức check.

