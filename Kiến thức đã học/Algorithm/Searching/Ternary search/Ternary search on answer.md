# Ternary Search on Answer

## 1) Bản chất
- Dùng khi hàm mục tiêu `f(x)` là **unimodal** trên miền tìm kiếm:
    - tăng rồi giảm (tìm max), hoặc
    - giảm rồi tăng (tìm min).
- Khác với binary search on answer: ternary không cần predicate đơn điệu `check(x)`.

## 2) Khi nào dùng
- Tối ưu trên miền liên tục hoặc nguyên khi có đúng 1 cực trị trong miền.
- Bài toán kiểu:
    - tìm `argmax f(x)` hoặc `argmin f(x)`
    - `f(x)` tính được trực tiếp (hoặc đủ nhanh) cho mỗi `x`

## 3) Điều kiện quan trọng
- Hàm phải có đúng một đỉnh/đáy trong miền xét (unimodal).
- Nếu có nhiều cực trị cục bộ, ternary không đảm bảo đúng.
- Nếu bài có tính "đúng/sai" đơn điệu, ưu tiên binary search on answer.

## Mẫu bài mẫu
[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/Searching/Tenary_Search.cpp)

## 6) Độ phức tạp
- Mỗi vòng gọi `f` 2 lần.
- Số vòng là `O(log(R-L))`.
- Tổng: `O(cost(f) * log(R-L))`.

## 7) Lỗi hay gặp
- Dùng ternary cho hàm không unimodal.
- Quên đảo điều kiện khi tìm min thay vì max.
- Trên miền nguyên không duyệt nốt đoạn cuối.
- So sánh số thực thiếu sai số (`eps`) khi bài nhạy chính xác.
