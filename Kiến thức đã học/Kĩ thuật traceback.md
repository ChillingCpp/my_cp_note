# Kĩ thuật Traceback

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms)

## 1) Mục tiêu
- Dùng khi đề yêu cầu **construct nghiệm** (không chỉ in giá trị tối ưu).
- Áp dụng nhiều trong: `graph`, `dynamic programming`, `greedy`.

## 2) Ý tưởng cốt lõi
- Khi cập nhật một trạng thái `v` từ trạng thái `u`, lưu lại:
    - `parent[v] = u` (đến từ đâu)
    - hoặc `choice[v]` (đã chọn hành động nào)
- Sau khi tìm được trạng thái đích/tối ưu, đi ngược qua `parent` để dựng nghiệm.

## 3) Quy tắc cập nhật parent
- Chỉ cập nhật `parent[v] = u` khi chuyển `u -> v` **tốt hơn** kết quả hiện tại của `v`.
- Nếu bằng nhau (`tie`), cần chốt quy tắc:
    - giữ parent cũ, hoặc
    - ưu tiên chỉ số nhỏ hơn, hoặc
    - ưu tiên đường đi từ điển nhỏ hơn.

## 4) Mẫu cho shortest path (BFS/Dijkstra/Bellman-Ford)
```cpp
if (dist[v] > dist[u] + w) {
    dist[v] = dist[u] + w;
    parent[v] = u;
}
```

Truy vết:
```cpp
vector<int> path;
for (int cur = t; cur != -1; cur = parent[cur]) path.push_back(cur);
reverse(path.begin(), path.end());
// path là đường đi từ s -> t nếu path[0] == s
```

## 5) Mẫu cho DP
- Ngoài `dp[state]`, lưu thêm:
    - `pre[state]`: state trước đó
    - `take[state]`: quyết định chọn gì để đi tới state này

```cpp
if (cand > dp[nxt]) {
    dp[nxt] = cand;
    pre[nxt] = cur;
    take[nxt] = action;
}
```

## 6) Lưu ý quan trọng
- Khởi tạo `parent` bằng `-1` để biết điểm dừng traceback.
- Với nhiều test, nhớ reset `parent/pre/take`.
- Với đồ thị có chu trình, traceback chỉ an toàn khi mảng parent được cập nhật đúng quy tắc tối ưu.
- Nếu bài yêu cầu in nhiều nghiệm, cần lưu nhiều parent (DAG of decisions), không chỉ 1 parent.


## 8) Checklist nhanh
1. State đích là gì?
2. Mỗi lần relax/update có lưu parent/choice không?
3. Điều kiện tie-break đã cố định chưa?
4. Có kiểm tra reachable trước khi in nghiệm không?

