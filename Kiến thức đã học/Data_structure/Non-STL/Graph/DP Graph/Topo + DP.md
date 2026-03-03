# Topo + DP trên đồ thị

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Graph/DP_Topological_sort.cpp)

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
- Đếm số lượng topo thỏa mãn mỗi child chỉ có duy nhất 1 parent : 
    - gọi $dp[u]$ là số hoán vị hợp lệ trong subtree, khởi tạo $dp[u]= 1$
    $$dp[u] = \frac{S_u!}{\prod s_i!}  \cdot  \prod dp[v_i]   \pmod{10^9+7}$$ với $S_u$ là size của subtree gốc u nhưng không bao gồm u
        - nếu có nhiều root $r_1,r_2,...r_i$ : $DP = \frac{R!}{\prod r_i!}  \cdot  \prod dp[r_i]   \pmod{10^9+7}$
        - [Combinatorics and Probability](<../../../../Math/Combinatorics and Probability.md>)
	
## Nếu graph có chu trình
- [condensation graph](<../Graph decomposition/condensation graph.md>)

