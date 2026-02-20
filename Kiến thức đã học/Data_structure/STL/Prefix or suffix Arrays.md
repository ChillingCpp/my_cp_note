[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

# Prefix or Suffix Arrays

## Ý tưởng chung
- Tiền xử lý mảng để trả lời truy vấn nhanh.
- mảng tĩnh không update
- Nếu phép toán có tính kết hợp (`associative`) thì prefix/suffix rất hiệu quả.

## Khung prefix tổng quát
```cpp
vector<long long> pref(n + 1);
pref[0] = identity;
for (int i = 1; i <= n; ++i) {
    pref[i] = op(pref[i - 1], a[i]);
}
```

## Công thức suffix
```cpp
suf[n + 1] = identity;
for (int i = n; i >= 1; --i) {
    suf[i] = op(a[i], suf[i + 1]);
}
```

## Khi dùng
- Mảng tĩnh, nhiều truy vấn.
- Tối ưu từ `O(n*q)` về `O(n + q)`.

## Liên kết
- [[Prefix sum 1D]]
- [[Prefix sum 2D]]
- [[Prefix min]]
- [[Prefix max]]
- [[Difference Array]]
