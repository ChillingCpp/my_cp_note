[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/monotonic_stack.cpp)

# Stack (LIFO)

## Khi nào dùng
- Cần xử lý theo nguyên tắc vào sau ra trước (Last In, First Out).
- Cần nhớ trạng thái tạm thời theo thứ tự lồng nhau.
- Cần loại bỏ nhanh các phương án kém hơn phần tử hiện tại (monotonic stack).

## Mẫu bài quan trọng
- Monotonic stack
    - Dùng khi có thể “bắc cầu” để loại các phần tử không còn hữu ích.
    - Thường dùng cho: next greater/smaller, previous greater/smaller.
    - Ứng dụng mạnh: tính đóng góp max/min của mỗi phần tử trong mọi subarray.
    - Value contribution (đóng góp từng phần tử):
    - Gọi `L` là chỉ số phần tử gần nhất bên trái còn hợp lệ, `R` là chỉ số phần tử gần nhất bên phải còn hợp lệ.
    - Số subarray mà `a[i]` đại diện = `(i - L) * (R - i)`.
    - Contribution của `a[i]` = `a[i] * (i - L) * (R - i)`.
    - `sumMax = Σ a[i] * (i - Lmax) * (Rmax - i)`.
    - `sumMin = Σ a[i] * (i - Lmin) * (Rmin - i)`.
    - Tổng `max - min` trên mọi subarray: `sumMax - sumMin`.
    - Luôn chọn **một bên strict, một bên non-strict**, có thể đảo ngược.
        - `L`: previous greater/smaller (`>`), `Rmax`: next greater/smaller or equal (`>=`).
- Balanced Bracket
    - Đẩy dấu mở vào stack, gặp dấu đóng thì kiểm tra cặp tương ứng.
- Evaluate Expression
    - Chuyển/đánh giá biểu thức (infix, postfix, prefix).
- DFS không đệ quy
    - Mô phỏng call stack bằng `stack` để tránh tràn ngăn xếp hệ thống.

## Lưu ý nhanh
- Luôn kiểm tra `empty()` trước khi gọi `top()` hoặc `pop()`.
- Với monotonic stack, xác định rõ điều kiện pop (`<`, `<=`, `>`, `>=`) để tránh đếm trùng.
- Mốc biên thường dùng: `L = -1`, `R = n` nếu không tồn tại phần tử phù hợp.
