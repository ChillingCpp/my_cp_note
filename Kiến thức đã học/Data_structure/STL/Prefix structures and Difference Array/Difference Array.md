# Difference Array

## Mục tiêu
- Tối ưu nhiều range update trên mảng tĩnh.

## Kỹ thuật
- Update `[l, r]` cộng `k`:
  - `diff[l] += k`
  - `diff[r+1] -= k`
- Lấy prefix sum cuối để ra mảng kết quả.
