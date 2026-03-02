# Basic Math

## 0) Hằng đẳng thức cơ bản

- $(a+b)^2 = a^2 + 2ab + b^2$.
- $(a-b)^2 = a^2 - 2ab + b^2$.
- $a^2 - b^2 = (a-b)(a+b)$.
- $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$.
- $(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$.
- $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$.
- $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$.
- $(a+b+c)^2 = a^2 + b^2 + c^2 + 2(ab+bc+ca)$.

## 1) Công thức tổng cơ bản

- $\sum_{i=1}^{n} i = \dfrac{n(n+1)}{2}$.
- $\sum_{i=1}^{n} i^2 = \dfrac{n(n+1)(2n+1)}{6}$.
- $\sum_{i=1}^{n} i^3 = \left(\dfrac{n(n+1)}{2}\right)^2$.
- Cấp số cộng:
  - $a_n = a_1 + (n-1)d$.
  - $S_n = \dfrac{n(a_1+a_n)}{2} = \dfrac{n(2a_1+(n-1)d)}{2}$.
- Cấp số nhân:
  - $a_n = a_1r^{n-1}$.
  - $S_n = a_1\dfrac{r^n-1}{r-1}$ với $r\neq 1$.
  - $S_\infty = \dfrac{a_1}{1-r}$ khi $|r|<1$.

## 2) Nhị thức Newton

- $(x+y)^n = \sum_{k=0}^{n} \binom{n}{k}x^{n-k}y^k$.
- Hệ số của $x^k$ trong $(1+x)^n$ là $\binom{n}{k}$.

## 3) Log, mũ, căn

- $a^{m+n}=a^m a^n$, $a^{m-n}=a^m/a^n$.
- $(a^m)^n=a^{mn}$.
- $\log_a(xy)=\log_a x + \log_a y$.
- $\log_a(x/y)=\log_a x - \log_a y$.
- $\log_a(x^k)=k\log_a x$.
- Đổi cơ số: $\log_a b = \dfrac{\log_c b}{\log_c a}$.

## 4) Phương trình bậc hai và Viète

Với $ax^2+bx+c=0$, $a\neq 0$:

- $\Delta = b^2-4ac$.
- $x_{1,2}=\dfrac{-b\pm\sqrt{\Delta}}{2a}$.
- Nếu nghiệm là $x_1,x_2$ thì:
  - $x_1+x_2=-\dfrac{b}{a}$.
  - $x_1x_2=\dfrac{c}{a}$.

## 5) Giá trị tuyệt đối và bất đẳng thức tam giác

- $|x|=\begin{cases}x,&x\ge 0\\-x,&x<0\end{cases}$.
- $|ab|=|a||b|$, $\left|\dfrac{a}{b}\right|=\dfrac{|a|}{|b|}$ ($b\neq 0$).
- $|a+b|\le |a|+|b|$.
- $||a|-|b||\le |a-b|$.

## 6) Bất đẳng thức tứ giác (Quadrangle Inequality)

Với hàm chi phí $w(i,j)$ (thường dùng trong DP trên đoạn), nếu
$a \le b \le c \le d$ thì:

$$
w(a,c)+w(b,d)\le w(a,d)+w(b,c).
$$

Dạng tương đương trên ma trận Monge:

$$
A[i][j] + A[i+1][j+1] \le A[i][j+1] + A[i+1][j].
$$

Ghi chú nhanh:
- Đây là điều kiện quan trọng trong các tối ưu DP như Knuth/Monge optimization.
- Thường đi kèm tính đơn điệu của điểm chia tối ưu.

## 7) Mẫu tối ưu hay gặp trong CP

### 7.1. Chặn dưới tổng bình phương khi biết tổng

Nếu $\sum x_i = S$ thì:

- $\sum x_i^2 \ge \dfrac{S^2}{n}$.

Ứng dụng:

- Chặn lower bound cho cost dạng bình phương.
- Ước lượng nhanh độ lớn trong chứng minh độ phức tạp/đánh giá đáp án.
