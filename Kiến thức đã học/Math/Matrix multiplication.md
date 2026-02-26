# Matrix Multiplication

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/math/matmul.cpp)

## Ý tưởng cốt lõi
- Ma trận biểu diễn phép biến đổi tuyến tính của trạng thái.
- Nếu có chuyển trạng thái 1 bước: `state_{t+1} = M * state_t` thì sau `n` bước:
`state_n = M^n * state_0`.
- Khi `n` rất lớn, tính `M^n` bằng binary exponentiation (`log n` lần nhân ma trận).

## Tính chất ứng dụng giải bài
- Dùng để tối ưu DP khi chuyển trạng thái là tuyến tính.
- Dùng cho truy hồi tuyến tính bậc `k` khi `n` rất lớn.
- Dùng để đếm số đường đi đúng `k` bước (nâng lũy thừa ma trận kề).
- Dùng để gộp nhiều phép biến đổi tuyến tính liên tiếp thành 1 phép nhân ma trận.
- Keyword nhận diện: `k-th step`, `linear recurrence`, `transition matrix`, `count walks length k`.
- Không phù hợp nếu chuyển trạng thái không tuyến tính hoặc số chiều trạng thái quá lớn.

## Chuyển DP sang nhân ma trận (quan trọng)
- Chỉ chuyển được dạng chuẩn ( rút gọn state step ):
    - $dp[i] = c1*dp[i-1] + c2*dp[i-2] + ... + ck*dp[i-k] + d1 + ... + dm$.
    - Bản ngắn gọn : $dp_i = \sum_{t=1}^{k} c_t\, *  dp_{i-t} + d1 + ... + dm$.
    - $d1 + ... + dm$ là 1 biến phụ không thay đổi theo step
- Đặt:
    - `state_i = [dp[i], dp[i-1], ..., dp[i-k+1]]^T`.
- Khi đó:
    - `state_i = M * state_{i-1}`, với ma trận chuyển:
    `M =`
    ```
    [c1 c2 c3 ... c(k-1) ck d1 ... dm]
    [ 1  0  0 ...     0  0  0  ... 0]
    [ 0  1  0 ...     0  0  0  ... 0]
    [...............................]
    [ 0  0  0 ...     1  0  0  ... 0]
    [ 0  0  0 ...     0  0  1  ... 0]
    [...............................]
    [ 0  0  0 ...     0  0  0  ... 1]
    ```

### Ví dụ đặt hệ số
- `dp[i] = 2*dp[i-1] + 5*dp[i-3] - dp[i-4]` (bậc `k=4`).
- State: `state_i = [dp[i], dp[i-1], dp[i-2], dp[i-3]]^T`.
- Hàng đầu của `M` là `[2, 0, 5, -1]`.
- Nếu modulo `mod`, thay `-1` bằng `mod-1`.

## Ví dụ nhanh: Fibonacci
- $F_n = F_{n-1} + F_{n-2}$.
- Đặt $state_n = [F_n, F_{n-1}]^T$.
- Khi đó:
$state_n = \begin{bmatrix} 1 & 1 \\ 1 & 0\end{bmatrix} ^{(n-1)} * state_1$.
- Tính được $F_n$ trong `O(log n)`.

## Lưu ý khi code
- Thường tính theo modulo (`1e9+7`, `998244353`, ...), nhớ `% mod` sau mỗi phép cộng/nhân.
- Cẩn thận thứ tự nhân: ma trận không giao hoán (`A*B != B*A`).
- Kiểm tra đúng chỉ số base case (`n=0`, `n=1`) trước khi nâng lũy thừa.
