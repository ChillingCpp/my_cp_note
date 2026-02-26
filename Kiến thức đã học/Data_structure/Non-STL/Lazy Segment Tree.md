# Lazy Segment Tree (Tổng quát)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/seg_tree/lazy_segtree_nobinsearch.cpp)

## Ý tưởng chung
- Thường sử dụng cho range update không thể prunning sớm, nếu có prunning sớm thì sử dụng [Segment Tree](<Segment Tree.md>) + update đệ quy
    - Điều kiện prunning sớm là nếu 1 operation chỉ được thực hiện tối đa log a hoặc k constant bất kì.
- Segment tree lưu thông tin đoạn trong `Node`.
- Lazy propagation lưu cập nhật treo trong `Lazy`.
- Mọi bài toán đều quy về 5 hàm đại số: `idn`, `idl`, `op`, `tf`, `opl`.
- Khi đổi bài, gần như chỉ sửa `Node/Lazy` và 5 hàm trên. Khung `lazyseg` giữ nguyên.

## ý nghĩa của từng hàm lõi
- `Node idn()`
    - Trả phần tử trung tính của `Node`.
    - Điều kiện: `op(idn(), x) = x` và `op(x, idn()) = x`.

- `Lazy idl()`
    - Trả lazy "không làm gì".
    - Điều kiện: `tf(x, idl()) = x`.

- `Node op(Node a, Node b)`
    - Gộp 2 node con thành node cha.
    - Điều kiện: tính chất kết hợp để query đúng khi tách đoạn.

- `Node tf(Node a, Lazy b)`
    - Áp một cập nhật lazy `b` lên node `a`.
    - Đây là hàm biến đổi dữ liệu node khi đoạn nhận update.

- `Lazy opl(Lazy a, Lazy b)`
    - Gộp hai lazy theo thứ tự "đang có `a`, cập nhật mới `b`".
    - Điều kiện tương thích với `tf`:
        - `tf(tf(x, a), b) = tf(x, opl(a, b))`.

## Chú thích các hàm trong Lazy Segment Tree
### Hàm sử dụng chính
- `lazyseg(vector<Node>& a)`
    - Build cây từ mảng gốc.
    - `n` là power of two nhỏ nhất >= `a.size()`.
    - `h` là chiều cao cây, dùng để push theo đường đi.

- `Node query(int l, int r)`
    - Truy vấn đoạn đóng `[l, r]`.
    - Bước 1: thực hiện `l += n, r += n + 1`
    - Bước 2: `push(l, r)` để đảm bảo các node trên đường đi là mới nhất.
    - Bước 3: duyệt 2 con trỏ kiểu iterative segment tree và gộp bằng `op`.

- `void apply(int l, int r, Lazy la)`
    - Cập nhật đoạn đóng `[l, r]` bằng lazy `la`.
    - Bước 1: thực hiện `l += n, r += n + 1` và `l1 = l, r1 = r`.
    - Bước 2: `push(l, r)` để tránh chồng sai lazy cũ.
    - Bước 3: duyệt 2 con trỏ kiểu iterative segment tree, gọi `apply_l`.
    - Bước 4: `update(l1, r1)` để kéo thông tin tổ tiên lên lại.


### Hàm phụ trợ
- `void apply_l(int p, Lazy l)`
- `void update(int p)`
- `void update(int l, int r)`
- `void push(int p)`
- `void push(int l, int r)`

## Invariant cần nhớ
- `st[p]` luôn là giá trị đúng của đoạn tại `p`, có tính cả lazy ở chính `p`.
- Lazy chưa đẩy chỉ nằm ở `lz[p]` với `p < n` (node trong).
- Mọi truy vấn/cập nhật đoạn đều phải `push(l, r)` trước, trước khi `push(l, r)` phải có dòng code `l += n, r += n + 1`.

## Checklist khi đổi sang bài khác
- Xác định `Node` lưu gì.
- Xác định `Lazy` biểu diễn update gì.
- Viết đúng `idn`, `idl`.
- Viết đúng `op`, `tf`, `opl` theo thứ tự compose.
- Kiểm tra lại đoạn chỉ số: template này dùng `[l, r]`.

## Độ phức tạp
- Build: `O(n)`
- Mỗi `query`: `O(log n)`
- Mỗi `apply`: `O(log n)`
