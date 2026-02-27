# All-Pairs Search

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Graph/Shortest_paths/dijkstra_all_pair.cpp)

## Mục tiêu
- Tìm thông tin đường đi cho mọi cặp đỉnh.

## Chọn thuật toán
- Floyd-Warshall: graph dày, `n` vừa phải.
- Chạy Dijkstra/BFS từ từng đỉnh: graph thưa.
- Johnson:
  	- Dùng khi graph thưa, trọng số âm nhưng **không có negative cycle**.
  	- Ý tưởng: Bellman-Ford/SPFA để lấy `h[v]`, 
  	- reweight cạnh `w'(u,v) = w(u,v) + h[u] - h[v]` (không âm), rồi chạy Dijkstra từ từng đỉnh.
  	- lấy khoảng cách gốc : `dist(u, v) = dist'(u,v) + h[u] - h[v]`

## Gợi ý
- Nếu chỉ cần vài nguồn đặc biệt, không cần all-pairs đầy đủ.
- Nếu có cạnh âm, cẩn thận điều kiện áp dụng của từng thuật toán.

## Liên kết
- [Khái niệm](<Khái niệm.md>)
- [Multisource](Multisource.md)

