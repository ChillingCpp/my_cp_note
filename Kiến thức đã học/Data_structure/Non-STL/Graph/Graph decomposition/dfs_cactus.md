( tạm thời chưa cần học )
# DFS Cactus Decomposition

## 1) Định nghĩa cactus graph
- `Cactus graph`: đồ thị vô hướng liên thông mà mỗi cạnh thuộc nhiều nhất 1 chu trình đơn.
- Tương đương: hai chu trình bất kỳ giao nhau nhiều nhất 1 đỉnh.

## 2) Mục tiêu decomposition
- Dùng DFS để:
  - kiểm tra đồ thị có phải cactus không
  - tách đồ thị thành các `block`:
    - block cạnh thường
    - block chu trình
- Từ đó có thể build cactus-tree/cactus-block graph để query.

## 3) Khung DFS thường dùng
1. DFS với `tin[u]`, `low[u]`, parent edge.
2. Dùng stack cạnh để gom block khi phát hiện một chu trình/BCC.
3. Mỗi lần kết thúc block:
   - nếu block có số cạnh = số đỉnh: block là 1 chu trình
   - nếu block có 1 cạnh: block cạnh thường
4. Nếu một cạnh bị gom vào hơn 1 chu trình -> không phải cactus.

Độ phức tạp: `O(n + m)`.

## 4) Tính chất quan trọng
- Trong cactus chuẩn:
  - Mỗi edge nằm trong tối đa 1 cycle.
  - Cấu trúc block-level là tree (hoặc forest nếu input không liên thông).
- Nhiều bài tối ưu đường đi có thể tách thành:
  - xử lý trên tree block
  - cộng thêm xử lý riêng cho từng cycle block

## 5) Ứng dụng điển hình
- Tính số đường đi/chi phí trên cactus.
- Query khoảng cách ngắn nhất khi cạnh có trọng số (cycle xử lý min theo hai hướng).
- Đếm số chu trình độc lập trong cấu trúc cactus.

## 6) Lỗi hay gặp
- Không phân biệt đúng back-edge và parent-edge trong đồ thị vô hướng.
- Dùng điều kiện low-link sai nên tách block sai.
- Input không liên thông nhưng chỉ DFS từ 1 đỉnh.
- Bỏ qua trường hợp multi-edge/self-loop (nhiều đề cấm, nhưng cần đọc kỹ).

## 7) Note cài đặt
- Nên lưu `edge_id` để tránh nhầm cạnh ngược của cùng một cạnh vô hướng.
- Với weighted cactus:
  - lưu prefix sum theo thứ tự đỉnh trên mỗi cycle
  - query trên cycle dùng `min(clockwise, counter_clockwise)`

## Đường dẫn
- [[Bridge_edge_tree]]
