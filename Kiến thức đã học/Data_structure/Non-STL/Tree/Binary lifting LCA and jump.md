


- $up[u] = up[up[u][i-1]][i-1]$
- $dp[u] = combine(dp[u][i-1], dp[up[u][i-1]][i-1])$
- $f(u, v) = f(u) + f(v) - 2*f(lca(u, v))$
