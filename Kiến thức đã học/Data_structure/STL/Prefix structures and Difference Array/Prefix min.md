[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

# Prefix min

## Định nghĩa
- `prefMin[i] = min(prefMin[i - 1], a[i])`.
- `prefMin[i]` là giá trị nhỏ nhất trong đoạn `[1, i]`.

## Build
```cpp
prefMin[1] = a[1];
for (int i = 2; i <= n; ++i) {
    prefMin[i] = min(prefMin[i - 1], a[i]);
}
```

## Khi dùng
- Truy vấn nhanh min tiền tố.
- Kết hợp suffix min để lấy min ngoài đoạn `[l, r]`.
- Hỗ trợ bài toán ràng buộc một chiều và greedy kiểm tra điều kiện.

## Độ phức tạp
- Build: `O(n)`.
- Query min tiền tố: `O(1)`.
