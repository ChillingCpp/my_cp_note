# Sweep Line

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/Geometry)

## 1) Khái niệm
- Sweep line là kỹ thuật quét các sự kiện theo một trục đã sắp thứ tự (thường là theo `x` hoặc theo thời gian).
- Tại mỗi sự kiện, cập nhật một cấu trúc dữ liệu trạng thái đang "active" để trả lời câu hỏi hiện tại.

## 2) Khi nào dùng
- Bài toán hình học/đoạn thẳng/hình chữ nhật có điều kiện giao nhau, phủ, đếm đoạn.
- Bài toán interval theo thời gian: số lượng công việc đồng thời, lịch, phòng họp.
- Bài toán có dạng "xử lý offline theo thứ tự".

## 3) Khung tư duy
1. Chuyển input thành `events` (điểm bắt đầu, kết thúc, query...).
2. Sort event theo khóa chính (`x/time`) và tie-break hợp lý.
3. Duy trì DS active:
   - multiset / priority_queue
   - Segment Tree (khi cần range query/update)
4. Ở mỗi event: add/remove/query theo bất biến bài toán.

## 4) Ví dụ event chuẩn
- Interval overlap:
  - `(l, +1)` khi bắt đầu
  - `(r, -1)` khi kết thúc
  - quét prefix để lấy số lượng active lớn nhất.
- Rectangle union area:
  - event mở/đóng theo trục `x`
  - segment tree theo trục `y` để giữ độ dài phủ.

## 5) Tie-break rất quan trọng
- Cùng tọa độ, phải xác định thứ tự event rõ ràng:
  - tùy đề có thể ưu tiên `remove trước add` hoặc ngược lại.
- Sai tie-break là nguồn WA phổ biến nhất của sweep line.

## 6) Độ phức tạp
- Thường là `O((n + q) log n)` do sort + cập nhật DS.


