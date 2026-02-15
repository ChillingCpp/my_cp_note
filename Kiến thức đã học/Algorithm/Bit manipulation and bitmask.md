# Bit Manipulation and Bitmask

## Mục tiêu
- Mã hóa trạng thái bằng bit để tối ưu thời gian/bộ nhớ.

## Phép cơ bản
- Bật bit `i`: `mask | (1 << i)`.
- Tắt bit `i`: `mask & ~(1 << i)`.
- Kiểm tra bit `i`: `(mask >> i) & 1`.
- Đếm bit 1: `__builtin_popcount(mask)`.
