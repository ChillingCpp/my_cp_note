# Connected Component Graph

## Mục tiêu
- Co mỗi connected component (vô hướng) thành node đại diện.

## Cách dựng
1. Tìm component bằng DFS/BFS/DSU.
2. Gán `comp[u]` cho mỗi node.
3. Với cạnh `(u,v)`, nếu `comp[u] != comp[v]` thì tạo cạnh giữa 2 component.
