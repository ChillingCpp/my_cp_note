# DP Digit

## Đường dẫn
[[Các dạng DP chính]]

## Mục tiêu
- Giải các bài toán trên đoạn số nguyên `[L, R]` với ràng buộc theo chữ số.
- Chuẩn hóa về hàm tiền tố:
  - `Ans([L, R]) = F(R) - F(L - 1)`
  - `F(X)`: kết quả trên đoạn `[0, X]`.

## Mô hình trạng thái tổng quát
Với `X >= 0`, tách `X` thành mảng chữ số `dig[0..n-1]` từ trái sang phải.

Định nghĩa:
`DP(pos, tight, started, state) -> T`

Trong đó:
- `pos`: đang xét đến vị trí thứ `pos` (`0..n`).
- `tight` (`0/1`): tiền tố đã chọn có còn đúng bằng tiền tố của `X` hay không.
- `started` (`0/1`): đã đặt chữ số khác `0` hay chưa (xử lý leading zero).
- `state`: trạng thái phụ mô tả ràng buộc (mod, tổng chữ số, automaton, ...).
- `T`: kiểu giá trị trả về (đếm, min/max, tổng, vector thống kê, ...).

## Công thức chuyển trạng thái
Giới hạn chữ số ở vị trí `pos`:
`lim = (tight ? dig[pos] : 9)`

Với mỗi chữ số `d` trong `[0, lim]`:
- `nstarted = started || (d != 0)`
- `ntight = tight && (d == dig[pos])`
- `nstate = Transition(state, d, nstarted)`

Chỉ xét nhánh hợp lệ theo ràng buộc tiền tố, khi đó:

`DP(pos, tight, started, state)`
`= ⨁_{d=0..lim} Lift( DP(pos+1, ntight, nstarted, nstate), d, pos )`

Trong đó:
- `⨁`: phép gộp kết quả (thường là cộng, min, max, hoặc gộp struct).
- `Lift`: cách cộng thêm đóng góp của chữ số hiện tại vào kết quả con.

Điều kiện dừng:
- Nếu `pos == n`: trả `Base(started, state)`.

## Khung đại số để tái sử dụng
Xem `T` như một monoid:
- `identity()`: phần tử trung hòa.
- `combine(a, b)`: phép gộp (`⨁`).
- `base(...)`: giá trị ở lá.
- `lift(...)`: nhúng đóng góp của cạnh hiện tại.

Nhờ vậy cùng một bộ khung có thể dùng cho:
- Đếm số lượng.
- Tính tổng chữ số / tổng giá trị số.
- Tối ưu min/max có ràng buộc.

## Công thức cho các kiểu truy vấn phổ biến
### 1) Đếm số lượng
- `T = long long`
- `combine = +`
- `lift(child, ...) = child`
- `base = 1 nếu state hợp lệ, ngược lại 0`

### 2) Tính tổng giá trị các số thỏa (không chỉ đếm)
Đặt `T = (cnt, sum)`:
- `cnt`: số lượng cách từ suffix.
- `sum`: tổng giá trị các số suffix tạo ra.

Nếu còn `k = n - pos - 1` vị trí phía sau, thì:
- `new_cnt += child.cnt`
- `new_sum += child.sum + child.cnt * d * 10^k`

## Thiết kế `state` phụ (mẫu tổng quát)
- Chia hết cho `m`:
  - `state = rem`
  - `Transition: rem' = (rem * 10 + d) mod m`
- Tổng chữ số:
  - `state = s`
  - `Transition: s' = s + d`
- Ràng buộc giữa các chữ số kề nhau:
  - `state = (prev_digit, flag, ...)`
- Chứa/tránh một pattern:
  - `state = node` của automaton (KMP/Aho).

Nguyên tắc: `state` phải "đủ và tối thiểu" để quyết định tương lai, không giữ thông tin dư.

## Chiến lược giải chuẩn
1. Viết lại bài toán thành `F(X)` trên đoạn `[0, X]`.
2. Xác định rõ `state`, `Transition`, `Base`.
3. Chọn kiểu `T` và `combine/lift` đúng mục tiêu.
4. Viết DFS + memo với trạng thái `(pos, tight, started, state)`.
5. Tính đáp án cuối bằng `F(R) - F(L - 1)`.
6. Brute force trên range nhỏ để kiểm chứng.

## Tối ưu và độ phức tạp
- Thường chỉ memo khi `tight = 0` để tái sử dụng mạnh.
- Thời gian:
  - `O(n * |State| * 10 * số_flag_phụ)`
- Bộ nhớ:
  - `O(n * |State| * số_flag_phụ)`

## Binary Search + Digit DP
- Lưu ý: thường **không** nói `dfs(...)` monotone theo trạng thái; hàm hay dùng để binary search là hàm tiền tố `F(X) = solve(X)`.
- Khi truy vấn là dạng:
  - "tìm `X` nhỏ nhất sao cho `F(X) >= K`"
  - hoặc predicate `P(X)` monotone, ví dụ `P(X): F(X) >= K`
  thì dùng binary search trên `X`.

Điều kiện áp dụng:
- `F(X)` phải đơn điệu không giảm theo `X` (đúng với đa số bài toán đếm/tích lũy).
- Biên tìm kiếm `[lo, hi]` xác định được (thường theo đề hoặc `0..10^18`).

Khuôn:
```cpp
long long first_true(long long lo, long long hi) { // [lo, hi]
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (solve(mid) >= K) hi = mid;   // P(mid) = true
        else lo = mid + 1;
    }
    return lo;
}
```

Độ phức tạp:
- `O(log(hi-lo+1) * cost_solve)`
- với `cost_solve ~ O(n * |State| * 10 * số_flag_phụ)`.

## Checklist tránh lỗi
- `X < 0` thì `F(X) = 0`.
- Quy ước số `0` có được tính hay không phải thể hiện rõ trong `Base`.
- Leading zero có cập nhật `state` hay không phải nhất quán.
- Reset memo đúng cách giữa các lần gọi `F(X)` khi cần.
- Cẩn thận overflow (`int64`, mod, hoặc big integer).
- Cận là inclusive: `[L, R]`.
- Khi binary search, kiểm tra trước `solve(hi) >= K`; nếu không thì "không tồn tại đáp án".

## Khung giả mã tổng quát
```cpp
T dfs(int pos, bool tight, bool started, State s) {
    if (pos == n) return base(started, s);

    if (!tight && vis[pos][started][s]) return memo[pos][started][s];

    int lim = tight ? dig[pos] : 9;
    T ans = identity();

    for (int d = 0; d <= lim; ++d) {
        bool nstarted = started || (d != 0);
        State ns = next_state(s, d, nstarted);
        if (!valid_prefix(ns, nstarted)) continue;

        bool ntight = tight && (d == dig[pos]);
        T child = dfs(pos + 1, ntight, nstarted, ns);
        ans = combine(ans, lift(child, d, pos));
    }

    if (!tight) {
        vis[pos][started][s] = true;
        memo[pos][started][s] = ans;
    }
    return ans;
}

T solve(long long X) {
    if (X < 0) return identity_zero_query();
    dig = to_digits(X);
    n = dig.size();
    clear_memo();
    return dfs(0, true, false, init_state());
}

// Answer on [L, R]
// solve(R) - solve(L - 1)
```
