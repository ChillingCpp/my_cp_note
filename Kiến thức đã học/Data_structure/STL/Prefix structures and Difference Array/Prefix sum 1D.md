# Prefix Sum 1D

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

## Định nghĩa
- `pref[i] = a[1] + a[2] + ... + a[i]`.
- Quy ước `pref[0] = 0`.

## Build
```cpp
pref[0] = 0;
for (int i = 1; i <= n; ++i) {
    pref[i] = pref[i - 1] + a[i];
}
```

## Query
- Tổng đoạn `[l, r]`:
`sum(l, r) = pref[r] - pref[l - 1]`.

## Biến thể
- Alternating prefix sum.
- Prefix trên mảng tần số.
- Prefix trên map (theo key đã sort).
- Cyclic prefix sum (nhân đôi mảng hoặc modulo).

## Khi dùng
- Mảng tĩnh, nhiều truy vấn tổng đoạn.
- Nền tảng cho difference/prefix constraints.

## Liên kết
- [Difference Array](<Difference Array.md>)
