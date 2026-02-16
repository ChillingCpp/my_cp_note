# Condensation Graph (SCC DAG)

## 1) Định nghĩa
- Với đồ thị có hướng `G`, gom mỗi `SCC` thành một siêu đỉnh.
- Các cạnh giữa hai SCC khác nhau tạo thành cạnh của đồ thị mới.
- Đồ thị thu được gọi là `condensation graph` và luôn là `DAG`.

## 2) Khi nào dùng
- Nén đồ thị có hướng để xử lý theo thứ tự topo.
- Bài toán DP trên đồ thị có chu trình.
- Xử lý phụ thuộc mạnh/yếu giữa các cụm đỉnh.

## 3) Cách build
1. Tìm SCC bằng `Kosaraju` hoặc `Tarjan` (`O(n + m)`).
2. Mỗi đỉnh `u` có `comp[u]`.
3. Với cạnh gốc `u -> v`, nếu `comp[u] != comp[v]` thì thêm cạnh `comp[u] -> comp[v]`.
4. Có thể dùng `set`/sort-unique để loại cạnh trùng.

## 4) Tính chất quan trọng
- Condensation graph không có chu trình.
- Mọi bài toán trên SCC có thể chuyển thành bài toán trên DAG.
- Số đỉnh mới = số SCC, thường nhỏ hơn nhiều so với `n`.

## 5) Ứng dụng điển hình
- Đếm số cạnh/đỉnh cần thêm để mạnh liên thông.
- DP dài nhất/ngắn nhất/số đường đi trên DAG SCC.
- Xác định SCC nguồn/đích (in-degree = 0, out-degree = 0).

## 7) Ghi chú cài đặt
- Mảng thường dùng:
  - `comp[n+1]`
  - `vector<vector<int>> dag(scc_cnt)`
  - `indeg[scc_cnt]`, `outdeg[scc_cnt]`
- Sau khi nén xong, các thuật toán DAG chuẩn chạy trực tiếp.

## Đường dẫn
- [[Topological sort]]
- [[Positive or Negative cycle]]
