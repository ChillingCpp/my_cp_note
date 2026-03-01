# Segment Tree (không lazy)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/seg_tree/seg_tree.cpp)

## Ý tưởng chung
- Segment Tree chia mảng thành các đoạn con, mỗi node lưu thông tin gộp của một đoạn.
- Hỗ trợ tốt khi cần:
    - Query đoạn `[l, r]` nhiều lần.
    - Update điểm (point update) nhiều lần.
    - Hoặc update đoạn có thể prune nhanh trong O(log n) hoặc O(1) bằng đệ quy.
- Độ phức tạp chuẩn:
    - Build: `O(n)`
    - Query: `O(log n)`
    - Point update: `O(log n)`

## Khi nào chọn Segment Tree
- Cần query đoạn với phép tính gộp kết hợp (`sum/min/max/gcd/xor/...`).
- Phép tính có thể không giao hoán
- Có update online, không xử lý offline được như prefix sum.
- Cần custom node phức tạp hơn Fenwick Tree (vd: max subarray, first position thỏa điều kiện).
- Tối ưu các công thức/phép tính yêu cầu range query xuống o(log n)

## Khung đại số cốt lõi
- `Node id()`
    - Phần tử trung tính của node.
    - Điều kiện: `op(id(), x) = x`.
- `Node op(Node a, Node b)`
    - Gộp node b vào node a
    - Cần tính kết hợp để query đúng.
    - Nếu không giao hoán thì cần đảm báo merge đúng vị trí

## Các dạng bài trực diện
### 1) Range Query + Point Update (kinh điển)
- Query `sum/min/max/gcd/xor` trên `[l, r]`.
- Update `a[pos] = val` hoặc `a[pos] += delta`.
- Nhận diện: số query lớn, vừa hỏi đoạn vừa sửa từng phần tử.

### 2) Bài Node phức hợp, Node không giao hoán
- Longest/Maximum subarray gì đó:
    - Node lưu `cur, prefĩx, suffix, best`.
- Node không giao hoán `merge(a, b) != merge(b, a)` :
    - Phải sử dụng `merge(left, st[l++])`, `merge(st[--r], right)` và `ans = merge(left, right)`;
- Nhận diện: thông tin đáp án không phải 1 số đơn giản, phải biết nhiều thông tin nữa.

### 3) Segment Tree đệ quy có prune (không cần lazy)
- Range update nhưng mỗi phần tử chỉ thay đổi hữu hạn lần ($O(\sqrt{n})$, $O(log n)$, $O(1) hoặc O(C)$):
    - Ví dụ `a[i] = floor(sqrt(a[i]))`, `a[i] = popcount(a[i])`.
- Dùng cờ dừng/giá trị max để bỏ qua node đã ổn định.
- Nhận diện: update đoạn nhưng có tính "co dần", một phần tử đổi rất ít lần.

### 4) Walk on Segment Tree (đi bộ trên cây)
- Không query ra giá trị rồi mới binary search, mà đi trực tiếp từ root xuống lá.
- Các bước thực hiện như sa:
    - Nếu node con (trái/phải) thỏa predicate  thì đi vào node đó.
    - Nếu không thỏa thì cập nhật trạng thái (trừ k, cộng dồn, đổi bound...) rồi đi node còn lại.
    - Dạng bài `leftmost`, `rightmost` hoặc không cố định.
- Dạng điển hình:
    - Tìm vị trí đầu tiên/cuối cùng trong `[l, r]` thỏa `predicate`.
    - Tìm k-th one/k-th zero.
    - Chỉ cần tìm một phần tử bất kỳ thỏa `predicate` (không phải k-th), miễn là node lưu đủ thông tin để quyết định đi nhánh nào.
    - Tìm phần tử đầu tiên từ phải qua trái hoặc trái qua phải theo ràng buộc.
- Nhận diện: đề hỏi "tìm chỉ số nhỏ nhất/lớn nhất", "k-th", hoặc "tìm 1 vị trí thỏa `predicate`" trong online `O(log n)`; `predicate` không đơn điệu theo chỉ số nên binary search thường không làm trực tiếp được.

## Các dạng ẩn (đề không nói thẳng Segment Tree)
### 1) Dynamic multiset trên chỉ số
- Add/remove phần tử, hỏi:
    - số lượng trong đoạn giá trị.
    - phần tử thứ `k`.
- Biến đổi:
    - Nén tọa độ giá trị -> segment tree đếm tần suất.

### 2) Binary search trên đáp án + segment tree check
- BS giá trị `mid`, dùng segment tree kiểm tra điều kiện nhanh.
- Ví dụ: kiểm tra tồn tại đoạn thỏa ràng buộc sau khi biến đổi theo `mid`.

### 3) Sweep line + segment tree (hình học / intervals)
- Quét theo trục `x`, segment tree trên trục `y`:
    - union area, max overlap, covered length.
- Dạng này ẩn vì nhìn như hình học hơn là mảng.

### 4) cần biết giá trị trong đoạn [l, r] nhanh
- tối ưu greedy/dp/graph

### 5) Các bài toán đếm
- Các bài toán đếm có rằng buộc <, >, <=, => về chỉ số, giá trị,...
- Quy về segment tree sum

## Gợi ý chọn cấu trúc khác
- Chỉ query tĩnh, không update: Prefix Sum / Sparse Table.
- Chỉ `sum` + point update: Fenwick Tree thường gọn hơn.
- Range update tổng quát: chuyển sang [Lazy Segment Tree](<Lazy Segment Tree.md>).

## Đường dẫn
- [Prefix sum](<Prefix sum.md>)

