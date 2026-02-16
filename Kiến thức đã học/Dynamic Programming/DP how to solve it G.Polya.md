# DP How To Solve It (G. Polya cho Dynamic Programming)

## 1) Understand The Problem
### What is unknown? What are data? What are conditions?
- `Unknown`: cần tính gì?
  - min / max / count / exist / số cách / giá trị tốt nhất
- `Data`: input + constraints
  - `n`, `m`, giá trị phần tử, giới hạn bộ nhớ/thời gian
  - đoán sớm mức độ phức tạp chấp nhận được
- `Conditions`: ràng buộc tác động đến quyết định
  - ràng buộc local hay global
  - có thứ tự thời gian/index không
  - có điều kiện “không được chọn kề nhau”, “đúng k phần tử”, “chẵn/lẻ”, “mask” không

Checklist:
1. Viết lại đề bằng 2-3 dòng ngôn ngữ của mình.
2. Gạch đầu dòng toàn bộ ràng buộc.
3. Nêu rõ output cần tối ưu hay đếm.

## 2) Devise A Plan
### Phân rã thành bài toán con
- Hỏi: “Nếu cố định một phần quyết định thì phần còn lại là gì?”
- Hỏi: “Để quyết định bước tiếp theo, cần nhớ tối thiểu thông tin nào?”

`Thông tin phải nhớ tối thiểu` chính là state.

Các trục state thường gặp:
- `i`: xử lý đến vị trí i
- `sum / cost / value`: tổng hoặc chi phí hiện tại
- `k`: đã chọn bao nhiêu phần tử
- `mask`: tập đã dùng/chưa dùng
- `last`: phần tử cuối hoặc trạng thái trước đó

Nếu bí:
1. Viết brute force tree của các lựa chọn.
2. Tìm các node con trùng nhau để gộp thành state.
3. Liên hệ các dạng chuẩn: knapsack, LIS, LCS, interval DP, tree DP, bitmask DP.

## 3) Carry Out The Plan
### Dàn khung chuẩn cho một lời giải DP
1. Định nghĩa state chính xác.
2. Xác định base case.
3. Viết transition từ state cũ -> state mới.
4. Chọn thứ tự duyệt để mọi phụ thuộc đã có trước khi dùng.
5. Tính đáp án từ tập state cuối.

Template tự kiểm:
- State:
  - `dp[ ... ]` biểu diễn gì (một câu duy nhất, không mơ hồ)
- Base:
  - giá trị khởi tạo cho trạng thái rỗng/đầu tiên
- Transition:
  - mỗi quyết định hợp lệ cập nhật ra sao
- Correctness:
  - không thiếu trường hợp
  - không đếm trùng
  - không bị cycle dependency
- Complexity:
  - số state * số chuyển mỗi state

Ghi chú:
- Có thể làm top-down (memo) hoặc bottom-up.
- Nếu phụ thuộc ít lớp trước, cân nhắc rolling array để giảm bộ nhớ.

## 4) Look Back (Tối ưu và khái quát)
- State có dư chiều không?
- Có thể bỏ chiều bằng invariant hoặc prefix/suffix không?
- Có thể tối ưu transition không?
  - prefix minima/maxima
  - monotonic queue
  - divide and conquer optimization
  - convex hull trick / slope trick
- Có thể đổi mô hình sang graph shortest path / DAG DP / bitset không?

Mục tiêu sau cùng:
- từ mô hình đúng -> mô hình gọn
- từ `O(n^2)` -> `O(n log n)` hoặc tốt hơn khi cần

## Mini checklist trước khi submit
1. Đã test case nhỏ tự tạo chưa?
2. Đã test case biên (`n=1`, toàn âm, toàn dương, impossible) chưa?
3. Khởi tạo `INF/-INF` có đúng kiểu dữ liệu (`long long`) chưa?
4. Có reset mảng giữa nhiều test không?
