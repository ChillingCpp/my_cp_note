# Harmonic Number

## 1) Định nghĩa
- Harmonic number bậc `n`:
  - `H_n = 1 + 1/2 + 1/3 + ... + 1/n`
- Tăng rất chậm:
  - `H_n = Theta(log n)`

## 2) Vì sao hay gặp trong độ phức tạp
Nhiều vòng lặp kiểu bội số:

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = i; j <= n; j += i) {
        // xử lý (i, j)
    }
}
```
Số lần lặp:
- Với mỗi `i`, số bước là `floor(n / i)`.
- Tổng là `sum_{i=1..n} floor(n / i) = n * H_n + O(n) = O(n log n)`.

Lưu ý:
- `H_n` là `O(log n)`, còn tổng số thao tác ở trên là `O(n log n)`.

## 3) Kỹ thuật harmonic / chia căn cho tổng thương
Dạng rất phổ biến:
- `sum floor(n / i)` hoặc query theo các đoạn có cùng giá trị `floor(n / i)`.

Mẹo nhóm đoạn:
- Với `v = floor(n / l)`, đoạn lớn nhất có cùng giá trị là
  - `r = floor(n / v)`
- Duyệt theo block `[l, r]` thay vì từng `i`.

```cpp
for (long long l = 1, r; l <= n; l = r + 1) {
    long long v = n / l;
    r = n / v;
    // floor(n / i) = v với mọi i trong [l, r]
}
```

Độ phức tạp:
- Số block chỉ `O(sqrt(n))`.

## 4) Khi nào dùng
- Bài toán divisor/multiple:
  - duyệt bội số của `i`
  - cộng đóng góp theo ước hoặc bội
- Sieve và một số bài number theory.
- DP có chuyển trạng thái theo dạng `i -> k*i` hoặc `i -> i/d`.
- Các bài có tổng dạng `sum f(i) * floor(n / i)`.

