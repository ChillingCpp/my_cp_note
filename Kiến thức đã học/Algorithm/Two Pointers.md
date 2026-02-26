# Two Pointers

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/merge2set.cpp)

## 1) Bản chất
- Dùng 2 con trỏ để duy trì một trạng thái hợp lệ và cập nhật đáp án theo thời gian tuyến tính hoặc gần tuyến tính.
- Ý tưởng chung: mỗi con trỏ chỉ đi tiến (hoặc đi theo quy tắc rất hạn chế), tránh duyệt `O(n^2)`.

## 2) Dạng 1: Cửa sổ trượt trên một mảng (quan trọng nhất)
- Điều kiện thường gặp:
    - nếu subarray `[L, R]` thỏa mãn thì các subarray con bên trong cũng thỏa mãn.
- Cách làm:
    - fixed `R`, tịnh tiến `L` để `[L, R]` trở lại hợp lệ.
    - cập nhật đáp án bằng cửa sổ hiện tại.

## 3) Dạng 2: Hai con trỏ ở hai đầu mảng
- Thường gặp trong bài đã sort hoặc có thể sort trước.
- Mục tiêu: ghép cặp, kiểm tra tổng/hiệu, tối ưu khoảng cách,...
- Đây là dạng ít gặp hơn sliding window nhưng rất mạnh trong bài greedy + sorting.

## 4) Dạng 3: Hai con trỏ trên hai mảng khác nhau
- Dùng để duyệt đồng thời 2 dãy đã sort.
- Ví dụ:
    - merge hai dãy
    - các bài greedy sorting cần so khớp phần tử giữa 2 tập

## 5) Slow/Fast Pointer (Floyd cycle finding)
- Dùng cho bài tìm chu trình trong quá trình lặp trạng thái (không nhất thiết là đồ thị tường minh).
- Công thức:
    - `slow = f(slow)`
    - `fast = f(f(fast))` hoặc phổ biến hơn `fast = f(fast)` hai lần mỗi bước.

## 6) Kĩ thuật adjust pointer trong greedy (ý rất quan trọng)
- Bắt đầu từ một `feasible solution`.
- Fixed một con trỏ, điều chỉnh con trỏ còn lại để duy trì điều kiện hợp lệ.
- So sánh/cập nhật với nghiệm tốt nhất hiện tại.
- Phần lớn bài hai con trỏ thực chất là dạng adjust pointer này.
- Luôn hướng tới local optimal ở mỗi bước để đạt global optimal.

## 7) Kĩ thuật 2 con trỏ greedy theo lựa chọn trực tiếp
- Thường kết hợp sort để mỗi bước chọn phương án cục bộ tốt nhất.
- Khởi tạo từ đầu mảng (hoặc hai đầu tùy bài).
- Mỗi bước là "chọn tốt nhất ngay" thay vì chỉ điều chỉnh để hợp lệ.

