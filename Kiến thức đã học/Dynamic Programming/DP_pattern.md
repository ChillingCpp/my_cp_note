# DP Pattern theo cấu trúc chuyển state

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/dp)

## 0. Tiêu chí phân loại gốc

Phân loại theo đồ thị chuyển trạng thái:

- Gọi `Next(state)` là tập state có thể chuyển tới từ `state`.
- `DP có lựa chọn`: tồn tại state có nhiều nhánh hợp lệ, tức `|Next(state)| > 1`.
- `DP không lựa chọn`: mọi state có nhiều nhất 1 nhánh hợp lệ, tức `|Next(state)| <= 1`.

## I. DP CÓ LỰA CHỌN

### 1. Mẫu công thức

- Dạng tổng quát:
  - `dp[state] = combine_{nxt in Next(state)}( transition_cost_or_count + dp[nxt] )`
  - `combine` có thể là `min/max/sum/or...`.

```cpp
for (state in order) {
    init(dp[state]); // INF, -INF, 0, false... tuy AGG
    for (nxt in Next(state)) {
        dp[state] = combine(dp[state], value(state, nxt) + dp[nxt]);
    }
}
```

### 2. Dấu hiệu nhận diện

- Từ một state có nhiều nhánh chuyển tiếp.
- Có vòng lặp duyệt danh sách nhánh `choice/next`.
- Có bước gộp kết quả từ nhiều nhánh (kể cả cộng tất cả để đếm).

### 3. Nhóm bài điển hình

- Pick/Skip DP: Knapsack, House Robber.
  - mỗi bước có nhiều phương án (lấy/bỏ), rồi gộp kết quả theo mục tiêu của bài.
- Chọn điểm tách: Interval DP, Matrix Chain Multiplication.
  - state là đoạn `dp[l][r]`, thử nhiều điểm chia `k` để lấy kết quả tốt nhất.
- Chọn trạng thái/cấu hình: Bitmask DP, TSP, Assignment DP, Digit DP, Tree DP.
  - từ mỗi cấu hình hiện tại có nhiều cách đi tiếp hợp lệ, nên phải duyệt nhánh và gộp.
- Chọn hành động theo lượt: Game DP, Minimax.
  - mỗi lượt có nhiều nước đi; state gộp theo luật đối kháng (`max/min` theo người chơi).
- Chọn thao tác chuyển đổi: Edit Distance, String transform DP.
  - mỗi state có nhiều thao tác chuyển tiếp (chèn/xóa/sửa/giữ), rồi lấy chi phí tốt nhất.
- DP đếm có phân nhánh: đếm đường đi, đếm số cách tạo cấu hình.
  - không chọn một nhánh tốt nhất mà cộng toàn bộ nhánh hợp lệ, nhưng bản chất vẫn là nhiều lựa chọn.

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
- DP mô phỏng hệ deterministic.
  - từ state hiện tại và input tương ứng, state kế tiếp được xác định duy nhất.
- DP theo thời gian với luật cập nhật cố định.
  - trạng thái ở thời điểm `t+1` suy ra trực tiếp từ `t`, không có hành động để lựa chọn.
- DP cập nhật tuần tự 1 hướng.
  - mỗi bước chỉ truyền sang một state kế tiếp theo quy tắc, nếu ra ngoài biên thì bỏ.

---

## III. Ranh giới dễ nhầm

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


## IV. Checklist phân loại nhanh (30 giây)

1. Viết `Next(state)` cho bài toán.
2. Có state nào mà `|Next(state)| > 1` không?
3. Nếu có: đây là `DP có lựa chọn` (dù bạn gộp bằng `min/max/sum/or`).
4. Nếu mọi state đều có `|Next(state)| <= 1`: đây là `DP không lựa chọn`.
5. Kiểm tra thêm: nhánh bị loại do điều kiện biên chỉ là nhánh không hợp lệ, không tạo loại mới.
