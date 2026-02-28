# CÁCH GIẢI MỘT BÀI TOÁN (Polya cho CP)

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

## 0) Khung trực giác (30-60 giây)
1. Bài thuộc loại gì?
    - đếm / tối ưu / xây dựng / kiểm tra tồn tại
2. Constraint chính là gì?
    - `n <= 20` / `n <= 2000` / `n <= 2e5` / nhiều query/test
3. Output là giá trị hay cấu hình?
4. Khám phá nhanh cấu trúc của bài toán
    - tìm keyword và phân loại
    - từ keyword chọn thuật toán [[chọn_nhanh_thuật_toán]] 
5. Rule:
- Nếu sau 60 giây chưa định hình được nhóm thuật toán, chuyển sang khung chi tiết.

## Khung chi tiết
### I. Understand Problem (Hiểu đúng đề)
1. Đề hỏi chính xác gì?
    - output là giá trị, cấu hình, hay chuỗi thao tác?
    - một đáp án hay nhiều đáp án hợp lệ?
2. Input/ràng buộc là gì?
    - kích thước, kiểu dữ liệu, giới hạn thời gian/bộ nhớ.
3. Có thể vô nghiệm không?
    - đề có yêu cầu xử lý trường hợp đó không?
4. Phân tích độ phức tạp để chọn thuật toán

Rule:
- Nếu chưa phát biểu lại đề trong 1-2 câu, coi như chưa hiểu đề.

### II. Discover Structure (Tìm cấu trúc)
4. Đáp án phụ thuộc dữ kiện theo cách nào?
    - cục bộ hay toàn cục, trực tiếp hay qua biến trung gian.
5. Cái gì thật sự quyết định đáp án?
    - dữ kiện nào thay đổi mà kết quả không đổi?
6. Tìm invariant/monotonic/bound:
    - thứ gì không đổi?
    - thứ gì chỉ tăng/giảm?
    - có chặn trên/dưới rõ ràng không?

### III. Tiến hành giải bài
- Chu trình: `biến đổi sơ cấp -> viết assumption -> biến đổi sâu hơn`.

#### III-A. Biến đổi sơ cấp (Reformulate nhẹ)
1. Chọn các tính chất đã tìm được ở phần II (invariant/monotonic/bound).
2. Biến đổi bài toán dựa trên chính các tính chất đó:
    - đổi cách phát biểu để bám vào tính chất mạnh nhất.
    - tách bài toán theo cấu trúc đã lộ ra.
3. Mục tiêu:
    - đưa bài toán về dạng dễ xử lý hơn mà chưa cần giả định mới.
4. Nếu chưa tạo được hướng tiến triển:
    - giữ dạng biến đổi tốt nhất hiện có và chuyển sang viết assumption để tìm thêm tính chất.

#### III-B. Viết assumption (Giả định có kiểm soát)
1. Viết assumption ra rõ ràng:
    - dạng `Giả sử ... thì ...`.
    - ghi phạm vi áp dụng (mọi test, hay chỉ sau biến đổi sơ cấp).
2. Mục tiêu:
    - dùng assumption để mở thêm tính chất mới cho bước biến đổi tiếp theo.
3. Ví dụ assumption thường dùng trong CP (tóm gọn):
    - `Fix để phá đối xứng (symmetry breaking)`: cố định một lựa chọn đại diện để loại các nghiệm tương đương.
    - `Fix thứ tự xử lý` (sort/topo/trái -> phải): tạo đơn điệu để xử lý dần (sweep line, two pointers, DP theo thứ tự).
    - `Fix một cấu hình chuẩn (canonical form)`: chuẩn hóa cách biểu diễn để so sánh/chứng minh dễ hơn.
    - `Fix để giảm chiều trạng thái`: giữ một mốc cố định để rút gọn số biến trạng thái.
    - `Giả sử chỉ cần trạng thái nén` (tập/đếm, không cần lịch sử chi tiết): mở ra DP/bitmask/frequency.
    - `Giả sử có vị trí vi phạm đầu tiên`: suy ra ràng buộc cục bộ rồi nâng thành invariant toàn cục.
    - `Giả sử tồn tại nghiệm tối ưu S`: dùng exchange argument để chuẩn hóa nghiệm (vd: interval scheduling chọn đoạn kết thúc sớm).
    - `Giả sử cấu hình cực trị` (max/min): tìm cấu trúc tight hoặc điểm biên.

#### III-C. Biến đổi sâu hơn (Decompose sâu)
1. Chứng minh assumption rồi biến đổi bài toán dựa trên assumption đó.
2. Đẩy từ quan sát cục bộ thành invariant/quy tắc toàn cục mới.
3. Nếu biến đổi fail thì coi như assumption fail:
    - có phản ví dụ, hoặc không chứng minh được.
    - hoặc không tạo được hướng tiến triển sau biến đổi.
4. Khi assumption fail:
    - loại assumption hiện tại và quay lại `III-B` để thử assumption khác.
    - nếu cần, quay lại `III-A` để đổi dạng biến đổi sơ cấp trước khi giả định lại.


### V. Commit Solution (Chốt thuật toán)
1. Chọn hướng giải theo cấu trúc đã tìm được: [[chọn_nhanh_thuật_toán]]
2. Nêu lý do đúng:
    - dựa trên invariant, tính đơn điệu, cấu trúc dữ liệu, hoặc quy nạp.
3. Kiểm tra độ phủ:
    - case thường, case biên, case xấu nhất.
4. Kiểm tra độ phức tạp:
    - có qua giới hạn đề không?

### VI. Implement & Validate (Code và xác thực)
16. Viết code theo block:
    - preprocess -> core logic -> output.
17. Test tối thiểu:
    - random nhỏ + brute force (nếu làm được)
    - edge cases tự thiết kế
18. Nếu WA/TLE:
    - quay lại bước II-IV trước khi sửa vặt code.

### VII. Look Back (Nhìn lại để tích lũy)
19. Gắn nhãn bài:
    - invariant-based, constructive, monotonicity, greedy, DP, graph,...
20. Ghi 1-2 câu "dấu hiệu nhận biết" để tái sử dụng cho bài sau.
