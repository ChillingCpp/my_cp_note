
- Sử dụng khi yêu cầu construct optimal/non-optimal solution khi giải graph/dp/greedy
- sử dụng  $parent[state(u)]$ để truy vết ngược lại
- chỉ update   $parent[state(v)] = state(u)$ khi từ state(u) -> state(v) tối ưu hơn state(v) trước đó 