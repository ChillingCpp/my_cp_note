# Shortest-path Subgraph (Tight-edge Graph)

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Data_Structures/Graph/Shortest_paths)

## Định nghĩa
- Cho nguồn `s`, sau khi có `dist[]` (khoảng cách ngắn nhất từ `s`), cạnh `u -> v` trọng số `w` được gọi là `tight` nếu:
    - `dist[u] + w = dist[v]`
- `Shortest-path subgraph` là đồ thị con giữ lại tất cả đỉnh reachable (`dist < INF`) và tất cả cạnh `tight`.

## Ý nghĩa
- Đồ thị con này chứa **mọi** đường đi ngắn nhất từ `s` đến các đỉnh reachable.
- Khác với `shortest-path tree`:
    - Tree chỉ giữ 1 parent cho mỗi đỉnh.
    - Subgraph giữ toàn bộ cạnh có thể nằm trên shortest path.

## Cách làm chuẩn
1. Chạy thuật toán shortest path phù hợp để lấy `dist[]`.
2. Duyệt từng cạnh gốc `u -> v (w)`.
3. Nếu `dist[u] != INF`, `dist[v] != INF` và `dist[u] + w == dist[v]` thì thêm vào subgraph.

## Chọn thuật toán lấy `dist`
- Trọng số không âm: `Dijkstra`.
- Trọng số `0/1`: `0-1 BFS`.
- Có cạnh âm, không có negative cycle: `Bellman-Ford`/`SPFA`.

## Tính chất quan trọng
- Mọi shortest path đều chỉ đi qua cạnh `tight`.
- Với mọi đường đi `s -> ... -> v` trong subgraph, tổng trọng số đúng bằng `dist[v]`.
- Subgraph **không nhất thiết là cây**.

## Khi nào subgraph là DAG?
- Nếu mọi cạnh `tight` làm khoảng cách tăng chặt (`dist[u] < dist[v]`), thì là DAG.
- Nếu có cạnh trọng số `0`, có thể có chu trình giữa các đỉnh cùng `dist`, nên không còn DAG thuần.
- Khi cần DAG để DP/topo:
    - Nén SCC của subgraph để được condensation DAG.

## Ứng dụng
- Đếm số shortest path (khi cấu trúc sau xử lý là DAG).
- Tìm cạnh/đỉnh bắt buộc xuất hiện trong mọi shortest path.
- Làm DP trên lớp khoảng cách.
- Lọc không gian tìm kiếm chỉ còn cạnh hữu ích cho shortest path.

## Lỗi thường gặp
- So sánh equality với số thực (`double`) mà không dùng `eps`.
- Cộng `dist[u] + w` trực tiếp gây overflow.
- Nhầm giữa `shortest-path tree` và `shortest-path subgraph`.
- Dùng Dijkstra khi có cạnh âm.

## Độ phức tạp
- Build subgraph: `O(m)`.
- Tổng: `O(chi_phi_SSSP + m)`.
    - Dijkstra: `O((n + m) log n)`.
    - 0-1 BFS: `O(n + m)`.

## Đường dẫn
- [Single source one best state](<../State space search/Single source one best state.md>)
- [Topo + DP](<../DP Graph/Topo + DP.md>)
- [Condensation graph](<../Graph decomposition/condensation graph.md>)
- [Positive or Negative cycle](<../Positive or Negative cycle.md>)
