# Prefix or Suffix Arrays

## Mục tiêu
- Tiền xử lý mảng tĩnh để trả lời truy vấn nhanh.

## Khung
```cpp
pref[0] = identity;
for (int i = 1; i <= n; ++i) pref[i] = op(pref[i-1], a[i]);
```

## Liên kết
- [[Prefix sum 1D]]
- [[Prefix sum 2D]]
- [[Prefix min]]
- [[Prefix max]]
- [[Difference Array]]
