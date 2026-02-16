# All-Pairs Search

## Mục tiêu
- Tìm thông tin đường đi cho mọi cặp đỉnh.

## Chọn thuật toán
- Floyd-Warshall: graph dày, `n` vừa phải.
- Chạy Dijkstra/BFS từ từng đỉnh: graph thưa.
- Johnson:
  - Dùng khi graph thưa, có thể có cạnh âm nhưng **không có negative cycle**.
  - Ý tưởng: Bellman-Ford/SPFA để lấy `h[v]`, 
  - reweight cạnh `w'(u,v) = w(u,v) + h[u] - h[v]` (không âm), rồi chạy Dijkstra từ từng đỉnh.
  - lấy khoảng cách gốc : `dist(u, v) = dist'(u,v) + h[u] - h[v]`
  - Độ phức tạp thường dùng: `O(n * m log n)` ( n * m <= 1e6 )
- Nếu có negative cycle: không tồn tại lời giải shortest path hữu hạn cho mọi cặp liên quan cycle.

## Gợi ý
- Nếu chỉ cần vài nguồn đặc biệt, không cần all-pairs đầy đủ.
- Nếu có cạnh âm, cẩn thận điều kiện áp dụng của từng thuật toán.

## Liên kết
- [[Khái niệm]]
- [[Multisource]]
