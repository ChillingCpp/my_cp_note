# KMP (Knuth-Morris-Pratt)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/String/kmp.cpp)

## 1) Mục tiêu
- Tìm pattern `p` trong text `s` trong `O(n + m)`.
- Tránh lùi con trỏ text khi mismatch.

## 2) Ý tưởng
- Xây mảng `pi[i]`: độ dài prefix dài nhất của `p[0..i]` cũng là suffix của đoạn đó.
- Khi mismatch tại `p[j]`, nhảy `j = pi[j-1]` thay vì quay lại đầu.
- tính chất : 
    - pi[i], pi[pi[i]], pi[pi[pi[i]]],... lần lượt là độ dài prefixnhất của `p[0..i]` cũng là suffix của đoạn đó.

## 3) tính chất
- P[0..pi[i]-1] == P[i - pi[i] + 1 .. i]
## 5) Độ phức tạp
- Build `pi`: `O(m)`
- Match: `O(n)`
- Tổng: `O(n + m)`

## 6) Khi nào dùng
- Single pattern matching cần chắc chắn tuyến tính.
- Bài toán prefix-suffix, border, periodic string.
