# I. DP CÓ LỰA CHỌN

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/dp)

Khái niệm:
- Ở một state, có từ 2 hướng chuyển tiếp hợp lệ trở lên.
- Ta phải gộp kết quả bằng `min / max / sum / or`.

Mẫu tổng quát:
- `dp[state] = aggregate( value(transition) + dp[next_state] )`
- Từ khóa nhận diện: `chọn`, `hoặc`, `tối ưu`, `đếm số cách`.

## 1. Lựa chọn hiện trong đề
Đề nói thẳng quyết định.

Dấu hiệu:
- Chọn hoặc không chọn.
- Chọn một trong nhiều thao tác.
- Chọn điểm tách/chia.

Ví dụ:
- Knapsack
- Coin Change
- Interval DP
- Edit Distance
- Game DP

## 2. Lựa chọn ẩn trong đề
Đề không nói từ "chọn", nhưng bản chất vẫn có nhánh.

### a) Chọn cấu hình
- Bitmask DP
- Assignment DP
- TSP DP

### b) Chọn trạng thái phụ
- Tree DP (màu/trạng thái node)
- Coloring DP
- DP có ràng buộc trạng thái trước/sau

### c) Chọn chuyển tiếp
- Automaton DP có nhiều cạnh chuyển
- String DP có nhiều thao tác
- Digit DP (chọn chữ số tiếp theo)

## 3. Lựa chọn đối kháng
Đối thủ cũng "ra quyết định", nên state có cạnh tranh.

Ví dụ:
- Minimax / game DP
- Grundy DP

## 4. Lựa chọn để tối ưu
Có lựa chọn + cần kỹ thuật tăng tốc.

Ví dụ:
- Scheduling DP
- DP + Greedy
- DP + Binary Search
- Knuth optimization, Divide and Conquer optimization, CHT

### Nhận diện DP có lựa chọn
- Có vòng lặp qua các transition.
- Có nhiều phương án cạnh tranh tại cùng một state.
- Có biểu thức kiểu `best among ...`.
- Câu hỏi cốt lõi: "Ở đây nên đi hướng nào?"

# II. DP KHÔNG DỰA VÀO LỰA CHỌN

Khái niệm:
- Mỗi state sinh ra state kế tiếp theo một quy tắc duy nhất.
- Không có bước "chọn phương án tốt nhất".

Mẫu tổng quát:
- `dp[next_state] = f(dp[state], data)`
- Không có `min/max over transitions`.

## 1. DP lan truyền tuyến tính
- Prefix/Suffix recurrence
- Rolling update tuyến tính
- Fibonacci và truy hồi 1 chiều chuẩn

## 2. DP đếm không nhánh
- Công thức đếm có quy tắc cố định.
- Không cần duyệt nhiều lựa chọn tại mỗi state.

Ví dụ:
- Một số truy hồi tổ hợp: Catalan/Bell/Stirling (khi dùng công thức cố định)

## 3. DP mô phỏng hệ xác định
- Hệ thống tiến hóa theo luật cố định.
- Từ state hiện tại suy ra duy nhất state kế.

Ví dụ:
- Automaton có đúng một cạnh chuyển cho mỗi input
- Mô phỏng máy trạng thái deterministic

## 4. DP theo thời gian deterministic
- Mỗi bước thời gian cập nhật theo công thức cố định.
- Không có cạnh tranh giữa các hành động.

## 5. DP theo công thức truy hồi thuần
- Truy hồi một đường, không tối ưu lựa chọn.
- Mục tiêu chính là tính giá trị, không phải chọn nhánh.

### Nhận diện DP không lựa chọn
- Không có loop qua danh sách transition cạnh tranh.
- Không có `best among choices`.
- State sau là tất yếu.
- Chỉ "tính tiếp", không "quyết định".

# III. Bảng ranh giới chuẩn

| Bài toán | Có lựa chọn? | Lý do |
|---|---|---|
| Fibonacci | Không | Truy hồi cố định |
| Prefix sum | Không | Cập nhật duy nhất |
| Digit DP | Có | Chọn chữ số tiếp theo |
| Tree DP | Có | Chọn trạng thái/chuyển của node |
| Interval DP | Có | Chọn điểm chia |
| TSP bitmask | Có | Chọn đỉnh đi tiếp |
| Đếm đường đi DAG (cộng từ predecessor cố định) | Thường không | Không tối ưu lựa chọn tại một state |
| Game DP | Có | Đối kháng, tối ưu theo lượt |

Ghi chú:
- Một số bài "đếm" vẫn có lựa chọn nếu phải cộng qua nhiều nhánh hợp lệ.
- Ranh giới thực tế nằm ở cấu trúc chuyển state, không nằm ở từ ngữ đề bài.

# IV. Kết luận cốt lõi

- Có thể nhìn DP theo 2 nhóm lớn: `có lựa chọn` và `không lựa chọn`.
- Tiêu chí phân loại mạnh nhất: số lượng chuyển tiếp hợp lệ từ mỗi state.
- "Lựa chọn" có thể ẩn trong cấu hình, ràng buộc, hoặc hành vi đối kháng.
- Phân loại đúng từ đầu giúp chọn công thức và tối ưu đúng hướng.

Checklist phân loại nhanh:
1. Một state có bao nhiêu next-state hợp lệ?
2. Có cần chọn tốt nhất/tổng các nhánh không?
3. Nếu bỏ dữ liệu đầu vào, quy luật còn deterministic không?
4. Mục tiêu là tối ưu theo quyết định hay chỉ mô phỏng truy hồi?

