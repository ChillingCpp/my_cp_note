# Matrix Multiplication

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/math/matmul.cpp)

## 1) Khi nào DP đổi sang nhân ma trận?

DP phải có dạng: $$dp_t[v] = \bigoplus_u \left(dp_{t-1}[u] \otimes W[u][v]\right).$$

Khi đó: $$dp_t = dp_{t-1} \star W.$$

Phép nhân ma trận tổng quát: $$(C = A \star B) \Rightarrow C[i][j] = \bigoplus_k \left(A[i][k] \otimes B[k][j]\right).$$

Trong đó:
- `⊕`: phép gộp (sum/min/max/or/...).
- `⊗`: phép nối khi chuyển trạng thái.
- `W`: ma trận chuyển.

## 2) Điều kiện bắt buộc (Semiring)

`⊕` và `⊗` phải tạo thành semiring:

| Điều kiện | Công thức |
| --- | --- |
| `⊕` kết hợp | \((a \oplus b) \oplus c = a \oplus (b \oplus c)\) |
| `⊗` kết hợp | \((a \otimes b) \otimes c = a \otimes (b \otimes c)\) |
| `⊗` phân phối qua `⊕` | \(a \otimes (b \oplus c) = (a \otimes b) \oplus (a \otimes c)\) |
| Phần tử trung lập | Tồn tại `zero` cho `⊕`, `one` cho `⊗` |

Nếu thỏa, phép nhân ma trận kết hợp nên có thể dùng lũy thừa nhanh.

## 3) Ý nghĩa của \(W^k\)

$((W^k)[i][j])$ là giá trị tốt nhất từ `i -> j` sau đúng `k` bước, vì: $$dp_k = dp_0 \star W^k.$$

## 4) Các semiring thường gặp

| Bài toán | \(\oplus\) | \(\otimes\) | `zero` | `one` |
| --- | --- | --- | --- | --- |
| Đếm số cách | \(+\) | \(\times\) | \(0\) | \(1\) |
| Shortest path đúng \(k\) cạnh | \(\min\) | \(+\) | \(+\infty\) | \(0\) |
| Longest path đúng \(k\) cạnh | \(\max\) | \(+\) | \(-\infty\) | \(0\) |
| Tồn tại đường đi | \(\lor\) | \(\land\) | `false` | `true` |


## 7) Quy trình áp dụng

1. Viết rõ công thức DP.
2. Tách rõ `⊕` và `⊗`.
3. Kiểm tra semiring.
4. Xây ma trận chuyển `W`.
5. Tính `W^k` bằng binary exponentiation.
6. Nhân với vector trạng thái ban đầu.

## 8) Khi nào nên dùng

- Tối ưu DP có chuyển trạng thái tuyến tính.
- Tính truy hồi tuyến tính bậc `k` khi `n` rất lớn.
- Đếm/đánh giá đường đi đúng `k` bước trên đồ thị.
- Gộp nhiều phép biến đổi tuyến tính thành một phép nhân.
- Keyword hay gặp: `k-th step`, `linear recurrence`, `transition matrix`, `count walks length k`.
- Không phù hợp nếu chuyển trạng thái phi tuyến hoặc không gian trạng thái quá lớn.

## 9) Ví dụ nhanh: Fibonacci

$$F_n = F_{n-1} + F_{n-2}, \quad state_n = [F_n, F_{n-1}]^T.$$

$$state_n = \begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix}^{n-1} \cdot state_1.$$

=> tính `F_n` trong `O(log n)`.

## 10) Lưu ý khi code

- Thường làm việc theo modulo (`1e9+7`, `998244353`, ...), nhớ `% mod` sau cộng/nhân.
- Ma trận không giao hoán: `A * B != B * A`.
- Xử lý đúng base case (`n=0`, `n=1`) trước khi lũy thừa.
