[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

# Difference Array (1D)

## Bài toán chuẩn
- Có `q` operations: cộng `k` vào mọi phần tử trong đoạn `[l, r]`.
- Cần xử lý nhanh nhiều range update.

## Kỹ thuật
- `diff[l] += k`
- `diff[r + 1] -= k` (nếu `r + 1 <= n`)
- Lấy prefix trên `diff` để khôi phục giá trị cộng dồn tại từng vị trí.

## Công thức khôi phục
```cpp
for (int i = 1; i <= n; ++i) {
    add[i] = add[i - 1] + diff[i];
    b[i] = a[i] + add[i]; // nếu có mảng gốc a
}
```

## Độ phức tạp
- Mỗi update: `O(1)`.
- Khôi phục cuối: `O(n)`.
- Tổng: `O(n + q)`.

## Lưu ý
- Cẩn thận chỉ số 0-based/1-based.
- Dùng `long long` nếu tổng cộng dồn lớn.
