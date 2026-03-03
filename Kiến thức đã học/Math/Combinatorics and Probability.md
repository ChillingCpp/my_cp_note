# Combinatorics and Probability

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/math)

## 0) Ký hiệu cơ bản

- $n! = 1 \cdot 2 \cdot \ldots \cdot n,\quad 0! = 1$.
- $P(n,k)=n(n-1)\cdots(n-k+1)=\dfrac{n!}{(n-k)!}$.
- $\binom{n}{k}=\dfrac{n!}{k!(n-k)!}$.
- $\binom{n}{k}=\binom{n}{n-k}$.

## 1) Quy tắc đếm nền tảng

- Quy tắc cộng: hai cách chọn rời nhau, tổng số cách bằng tổng.
- Quy tắc nhân: làm lần lượt nhiều bước độc lập, số cách bằng tích.
- Song ánh: đếm $A$ bằng cách đếm $B$ nếu có song ánh $A \leftrightarrow B$.

## 2) Hoán vị - chỉnh hợp - tổ hợp

### 2.1. Hoán vị

- Hoán vị $n$ phần tử phân biệt: $n!$.
- Hoán vị có lặp, với tần suất $a_1,a_2,\ldots,a_m$ và $n=\sum_{i=1}^m a_i$:
    - Số cách: $\dfrac{n!}{a_1!a_2!\cdots a_m!}$.
- Hoán vị vòng tròn $n$ phần tử phân biệt:
    - $(n-1)!$.

### 2.2. Chỉnh hợp

- Chọn có thứ tự $k$ phần tử từ $n$ phần tử:
    - $P(n,k)=\dfrac{n!}{(n-k)!}$.

### 2.3. Tổ hợp

- Chọn không thứ tự $k$ phần tử từ $n$ phần tử:
    - $\binom{n}{k}$.
- Chọn lặp $k$ phần tử từ $n$ loại:
    - $\binom{n+k-1}{k}$.

## 3) Đồng nhất thức tổ hợp quan trọng

- Pascal:
    - $\binom{n}{k}=\binom{n-1}{k}+\binom{n-1}{k-1}$.
- Tổng hàng:
    - $\sum_{k=0}^{n}\binom{n}{k}=2^n$.
- Tổng có trọng số:
    - $\sum_{k=0}^{n}k\binom{n}{k}=n2^{n-1}$.
- Hockey-stick:
    - $\sum_{i=r}^{n}\binom{i}{r}=\binom{n+1}{r+1}$.
- Vandermonde:
    - $\sum_{k}\binom{a}{k}\binom{b}{m-k}=\binom{a+b}{m}$.
- Multinomial:
    - $\binom{n}{a_1,a_2,\ldots,a_m}=\dfrac{n!}{a_1!a_2!\cdots a_m!}$, với $\sum_{i=1}^{m}a_i=n$.

## 4) Stars and Bars (chia bi vào hộp)

- Nghiệm nguyên không âm của $x_1+\cdots+x_k=n$:
    - $\binom{n+k-1}{k-1}$.
- Nghiệm nguyên dương của $x_1+\cdots+x_k=n$:
    - $\binom{n-1}{k-1}$.
- Có chặn trên $x_i\le u_i$:
    - Dùng Inclusion-Exclusion.

## 5) Inclusion-Exclusion (PIE)

Với tập điều kiện xấu $A_1,\ldots,A_m$:

$$
\left|\bigcup_{i=1}^{m}A_i\right|
=
\sum_i |A_i|
-\sum_{i<j}|A_i\cap A_j|
+\sum_{i<j<k}|A_i\cap A_j\cap A_k|
-\cdots
+(-1)^{m+1}|A_1\cap\cdots\cap A_m|.
$$

$$
|good|=|U|-\left|\bigcup_{i=1}^{m}A_i\right|.
$$

### Derangement (hoán vị không điểm cố định)

- $!n=n!\sum_{i=0}^{n}\dfrac{(-1)^i}{i!}$.
- Xấp xỉ: $!n\approx \dfrac{n!}{e}$.

## 6) Khai triển nhị thức và hệ số

- Binomial theorem:
    - $(x+y)^n=\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k$.
- Hệ số của $x^k$ trong $(1+x)^n$ là $\binom{n}{k}$.
- Hệ số của $x^m$ trong tích đa thức là tổng chập (convolution) bậc $m$.

## 7) Xác suất cơ bản

- Không gian mẫu $\Omega$, biến cố $A$.
- Nếu đồng khả năng:
    - $P(A)=\dfrac{|A|}{|\Omega|}$.
- Quy tắc cộng:
    - $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
- Xác suất có điều kiện:
    - $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$, với $P(B)>0$.
- Quy tắc nhân:
    - $P(A\cap B)=P(A)P(B\mid A)=P(B)P(A\mid B)$.
- Độc lập:
    - $A,B$ độc lập khi $P(A\cap B)=P(A)P(B)$.

## 8) Total Probability và Bayes

- Công thức xác suất toàn phần (với phân hoạch $B_1,\ldots,B_m$):
    - $P(A)=\sum_i P(A\mid B_i)P(B_i)$.
- Bayes:
    - $P(B_j\mid A)=\dfrac{P(A\mid B_j)P(B_j)}{\sum_i P(A\mid B_i)P(B_i)}$.

## 9) Kỳ vọng - phương sai

- $E[X]=\sum_x x\,P(X=x)$ (rời rạc).
- Tuyến tính kỳ vọng:
    - $E[X+Y]=E[X]+E[Y]$ (không cần độc lập).
- Indicator trick:
    - $\mathbf{1}_A\in\{0,1\}$, $E[\mathbf{1}_A]=P(A)$.
    - Hay dùng để đếm số đối tượng thỏa điều kiện.
- $\mathrm{Var}(X)=E[X^2]-E[X]^2$.
- $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$.
- Nếu độc lập:
    - $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$.

## 10) Công thức gộp block trong DP đếm cấu hình

- $dp[i]$: số cấu hình hợp lệ bên trong block $i$.
- $s_i$: kích thước block $i$.

Với các block độc lập $B_1,\ldots,B_k$, đặt:
- $S=\sum_i s_i$.

Số cách gộp:

$$
\mathrm{ways}
=
\frac{S!}{\prod_i s_i!}
\cdot
\prod_i dp[B_i].
$$

Trực giác:
- $\prod_i dp[B_i]$: chọn cấu hình nội bộ từng block.
- $\dfrac{S!}{\prod_i s_i!}$: số cách trộn thứ tự các block (multinomial shuffle).

Dạng đệ quy tổng quát:

$$
dp[\text{structure}]
=
\text{multinomial}
\cdot
\prod_{\text{sub}} dp[\text{substructure}].
$$

## 11) Một số mẫu dùng nhanh trong CP

- Số cách chèn chuỗi $a$ vào dãy $S$:
    - $\binom{|S|+|a|}{|a|}$.
- Chọn ngẫu nhiên 2 phần tử khác nhau từ $n$ phần tử:
    - Tổng số cặp $\binom{n}{2}$.
- "Ít nhất một" biến cố:
    - Dùng bù: $1-P(\text{không có biến cố nào})$.
- "Đúng $k$ lần thành công trong $n$ lần thử độc lập":
    - Binomial.

## 12) Ghi chú triển khai modulo (CP)

- Thường dùng $mod=10^9+7$ hoặc $998244353$.
- Tiền xử lý:
    - $fac[i]=i!\bmod mod$.
    - $invfac[i]=(i!)^{-1}\bmod mod$.
- Khi $mod$ là số nguyên tố:
    - $inv(x)=x^{mod-2}\bmod mod$ (Fermat).
    - $\binom{n}{k}\bmod mod=fac[n]\cdot invfac[k]\cdot invfac[n-k]\bmod mod$.
- $n$ rất lớn, $mod$ nhỏ nguyên tố:
    - Cân nhắc Lucas theorem.
