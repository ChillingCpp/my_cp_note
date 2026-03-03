# DP Digit

## Đường dẫn
[Các dạng DP chính](<Các dạng DP chính.md>)

## Mục tiêu cốt lõi
Digit DP trong CP thường chỉ cần 2 truy vấn:
1. `count(L, R)`: đếm số thỏa điều kiện trong đoạn.
2. `kth(K)`: tìm số nhỏ nhất `X` sao cho có ít nhất `K` số thỏa trong `[0, X]`.

Chuẩn hóa:
- `count(L, R) = F(R) - F(L - 1)`
- `F(X)`: số lượng số thỏa trong `[0, X]`.

## Khung trạng thái tối thiểu
Với `X >= 0`, tách `X` thành mảng chữ số `dig` từ trái sang phải.

`dfs(pos, tight, started, state)`:
- `pos`: vị trí đang xét.
- `tight`: tiền tố hiện tại còn bám sát `X` hay không.
- `started`: đã đặt chữ số khác `0` chưa (xử lý leading zero).
- `state`: thông tin đủ để kiểm tra điều kiện (vd: `sum`, `mod`, `prev`, ...).

Base case:
- `pos == n`: trả `1` nếu trạng thái hợp lệ, ngược lại `0`.

Chuyển trạng thái:
- `lim = tight ? digit[pos] : 9`
- duyệt `d` từ `0..lim`, cập nhật `(ntight, nstarted, nstate)`, cộng kết quả con.

## Dạng 1: Count
1. Viết `F(X)` bằng Digit DP.
2. Trả lời đoạn bằng `F(R) - F(L - 1)`.
3. Nếu `X < 0` thì `F(X) = 0`.

## Dạng 2: K-th
Muốn tìm số thứ `K` theo thứ tự tăng dần:
1. Cần hàm đếm tiền tố `F(X)` (đơn điệu không giảm).
2. Tìm kiếm nhị phân `X` nhỏ nhất sao cho `F(X) >= K`.
3. Kết quả là `X` đó (nếu tồn tại).

## Checklist ngắn
- Quy ước số `0` có tính hay không phải thống nhất ở base case.
- Leading zero có cập nhật `state` hay không phải nhất quán.
- Memo thường cache khi `tight = 0`.
- Reset memo đúng cách giữa các lần gọi `F(X)` (nếu cần).
- Dùng `int64` cho số lượng cách đếm.
