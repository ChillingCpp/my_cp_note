# DP Bitmask

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/dp/dp_bitmask.cpp)


## Đường dẫn
[[Bit manipulation and bitmask]]

## Mục tiêu
- Dùng DP trên tập con khi `n` nhỏ.

## Dạng cơ bản
- `dp[mask]`: giá trị tốt nhất cho tập `mask`.
- `dp[mask][i]`: tốt nhất khi đang ở vị trí `i` với tập `mask` đã chọn.

### Công thức quy hoạch động hay dùng
- Dạng 1 chiều:
  - `dp[mask] = opt(dp[mask | (1 << i)] + val(i, mask))`, với `i` thuộc `mask`.
- Dạng 2 chiều (TSP/Hamiltonian):
  - `dp[mask][i] = opt(dp[mask | (1 << i)][j] + cost[j][i])`, với `j` thuộc `mask`, `i` không thuộc `mask`, `j != i`.
- Dạng mở rộng trạng thái (forward):
  - `dp[mask | (1 << j)][j] = opt(dp[mask][i], cost[i][j])`, với `i` thuộc `mask`, `j` không thuộc `mask`.
- Dạng ghép cặp 2 vị trí:
  - `dp[mask | (1 << i) | (1 << j)] = opt(dp[mask], cost[i][j])`, với `i, j` chưa thuộc `mask`.

### Khởi tạo thường gặp
- `dp[0] = 0`, các trạng thái khác = `INF` (bài toán min).
- Với bài có điểm bắt đầu `s`: `dp[1 << s][s] = 0`.

### Độ phức tạp thường gặp
- `dp[mask]` + duyệt phần tử: `O(2^n * n)`.
- `dp[mask][i]` + chuyển qua `j`: `O(2^n * n^2)`.

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

