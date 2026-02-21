[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/monotonic_stack.cpp)

# Stack (LIFO)

## Khi nào dùng
- Cần xử lý theo nguyên tắc vào sau ra trước (Last In, First Out).
- Cần nhớ trạng thái tạm thời theo thứ tự lồng nhau.
- Cần loại bỏ nhanh các phương án kém hơn phần tử hiện tại (monotonic stack).

## Mẫu bài quan trọng
- Monotonic stack.
- Balanced Bracket.
- Evaluate Expression (infix/postfix/prefix).
- DFS không đệ quy.

## Value contribution với monotonic stack
- Gọi `L` là vị trí gần nhất bên trái còn hợp lệ, `R` là vị trí gần nhất bên phải còn hợp lệ.
	- Luôn chọn một bên strict, một bên non-strict.
		- ví dụ :  `L` : previous `> hoặc <`,  `R` : next `>= hoặc <=`
	- Mốc biên thường dùng khi không tồn tại: `L = -1`, `R = n`.
	- Số subarray mà `a[i]` đại diện: `count(i) = (i - L) * (R - i)`.
	- Đóng góp của `a[i]`: `contrib(i) = a[i] * (i - L) * (R - i)`.
	- Tổng max: `sumMax = Σ a[i] * (i - Lmax) * (Rmax - i)`.
	- Tổng min: `sumMin = Σ a[i] * (i - Lmin) * (Rmin - i)`.
	- Bài tổng `(max - min)` mọi subarray: `answer = sumMax - sumMin`.

## Range query với monotonic stack
- Gọi `L` là vị trí gần nhất bên trái còn hợp lệ, `R` là vị trí gần nhất bên phải còn hợp lệ.
- Mỗi giá trị khi làm `max/min` sẽ xác định một đoạn ảnh hưởng `(L[i], R[i])`, nên có thể đổi góc nhìn thành bài toán [[range query]] trên các đoạn này.