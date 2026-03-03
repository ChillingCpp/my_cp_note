# DP Pattern theo 2 nhóm: Có lựa chọn vs Không lựa chọn

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/dp)

## 0. Tiêu chí phân loại gốc

Bạn đang dùng đúng hướng: chia DP thành 2 loại lớn.

- `DP có lựa chọn`:
    - Tại một state có nhiều phương án hợp lệ.
    - Ta phải ra quyết định (chọn tốt nhất, hoặc xét nhánh theo quyết định).
- `DP không lựa chọn` (hoặc chỉ có `1 lựa chọn` để tạo state):
    - Công thức cập nhật đã cố định.
    - Không có bước "quyết định phương án nào tốt hơn".

Quy tắc 1 câu để phân loại:
- Nếu có thể bỏ một nhánh vì "kém hơn" -> `có lựa chọn`.
- Nếu mọi thành phần đều phải lấy theo công thức cố định -> `không lựa chọn`.

---

## I. DP CÓ LỰA CHỌN

### 1. Mẫu công thức

- `dp[state] = best over choices( cost(choice) + dp[next_state] )`
- Toán tử thường gặp: `min`, `max`, đôi khi `or/and` cho bài tồn tại.

```cpp
for (state in order) {
    dp[state] = INF; // hoac -INF tuy bai
    for (choice in choices(state)) {
        dp[state] = min(dp[state], cost(state, choice) + dp[next(state, choice)]);
    }
}
```
### 2. Dấu hiệu nhận diện

- Đề bài có "chọn hoặc không chọn", "chọn 1 trong k", "chọn điểm tách".
- Có cụm "tối ưu", "ít nhất", "lớn nhất".
- Câu hỏi cốt lõi: "Ở state này nên đi hướng nào?".

### 3. Nhóm bài điển hình

- Pick/Skip DP: Knapsack, House Robber.
    - mỗi bước có ít nhất 2 phương án (lấy hoặc bỏ), rồi chọn phương án cho kết quả tối ưu toàn cục.
- Chọn điểm tách: Interval DP, Matrix Chain Multiplication.
    - state thường là đoạn `dp[l][r]`, thử mọi điểm chia `k` và lấy cách tách tốt nhất.
- Chọn trạng thái/cấu hình: Bitmask DP, TSP, Assignment DP, Digit DP, Tree DP.
    - đáp án phụ thuộc cấu hình hiện tại (tập đã chọn, vị trí, ràng buộc), nên phải chọn chuyển tiếp hợp lệ tốt nhất từ cấu hình đó.
- Chọn hành động theo lượt: Game DP, Minimax.
    - quyết định ở state phụ thuộc người chơi hiện tại, thường luân phiên giữa mục tiêu `max` và `min`.
- Chọn thao tác chuyển đổi: Edit Distance, String transform DP.
    - mỗi state biểu diễn mức khớp hiện tại giữa hai chuỗi, rồi chọn thao tác (chèn/xóa/sửa/giữ) có chi phí tối ưu.

### 4. Lưu ý

- "Lựa chọn" có thể ẩn trong state (mask, last, color), không nhất thiết viết từ "chọn" trong đề.
- Nếu có nhiều nhánh cạnh tranh và phải lấy `best`, đây gần như chắc chắn là DP có lựa chọn.

## II. DP KHÔNG LỰA CHỌN (HOẶC CHỈ 1 LỰA CHỌN)

### 1. Mẫu công thức

#### a) 1 chuyển tiếp duy nhất

- `dp[next] = f(dp[cur], data)`

```cpp
for (state in order) {
    dp[next(state)] = f(dp[state], data[state]);
}
```

#### b) Tổng hợp bắt buộc từ tập cố định

- `dp[i] = fixed_aggregate( contributions bắt buộc )`
- Có thể vẫn có vòng lặp, nhưng không phải "chọn nhánh tốt nhất".

```cpp
for (int i = 1; i <= n; ++i) {
    dp[i] = 0;
    for (int j : fixed_set(i)) {
        dp[i] += contrib(j, i); // cong bat buoc, khong min/max
    }
}
```

### 2. Dấu hiệu nhận diện

- Không có `best among choices`.
- State kế tiếp được quyết định bởi quy tắc cố định.
- Mục tiêu là "tính tiếp" hoặc "cộng dồn theo luật", không phải quyết định hành động tối ưu.

### 3. Nhóm bài điển hình

- Prefix/Suffix recurrence, Fibonacci chuẩn.
    - Ghi chú: mỗi state được tính từ một tập trạng thái trước đã cố định, không có bước so sánh để chọn phương án tốt hơn.
- DP mô phỏng hệ deterministic.
    - Ghi chú: từ state hiện tại và input tương ứng, state kế tiếp được xác định duy nhất theo luật chuyển cố định.
- DP theo thời gian với luật cập nhật cố định.
    - Ghi chú: trạng thái ở thời điểm `t+1` được suy ra trực tiếp từ thời điểm `t` theo quy tắc đã cho, không có hành động để lựa chọn.
- Đếm theo công thức cố định (không chọn nhánh tối ưu).
    - Ghi chú: mục tiêu là cộng/tổng hợp đầy đủ các đóng góp theo định nghĩa truy hồi, không loại bỏ nhánh nào vì "kém".
- Đếm đường đi DAG khi mỗi state cộng từ tập predecessor cố định.
    - Ghi chú: `dp[v]` là tổng từ toàn bộ predecessor hợp lệ trong DAG theo thứ tự topo, không cần quyết định predecessor tốt nhất.

## III. Ranh giới dễ nhầm

| Bài toán | Nhóm | Lý do |
|---|---|---|
| Fibonacci | Không lựa chọn | Truy hồi cố định |
| Prefix sum | Không lựa chọn | Mỗi bước chỉ 1 cập nhật |
| Đếm đường đi DAG | Không lựa chọn | Cộng toàn bộ predecessor cố định |
| Knapsack 0/1 (max value) | Có lựa chọn | Pick/skip tại mỗi phần tử |
| Interval DP (min cost) | Có lựa chọn | Chọn điểm chia `k` tốt nhất |
| TSP bitmask | Có lựa chọn | Chọn đỉnh đi tiếp |
| Game DP | Có lựa chọn | Quyết định đối kháng |

Ghi chú quan trọng:
- "Có vòng lặp qua nhiều `j`" chưa chắc là có lựa chọn.
- Điểm khác biệt nằm ở bản chất:
    - `min/max` giữa phương án cạnh tranh -> có lựa chọn.
    - `sum/merge` bắt buộc theo tập cố định -> không lựa chọn.

---

## IV. Checklist phân loại nhanh (30 giây)

1. Viết nháp công thức chuyển state.
2. Tại state, có cần chọn phương án tốt nhất không?
3. Có thể bỏ một nhánh vì "kém hơn" không?
4. Hay phải lấy đầy đủ mọi đóng góp theo quy tắc cố định?

Kết luận:
- Có bước quyết định -> `DP có lựa chọn`.
- Không có bước quyết định (hoặc chỉ 1 cách tạo state) -> `DP không lựa chọn`.
