# Combinatorics and Probability

## 1. Định nghĩa trạng thái `dp[i]`

Trong mô hình tổng quát (không phụ thuộc cây/đồ thị), giả sử cấu trúc được chia thành nhiều **block độc lập**.

Với mỗi block `i`:

- `s_i`: kích thước block `i`
- `dp[i]`: số cấu hình hợp lệ **bên trong** block `i`

Ta định nghĩa:

```text
dp[i] = số cấu hình hợp lệ bên trong block i
```

## 2. Khi gộp nhiều block lại

Giả sử cần ghép `k` block: `B_1, B_2, ..., B_k`.

- Tổng kích thước:

```text
S = Σ s_i
```

Quá trình đếm gồm 2 phần độc lập:

### 2.1. Chọn cấu hình nội bộ từng block

```text
Π dp[i]
```

### 2.2. Trộn thứ tự các block với nhau (shuffle)

```text
S! / (Π s_i!)
```

## 3. Transition tổng quát

Kết hợp hai phần trên:

```text
DP = (S! / Π s_i!) * Π dp[i]
```

Ý nghĩa:

- Đây là transition của phép **shuffle product** giữa các cấu trúc có thứ tự.
- Không phải transition riêng cho cây; áp dụng được cho nhiều mô hình có thành phần độc lập.

## 4. Dạng đệ quy tổng quát

Nếu một cấu trúc được tạo bằng cách:

- tách thành các thành phần con độc lập,
- rồi gộp lại,

thì có thể viết:

```text
dp[structure] = multinomial * Π dp[substructure]
```

Trong đó `multinomial` là hệ số tổ hợp khi trộn các thành phần con.
