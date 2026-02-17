# Manacher (mẫu `manacherv2`)

## 1) Mục tiêu
- Tính bán kính palindrome tại mọi tâm trong `O(n)`.
- Tìm longest palindromic substring trong `O(n)`.

## 2) Code mẫu (gộp cả odd/even)
[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/String/manacher.cpp)

## 3) Ý nghĩa biến trong code
- `z = 0`: palindrome chẵn.
- `z = 1`: palindrome lẻ.
- `p[z][i]`: bán kính theo định nghĩa của từng loại tâm.
- `[l, r]`: đoạn palindrome xa nhất bên phải đã biết cho loại `z`.
- `L, R`: biến tạm để mở rộng palindrome tại tâm `i`.

## 4) Định nghĩa độ dài từ `p`
- Với `z = 1` (lẻ):
  - tâm tại `i`
  - độ dài `len = 2 * p[1][i] + 1`
  - đoạn `[L, R] = [i - p[1][i], i + p[1][i]]`
- Với `z = 0` (chẵn):
  - tâm nằm giữa `i - 1` và `i`
  - độ dài `len = 2 * p[0][i]`
  - đoạn `[L, R] = [i - p[0][i], i + p[0][i] - 1]`

## 5) Lấy longest palindrome
- Duyệt tất cả `i`:
  - cập nhật max từ `2 * p[1][i] + 1` (lẻ)
  - cập nhật max từ `2 * p[0][i]` (chẵn)
- Lưu lại `bestL, bestR` theo công thức map ở trên.

## 6) Độ phức tạp
- Thời gian `O(n)`.
- Bộ nhớ `O(n)`.
