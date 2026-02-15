# Topo + DP trên đồ thị

## Khi dùng
- Đồ thị có hướng không chu trình (DAG).
- Cần tối ưu hoặc đếm số cách trên đường đi.

## Ý tưởng
1. Topological sort.
2. Duyệt theo topo để chuyển trạng thái `u -> v`.
3. Có 2 hướng đi chuẩn : 
	1. Cập nhật `dp[v]` từ `dp[u]`. ( từ cha xuống con )
	2. Cập nhật `dp[u]` từ `dp[v]`. ( từ con lên cha )

## Công thức khung
- Tối ưu: `dp[v] = best(dp[v], combine(dp[u], edge(u, v)))`.
- Đếm cách: `dp[v] += ways_from_u` (có mod nếu đề yêu cầu).

## Nếu graph có chu trình
- [[condensation graph]]
