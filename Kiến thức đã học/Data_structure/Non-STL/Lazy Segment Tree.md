# Lazy Segment Tree (Tổng quát)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/seg_tree/lazy_segtree_nobinsearch.cpp)

## Ý tưởng chung
- Segment tree lưu thông tin đoạn trong `Node`.
- Lazy propagation lưu cập nhật treo trong `Lazy`.
- Mọi bài toán đều quy về 5 hàm đại số: `idn`, `idl`, `op`, `tf`, `opl`.
- Khi đổi bài, gần như chỉ sửa `Node/Lazy` và 5 hàm trên. Khung `lazyseg` giữ nguyên.

## Hợp đồng của từng hàm lõi
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

## Chú thích các hàm trong struct `lazyseg`
- `lazyseg(vector<Node>& a)`
  - Build cây từ mảng gốc.
  - `n` là power of two nhỏ nhất >= `a.size()`.
  - `h` là chiều cao cây, dùng để push theo đường đi.

- `Node query(int l, int r)`
  - Truy vấn đoạn đóng `[l, r]`.
  - Bước 1: dời chỉ số lên tầng lá (`+n`).
  - Bước 2: `push(l, r)` để đảm bảo các node trên đường đi là mới nhất.
  - Bước 3: duyệt 2 con trỏ kiểu iterative segment tree và gộp bằng `op`.

- `void apply(int l, int r, Lazy la)`
  - Cập nhật đoạn đóng `[l, r]` bằng lazy `la`.
  - Bước 1: dời chỉ số lên tầng lá (`+n`).
  - Bước 2: `push(l, r)` để tránh chồng sai lazy cũ.
  - Bước 3: duyệt 2 con trỏ kiểu iterative segment tree, gọi `apply_l`.
  - Bước 4: `update(l1, r1)` để kéo thông tin tổ tiên lên lại.


- `void apply_l(int p, Lazy l)`
  - Áp trực tiếp lazy `l` lên node `p` bằng `tf`.
  - Nếu `p` là node trong (chưa phải lá), cộng dồn lazy vào `lz[p]` bằng `opl`.

- `void update(int p)`
  - Tính lại node `p` từ 2 con bằng `op`.

- `void update(int l, int r)`
  - Sau update đoạn, chỉ rebuild các tổ tiên thực sự bị ảnh hưởng.
  - Tối ưu hơn việc build lại toàn cây.

- `void push(int p)`
  - Đẩy lazy từ node `p` xuống 2 con.
  - Sau khi đẩy xong, reset `lz[p] = idl()`.

- `void push(int l, int r)`
  - Đẩy lazy từ trên xuống dọc theo 2 đường đi tới `l` và `r-1`.
  - Đảm bảo trước khi query/apply ở tầng dưới, mọi thông tin đều đồng bộ.

## Invariant cần nhớ
- `st[p]` luôn là giá trị đúng của đoạn tại `p`, có tính cả lazy ở chính `p`.
- Lazy chưa đẩy chỉ nằm ở `lz[p]` với `p < n` (node trong).
- Mọi truy vấn/cập nhật đoạn đều phải `push(l, r)` trước.

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
