# Basic Number Theory

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/math)

## Chủ đề nền tảng
- GCD/LCM.
- Prime test, sieve.
- Binary exponentiation `a^b mod m`.
- Extended Euclid.
- Inverse modulo.
- Euler phi, divisor function, CRT.

## 1. Chia hết và đồng dư
- `a | b` nghĩa là tồn tại `k` để `b = ak`.
- `a ≡ b (mod m)` <=> `m | (a - b)`.
- Chuẩn hóa modulo (để luôn không âm): `((x % m) + m) % m`.
- Tính chất:
  - `(a + b) mod m = ((a mod m) + (b mod m)) mod m`.
  - `(a - b) mod m = ((a mod m) - (b mod m) + m) mod m`.
  - `(a * b) mod m = ((a mod m) * (b mod m)) mod m`.
  - Nếu `a ≡ b (mod m)` thì `f(a) ≡ f(b) (mod m)` với `f` là đa thức hệ số nguyên.
- Luôn có `0 <= a mod b < b` với `b > 0`.
- phép `a mod b` chỉ thực hiện tối đa `log(a)` lần, có thể dùng cho range prunning

## 2. GCD / LCM
- `gcd(a, b) = gcd(b, a mod b)` (Euclid), độ phức tạp `O(log(min(a, b)))`.
- `gcd(a, 0) = |a|`, `gcd(0, 0) = 0`.
- `lcm(a, b) = |a / gcd(a, b) * b|`.
- `gcd(a, b) * lcm(a, b) = |ab|`.
- `gcd(ka, kb) = |k| * gcd(a, b)`.
- `gcd(a, b, c) = gcd(gcd(a, b), c)`.

## 3. Sàng số Harmonic
### 3.1. Số nguyên tố và phân tích thừa số
- Kiểm tra nguyên tố bằng trial division: thử đến `i * i <= n`, độ phức tạp `O(sqrt(n))`.
- Phân tích thừa số trong `O(sqrt(n))` nếu `n quá lớn`
- Phân tích chuẩn:
  - `n = p1^e1 * p2^e2 * ... * pk^ek` (các `pi` nguyên tố phân biệt).
- Smallest prime factor
    - Phân tích thừa số nguyên tố trong `log(a)` khi `a <= 1e6`
- Dạng toán: kiểm tra `a*b` có là số chính phương
  - Đặt `sqf(n) = ∏ pi^(ei mod 2)` với mọi prime `pi` trong phân tích của `n` (square-free kernel).
  - Khi đó: `a*b` là số chính phương <=> `sqf(a) = sqf(b)`.
  - Ứng dụng: đếm cặp `(i, j)` sao cho `ai*aj` là chính phương bằng cách group theo `sqf(ai)`.
- Sieve Eratosthenes



### 3.2. Euler Phi `phi(n)`
- Định nghĩa: số lượng `1 <= x <= n` sao cho `gcd(x, n) = 1`.
- Công thức:
  - Nếu `n = p1^e1 ... pk^ek`:
    - `phi(n) = n * (1 - 1/p1) * ... * (1 - 1/pk)`.
- Tính nhân:
  - Nếu `gcd(a, b) = 1` thì `phi(ab) = phi(a)phi(b)`.
- Identity hữu ích:
  - `sum_{d|n} phi(d) = n`.
- Sàng phi `1..N`:
  - `phi[i] = i` ban đầu.
  - Với mỗi prime `p`, cho mọi bội `j`: `phi[j] -= phi[j] / p`.

### 3.3. Hàm ước số
- Sử dụng sieve harmonic cho division count/sum/list
- Lưu trữ giá tri `k` nào đó thỏa `k mod i == 0` và `k` là 1 dạng số nào đó 

## 6. Lũy thừa nhanh và định lý
- Binary exponentiation:
  - Tính `a^b` hoặc `a^b mod m` trong `O(log b)`.
- Euler:
  - Nếu `gcd(a, m) = 1` thì `a^phi(m) ≡ 1 (mod m)`.
  - Suy ra `a^(k mod phi(m))` có thể rút gọn số mũ khi điều kiện nguyên tố cùng nhau thỏa.

## 7. Extended Euclid + phương trình Diophantine
- Extended Euclid tìm `x, y` sao cho:
  - `ax + by = g`, với `g = gcd(a, b)`.
- Phương trình `ax + by = c` có nghiệm <=> `gcd(a, b) | c`.
- Nếu có nghiệm riêng `(x0, y0)` cho `ax + by = c`, mọi nghiệm:
  - `x = x0 + k * (b / g)`.
  - `y = y0 - k * (a / g)`.
  - với `k ∈ Z`, `g = gcd(a, b)`.

## 9. Nghịch đảo modulo
- `a` có nghịch đảo mod `m` <=> `gcd(a, m) = 1`.
- Dùng Extended Euclid:
  - Tìm `x, y`: `ax + my = 1` => `x mod m` là nghịch đảo.
- Dùng pow:
  - Nếu `m` nguyên tố: `inv(a) = a^(m - 2) mod m`.
  - Nếu biết `phi(m)` và `gcd(a, m)=1`: `inv(a) = a^(phi(m) - 1) mod m`.
- Với mod nguyên tố `p`, tiền xử lý `inv[1..n]`:
  - `inv[1] = 1`.
  - `inv[i] = p - (p / i) * inv[p % i] % p`.

## 9. Đồng dư tuyến tính
- `ax ≡ b (mod m)`.
- Đặt `g = gcd(a, m)`.
  - Có nghiệm <=> `g | b`.
  - Nếu có, chia cả 3 cho `g`:
    - `a' = a/g`, `b' = b/g`, `m' = m/g`.
    - Nghiệm cơ bản: `x ≡ b' * inv(a') (mod m')`.
  - Có đúng `g` nghiệm khác nhau theo mod `m`.

## 10. Chinese Remainder Theorem (CRT)
- Hệ:
  - `x ≡ a1 (mod m1)`
  - `x ≡ a2 (mod m2)`
  - ...
- Nếu các `mi` đôi một nguyên tố cùng nhau:
  - Có nghiệm duy nhất theo mod `M = m1*m2*...*mk`.
  - Công thức ghép:
    - `Mi = M/mi`.
    - `ti = inv(Mi mod mi)`.
    - `x ≡ sum(ai * Mi * ti) (mod M)`.
- Trường hợp không pairwise coprime:
  - Cần điều kiện tương thích: `ai ≡ aj (mod gcd(mi, mj))`.

## 11. Công thức hay dùng trong CP
- [Harmonic Number](<Harmonic Number.md>).
- Legendre (số mũ của prime `p` trong `n!`):
  - `v_p(n!) = floor(n/p) + floor(n/p^2) + ...`.
- Trong tổ hợp:
  - `v_p(C(n, k)) = v_p(n!) - v_p(k!) - v_p((n-k)!)`.
- Mẹo chia đoạn theo thương `n / i`:
  - Nếu `q = n / l` thì `r = n / q`, mọi `i ∈ [l, r]` có cùng thương `q`.
  - Duyệt được trong `O(sqrt(n))` số đoạn.
