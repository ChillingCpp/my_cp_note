# Harmonic Number

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/math/basic.cpp)

## 1) Định nghĩa
- Harmonic number bậc `n`:
  - `H_n = 1 + 1/2 + 1/3 + ... + 1/n`
- Tăng rất chậm:
  - `H_n = Theta(log n)`

## 2) Vì sao hay gặp trong độ phức tạp

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = i; j <= n; j += i) {
        // xử lý (i, j)
    }
}
```

## 3) Khi nào dùng
- Bài toán divisor/multiple:
  - duyệt bội số của `i`
  - cộng đóng góp theo ước hoặc bội
- Sieve và một số bài number theory.
- DP có chuyển trạng thái theo dạng `i -> k*i` hoặc `i -> i/d`.

