[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

# Prefix max

## Định nghĩa
- `prefMax[i] = max(prefMax[i - 1], a[i])`.
- `prefMax[i]` là giá trị lớn nhất trong đoạn `[1, i]`.

## Build
```cpp
prefMax[1] = a[1];
for (int i = 2; i <= n; ++i) {
    prefMax[i] = max(prefMax[i - 1], a[i]);
}
```

## Khi dùng
- Truy vấn nhanh max tiền tố.
- Kết hợp suffix max để lấy max ngoài đoạn `[l, r]`.
- Tiền xử lý cho các bài tối ưu có ràng buộc một chiều.

## Độ phức tạp
- Build: `O(n)`.
- Query max tiền tố: `O(1)`.
