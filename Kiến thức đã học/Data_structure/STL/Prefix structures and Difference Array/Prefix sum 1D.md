# Prefix Sum 1D

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

## Build
```cpp
pref[0] = 0;
for (int i = 1; i <= n; ++i)
    pref[i] = pref[i - 1] + a[i];
```

## Query
- Tổng đoạn `[l, r]`:
`sum(l, r) = pref[r] - pref[l - 1]`.

## Biến thể
- Alternating prefix sum.
- Prefix trên mảng tần số.
- Prefix trên map
- Cyclic prefix sum.

## Khi dùng
- Mảng tĩnh, nhiều truy vấn tổng đoạn.
- prefix difference
- 

## Liên kết
- [[Difference Array]]

