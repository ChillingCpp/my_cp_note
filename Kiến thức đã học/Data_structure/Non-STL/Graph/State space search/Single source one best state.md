# Single Source - One Best State

## Mục tiêu
- Tìm trạng thái tốt nhất duy nhất cho mỗi node (hoặc mỗi state của node).

## Khung giải
1. Khởi tạo state bắt đầu và đẩy vào queue/heap.
2. Pop trạng thái tốt nhất hiện tại.
3. Relax sang trạng thái kế tiếp.
4. Bỏ qua trạng thái lỗi thời nếu không còn tối ưu.

## Chọn thuật toán
- BFS: cạnh trọng số đều.
- 0-1 BFS: trọng số `0/1`.
- Dijkstra: trọng số không âm.

## Đường dẫn
- [[Khái niệm]]
