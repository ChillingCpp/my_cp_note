# Bài toán bracket (ngắn gọn)

## 1) Invariant bắt buộc
- Với `()` quy ước `(` = `+1`, `)` = `-1`, gọi `balance` là prefix sum.
- Chuỗi hợp lệ iff:
  - mọi prefix có `balance >= 0`;
  - `balance` cuối cùng bằng `0`.
- Đoạn `[l..r]` hợp lệ iff:
  - `balance[r] - balance[l-1] = 0`;
  - `min(balance[l..r]) - balance[l-1] >= 0`.

## 2) Các dạng chính và cách xử lý
| Dạng | Kỹ thuật chuẩn | Ghi chú |
|---|---|---|
| `valid` với `()` | Duyệt 1 lần, biến `bal` | Nếu có lúc `bal < 0` thì sai; cuối cùng cần `bal = 0`, `O(n)` |
| `longest valid parentheses` | Stack chỉ số + sentinel `-1` | Gặp `)` thì pop; rỗng thì push mốc mới, else cập nhật `ans = i - st.top()`, `O(n)` |
| `longest` (cách 2) | DP `dp[i]` = longest kết thúc tại `i` | Nếu `s[i]=')'`: `()` thì `dp[i]=dp[i-2]+2`; `))` thì xét `j=i-dp[i-1]-1`, `O(n)` |
| `count` số chuỗi đúng độ dài `2n` | Catalan hoặc DP `f[pos][bal]` | Catalan: `C(2n,n)/(n+1)`; DP dùng khi có ràng buộc/wildcard, thường `O(n^2)` |
| `k-th lexicographic` | DP đếm suffix + greedy từng ký tự | Thử đặt `(` trước, so số cách với `k`; nhớ check `k` không vượt tổng số cách |
| Query đoạn / update online | Segment tree bracket node | Node: `open, close, matched`; merge với `t=min(L.open,R.close)`; độ dài valid trong đoạn là `2*matched`, `O(log n)` |

## 3) Công thức Segment Tree bracket
- Merge `L`, `R`:
  - `t = min(L.open, R.close)`
  - `matched = L.matched + R.matched + t`
  - `open = L.open + R.open - t`
  - `close = L.close + R.close - t`
- Đoạn hợp lệ hoàn toàn khi `open = 0` và `close = 0`.

## 6) Link liên quan
- [Stack](<../Data_structure/STL/Stack.md>)
- [Segment Tree](<../Data_structure/Non-STL/Segment Tree.md>)
- [Lazy Segment Tree](<../Data_structure/Non-STL/Lazy Segment Tree.md>)
- [Các dạng DP chính](<../Dynamic Programming/Các dạng DP chính.md>)
- [Combinatorics and Probability](<../Math/Combinatorics and Probability.md>)
