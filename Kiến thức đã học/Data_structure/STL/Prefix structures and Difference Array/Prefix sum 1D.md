# Prefix Sum 1D

## Build
```cpp
pref[0] = 0;
for (int i = 1; i <= n; ++i) pref[i] = pref[i-1] + a[i];
```

## Query
- `sum(l, r) = pref[r] - pref[l-1]`.

## Khi dùng
- Mảng tĩnh, nhiều truy vấn tổng đoạn.
- Kết hợp với map cho bài subarray sum/mod.
