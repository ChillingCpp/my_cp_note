# Multi-source Search

## Ý tưởng
- Khởi tạo nhiều nguồn cùng lúc với khoảng cách 0, sau đó chạy BFS/Dijkstra như single-source.

## Tương đương lý thuyết
- Thêm super source `S`.
- Nối `S -> s_i` trọng số 0 cho mọi nguồn `s_i`.

## Sử dụng khi
- có nhiều nguồn, chỉ cần biết có tồn tại nguồn bất kì.
- trạng thái tốt nhất từ 1 đỉnh tới 1 nguồn bất kì
- Flood fill từ nhiều điểm.
- Nearest special node.
- Kiểm tra tồn tại đường đi từ tập nguồn.

## Biến thể hay gặp
- reverse directed graph
- Multi-source + 0-1 BFS.
- Multi-source trên DAG.
- Chạy từ 2 tập nguồn để meet-in-the-middle trên graph.

## Độ phức tạp
- BFS: `O(n + m)`.
- Dijkstra: `O((n + m) log n)`.
