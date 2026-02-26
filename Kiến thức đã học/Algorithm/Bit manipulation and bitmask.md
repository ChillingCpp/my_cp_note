# Bit Manipulation and Bitmask

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/bitmask.cpp)

## 1) Bit manipulation cơ bản
- Toán tử chính: `&`, `|`, `^`, `~`, `<<`, `>>`.
- Kỹ thuật thường dùng:
  - check bit `k`: `(x >> k) & 1`
  - bật bit `k`: `x |= (1 << k)`
  - tắt bit `k`: `x &= ~(1 << k)`
  - đảo bit `k`: `x ^= (1 << k)`
  - lấy bit thấp nhất đang bật: `x & -x`

## 2) Bitmask là gì
- Bitmask biểu diễn một tập con: bit `i = 1` nghĩa là phần tử `i` đang được chọn.
- Hay dùng khi `n` nhỏ (thường `n <= 20..22`).

## 3) Mẫu duyệt chuẩn
- Duyệt mọi mask:
```cpp
for (int mask = 0; mask < (1 << n); mask++) 
```
- Duyệt submask của `mask`:
```cpp
for (int sub = mask; sub; sub = (sub - 1) & mask) 
```
- Duyệt đúng 1 bit bật:
```cpp
for (int b = mask; b; b &= (b - 1)) {
    int bit = __builtin_ctz(b);
}
```

## 4) Ứng dụng chính
- DP bitmask (TSP, assignment, set partition).
- Meet-in-the-middle kết hợp trạng thái tập con.
- Tối ưu kiểm tra tập/điều kiện logic bằng thao tác bit.

## 5) Độ phức tạp hay gặp
- Duyệt tất cả tập con: `O(2^n)`.
- DP mask + chọn đỉnh kế: `O(n * 2^n)` hoặc `O(n^2 * 2^n)`.

## 7) Ghi nhớ nhanh
- `popcount(mask)`: số bit bật.
- `ctz(x)`: vị trí bit 1 thấp nhất.
- `mask ^ (1 << i)`: toggle phần tử `i`.

