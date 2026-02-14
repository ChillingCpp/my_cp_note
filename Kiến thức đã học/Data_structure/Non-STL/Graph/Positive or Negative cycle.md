# Positive / Negative Cycle

## Mục tiêu
- Phát hiện chu trình âm (hoặc dương nếu đổi dấu).

## Cách 1: SPFA
- Nếu một node bị relax quá `n` lần, có khả năng dính chu trình âm.
- Để lan truyền ảnh hưởng cycle từ nguồn `s` đến đích `t`, tiếp tục đẩy relax thêm 5 vòng và đánh dấu node chịu ảnh hưởng, việc lan truyền ảnh hưởng cycle sẽ bỏ qua block if $d[u] > d[v] + w$, có cấu trúc là sử dụng block if $d[u] > d[v] + w$

## Cách 2: Floyd-Warshall
- Sau khi chạy Floyd, nếu `dist[i][i] < 0` thì có chu trình âm đi qua `i`.

## Ghi chú
- Positive cycle tương tự negative cycle nếu đổi quy ước dấu khi tối ưu.
- Khi cần truy vết cycle cụ thể, dùng mảng parent (traceback).
