# DP Pattern theo cấu trúc chuyển state

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/dp)

## 0. Tiêu chí phân loại gốc

### 0. Mô hình hóa
- Xem DP như một đồ thị chuyển trạng thái có hướng:
	- Mỗi state là một đỉnh u
	- Mỗi transition hợp lệ là một cạnh có hướng u → v
	- Gọi Next(u) là tập các cạnh chuyển hợp lệ đi ra từ u tới 1 hoặc nhiều đỉnh khác nhau
	- DP luôn có 1 fixed set edges cố định, nhưng chỉ những edges hợp lệ mới được tính toán

### 1. Phân loại theo đồ thị chuyển trạng thái:

- Gọi `Next(state)` là tập state có thể chuyển tới từ `state`.
- `DP có lựa chọn`: tồn tại state có nhiều cạnh hợp lệ, tức `|Next(state)| > 1`.
- `DP không lựa chọn`: mọi state có nhiều nhất 1 cạnh hợp lệ, tức `|Next(state)| <= 1`.

## I. DP CÓ LỰA CHỌN

### 1. Mẫu công thức

- Dạng tổng quát:
  - `dp[u] = combine_{e ∈ Trans(u)} ( cost(e) ⊕ dp[to(e)] )
`
  - `combine` có thể là `min/max/sum/or...`.

### 2. Dấu hiệu nhận diện

- Từ một state có nhiều nhánh chuyển tiếp.
- Có vòng lặp duyệt danh sách nhánh `choice/next`.
- Có bước gộp kết quả từ nhiều nhánh (kể cả cộng tất cả để đếm).

### 3. Nhóm bài điển hình

- Pick/Skip DP: Knapsack, House Robber.
  - mỗi bước có nhiều phương án (lấy/bỏ), rồi gộp kết quả theo mục tiêu của bài.
  - Công thức mẫu: `dp[i] = combine( dp[i-1], gain(i) + dp[prev(i)] )`, với `combine` là `max/min/sum`.
- Chọn số lượng/phân phối tài nguyên: Unbounded/Bounded Knapsack, chia tài nguyên cho nhóm.
  - nhiều cách chọn số lượng `k` cho mỗi món/nhóm để tối ưu.
  - Công thức mẫu: `dp[i][w] = combine_{k in feasible}( dp[i-1][w - k*cost(i)] + value(i,k) )`.
- Chọn điểm tách:  Interval DP
  - state là đoạn `dp[l][r]`  thử nhiều điểm chia `k` có thể để lấy kết quả tốt nhất.
  - Công thức mẫu: `dp[l][r] = combine_{k in [l,r)}( dp[l][k] + dp[k+1][r] + cost(l,r) )`.
- Chọn số nhóm/đoạn: Partition DP theo số nhóm `k`.
  - chọn điểm chia có ràng buộc số đoạn/nhóm.
  - Công thức mẫu: `dp[i][g] = combine_{j<i}( dp[j][g-1] + cost(j+1,i) )`.
- Chọn trạng thái/cấu hình: Bitmask DP, TSP, Assignment DP, Digit DP, Tree DP.
  - từ mỗi cấu hình hiện tại có nhiều cách đi tiếp hợp lệ, nên phải duyệt nhánh và gộp.
  - Công thức mẫu: `dp[mask][i] = combine_{j in (mask \ {i})}( dp[mask^(1<<i)][j] + trans(j,i) )`.
- Chọn hành động theo lượt: Game DP, Minimax.
  - mỗi lượt có nhiều nước đi; state gộp theo luật đối kháng (`max/min` theo người chơi).
  - Công thức mẫu: `dp[state] = combine_{move in moves(state)}( gain(move) - dp[next(state,move)] )`.
- Chọn thao tác chuyển đổi: Edit Distance, String transform DP.
  - mỗi state có nhiều thao tác chuyển tiếp (chèn/xóa/sửa/giữ), rồi lấy chi phí tốt nhất.
  - Công thức mẫu: `dp[i][j] = combine( dp[i-1][j] + cost_del, dp[i][j-1] + cost_ins, dp[i-1][j-1] + cost_sub(i,j) )`.
- Di chuyển trên lưới/đồ thị có nhiều bước hợp lệ: Grid DP, đường đi trên DAG.
  - mỗi ô/đỉnh có nhiều hướng đi hợp lệ.
  - Công thức mẫu: `dp[v] = combine_{u in pred(v)}( dp[u] + cost(u,v) )`.
- DP đếm có phân nhánh: đếm đường đi, đếm số cách tạo cấu hình.
  - không chọn một nhánh tốt nhất mà xét toàn bộ nhánh hợp lệ.
  - Công thức mẫu: `dp[state] = sum_{nxt in Next(state)} ways(state,nxt) * dp[nxt]`.

### 4. Lưu ý

- "Lựa chọn" có thể ẩn trong state, không nhất thiết xuất hiện chữ "chọn" trong đề.
- Nếu `|Next(state)| > 1` thì mặc định nên xem là nhánh lựa chọn, kể cả bài đếm.

---

## II. DP KHÔNG LỰA CHỌN (HOẶC CHỈ 1 LỰA CHỌN)

### 1. Mẫu công thức

- Dạng chuyển tiếp duy nhất:
  - `dp[next(state)] = f(dp[state], data)` nếu `next(state)` hợp lệ.
- Dạng truy hồi chỉ số cố định:
  - `dp[i] = g(dp[i-1], dp[i-2], ...)` với các chỉ số phụ thuộc đã cố định bởi công thức.

```cpp
for (state in order) {
    nxt = next(state); // duy nhat theo quy tac
    if (valid(nxt)) {
        dp[nxt] = f(dp[state], data[state]);
    }
}
```

### 2. Dấu hiệu nhận diện

- Mỗi state chỉ có 0 hoặc 1 nhánh hợp lệ.
- Không có vòng lặp duyệt danh sách phương án tại một state.
- Chuyển tiếp được xác định sẵn bởi quy tắc; chỉ có thể bị chặn bởi điều kiện biên.

### 3. Nhóm bài điển hình

- Prefix/Suffix recurrence, Fibonacci chuẩn.
  - công thức cập nhật là cố định theo chỉ số, không phát sinh nhánh quyết định tại mỗi state.
  - Công thức mẫu: `dp[i] = f(dp[i-1], a[i])` hoặc `dp[i] = g(dp[i-1], dp[i-2])`.
- Recurrence tuyến tính bậc `k` cố định.
  - số lượng chỉ số phụ thuộc là hằng số, không có nhánh lựa chọn.
  - Công thức mẫu: `dp[i] = combine_linear( dp[i-1..i-k], coeffs )`.
- DP mô phỏng hệ deterministic.
  - từ state hiện tại và input tương ứng, state kế tiếp được xác định duy nhất.
  - Công thức mẫu: `state_{t+1} = next(state_t, input_t)` hoặc `dp[t+1][next(s,input_t)] = trans(dp[t][s], input_t)`.
- DP theo thời gian với luật cập nhật cố định.
  - trạng thái ở thời điểm `t+1` suy ra trực tiếp từ `t`, không có hành động để lựa chọn.
  - Công thức mẫu: `dp[t+1] = F(dp[t], input_t)`.
- DP cập nhật tuần tự 1 hướng.
  - mỗi bước chỉ truyền sang một state kế tiếp theo quy tắc, nếu ra ngoài biên thì bỏ.
  - Công thức mẫu: `dp[i+1] = g(dp[i], a[i+1])`.
- DP tích lũy min/max cố định.
  - chỉ lấy min/max trên chuỗi theo quy tắc cố định, không có nhánh.
  - Công thức mẫu: `best[i] = combine(best[i-1], val[i])` với `combine` là `min/max`.

---

## III. DP TRẠNG THÁI HỮU HẠN (FINITE-STATE DP)

### 1. Ý tưởng cốt lõi

- Mỗi phần tử chỉ có `k` trạng thái hữu hạn (thường k nhỏ).
- Mỗi state mô tả cấu hình cục bộ của phần tử: màu, bật/tắt, kiểu đặt, trạng thái automaton, ...
- DP lưu kết quả cho từng state của phần tử hiện tại: `dp[states][k]`.
- DP này vừa có thể là không có lựa chọn, vừa có thể là có lựa chọn.

### 2. Mô hình tổng quát

- 1 chiều (mảng/chuỗi):
  - `dp[i][s]` = giá trị tốt nhất / số cách khi xử lý đến phần tử `i` và phần tử `i` ở trạng thái `s`.
  - Chuyển tiếp:
    - `dp[i][s] = combine_{p ∈ Prev(s)}( dp[i-1][p] ⊕ cost(i,s,p) )`
  - `Prev(s)` là tập state trước đó có thể chuyển sang `s`.
- 2 chiều (lưới):
  - Nếu phụ thuộc cục bộ (trên, trái): `dp[i][j][s]` với chuyển tiếp từ `dp[i-1][j][*]`, `dp[i][j-1][*]`.
  - Nếu phụ thuộc cả hàng/cột: dùng state theo hàng/bitmask: `dp[row][mask]`.
- Đồ thị / cây:
  - Cây: `dp[u][s]` = gộp từ các con `v` qua các state tương thích.
  - Đồ thị có chu trình: cần thứ tự topo (DAG) hoặc thêm trục thời gian/bước đi để tránh vòng lặp.

### 3. Nhận diện nhanh

- Mỗi vị trí/đỉnh có số trạng thái nhỏ và cố định.
- Ràng buộc chủ yếu là giữa các phần tử kề nhau (adjacent) hoặc theo cạnh.
- Công thức có vòng lặp qua state trước/sau, thường là `O(k^2)` mỗi phần tử.
	- Partition DP

### 4. Ví dụ điển hình

- Tô màu dãy/đồ thị với `k` màu và ràng buộc kề nhau.
  - `dp[i][s] = min_{p != s}( dp[i-1][p] ) + cost(i,s)`
- Đếm số chuỗi độ dài `n` tránh một mẫu cấm bằng automaton (DFA).
  - `dp[i+1][next(s,c)] += dp[i][s]`
- Bài đặt trạng thái nhỏ theo ô lưới (đặt gạch, chọn hướng, ...).
- Tree DP với `k` trạng thái mỗi đỉnh (chọn/không chọn, màu, trạng thái bảo vệ, ...).


### 5. Lưu ý tối ưu

- Độ phức tạp thường là `O(f(x))`
- Nếu `Prev[s]` nhỏ hằng số → `O(f(x)*k)`.
- Nếu dùng `min/max` trên tất cả state trước đó, có thể dùng prefix/suffix best để tối ưu.
- Với đếm số cách, chú ý modulo.

---

## IV. Ranh giới dễ nhầm

| Bài toán | Nhóm | Lý do |
|---|---|---|
| Fibonacci | Không lựa chọn | Quy tắc truy hồi cố định, không duyệt nhánh chọn |
| Prefix sum | Không lựa chọn | Mỗi bước cập nhật theo công thức duy nhất |
| Automaton deterministic | Không lựa chọn | Mỗi cặp (state, input) có đúng 1 state kế |
| Đếm đường đi DAG | Có lựa chọn | Từ state có thể đi nhiều cạnh, đếm bằng tổng qua nhánh |
| Coin Change (đếm số cách) | Có lựa chọn | Mỗi trạng thái có nhiều cách chọn đồng hợp lệ |
| Knapsack 0/1 (max value) | Có lựa chọn | Pick/skip tại mỗi phần tử |
| Interval DP (min cost) | Có lựa chọn | Chọn điểm chia `k` |
| TSP bitmask | Có lựa chọn | Chọn đỉnh đi tiếp |
| Game DP | Có lựa chọn | Nhiều nước đi ở mỗi lượt |


## V. Checklist phân loại nhanh (30 giây)

1. Viết `Next(state)` cho bài toán.
2. Có state nào mà `|Next(state)| > 1` không?
3. Nếu có: đây là `DP có lựa chọn` (dù bạn gộp bằng `min/max/sum/or`).
4. Nếu mọi state đều có `|Next(state)| <= 1`: đây là `DP không lựa chọn`.
5. Kiểm tra thêm: nhánh bị loại do điều kiện biên chỉ là nhánh không hợp lệ, không tạo loại mới.
