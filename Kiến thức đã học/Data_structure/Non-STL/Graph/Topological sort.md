# Topological Sort

## Khi dùng
- Đồ thị có hướng không chu trình (DAG).

## Tính chất
- Mọi cạnh `u -> v` thì `u` đứng trước `v` trong topo order.

## Thuật toán
- DFS topo.
- Kahn (indegree).

## Ghi chú
- Dùng min-heap trong Kahn nếu cần thứ tự từ điển nhỏ nhất.
