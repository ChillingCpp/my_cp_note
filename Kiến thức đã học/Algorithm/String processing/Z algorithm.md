# Z Algorithm

## 1) Mục tiêu
- Tính mảng `z[i]`: độ dài đoạn dài nhất bắt đầu tại `i` trùng với prefix của chuỗi.
- Tìm pattern trong text bằng `p + '#' + s`.

## 2) Ý tưởng
- Duy trì đoạn `[l, r]` là đoạn khớp prefix xa nhất hiện tại.
- Với `i` trong đoạn này, tái sử dụng kết quả cũ để giảm so sánh ký tự.

## 3) Mẫu cài đặt
[[https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/String/Z.cpp]](Source code)

## 4) Match pattern
- Tạo `t = p + '#' + s`.
- Với mọi `i`, nếu `z[i] == |p|` thì có một match.

## 5) Độ phức tạp
- `O(n)` cho một chuỗi.

## 6) Khi nào dùng
- Pattern matching tuyến tính như KMP.
- Bài toán cần so sánh prefix với mọi suffix nhanh.

## 7) Lỗi hay gặp
- Chọn ký tự phân tách (`#`) trùng với alphabet input.
- Quên map chỉ số từ `t` về vị trí trong `s`.
