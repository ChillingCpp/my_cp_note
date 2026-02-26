# CÁCH GIẢI MỘT BÀI TOÁN (Polya cho CP)

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

## 0) Mục tiêu
- Ưu tiên sử dụng trực giác để tìm được lời giải nhanh cho bài toán hơn
- Trường hợp sử dụng khung này :
    - nếu như 1 lời giải bằng trực giác bị WA, error trong 30p thì sử dụng khung này
    - trực giác không thể cho được lời giải tối ưu.
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

## II. Discover Structure (Tìm cấu trúc)
4. Đáp án phụ thuộc dữ kiện theo cách nào?
    - cục bộ hay toàn cục, trực tiếp hay qua biến trung gian.
5. Cái gì thật sự quyết định đáp án?
    - dữ kiện nào thay đổi mà kết quả không đổi?
6. Tìm invariant/monotonic/bound:
    - thứ gì không đổi?
    - thứ gì chỉ tăng/giảm?
    - có chặn trên/dưới rõ ràng không?

## Lặp đi lặp lại các bước sau 
### III. Dùng Assumption (Giả định có kiểm soát)
10. Viết assumption ra rõ ràng:
    - dạng `Giả sử ... thì ...`.
    - ghi phạm vi áp dụng (mọi test, hay chỉ sau khi biến đổi bài toán).
14. Ví dụ assumption thường dùng trong CP (tóm gọn):
    - Các assumption quan trọng :
        - `Fix để phá đối xứng (symmetry breaking)`: cố định một lựa chọn đại diện để loại các nghiệm tương đương.
        - `Fix thứ tự xử lý` (sort/topo/trái -> phải): tạo đơn điệu để xử lý dần (sweep line, two pointers, DP theo thứ tự).
        - `Fix một cấu hình chuẩn (canonical form)`: chuẩn hóa cách biểu diễn để so sánh/chứng minh dễ hơn.
        - `Fix để giảm chiều trạng thái`: giữ một mốc cố định để rút gọn số biến trạng thái.
        - `Giả sử chỉ cần trạng thái nén` (tập/đếm, không cần lịch sử chi tiết): mở ra DP/bitmask/frequency.
        - `Giả sử có vị trí vi phạm đầu tiên`: suy ra ràng buộc cục bộ rồi nâng thành invariant toàn cục.
        - `Giả sử tồn tại nghiệm tối ưu S`: dùng exchange argument để chuẩn hóa nghiệm (vd: interval scheduling chọn đoạn kết thúc sớm).
        - `Giả sử cấu hình cực trị` (max/min): tìm cấu trúc tight hoặc điểm biên.

### IV. Reformulate & Decompose (Biến đổi và phân rã)
6. Biến đổi bài toán dựa trên assumption
11. Kiểm chứng assumption:
    - suy ra trực tiếp từ đề, hoặc chứng minh bằng invariant/exchange argument.
    - thử phản ví dụ nhỏ: `n=1`, tất cả bằng nhau, đảo thứ tự, biên âm/0/cực đại.
12. Loại bỏ assumption:
    - Nếu có phản ví dụ, hoặc không chứng minh được.
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
10. Nếu không thể biến đổi:
    - loại bỏ assumption, và bắt đầu lại


## V. Commit Solution (Chốt thuật toán)
12. Chọn hướng giải theo cấu trúc đã tìm được: [[chọn_nhanh_thuật_toán]]
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
