# DP Bitmask

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/dp/dp_bitmask.cpp)


## Đường dẫn
[Bit manipulation and bitmask](<../Algorithm/Bit manipulation and bitmask.md>)

## Mục tiêu
- Dùng DP trên tập con khi `n` nhỏ.

## Dạng cơ bản
- `dp[mask]`: giá trị tốt nhất cho tập `mask`.
- `dp[mask][i]`: tốt nhất khi đang ở vị trí `i` với tập `mask` đã chọn.

## Chuyển trạng thái mẫu
```cpp
for (int mask = 0; mask < (1 << n); ++mask) {
    for (int i = 0; i < n; ++i) if (mask & (1 << i)) {
        for (int j = 0; j < n; ++j) if (!(mask & (1 << j))) {
            int nmask = mask | (1 << j);
            dp[nmask][j] = min(dp[nmask][j], dp[mask][i] + cost[i][j]);
        }
    }
}
```

## Khi dùng
- TSP, assignment, pairing, Hamiltonian path dạng `n <= 20`.

## Lưu ý
- Cần ước lượng trước số trạng thái: `2^n * n`.

