# Bit contribution

## 1) Tư tưởng cốt lõi
- Với nhiều bài `xor/and/or`, mỗi bit đóng góp độc lập.
- Thay vì duyệt mọi cặp/mọi đoạn, đếm số lần bit `b = 1` xuất hiện trong kết quả, rồi nhân `2^b`.
- Mẫu chung: `answer = Σ (count_bit1 * 2^b)`.
- gọi `C(n, k)` là tổ hợp chập k của n

## 2) Khi nào nghĩ tới bit contribution
- Đề có cụm: `sum xor mọi cặp`, `sum and/or mọi cặp`, `mọi subarray`, `đếm parity bit`.
- Giá trị lớn nhưng số bit nhỏ cố định (`0..30` hoặc `0..60`).
- Cần từ `O(n^2)` xuống `O(n * log A)`.

## 3) Công thức kinh điển
Giả sử xét bit `b`, `cnt1` là số phần tử có bit `b = 1`, `cnt0 = n - cnt1`.

### a) Tổng XOR trên mọi cặp không thứ tự `(i < j)`
- Số cặp cho bit `b = 1`: `cnt1 * cnt0`.
- Đóng góp: `cnt1 * cnt0 * 2^b`.

### b) Tổng AND trên mọi cặp không thứ tự
- Số cặp cho bit `b = 1`: `C(cnt1, 2)`.
- Đóng góp: `C(cnt1, 2) * 2^b`.

### c) Tổng OR trên mọi cặp không thứ tự
- Số cặp cho bit `b = 1`: `C(cnt1, 2) + cnt1 * cnt0`.
- Tương đương: `totalPairs - C(cnt0, 2)`.

### d) Tổng XOR trên mọi subarray
- Dùng prefix XOR + count :  `cnt[2] = {1, 0} và px = 0`
- Đếm contribution dựa trên prefix xor
- Cách tiếp cận khác : nếu trong dãy prefix có `cnt0` prefix bit `0` và `cnt1` prefix bit `1`:
    - Số đoạn có bit `b = 1` là `cnt0 * cnt1`.

## 4) Độ phức tạp
- Thường là `O(B * n)`, với `B = 31` (int) hoặc `61` (long long).
- Bộ nhớ `O(1)` hoặc `O(B)`.

## 5) Liên kết
- [Bit Manipulation and Bitmask](<Bit manipulation and bitmask.md>)
- [source code](https://github.com/ChillingCpp/DSA_CP/edit/main/Algorithms/bit_contribution.cpp)
