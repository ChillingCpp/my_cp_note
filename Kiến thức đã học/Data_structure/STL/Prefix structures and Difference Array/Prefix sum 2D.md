# Prefix Sum 2D

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Data_Structures/DiamondSum.cpp)

## Mục tiêu
- Tính nhanh tổng trên hình chữ nhật con của ma trận tĩnh.

## Build
```cpp
for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= m; ++j) 
        pref[i][j] =  pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
```

## Query
- Tổng trên hình chữ nhật `(x1, y1) -> (x2, y2)`:
```cpp
long long query(int x1, int y1, int x2, int y2) {
    return pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
}
```

## Hình thoi Manhattan (|x-x0| + |y-y0| <= k) : hiếm có
Ý tưởng: xoay 45 độ bằng biến đổi `u = x + y`, `v = x - y + m + 1` để hình thoi thành hình chữ nhật trong không gian `(u, v)`.

### Build trên lưới (u, v)
Giả sử `x in [1..n]`, `y in [1..m]`. Khi đó:
- `u` nằm trong `[2 .. n + m]`
- `v` nằm trong `[2 .. n + m]`



## Điều kiện triển khai
- Dùng mảng `1-based` hoặc thêm hàng/cột `0` bằng `0` để tránh if biên.
- Đảm bảo `x1 <= x2`, `y1 <= y2`.

## Độ phức tạp
- Build: `O(n*m)`.
- Mỗi query: `O(1)`.
