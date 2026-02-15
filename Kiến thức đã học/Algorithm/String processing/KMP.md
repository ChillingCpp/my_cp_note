# KMP

## Mục tiêu
- Tìm mọi vị trí xuất hiện pattern `p` trong text `t` trong `O(n + m)`.

## Ý tưởng
- Build `pi[i]`: tiền tố dài nhất của `p[0..i]` cũng là hậu tố.
- Khi mismatch, nhảy theo `pi` thay vì lùi text.

## Khi dùng
- Pattern matching exact, deterministic.
