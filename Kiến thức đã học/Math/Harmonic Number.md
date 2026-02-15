# Harmonic Number

## Ý tưởng
- Các vòng lặp dạng bội số thường có độ phức tạp xấp xỉ `O(n log n)`:
```cpp
for (int i = 1; i <= n; ++i)
    for (int j = i; j <= n; j += i)
```

## Khi dùng
- Bài toán divisor/multiple trong DP hoặc number theory.
