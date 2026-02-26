# Positive / Negative Cycle

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Graph/Shortest_paths/SPFA.cpp)

## Mục tiêu
- Phát hiện chu trình âm (hoặc dương nếu đổi dấu).

## Cách 1: SPFA
- Nếu một node bị relax quá `n` lần, có khả năng dính chu trình âm.
- Điều kiện relax chuẩn: `d[v] > d[u] + w`.
- Traceback negative cycle:
  - Lưu `parent[v]` mỗi khi relax thành công `u -> v`.
  - Khi có `cnt[v] >= n`, đặt `x = v` (đã phát hiện dính chu trình âm).
  - Dựng chu trình:
    1. Đi ngược `n` bước theo `parent` từ `x` để chắc chắn vào trong cycle.
    2. Từ đỉnh đó, tiếp tục đi theo `parent` đến khi quay lại đỉnh bắt đầu.

- Lan truyền ảnh hưởng cycle:
  - Sau khi có các đỉnh dính chu trình âm, BFS/DFS từ tập đỉnh đó trên đồ thị gốc để đánh dấu toàn bộ đỉnh bị ảnh hưởng.

## Cách 2: Floyd-Warshall
- Sau khi chạy Floyd, nếu `dist[i][i] < 0` thì có chu trình âm đi qua `i`.
- Traceback negative cycle:
  - Lưu thêm ma trận `nxt[u][v]` (đỉnh kế tiếp khi đi từ `u` đến `v`).
  - Khởi tạo:
    - Có cạnh `u -> v` thì `nxt[u][v] = v`
    - Không có cạnh thì `nxt[u][v] = -1`
  - Khi relax qua `k`:
    - Nếu `dist[u][k] + dist[k][v] < dist[u][v]` thì cập nhật
      - `nxt[u][v] = nxt[u][k]`
  - Sau Floyd, chọn `x` sao cho `dist[x][x] < 0`, khi đó có chu trình âm.
  - Cách dựng chu trình:
    1. Đặt `cur = x`
    3. Từ `start = cur`, lặp `cur = nxt[cur][x]` và ghi vào mảng đến khi quay lại `start`

## Ghi chú
- Positive cycle tương tự negative cycle nếu đổi quy ước dấu khi tối ưu.
- Khi cần truy vết cycle cụ thể, dùng mảng parent (traceback).
- [Kĩ thuật traceback](<../../../Kĩ thuật traceback.md>)
