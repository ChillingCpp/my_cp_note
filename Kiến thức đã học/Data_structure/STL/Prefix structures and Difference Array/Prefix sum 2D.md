# Prefix Sum 2D

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

## Mục tiêu
- Tính nhanh tổng trên hình chữ nhật con.

## Build
```cpp
for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
        pref[i][j] = pref[i - 1][j] + pref[i][j - 1]
                   - pref[i - 1][j - 1] + a[i][j];
    }
}
```

## Query
- Tổng trên hình chữ nhật `(x1, y1) -> (x2, y2)` (`x1 <= x2`, `y1 <= y2`):
```cpp
auto query = [&](int x1, int y1, int x2, int y2) {
    return pref[x2][y2] - pref[x1 - 1][y2]
         - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
};
```

## Khi dùng
- Mảng 2D tĩnh, nhiều truy vấn tổng hình chữ nhật.
- có 2 rằng buộc cần thiết cho tính toán tổng lượng thỏa mãn
