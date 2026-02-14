# State Space Search - Khái niệm

## Mục tiêu
- Mở rộng node thành trạng thái `(u, extra_state...)` để biểu diễn ràng buộc của đề.

## Mô hình
- Mỗi state là một node trong đồ thị trạng thái.
- Chuyển trạng thái theo cạnh hợp lệ.
- Dùng BFS/Dijkstra/0-1 BFS tùy trọng số.

## Khung cập nhật
- Gọi `best[s]` là giá trị tốt nhất tại state `s`.
- Với chuyển `s -> t` có cost `w`:
  - nếu `best[t]` tốt hơn khi đi qua `s` thì cập nhật và push lại.

## Khi dùng
- Bài có đường đi tối ưu kèm ràng buộc (số bước, số lần dùng phép, mask, parity...).
- Bài k-best state hoặc multi-layer graph.

## Lưu ý
- Đếm đúng số trạng thái trước khi code để tránh nổ bộ nhớ.
- Chọn cấu trúc dữ liệu push/pop theo loại trọng số.
