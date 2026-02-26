# Basic Number Theory

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/math)

## Chủ đề nền tảng
- GCD/LCM.
- Prime test, sieve.
- Binary exponentiation `a^b mod m`.
- Extended Euclid.
- Inverse modulo.

## Một số tính chất quan trọng
- phép `a mod b` chia làm 2 trường hợp :
	- `a < b` : = a
	- `a >= b` : < a / 2
		- phép `a mod b` hoạt động tối đa `log a` lần nên gcd(a, b) có độ phức tạp log 
		- 
 ## Công thức đếm ước
- Nếu `n = p1^f1 * p2^f2 * ... * pk^fk` thì:
`num_divisors(n) = (f1 + 1)(f2 + 1)...(fk + 1)`.
- siêu hợp số <= N : là số có số lượng ước số lớn nhất <= N
	- sinh siêu hợp số từ 1 -> 1e18 bằng backtracking
- Các só chính phương có số lượng ước số là lẻ
## Kỹ thuật liên quan
- [Harmonic Number](<Harmonic Number.md>)
- Euler phi : phi[j] -= phi[j] / i.
- Smallest prime factor (SPF).
- divisor count/sum/list

