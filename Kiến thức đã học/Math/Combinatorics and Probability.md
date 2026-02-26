# Combinatorics and Probability

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/math)

- số cách chèn 1 chuỗi a vào dãy S
    - $$\binom{|S| + |a|}{|a|}$$

## DP đếm cấu hình

`dp[i]` = số cấu hình hợp lệ bên trong block `i`  
`s_i` = kích thước block `i`

## Công thức gộp block (shuffle)
Với các block độc lập `B_1..B_k`, đặt:
$S = \sum s_i$

Số cách gộp:
$dp[i] = (\frac{S!}{\prod s_i!}) * \prod dp[sub_i]$
Trong đó:
- $\prod dp[i]$: chọn cấu hình nội bộ từng block
- $(\frac{S!}{\prod s_i!})$: trộn thứ tự phần tử giữa các block

## Dạng đệ quy tổng quát

$dp[structure] = multinomial * \prod dp[substructure]$
`multinomial` là hệ số tổ hợp khi trộn các thành phần con độc lập.

