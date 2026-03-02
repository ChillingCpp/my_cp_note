# Invariants và Monovariants

## 1. Trực giác lớn nhất
- Hãy xem mỗi trạng thái của bài toán là một đỉnh trong đồ thị.
- Mỗi thao tác hợp lệ là một cạnh nối sang trạng thái mới.

Khi đó:
- `Invariant` là “nhãn” của đỉnh không đổi khi đi theo cạnh.
- `Monovariant` là “độ cao” của đỉnh chỉ đi một chiều khi đi theo cạnh.

Từ đó suy ra trực giác:
- Invariant dùng để chặn **nơi có thể đi tới**.
- Monovariant dùng để chặn **đi được bao lâu**.

## 2. Định nghĩa hình thức (đủ dùng cho chứng minh)
Giả sử:
- `S` là tập trạng thái.
- `s -> t` nghĩa là từ `s` thực hiện được 1 thao tác để tới `t`.

### Invariant
Hàm `I: S -> X` là invariant nếu:
- Với mọi `s -> t`, ta có `I(s) = I(t)`.

Hệ quả quan trọng:
- Nếu `I(s0) != I(goal)` thì `goal` không thể đạt từ `s0`.
- Reachable set từ `s0` luôn nằm trong lớp `I = I(s0)`.

### Monovariant
Hàm `M: S -> Y` (với thứ tự `<=`) là monovariant nếu:
- Với mọi `s -> t`, ta có `M(t) <= M(s)` (hoặc ngược chiều tùy chọn).

Phân biệt:
- `non-strict`: `M(t) <= M(s)`.
- `strict`: `M(t) < M(s)`.

Điểm mấu chốt để kết luận dừng:
- Nếu giảm nghiêm ngặt vào `N` (hoặc bất kỳ tập well-founded), quá trình chắc chắn hữu hạn.

## 3. Lý thuyết dừng: vì sao monovariant hiệu quả
Nếu có `M: S -> N` sao cho mỗi bước `M` giảm ít nhất 1:
- `M(s0), M(s1), M(s2), ...` là dãy số tự nhiên giảm nghiêm ngặt.
- Điều này là bất khả vì số tự nhiên không thể giảm vô hạn lần.
- Nên số bước tối đa là `M(s0) - M_min`.

Nếu chỉ có `M(t) <= M(s)`:
- Chưa đủ để kết luận dừng.
- Có thể tồn tại chu trình giữ nguyên `M`.

Muốn mạnh hơn trong case này:
- Dùng cặp thế năng từ điển `M = (M1, M2)` với thứ tự lexicographic.
- Hoặc chứng minh không thể quay lại trạng thái cũ.
- Hoặc chứng minh không gian trạng thái hữu hạn + có tiến bộ định kỳ.

## 4. Lý thuyết “không thể đạt”: vì sao invariant hiệu quả
Invariant cho một điều kiện cần rất cứng:
- Mọi trạng thái reachable phải có cùng giá trị invariant với trạng thái đầu.

Mẫu phản chứng chuẩn:
1. Giả sử đạt được trạng thái đích.
2. Theo invariant, giá trị invariant ở đích = ở đầu.
3. Nhưng tính trực tiếp ở đích khác ở đầu.
4. Mâu thuẫn, nên không thể đạt.

Lưu ý:
- Invariant thường cho điều kiện **cần**.
- Không tự động là điều kiện **đủ** (trừ khi chứng minh thêm phần xây dựng).

## 5. Cách tìm invariant/monovariant có hệ thống
### 5.1. Bước khởi đầu: viết biến thiên một thao tác
Đặt đại lượng thử nghiệm `F`.
Tính:
`Delta = F(sau) - F(trước)`.

Nếu:
- `Delta = 0` mọi thao tác -> invariant.
- `Delta <= 0` mọi thao tác -> monovariant giảm.
- `Delta < 0` mọi thao tác -> monovariant giảm nghiêm ngặt.

### 5.2. Các “kho” đại lượng nên thử
- Chẵn lẻ (`mod 2`).
- Modulo nhỏ (`mod 3, mod 4, mod 9`).
- Tổng, hiệu, tổng có trọng số.
- Số đối tượng “xấu”: số nghịch thế, số cặp vi phạm, số cạnh conflict.
- Khoảng cách tới cấu hình chuẩn.
- Vector nhiều tiêu chí (lexicographic).

### 5.3. Tô màu và trọng số
Với lưới/đồ thị:
- Tô 2 màu hoặc nhiều màu.
- Gán trọng số theo màu.
- Theo dõi tổng có trọng số.

Đây là nguồn invariant rất mạnh trong bài “chessboard”.

### 5.4. Tư duy bảo toàn - tiêu hao
- Nếu thao tác chỉ “chuyển” giá trị giữa các phần mà không tạo/khử ròng -> dễ có invariant.
- Nếu thao tác luôn “tiêu hao” một đại lượng xấu -> dễ có monovariant.

## 6. Hai ví dụ tiêu biểu (giữ ít ví dụ, tập trung ý)

### Ví dụ A: tổng chữ số lặp đến 1 chữ số (Invariant modulo 9)
Đặt `S(n)` là tổng chữ số của `n`.
Ta có:
- `S(n) = n (mod 9)`.
- Nên thay `n` bằng `S(n)` không đổi giá trị modulo 9.

Kết luận:
- Kết quả cuối cùng là digital root, tức đại diện của `n mod 9` trong `[1..9]`.
- Với `1..100000`, mẫu kết quả lặp `1..9`, nên số lượng `1` hơn số lượng `2` đúng 1.

### Ví dụ B: xếp người quanh bàn tròn (Monovariant số cặp xung đột)
Đặt:
- `M = số cặp hàng xóm là kẻ thù`.

Ý tưởng chứng minh:
- Thiết kế một phép đảo đoạn làm mất ít nhất 1 cặp xung đột.
- Không tạo thêm đủ cặp xung đột để bù lại.
- Vậy `M` giảm ít nhất 1 sau bước đó.

Do `M >= 0`, quá trình hữu hạn và dừng tại `M = 0`.

## 7. Những bẫy rất hay gặp
- Có đại lượng “gần như không đổi” nhưng không thật sự invariant.
- Monovariant không nghiêm ngặt rồi kết luận dừng ngay.
- Chứng minh điều kiện cần rồi nhầm là đủ.
- Chỉ kiểm tra 1-2 thao tác mẫu, không kiểm tra toàn bộ loại thao tác.
- Quên kiểm tra điều kiện hợp lệ của phép biến đổi (âm/dương, biên mảng, adjacency).

## 8. Khung chứng minh nhanh trong contest
1. Định nghĩa trạng thái + thao tác hợp lệ thật rõ.
2. Chọn đại lượng `I` hoặc `M`.
3. Chứng minh tác động của đúng 1 thao tác bất kỳ lên đại lượng.
4. Rút ra kết luận:
- `I`: chặn reachability / impossible.
- `M`: chặn số bước / termination.
5. Nếu bài hỏi “có thể đạt”:
- Cần thêm phần xây dựng hoặc thuật toán explicit.

## 9. So sánh ngắn gọn để nhớ lâu
- Invariant: “bạn đang ở đúng lớp trạng thái nào”.
- Monovariant: “bạn còn bao nhiêu mức để đi”.
- Invariant thiên về hình học của không gian trạng thái.
- Monovariant thiên về động lực của tiến trình.
- Bài mạnh thường kết hợp cả hai.

### 10. Checklist nhanh khi dùng hướng đếm
1. Có thể mô tả cấu hình bằng tham số rời rạc rõ ràng không.
2. Invariant có cắt được nhiều trạng thái vô nghĩa không.
3. Công thức/DP đếm có tránh overcount không.
4. `cnt > 0` có thực sự tương đương với “reachable” theo thao tác đề bài không.
