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
- Cần query đoạn với phép gộp kết hợp (`sum/min/max/gcd/xor/...`).
- Có update online, không xử lý offline được như prefix sum.
- Cần custom node phức tạp hơn Fenwick Tree (vd: max subarray, first position thỏa điều kiện).
- Tối ưu các công thức/phép tính yêu cầu range query xuống o(log n)

## Khung đại số cốt lõi
- `Node id()`
    - Phần tử trung tính của node.
    - Điều kiện: `op(id(), x) = x`.
- `Node op(Node a, Node b)`
    - Gộp 2 node con thành node cha.
    - Cần tính kết hợp để query đúng.

## Các dạng bài trực diện
### 1) Range Query + Point Update (kinh điển)
- Query `sum/min/max/gcd/xor` trên `[l, r]`.
- Update `a[pos] = val` hoặc `a[pos] += delta`.
- Nhận diện: số query lớn, vừa hỏi đoạn vừa sửa từng phần tử.

### 2) Tìm phần tử đầu tiên/thứ k thỏa điều kiện
- First position có prefix sum `>= k`.
- First position trong `[l, r]` có `a[i] > x`.
- K-th one / k-th zero khi node lưu số lượng.
- Nhận diện: đề yêu cầu "vị trí đầu tiên", "k-th", "leftmost/rightmost".

### 3) Bài Node phức hợp
- Maximum subarray sum:
    - Node lưu `sum, pref, suff, best`.
- Longest đoạn liên tiếp thỏa điều kiện (0/1):
    - Node lưu prefix/suffix length + best length.
- Nhận diện: thông tin đáp án không phải 1 số đơn giản, phải gộp từ 2 nửa.

### 4) Segment Tree đệ quy có prune (không cần lazy)
- Range update nhưng mỗi phần tử chỉ thay đổi hữu hạn lần ($O(\sqrt{n})$, $O(log n)$, $O(1) hoặc O(C)$):
    - Ví dụ `a[i] = floor(sqrt(a[i]))`, `a[i] = popcount(a[i])`.
- Dùng cờ dừng/giá trị max để bỏ qua node đã ổn định.
- Nhận diện: update đoạn nhưng có tính "co dần", một phần tử đổi rất ít lần.

## Các dạng ẩn (đề không nói thẳng Segment Tree)
### 1) Dynamic multiset trên chỉ số
- Add/remove phần tử, hỏi:
    - số lượng trong đoạn giá trị.
    - phần tử thứ `k`.
- Biến đổi:
    - Nén tọa độ giá trị -> segment tree đếm tần suất.

### 2) Quản lý chỗ trống/chỗ ngồi/phòng
- Các thao tác allocate/deallocate trên đoạn.
- Hỏi đoạn trống dài nhất hoặc vị trí đầu tiên đủ chỗ.
- Node thường lưu:
    - `prefEmpty, suffEmpty, bestEmpty, len`.

### 3) Dãy nhị phân bật/tắt + query liên tiếp
- Flip một vị trí hoặc một đoạn nhỏ, hỏi "chuỗi 1 dài nhất".
- Không nói "segment tree", nhưng bản chất là merge prefix/suffix/best.

### 4) Bài "online + nhiều truy vấn trộn"
- Nếu xử lý offline/sắp xếp không giữ được thứ tự thời gian:
    - thường cần cấu trúc online như segment tree.
- Dấu hiệu: query phụ thuộc kết quả update trước đó.

### 5) Binary search trên đáp án + segment tree check
- BS giá trị `mid`, dùng segment tree kiểm tra điều kiện nhanh.
- Ví dụ: kiểm tra tồn tại đoạn thỏa ràng buộc sau khi biến đổi theo `mid`.

### 6) Sweep line + segment tree (hình học / intervals)
- Quét theo trục `x`, segment tree trên trục `y`:
    - union area, max overlap, covered length.
- Dạng này ẩn vì nhìn như hình học hơn là mảng.
### 7) cần biết giá trị trong đoạn [l, r] nhanh
- tối ưu greedy/dp/graph

## Gợi ý chọn cấu trúc khác
- Chỉ query tĩnh, không update: Prefix Sum / Sparse Table.
- Chỉ `sum` + point update: Fenwick Tree thường gọn hơn.
- Range update tổng quát: chuyển sang [Lazy Segment Tree](<Lazy Segment Tree.md>).

## Đường dẫn
- [Prefix sum](<Prefix sum.md>)

