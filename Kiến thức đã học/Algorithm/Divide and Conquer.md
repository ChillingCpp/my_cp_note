# Divide and Conquer

## Mục tiêu
- Chia bài toán lớn thành các bài toán con độc lập, giải rồi gộp kết quả.

## Dấu hiệu nhận biết
- Có thể tách `A` thành `B, C, ...`.
- Kết quả cuối có dạng `combine(solve(B), solve(C), ...)`.
- Kích thước bài toán con giảm rõ rệt (`n/2`, `n/3`, ...).

## Ví dụ
- Merge sort, count inversion.
