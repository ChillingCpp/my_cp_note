


- $up[u] = up[up[u][i-1]][i-1]$
- jump :  $if ((1 << i) & k) u = up[u][i]$
- $dp[u] = combine(dp[u][i-1], dp[up[u][i-1]][i-1])$
	- hàm combine phải có tính chất kết hợp
	- tính chất giao hoán có thể không cần : lưu (prefix, suffix), hash của string processing
- gọi f(root, x) là giá trị từ root -> x, rút gọn lại thành f(x), ta có công thức sau :  $f(u, v) = f(u) + f(v) - 2*f(lca(u, v))$
