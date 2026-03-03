# CHỐNG THIẾU CASE KHI THI (1 SUBMIT DUY NHẤT)

Mục tiêu: tránh WA do thiếu trường hợp khi **chỉ có 1 lần submit** và **không có feedback sau submit**.

Nguyên tắc: không bắt đầu code nếu chưa chứng minh được 2 điều:
1. Bộ case đã **đủ phủ** (mọi input hợp lệ rơi vào ít nhất 1 case).
2. Mỗi case đã có **nhánh xử lý rõ ràng** (công thức/thuật toán cụ thể).

---

## I. Quy trình trước khi code (Go/No-Go)

### B1) Chuẩn hóa đề (2-3 phút)
Viết lại đề theo mẫu:
- `Object`: mảng/đồ thị/cây/chuỗi...
- `Operation`: query/update/đếm/tối ưu...
- `Goal`: cần in gì, 1 đáp án hay nhiều đáp án hợp lệ.

Chốt ngay các giới hạn quan trọng:
- `n, m, q`, miền giá trị, có âm không, có thể vô nghiệm không.

### B2) Liệt kê trục dễ sót case (3 phút)
Không brainstorm lan man. Chỉ xét các trục dưới đây:
1. Biên kích thước: `0`, `1`, `2`, max.
2. Quan hệ điều kiện: `<`, `=`, `>`.
3. Dấu giá trị: âm / 0 / dương.
4. Cấu trúc đặc biệt: rỗng, disconnected, duplicate, self-loop, multi-edge (nếu đề cho), symmetric.
5. Trạng thái tồn tại: có đáp án / không có đáp án.
6. Trạng thái thứ tự: cặp `(u, v)` là **có thứ tự** hay **không thứ tự**.

### B3) Lập `Case Ledger` (bắt buộc, 5 phút)
Tạo bảng và điền đủ trước khi code:

```text
ID | Điều kiện vào case | Xử lý dự kiến | Output mong đợi | Test đại diện
```

Rule:
- Không để dòng nào trống cột `Xử lý dự kiến`.
- Nếu 2 dòng có cùng xử lý, gộp lại để giảm nhánh code.
- Nếu 1 dòng chưa rõ xử lý, quay lại B2 (chưa được code).

### B4) Vẽ khung nhánh code trước (3 phút)
Viết pseudocode mức branch (chưa code chi tiết):

```text
if (case A) -> handle_A
else if (case B) -> handle_B
else -> handle_C
```

Gắn mỗi nhánh với `ID` trong `Case Ledger`.
Mục tiêu: chứng minh mọi case đều có đường đi trong code.

### B5) Thiết kế bộ test tối thiểu trước khi code (5 phút)
Bắt buộc có:
1. 1 test cho mỗi dòng `Case Ledger`.
2. 1 test biên toàn cục (size nhỏ nhất/lớn nhất hợp lệ).
3. 1 test phá điều kiện bằng (`=`) vì đây là nhánh hay thiếu nhất.
4. 1 test phá đối xứng để bắt lỗi thiếu đảo đầu mút (`cand2 < cand1`).
5. 3-5 test random nhỏ để dry-run tay.

---

## II. Checklist No-Go (còn 1 mục chưa đạt thì chưa code)

1. Đã có `Case Ledger` đầy đủ và không dòng nào mơ hồ?
2. Đã cover cả `<`, `=`, `>` cho mọi điều kiện rẽ nhánh chính?
3. Đã có case “không tồn tại đáp án” (nếu đề có thể xảy ra)?
4. Đã map 1-1 giữa `Case Ledger` và nhánh pseudocode?
5. Đã có test đại diện cho từng case?
6. Đã xác định kiểu dữ liệu an toàn (`int64`, overflow, modulo)?
7. Đã chốt complexity qua được cận đề trong worst-case?
8. Với công thức trên cặp `(u, v)`: đã xác định rõ ordered/unordered, và nếu unordered đã xét cả 2 hướng?

Nếu bất kỳ câu nào trả lời “chưa” -> No-Go.

---

## III. Kỹ thuật giảm sót case trong lúc code

1. Code theo thứ tự: `base cases -> nhánh tổng quát -> output`.
2. Mỗi lần viết `if`, tự hỏi ngay: nhánh `else` tương ứng là case nào trong ledger?
3. Không viết điều kiện gộp quá sớm (`if (a<=b && ... )`) khi chưa test nhánh `a=b` riêng.
4. Tách hàm cho case khó để tránh lẫn logic.
5. Giữ 1 comment ngắn trên nhánh khó: `// Ledger: C3, C4`.
6. Với công thức đồ thị đi qua cặp đầu mút `(u, v)`:
    - Nếu cặp **không thứ tự** (undirected/pair), luôn tính cả 2 hướng:
    - `cand1 = dist(a, u) + w(u, v) + dist(v, b)`
    - `cand2 = dist(a, v) + w(u, v) + dist(u, b)`
    - `cand = min(cand1, cand2)`
    - Nếu cặp **có thứ tự** (directed `u -> v`), chỉ dùng hướng hợp lệ.
7. Luôn tạo 1 test “đảo đầu mút thắng” để bắt bug này:
    - test sao cho `cand2 < cand1`.

---

## IV. 11 lỗi thiếu case gặp nhiều nhất
 
1. Quên trường hợp đảo đầu mút `(u, v)` thành `(v,u)` trong đồ thị vô hướng trong công thức kiểu `dist(a, u) + dist(v, b)`.
2. Quên nhánh `=` khi chỉ nghĩ `<` và `>`.
3. Quên `n=1` hoặc mảng/đồ thị rỗng đặc biệt.
4. Quên dữ liệu trùng (duplicate).
5. Quên giá trị âm hoặc zero.
6. Quên trường hợp “không có đáp án”.
7. Quên disconnected graph.
8. Quên self-loop/multi-edge khi đề không cấm.
9. Quên reset state giữa test cases.
10. Quên nhánh biên của binary search (`first true`/`last true`).
11. Quên overflow trung gian dù kết quả cuối hợp lệ.

---

## V. Mẫu dùng ngay trong phòng thi

```text
[Case Ledger]
C1 | ... | ... | ... | test #1
C2 | ... | ... | ... | test #2
C3 | ... | ... | ... | test #3

[Pseudocode Branch Map]
if (...)   // C1
else if (...) // C2
else       // C3

[No-Go Check]
- < = > covered? [ ]
- impossible case covered? [ ]
- ordered/unordered pair checked? [ ]
- each case has a test? [ ]
- overflow checked? [ ]
```

---

## VI. Quy tắc cuối cùng

Trong mode 1-submit, ưu tiên đúng tuyệt đối hơn code nhanh:
- Chậm 8-10 phút để khóa đủ case vẫn tốt hơn submit sớm và WA.
- Chỉ code khi `Case Ledger` đã kín và `No-Go` đều pass.
