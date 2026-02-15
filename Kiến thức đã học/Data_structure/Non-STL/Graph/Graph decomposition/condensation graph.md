# Condensation Graph

## Mục tiêu
- Co mỗi SCC thành 1 node để biến directed graph có chu trình thành DAG.

## Cách dựng
1. Tìm SCC (Tarjan/Kosaraju).
2. Gán `comp[u]`.
3. Với cạnh `u -> v`, nếu `comp[u] != comp[v]` thì thêm cạnh mới.

## Tính chất
- Đồ thị co rút luôn là DAG.
