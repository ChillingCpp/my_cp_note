# Manacher

## 1) Mục tiêu
- Tính bán kính palindrome tại mọi tâm trong `O(n)`.
- Tìm longest palindromic substring trong `O(n)`.

## 2) Code và các ứng dụng (gộp cả odd/even)
[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/String/manacher.cpp)

## 3) Ý nghĩa biến trong code
- `z = 0`: palindrome chẵn.
- `z = 1`: palindrome lẻ.
- `p[z][i]`: bán kính theo định nghĩa của từng loại tâm.
    - lẻ : độ dài của $[i+1...i + p[1][i]]$ : không bao gồm tâm i
    - chẵn : độ dài của $[i...i + p[0][i] - 1]$ : bao gồm tâm i
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

## 5) Tính chất và ứng dụng
- đếm số lượng palindrome : $\text{answer} = \sum d1[i] + \sum d2[i]$
- tìm longest palindrome : $ans = max(2*p[1][i] + 1, 2 * p[0][i])$
- Tạo mảng longest palindrome kết thúc tại `i`
- Range query check substring $[l, r]$ là palindrome
