# Shortest Path - Tổng quan và tính chất

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Data_Structures/Graph/Shortest_paths)

## Vai trò trong State Space Search
- Shortest path là trường hợp đặc biệt của state space search: state chỉ là đỉnh `u` hoặc `(u, extra_state...)`.
- Khi có ràng buộc (số lần dùng phép, parity, mask, số cạnh...), mở rộng sang đồ thị trạng thái rồi chạy BFS/Dijkstra/0-1 BFS.

## Tính chất cốt lõi
- **Optimal substructure**: mọi đoạn con của một shortest path cũng là shortest path giữa hai đầu đoạn đó.
- **Triangle inequality**: `dist(a, b) <= dist(a, c) + dist(c, b)`.
- Là simple path nếu không có **negative cycle**
- Tập cạnh cha từ 1 nguồn tạo thành **Shortest Path Tree (SPT)** (có thể không duy nhất nếu có nhiều đường đi bằng nhau).
- Multi-source tương đương thêm super source `S` nối cạnh trọng số `0` tới tập nguồn `S'`
- Nếu có reweight cạnh (u, v, w) thành (u, v, w') thì xét các trường hợp :
    - undirected : `dist(a, b) = min(dist(a, b), dist(a, u) + w' + dist(v, b), dist(a, v) + w' + dist(u, b))`
    - directed : `dist(a, b) = min(dist(a, b), dist(a, u) + w' + dist(v, b))`
- Truy vấn "tìm 1 đỉnh bất kì đi đến 1 đích `t`" thường xử lý nhanh bằng cách chạy từ `t` trên **reverse graph**.

## Tính chất theo loại đồ thị
- **Undirected**: nếu trọng số đối xứng, `dist(u, v) = dist(v, u)`.
- **Directed**: khoảng cách có thể bất đối xứng, cần phân biệt rõ chiều cạnh.
- **DAG**: cho phép cạnh âm nhưng vẫn giải tuyến tính bằng topo DP.
- **Tree**: đường đi giữa 2 đỉnh là duy nhất, nên shortest path chính là đường đi duy nhất đó.
- **Implicit graph** (trạng thái sinh online): không cần dựng đủ đồ thị, chỉ cần hàm sinh neighbor hợp lệ.

## Thuật toán theo loại đồ thị / trọng số
| Loại graph / cạnh | Thuật toán chuẩn | ĐK áp dụng | Độ phức tạp |
|---|---|---|---|
| Unweighted / cùng trọng số | BFS | Cạnh cùng cost | `O(n + m)` |
| Trọng số `0/1` | 0-1 BFS (deque) | `w in {0,1}` | `O(n + m)` |
| Trọng số nguyên nhỏ không âm | Dial / bucket | `0 <= w <= C` nhỏ | `O(m + nC)` |
| Không âm | Dijkstra + heap | `w >= 0` | `O((n + m) log n)` |
| Không âm, graph dày | Dijkstra `O(n^2)` | `m ~ n^2` | `O(n^2)` |
| Có cạnh âm, không negative cycle | Bellman-Ford | Tổng quát | `O(nm)` |
| DAG (có thể âm) | DP topo order | Đồ thị có hướng không chu trình | `O(n + m)` |
| All-pairs, `n` vừa, graph dày | Floyd-Warshall | Có thể âm, không negative cycle | `O(n^3)` |
| All-pairs graph thưa + có cạnh âm | Johnson + Dijkstra | Không negative cycle | `O(nm log n)` |
| Tree | DFS/BFS cộng dồn cost | Không chu trình | `O(n)` từ 1 nguồn |

## Các loại shortest path thường gặp
- **Single-pair** `s -> t`: chạy từ `s`, có thể dừng sớm khi pop ra `t` (BFS/Dijkstra).
- **Single-source**: từ 1 nguồn đến mọi đỉnh.
- **Single-destination**: từ mọi đỉnh đến 1 đích, chạy trên reverse graph.
- **Multi-source**: từ tập nguồn đến mọi đỉnh gần nhất.
- **All-pairs**: mọi cặp đỉnh.
- **K shortest distances per node**: giữ tối đa `k` dist tốt nhất mỗi node + heap toàn cục.
- **Second shortest path**: lưu `best1`, `best2` cho mỗi đỉnh.
- **Shortest path có ràng buộc** (state space search):
        - đúng `k` cạnh / không quá `k` cạnh
        - chẵn/lẻ số cạnh (parity)
        - đi qua tập đỉnh bắt buộc
        - có budget tài nguyên (fuel, số lần phép, coupon...)
- **Minimax path** (minimize max edge) và **widest path** (maximize min edge) là họ "path optimization" gần shortest path, thường giải bằng biến thể Dijkstra

## Biến thể nâng cao thường gặp trong contest
- **Bidirectional BFS / Dijkstra**: chạy từ cả `s` và `t` để giảm không gian tìm kiếm.
- **K shortest paths (toàn bộ path)**:
    - Cho phép lặp đỉnh/cạnh (walk): thường dùng PQ + dist mở rộng.
- **Nhiều truy vấn trên tree**:
    - Trọng số không đổi: preprocess LCA + dist gốc.
    - Có update/query phức tạp: HLD + segment tree/Fenwick.

## Tính đúng của thuật toán (ý chính)
- BFS đúng vì mở rộng theo lớp số cạnh tăng dần.
- 0-1 BFS đúng vì deque giữ invariant dist tăng dần (đẩy trước với cạnh `0`, đẩy sau với cạnh `1`).
- Dijkstra đúng khi tất cả cạnh không âm: đỉnh pop đầu tiên khỏi heap có dist đã cố định.
- Bellman-Ford đúng vì sau `i` vòng relax có đáp án tốt nhất với tối đa `i` cạnh.
- Floyd-Warshall DP trên tập đỉnh trung gian.

## Liên kết
- [Khái niệm](<Khái niệm.md>)
- [Single source one best state](<Single source one best state.md>)
- [Single source k best state](<Single source k best state.md>)
- [Multisource](Multisource.md)
- [All pair search](<All pair search.md>)
