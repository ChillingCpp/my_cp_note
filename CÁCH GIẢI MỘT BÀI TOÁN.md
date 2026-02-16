# CÁCH GIẢI MỘT BÀI TOÁN (Polya cho CP)

## 0) Mục tiêu
- Đây là khung thực chiến: **ngắn, đủ ý quan trọng**, dùng để ép tư duy Polya vào competitive programming.

## I. Understand Problem (Hiểu đúng đề)
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

## II. Discover Structure (Tìm cấu trúc, Biến đổi bài toán)
4. Đáp án phụ thuộc dữ kiện theo cách nào?
    - cục bộ hay toàn cục, trực tiếp hay qua biến trung gian.
5. Cái gì thật sự quyết định đáp án?
    - dữ kiện nào thay đổi mà kết quả không đổi?
6. Tìm invariant/monotonic/bound:
    - thứ gì không đổi?
    - thứ gì chỉ tăng/giảm?
    - có chặn trên/dưới rõ ràng không?

## III. Reformulate & Decompose (Biến đổi và phân rã)
7. Đổi cách phát biểu:
    - tối ưu -> kiểm tra tồn tại
    - đếm trực tiếp -> đếm bù
    - điều kiện khó -> điều kiện tương đương
8. Xét bài toán con và biên:
    - bỏ bớt điều kiện thì gì xảy ra?
    - thêm điều kiện mạnh thì bài có trở nên tầm thường không?
    - test nhỏ nhất/lớn nhất/trường hợp biên có hành vi khác thường không?
9. Tách bài toán:
    - theo đoạn, theo phần tử, theo bước, theo component.
    - các phần độc lập hay phụ thuộc?

## IV. Assumption Control (Kiểm soát giả định - bắt buộc trong CP)
10. Liệt kê giả định ngầm:
    - input luôn hợp lệ?
    - có trùng lặp?
    - thứ tự có quan trọng?
11. Tự tạo phản ví dụ cho ý tưởng hiện tại.
    - nếu ý tưởng không qua được test phá thì bỏ sớm.

## V. Commit Solution (Chốt thuật toán)
12. Chọn hướng giải theo cấu trúc đã tìm được: [[Nhận diện thuật toán]]
13. Nêu lý do đúng:
    - dựa trên invariant, tính đơn điệu, cấu trúc dữ liệu, hoặc quy nạp.
14. Kiểm tra độ phủ:
    - case thường, case biên, case xấu nhất.
15. Kiểm tra độ phức tạp:
    - có qua giới hạn đề không?

## VI. Implement & Validate (Code và xác thực)
16. Viết code theo block:
    - preprocess -> core logic -> output.
17. Test tối thiểu:
    - random nhỏ + brute force (nếu làm được)
    - edge cases tự thiết kế
18. Nếu WA/TLE:
    - quay lại bước II-IV trước khi sửa vặt code.

## VII. Look Back (Nhìn lại để tích lũy)
19. Gắn nhãn bài:
    - invariant-based, constructive, monotonicity, greedy, DP, graph,...
20. Ghi 1-2 câu "dấu hiệu nhận biết" để tái sử dụng cho bài sau.
