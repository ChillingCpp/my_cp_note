# CÁCH GIẢI MỘT BÀI TOÁN (Polya cho CP)

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

## 0) Khung trực giác (30-60 giây)
1. Bài thuộc loại gì?
    - đếm / tối ưu / xây dựng / kiểm tra tồn tại
2. Constraint chính là gì?
    - `n <= 20` / `n <= 2000` / `n <= 2e5` / nhiều query/test
3. Output là giá trị hay cấu hình?
4. Chọn thuật toán nhanh dựa trên cấu trúc của bài toán và time complexity
    - [[chọn_nhanh_thuật_toán]]
    
Rule:
- Nếu sau 60 giây chưa định hình được nhóm thuật toán, chuyển sang khung chi tiết.

## 1) Khi nào dùng khung chi tiết (20 phút đầu)
- Lời giải trực giác bị WA/TLE/Error trong khoảng 20 phút.
- Trực giác chưa cho hướng tối ưu.
- Cần một quy trình ổn định để tránh sửa vặt theo cảm tính.

## I. Understand Problem (Hiểu đúng đề)
1. Đề hỏi chính xác gì?
    - output là gì, một đáp án hay nhiều đáp án hợp lệ?
2. Input/ràng buộc là gì?
    - kích thước dữ liệu, kiểu dữ liệu, thời gian/bộ nhớ
3. Có thể vô nghiệm không?
    - đề có yêu cầu xử lý trường hợp này không?
4. Mức độ phức tạp mục tiêu là bao nhiêu?

Rule:
- Nếu chưa phát biểu lại đề trong 1-2 câu của riêng mình, coi như chưa hiểu đề.

## II. Discover Structure (Tìm cấu trúc)
1. Đáp án phụ thuộc dữ kiện theo cách nào?
    - cục bộ hay toàn cục, trực tiếp hay qua biến trung gian
2. Cái gì thật sự quyết định đáp án?
    - dữ kiện nào thay đổi mà kết quả không đổi?
3. Tìm các tính chất:
    - invariant (không đổi)
    - monotonic (chỉ tăng/giảm)
    - bound (chặn trên/dưới)

Output của phần II:
- Danh sách tính chất đã xác định được để dùng làm nền cho bước biến đổi.

## III. Vòng lặp khám phá lời giải
Chu trình cố định: `biến đổi sơ cấp -> viết assumption -> chứng minh/biến đổi sâu hơn`.

### III-A. Biến đổi sơ cấp (dựa trên tính chất đã có)
1. Chọn 1-2 tính chất mạnh nhất từ phần II.
2. Biến đổi bài toán dựa trên các tính chất đó:
    - đổi cách phát biểu để bám vào tính chất mạnh nhất
    - tách bài toán theo cấu trúc đã lộ ra
    - loại bỏ thành phần không ảnh hưởng đáp án
3. Mục tiêu:
    - đưa bài toán về dạng dễ thao tác hơn mà chưa thêm giả định mới
4. Nếu chưa mở được hướng tiến triển:
    - giữ dạng biến đổi tốt nhất hiện có rồi sang bước viết assumption

### III-B. Viết assumption (để mở thêm tính chất)
1. Viết rõ assumption theo mẫu: `Giả sử ... thì ...`.
2. Ghi phạm vi áp dụng:
    - đúng cho mọi test, hay chỉ đúng sau biến đổi sơ cấp ở III-A
3. Tiêu chí assumption tốt:
    - giúp lộ thêm cấu trúc
    - có khả năng chứng minh hoặc phản chứng bằng test nhỏ
4. Các assumption thường dùng trong CP:
    - fix để phá đối xứng (symmetry breaking)
    - fix thứ tự xử lý (sort/topo/trái -> phải)
    - fix cấu hình chuẩn (canonical form)
    - fix mốc để giảm chiều trạng thái
    - giả sử chỉ cần trạng thái nén (không cần toàn bộ lịch sử)
    - giả sử có vị trí vi phạm đầu tiên
    - giả sử tồn tại nghiệm tối ưu chuẩn hóa được (exchange argument)
    - giả sử cấu hình cực trị (max/min)

### III-C. Chứng minh assumption và biến đổi sâu hơn
1. Thử chứng minh assumption:
    - suy ra trực tiếp từ đề, hoặc dùng invariant/exchange/đối ngẫu
2. Thử phản ví dụ nhanh:
    - `n = 1`, tất cả bằng nhau, thứ tự đảo ngược, biên âm/0/cực đại
3. Nếu assumption đúng:
    - biến đổi sâu hơn để tạo quy tắc toàn cục hoặc thuật toán cụ thể
4. Nếu biến đổi fail thì coi như assumption fail:
    - có phản ví dụ
    - không chứng minh được
    - hoặc không tạo ra tiến triển sau biến đổi
5. Khi assumption fail:
    - loại assumption hiện tại, quay lại III-B để chọn assumption khác
    - nếu cần, quay lại III-A hoặc II để đổi nền tảng biến đổi

Điều kiện thoát vòng lặp III:
- Đã có mô hình lời giải rõ ràng + lý do đúng sơ bộ + complexity dự kiến hợp lệ.

## IV. Commit Solution (Chốt thuật toán)
1. Chọn thuật toán cụ thể theo cấu trúc đã tìm được: [[chọn_nhanh_thuật_toán]]
2. Nêu lý do đúng:
    - dựa trên invariant, đơn điệu, cấu trúc dữ liệu, hoặc quy nạp
3. Kiểm tra độ phủ:
    - case thường, case biên, case xấu nhất
4. Kiểm tra độ phức tạp:
    - có qua giới hạn đề không?

## V. Implement & Validate (Code và xác thực)
1. Viết code theo block:
    - preprocess -> core logic -> output
2. Test tối thiểu:
    - random nhỏ + brute force (nếu làm được)
    - edge cases tự thiết kế
3. Nếu WA/TLE:
    - quay lại II-III trước khi sửa vặt code

## VI. Look Back (Nhìn lại để tích lũy)
1. Gắn nhãn bài:
    - invariant-based, constructive, monotonicity, greedy, DP, graph...
2. Ghi 1-2 câu "dấu hiệu nhận biết" để tái sử dụng cho bài sau.
3. Ghi lại assumption đã fail để tránh lặp lại sai lầm tương tự.
