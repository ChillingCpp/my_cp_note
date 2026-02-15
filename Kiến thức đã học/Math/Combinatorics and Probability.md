# Combinatorics and Probability

- số cách chèn 1 chuỗi a vào dãy S
    -$ \[ \binom{abs(S)+ abs(a)}{abs(a)} \]$

## DP đếm cấu hình

`dp[i]` = số cấu hình hợp lệ bên trong block `i`  
`s_i` = kích thước block `i`

## Công thức gộp block (shuffle)
Với các block độc lập `B_1..B_k`, đặt:
`S = Σ s_i`

Số cách gộp:
`dp[i] = (S! / Π s_i!) * Π dp[sub_i]`
Trong đó:
- `Π dp[i]`: chọn cấu hình nội bộ từng block
- `S! / Π s_i!`: trộn thứ tự phần tử giữa các block

## Dạng đệ quy tổng quát

`dp[structure] = multinomial * Π dp[substructure]`
`multinomial` là hệ số tổ hợp khi trộn các thành phần con độc lập.
