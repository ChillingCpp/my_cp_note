# Old Driver Tree (ODT / Chtholly Tree)

## Ý tưởng cốt lõi
- Duy trì các đoạn rời nhau có cùng giá trị.
- Mỗi đoạn lưu `l, r, val` trong `set` sắp theo `l`.
- Mỗi update bắt đầu bằng `split`.

## Hàm `split(x)`
- Nếu `x` nằm giữa đoạn `[l, r]`, tách thành `[l, x-1]` và `[x, r]`, trả iterator tới đoạn bắt đầu tại `x`.
- Nếu `x > n` thì trả `end`.

## Thao tác cơ bản
- Assign `[l, r] = v`: `itR = split(r+1)`, `itL = split(l)`, xóa `[itL, itR)`, chèn `(l, r, v)`.
- Add `[l, r] += v`: lặp qua các đoạn trong `[itL, itR)` và cộng `v`.
- Query sum `[l, r]`: cộng `len * val` trên các đoạn giao với `[l, r]`.
- Query k-th theo giá trị: gom cặp `(val, len)`, sort theo `val`, chọn theo prefix.


## Khi nên cân nhắc ODT thay cho lazy segment tree
- Update dạng `a[i] = f(a[i])` nhưng không thể áp dụng lên aggregate của node (sum/max/...) vì cần biết phân bố giá trị.
- `f` là mapping rời rạc / relabel theo value (ví dụ `1->5, 5->2`) và mapping có thể thay đổi theo query.
- `f` là piecewise theo giá trị (ví dụ `x < k`, `x % 3`), trong một đoạn có thể lẫn nhiều lớp giá trị.
- `f` phụ thuộc tần suất xuất hiện của value trong đoạn hoặc phụ thuộc lịch sử số lần update.
- `f` không thể compose gọn thành một lazy tag nhỏ, tag sẽ phình hoặc phải lưu quá nhiều thông tin.
- ODT xử lý bằng cách tách đoạn rồi apply từng đoạn giá trị đồng nhất, đổi lại chỉ là heuristic và có worst-case xấu.

## Độ phức tạp (heuristic)
- Trung bình gần `O((n + q) log n)` khi dữ liệu "ngẫu nhiên" hoặc cập nhật làm giảm số đoạn.
- Worst-case có thể `O(n^2)` nếu gặp dữ liệu adversarial.

## Khi nên dùng
- Cập nhật gán / cộng đoạn online, dữ liệu không adversarial.
- Không yêu cầu bảo hành worst-case.

## Lưu ý
- Cần `long long` cho độ dài và giá trị.
- Cảnh báo biên `r+1` vượt `n`.
