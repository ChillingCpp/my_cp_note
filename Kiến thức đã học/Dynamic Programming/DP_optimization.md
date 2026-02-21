# DP Optimization

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/dp)

## Liên kết
- Đây là phần chi tiết cho bước 4 trong [[DP how to solve it G.Polya]].
- Chủ đề liên quan: [[Divide and Conquer]], [[Deque]], [[Slope trick]].

## Tư tưởng cốt lõi
- Chỉ tối ưu sau khi công thức DP gốc đã đúng.
- Luôn ước lượng:
  - số state
  - số transition mỗi state
  - tổng complexity = `(#state) * (transition/state)`.
- Mục tiêu:
  - giảm chiều state
  - giảm số transition
  - giảm hằng số bằng cấu trúc dữ liệu phù hợp.

## Quy trình chuẩn
1. Viết công thức chưa tối ưu.
2. Tách phần phụ thuộc `i` và phần phụ thuộc `j`.
3. Nhìn dạng truy vấn:
   - min/max trên đoạn
   - min/max trên cửa sổ
   - prefix/suffix
   - ứng viên động thêm/xóa
4. Chọn cấu trúc dữ liệu/thuật toán tối ưu tương ứng.
5. Test brute force với `n` nhỏ.

## Nhóm nên học trước

### 1) Giảm chiều state
- Khi `dp[i][*]` chỉ phụ thuộc một vài lớp trước.
- Kỹ thuật:
  - rolling array
  - bỏ chiều bằng invariant/prefix/suffix.
- Lợi ích:
  - giảm bộ nhớ `O(n*m)` -> `O(m)`.

### 2) Prefix/Suffix Min-Max
- Dạng:
  - `dp[i] = min_{j < i}(f(j) + g(i))`
- Ý tưởng:
  - giữ `best so far` khi quét.
- Lợi ích:
  - thường `O(n^2)` -> `O(n)`.

### 3) DP tối ưu hóa bằng các cấu trúc dữ liệu

#### a) Deque (monotonic queue)
- Dạng:
  - `dp[i] = a[i] + min/max(dp[j])`, `j` trong cửa sổ `[i-k, i-1]`.
- Độ phức tạp:
  - `O(n*k)` -> `O(n)`.
- Lưu ý:
  - pop front khi out-of-window, pop back theo điều kiện đơn điệu chuẩn.

#### b) Stack (monotonic stack)
- Có bài DP dùng stack để tìm nhanh:
  - previous/next smaller element
  - previous/next greater element
  - đoạn gần nhất thỏa điều kiện để chuyển trạng thái.
- Mẫu tư duy:
  - nếu transition cần "điểm gần nhất bên trái/phải" thỏa một quan hệ đơn điệu, stack thường giảm vòng lặp lồng nhau.
- Độ phức tạp thường gặp:
  - từ `O(n^2)` xuống `O(n)` hoặc `O(n log n)` tùy công thức.
- Ví dụ nhóm bài:
  - DP trên histogram/rectangle
  - DP partition với ràng buộc min/max đoạn
  - DP có bước nhảy tới phần tử trước gần nhất thỏa điều kiện.

#### c) Segment Tree
- Dạng:
  - cần query `min/max/sum` trên đoạn của các giá trị `dp` đã biết.
- Độ phức tạp:
  - thường `O(n^2)` -> `O(n log n)`.

#### d) Fenwick Tree (BIT)
- Dạng:
  - query prefix + point update, thường sau coordinate compression.
- Độ phức tạp:
  - thường `O(n^2)` -> `O(n log n)`.

#### e) Priority Queue (heap)
- Dạng:
  - luôn lấy ứng viên tốt nhất trong tập động theo thời gian/cửa sổ.
- Kỹ thuật:
  - lazy deletion cho phần tử hết hạn.
- Độ phức tạp:
  - `O(log n)` mỗi thao tác.

#### f) Multiset / Ordered Set
- Dạng:
  - thêm/xóa trạng thái động và cần lấy min/max tức thời.
- Độ phức tạp:
  - thường `O(n log k)` cho bài cửa sổ dài `k`.

#### g) Hash map (sparse DP)
- Dạng:
  - state thưa, không phù hợp mảng lớn.
- Ý tưởng:
  - chỉ lưu state xuất hiện (`unordered_map`/`map`).
- Lợi ích:
  - giảm bộ nhớ và tránh duyệt state rỗng.

#### h) Bitset
- Dạng:
  - knapsack boolean/subset sum.
- Ý tưởng:
  - dịch bit hàng loạt thay cho loop thủ công.
- Lợi ích:
  - cải thiện đáng kể hằng số thời gian.

### 4) Binary Search + DP Check
- Dạng:
  - tối ưu đáp án toàn cục nhưng có hàm check đơn điệu.
- Ý tưởng:
  - nhị phân đáp án, mỗi lần check bằng DP.
- Độ phức tạp:
  - `O(log Ans * f(n))`.

## Nhóm nâng cao (chưa cần học đến)

### 1) Divide and Conquer Optimization (chưa cần học đến)
- Dạng:
  - `dp[t][i] = min_{j < i}(dp[t-1][j] + C(j,i))`
- Điều kiện:
  - `opt[t][i] <= opt[t][i+1]` (argmin đơn điệu).
- Thường:
  - `O(k*n^2)` -> `O(k*n log n)`.

### 2) Knuth Optimization (chưa cần học đến)
- Dạng:
  - `dp[l][r] = w(l,r) + min_{k in [l, r-1]}(dp[l][k] + dp[k+1][r])`
- Điều kiện:
  - `opt[l][r-1] <= opt[l][r] <= opt[l+1][r]`.
- Thường:
  - `O(n^3)` -> `O(n^2)`.

### 3) Convex Hull Trick / Li Chao Tree (chưa cần học đến)
- Dạng:
  - `dp[i] = min/max_j (m_j * x_i + b_j) + extra(i)`.
- Thường:
  - `O(n^2)` -> `O(n log n)` hoặc `O(n)` khi đơn điệu tốt.

### 4) Slope Trick (chưa cần học đến)
- Dùng cho hàm mục tiêu convex piecewise-linear.
- Tư duy:
  - duy trì trực tiếp hình dạng hàm chi phí thay vì full DP table.

## Bảng nhận diện nhanh

| Dạng công thức | Kỹ thuật gợi ý |
|---|---|
| Min/Max trên cửa sổ trượt | Deque |
| Cần previous/next thỏa điều kiện đơn điệu | Monotonic Stack |
| Query đoạn trên `dp` | Segment Tree / Fenwick |
| Ứng viên động, cần top nhanh | Priority Queue / Multiset |
| State thưa | Hash map |
| Boolean knapsack/subset | Bitset |
| Feasibility đơn điệu theo đáp án | Binary Search + DP |
| `min_j(dp[j] + C(j,i))` + opt đơn điệu | D&C (chưa cần học đến) |
| Interval DP tách tại `k` | Knuth (chưa cần học đến) |
| `m*x+b` | CHT / Li Chao (chưa cần học đến) |

## Checklist trước khi áp dụng tối ưu
1. Công thức gốc đã đúng chưa?
2. Điều kiện áp dụng kỹ thuật đã được chứng minh/test nhỏ chưa?
3. Biên `j < i`, `j <= i`, cửa sổ có đúng không?
4. Có overflow (`long long`, `INF`) không?
5. Nhiều test case đã reset cấu trúc dữ liệu chưa?

## Lỗi hay gặp
- Tối ưu khi công thức gốc còn sai.
- Dùng sai điều kiện pop trong deque/stack (`<` hay `<=`).
- Dùng segment tree/Fenwick sai index sau nén tọa độ.
- Heap/multiset không xóa ứng viên hết hạn.
- Dùng kỹ thuật nâng cao khi chưa đủ điều kiện toán học.

## Kết luận
- DP optimization = mô hình đúng nhưng chậm -> mô hình đúng và đủ nhanh.
- Thứ tự an toàn:
  1. đúng công thức
  2. chọn đúng cấu trúc dữ liệu
  3. mới tối ưu nâng cao.
