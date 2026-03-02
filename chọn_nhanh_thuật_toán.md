# Pattern Recognize + Potential Ranking

## Yêu cầu về file chọn thuật toán tối nhanh
- Cách giải 1 bài toán dựa vào [how_to_solve_it](how_to_solve_it.md)
- Chọn thuật toán là 1 bước trong file đó, đọc file đó và sau đó đọc file này

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

## 0) Flow mapping nhanh 30s (dùng trước mọi thứ)

1. Chuẩn hóa đề trong 1 câu: `object + thao tác + mục tiêu`.
2. Xác định lớp bài: `number` hoặc `linear` hoặc `graph/tree/state`.
3. Xác định kiểu thao tác: `single` / `many queries` / `dynamic updates`.
4. Xác định kiểu mục tiêu: `optimize` / `count` / `exist` / `k-th`.
5. Gắn keyword cứng: `subarray`, `submatrix`, `nearest`, `component`, `dependency`, `cycle`, `palindrome`, `check(x)`, `first/last`, `first true/last true`, `leftmost/rightmost`, `k-th`, `find any`, `range query/update`, `point update`, `range update`, `walk on segment tree`, `non-commutative merge`, `tight-started-state`, `F(R)-F(L-1)`, `divisor/multiple`, `one-shot`, `non-tree edge`, `second-best MST`, `critical edge/node`, `BET/BCT`, `cactus`, `multisource`, `construct path`, `linearizing 2D -> 1D`, `fixed top/bottom`, `fixed left/right`, `compressed[]`, `Kadane 2D`, `submatrix sum = k`, `O(K^2 * F(L))`.
6. Chạy hard filter.
7. Chấm điểm tiềm năng (0-10): `fit cấu trúc` + `fit thao tác` + `fit complexity` + `fit tính chất đặc biệt`.
8. Xếp hạng:
   - `High`: 8-10
   - `Medium`: 5-7
   - `< 5`: loại khỏi shortlist (không xếp hạng)
9. Chốt thứ tự thử: `High dễ code trước`, rồi `High còn lại`, rồi `Medium`.
10. Kiểm tra trước khi code: phản ví dụ nhỏ + complexity check.

### Mẫu điền nhanh (copy/paste)

- `Object`:
- `Ops`:
- `Goal`:
- `Constraints`:
- `Keywords`:
- `Hard filters pass/fail`:
- `High`:
- `Medium`:
- `Rejected (nếu có)`:

### Mục tiêu: **không đoán thuật toán trực tiếp từ đề**, mà **biến đổi bài toán -> trích xuất từ khóa -> xếp hạng tiềm năng thuật toán (High/Medium)**.
### Đầu ra cuối cùng phải là **một shortlist có thứ tự ưu tiên**, không phải một thuật toán duy nhất.


## I. Quy tắc bắt buộc trước khi tra từ khóa

### 1) Chuẩn hóa đối tượng

- Tree -> Euler tour/flatten -> array/range.
- Subtree -> đoạn `[tin, tout]`.
- Path query on tree -> LCA + tách đoạn hoặc HLD.
- Grid 2D -> graph/component hoặc prefix 2D hoặc `linearizing 2D -> 1D` (cố định 2 biên + mảng nén `compressed[]`).
- Quan hệ phụ thuộc/trạng thái -> directed graph hoặc state-space graph.

### 2) Chuẩn hóa yêu cầu

- Tối ưu -> `min/max` hoặc chuyển sang feasibility.
- Đếm -> frequency/prefix/combinatorics/DP count.
- Tồn tại -> boolean check.
- `k-th` -> order statistic hoặc binary search on answer + counting.
- Nếu đề yêu cầu **in nghiệm cụ thể**: thêm trục `traceback` (`parent/pre/take/choice`), không chỉ tối ưu giá trị.

### 3) Chuẩn hóa trục thời gian

- Một lần xử lý -> normal.
- Nhiều truy vấn -> query problem.
- Có update -> dynamic.
- Có thể xử lý offline hay bắt buộc online.

### 4) Chuẩn hóa ràng buộc

- `n, m, q` cỡ nào (`1e5`, `2e5`, `1e6`...).
- Cần `O(n)`, `O(n log n)`, hay chấp nhận `O(n sqrt n)`.
- Giá trị có âm/không âm, có thể có cycle âm không.

### 5) Nếu chưa chuẩn hóa xong 4 bước này thì chưa xếp hạng tiềm năng.

---

## II. Cơ chế chấm tiềm năng (High / Medium + loại bỏ)

### 1) Hard filter (lọc cứng)

Nếu vi phạm điều kiện cứng thì thuật toán đó bị **loại khỏi shortlist**:

| Thuật toán | Điều kiện cứng | Nếu thiếu điều kiện |
|---|---|---|
| Prefix sum / Prefix min-max | Dữ liệu tĩnh hoặc truy vấn không update phá prefix | Loại khỏi shortlist |
| Difference Array | Nhiều range update + tổng hợp cuối/offline | Loại khỏi shortlist |
| Segment Tree | Phép gộp có tính kết hợp (có thể không giao hoán), cần query/update online | Loại khỏi shortlist |
| Lazy Segment Tree | Range update tổng quát, không prune one-shot | Loại khỏi shortlist |
| Mo | Offline query + add/remove cục bộ hiệu quả | Loại khỏi shortlist |
| Binary Search on Answer | Có `check(x)` đơn điệu | Loại khỏi shortlist |
| Parallel Binary Search | Nhiều query cùng kiểu check đơn điệu theo mốc | Loại khỏi shortlist |
| DSU Jump Pointer | One-shot + thứ tự tuyến tính + không rollback | Loại khỏi shortlist |
| Topological Sort | Directed graph + lý do thứ tự phụ thuộc | Loại khỏi shortlist |
| Dijkstra | Trọng số không âm | Loại khỏi shortlist |
| Manacher | Bài lõi palindrome substring | Loại khỏi shortlist |
| DSU theo component | Quan hệ nối-vô-hướng hoặc connectivity offline phù hợp | Loại khỏi shortlist cho reachability đồ thị có hướng |
| Bridge / Articulation (Tarjan low-link cơ bản) | Đồ thị vô hướng | Loại khỏi shortlist cho đồ thị có hướng |

- Ghi chú quan trọng:
    - Ví dụ không phù hợp: dùng DSU để xử lý phụ thuộc reachability trong đồ thị có hướng.
    - Ví dụ không phù hợp: tìm cầu/khớp chuẩn vô hướng cho đồ thị có hướng.

### 2) Điểm tiềm năng mềm

Chấm mỗi thuật toán theo 4 tiêu chí:

- `Fit cấu trúc dữ liệu`: 0-3.
- `Fit loại thao tác (query/update/path/substring...)`: 0-3.
- `Fit độ phức tạp theo ràng buộc`: 0-2.
- `Mức tận dụng tính chất đặc biệt (monotonic/invariant/offline...)`: 0-2.

`Total = 0..10`.

- `High`: 8-10.
- `Medium`: 5-7.
- `< 5`: loại khỏi shortlist.

### Quy tắc thực chiến: thuật toán có keyword khớp mạnh nhưng sai độ phức tạp vẫn phải hạ xuống `Medium` hoặc loại khỏi shortlist.

---

## III. Nhánh quyết định: `exist` -> thử `count` trước

Khi đề bài hỏi **có tồn tại không** (`exist`), đừng mặc định phải dựng cấu hình ngay.
Nhiều bài giải nhanh hơn nếu đổi sang:
- Đếm số cấu hình hợp lệ `cnt`.
- Kết luận `exist` khi `cnt > 0`.

### 1) Khi nào nên nâng nhánh đếm lên `High`
- Không gian cấu hình có thể chuẩn hóa rõ ràng (theo block, tần suất, residue class, state DP).
- Có đối xứng/cấu trúc tổ hợp rõ (permutation, partition, matching, placement).
- Điều kiện hợp lệ mang tính ràng buộc toàn cục, khó check trực tiếp nhưng dễ gom trong công thức/DP.
- Có thể dùng invariant để lọc mạnh không gian trước khi đếm.

### 2) Pipeline chuẩn `exist -> count`
1. Chuẩn hóa tập ứng viên `Omega` (mỗi cấu hình có biểu diễn chuẩn, tránh đếm trùng).
2. Cắt `Omega` bằng invariant/ràng buộc cứng -> `Omega'`.
3. Chọn kỹ thuật đếm:
4. Đọc kết luận:
   - `cnt = 0` -> không tồn tại.
   - `cnt > 0` -> tồn tại ít nhất một cấu hình logic.
5. Nếu đề có thao tác biến đổi:
   - Kiểm tra thêm `reachable by operations`, không chỉ “logic feasible”.

### 3) Hard filter cho hướng đếm (sai là loại)
- Đếm trùng do đối xứng/đổi nhãn mà chưa canonicalize.
- Chỉ có `cnt mod p` rồi kết luận `cnt > 0` khi chưa có chặn phù hợp.
- Đếm trên tập “hợp lệ tĩnh” nhưng bỏ qua điều kiện reachability theo phép biến đổi.
- Complexity của bước đếm vượt constraint dù ý tưởng đúng.

---

## IV. Hệ từ khóa cấp 0 (phân loại gốc)

### 1) Number / Value / Single answer

| Tính chất | High | Medium |
|---|---|---|
| Chủ yếu là số học, modulo, gcd/lcm, prime | Number theory (`gcd/lcm`, mod, fast power, ext-euclid, sieve, SPF) | Binary search on answer (nếu có monotonic) |
| Hệ đồng dư / phương trình Diophantine | CRT, ext-euclid, modular inverse | Brute force kiểm chứng mẫu nhỏ |
| N nhỏ (`<= 20..22`), xét tập con | Bitmask, DP bitmask, backtracking | Meet-in-the-middle, branch and bound |
| N tầm `30..45`, tách đôi độc lập | Meet-in-the-middle | Backtracking có pruning mạnh |
| Truy hồi tuyến tính dài, bước rất lớn (`k-th step`, `linear recurrence`, `transition matrix`) | Matrix exponentiation | DP thường |
| Đếm/tổng trên đoạn số `[L, R]` với ràng buộc chữ số (`tight`, `started`, `state`) | Digit DP (`F(R)-F(L-1)`, `DP(pos, tight, started, state)`) | Binary Search + Digit DP (`k-th` theo prefix count) |
| Dạng divisor/multiple (`for (j=i; j<=n; j+=i)`), chuyển `i -> k*i` hoặc `i -> i/d` | Harmonic-number thinking + number theory/sieve | Brute force theo ước/bội (n nhỏ) |
| Đếm cấu hình có tách block độc lập | Combinatorics + multinomial + DP count | Backtracking (n nhỏ) |
| Tối đa số ước trong miền `<= N` (siêu hợp số / highly composite) | Backtracking đệ quy theo prime + số mũ không tăng, prune theo `N` | Sinh ứng viên bằng DFS + log bound |

### 2) Array / String / Sequence / Grid / Tree / Graph

- Chuyển sang cấp 1: `Linearizable` hoặc `Non-linear`.

---

## V. Cấp 1: Linearizable vs Non-linear

### A) Linearizable

Keyword mạnh:

- `subarray`, `substring`, `prefix`, `suffix`, `left-right`, `window`, `nearest`, `flatten tree`.
- `submatrix`, `fixed top/bottom`, `fixed left/right`, `compressed[]`, `linearizing 2D -> 1D`.

### B) Non-linear

Keyword mạnh:

- `graph`, `dependency`, `component`, `path`, `cycle`, `state (u, mask, k, parity...)`.

- Quy ước: bài có quan hệ đỉnh-cạnh thì gom về `graph` trước, rồi tách `undirected` / `directed`.

---

## VI. Cấp 2A: Linear Problem (bảng tiềm năng)

### 1) Subarray / Substring / Prefix-Suffix

| Tính chất | High | Medium |
|---|---|---|
| `sum/xor` trên đoạn tĩnh | Prefix sum/xor, prefix frequency, hashing | Sqrt decomposition |
| `max/min` trên cửa sổ | Monotonic deque/stack, sliding window | Segment tree, divide and conquer |
| Max subarray / best segment | Kadane, prefix-min trick | Segment tree cho nhiều truy vấn |
| `exactly/at most/at least k` với cửa sổ hợp lệ đơn điệu | Two pointers, sliding window, prefix + binary search | Mo (offline) |
| `next/previous/nearest` | Monotonic stack, neighbor-linked array/DSU next-pointer | Balanced BST / set |
| LIS/LNDS theo thứ tự tuyến tính | Patience sorting + binary search | Segment tree/BIT với nén tọa độ |

### 2) Range query/update trên mảng

| Tính chất | High | Medium |
|---|---|---|
| Static query nhiều lần | Prefix/suffix, sparse table | Sqrt decomposition |
| Point update + range query online (`sum/min/max/gcd/xor`) | Segment tree, Fenwick | Set/map tùy bài |
| Node custom / merge không giao hoán (vd `sum/pref/suff/best`) | Segment tree | Chia bài theo block hoặc custom DS khác |
| Range update tổng quát + range query | Lazy segment tree | Sqrt lazy |
| Range update one-shot/co dần | Segment tree không lazy + prune | Difference array (offline) |
| Tìm vị trí đầu/cuối hoặc 1 vị trí bất kỳ thỏa điều kiện trên đoạn (`first true/last true`, `leftmost/rightmost`, `k-th`, `find any`) | Segment tree (descent/walk theo node) | Fenwick + binary lifting/lower_bound (khi điều kiện phù hợp) |
| Offline query theo ngưỡng (`<= x`, `> x`) | Sort query + Fenwick offline | Parallel Binary Search |
| K-th/order statistics trên đoạn (nhiều query) | Persistent segment tree, wavelet tree | Merge-sort tree + BS |

### 3) Set interval (split-merge động)

| Tính chất | High | Medium |
|---|---|---|
| Trạng thái đồng nhất trên các đoạn liên tiếp, cần split/merge nhiều lần | Set interval (`std::set` lưu đoạn) | Lazy segment tree |
| Update/query interval động, thứ tự chỉ số ổn định | Set interval + lower_bound + merge lân cận | Segment tree + custom node |
| Chỉ xử lý one-shot, xóa 1 lần và không kích hoạt lại | DSU next pointer / Neighbor-linked array | Set interval |
| Không gom được thành đoạn, hoặc thứ tự không ổn định | Segment tree/Fenwick/graph DS phù hợp bài | Sqrt decomposition |

### 4) Frequency / Distinct / Offline queries

| Tính chất | High | Medium |
|---|---|---|
| Offline queries độc lập, add/remove O(1) | Mo / Hilbert order | Prefix offline trick, sqrt decomposition |
| Dynamic multiset (add/remove + count range + `k-th`) | Fenwick/Segment tree + nén tọa độ | Balanced BST / ordered set |
| Distinct in range (static) | Offline BIT theo last occurrence | Mo |
| Query theo thời gian mốc đầu tiên thỏa | Parallel Binary Search + DS check | Binary search từng query |
| K-th trong subarray (static nhiều query) | Persistent segment tree / wavelet tree | Mo + heuristic |

### 5) String processing

| Tính chất | High | Medium |
|---|---|---|
| Exact pattern matching 1 pattern | KMP, Z algorithm | Rolling hash (chấp nhận collision) |
| Nhiều pattern cùng lúc | Aho-Corasick | Trie + hash filter |
| So sánh nhiều substring | Rolling hash (2 mod), prefix hash | Suffix array + LCP |
| Palindrome substring | Manacher | Hash thuận-ngược + binary search |
| Prefix dictionary / autocomplete / XOR trie | Trie | Hash map prefix |
| Bài substring nâng cao (đếm distinct, lexicographic) | Suffix array/Suffix automaton | Rolling hash + binary search |

### 6) Keyword đặc thù khác trong nhánh tuyến tính

| Tính chất | High | Medium |
|---|---|---|
| Event theo trục thời gian/toạ độ | Sweep line + set/heap/segment tree (covered length/union area/max overlap) | Sorting + prefix |
| Chia bài thành 2 nửa độc lập | Divide and conquer / Meet-in-the-middle | Backtracking có pruning |
| Truy vết chu trình hàm lặp | Floyd cycle finding | Hash visited |
| Truy vấn median/percentile chạy động | Two-heaps + lazy delete | Multiset đôi |

### 7) Grid 2D nhưng linearizable về 1D

| Tính chất | High | Medium |
|---|---|---|
| Submatrix tối ưu/đếm, phép gộp theo lát cắt cộng dồn được | `linearizing 2D -> 1D`: cố định `top/bottom` hoặc `left/right`, cập nhật `compressed[]`, rồi chạy thuật toán 1D phù hợp | Prefix sum 2D + duyệt nhiều biên khi `n, m` nhỏ |
| Nhận diện độ phức tạp qua `K = min(n,m)`, `L = max(n,m)` | Mục tiêu `O(K^2 * F(L))`, bộ nhớ `O(L)` | `O(n^2 m^2)` brute force khi dữ liệu nhỏ |
| Maximum sum submatrix | Kadane 1D trên `compressed[]` (Kadane 2D) | Prefix sum 2D kiểm mọi hình chữ nhật |
| Đếm submatrix có tổng = `k` | Prefix sum 1D + hash map trên `compressed[]` cho mỗi cặp biên | Prefix sum 2D + đếm brute force |

---

## VII. Cấp 2B: Non-linear Problem (graph/tree/state)

### 1) Undirected graph

| Tính chất | High | Medium |
|---|---|---|
| connected/component | DFS/BFS, DSU | Dynamic connectivity offline (rollback) |
| bridge / articulation | Tarjan low-link | BET/BCT (nhiều query path) |
| Nhiều query path về cạnh/đỉnh critical (`critical edge/node`) | Bridge-Edge Tree / Block-Cut Tree + LCA/HLD | Bridge/AP + xử lý từng query |
| bipartite / odd cycle | BFS/DFS coloring, DSU bipartite | BFS theo lớp + parity state |
| chu trình ngắn nhất (unweighted) | BFS từ từng đỉnh (có prune theo `dist`) | DFS/back-edge heuristic (n nhỏ) |
| Ràng buộc quan hệ tương đối (`same/different`, parity, xor-distance), cần detect contradiction | DSU parity / weighted DSU | State graph + BFS/DFS theo parity |
| MST | Kruskal + DSU, Prim | Boruvka (nếu có) |
| Có nhiều `non-tree edge`, cần kiểm tra thay cạnh trên path (`max edge`, `second-best MST`) | Spanning tree + Binary lifting/Sparse DP trên path | Recompute cục bộ (n nhỏ) |
| Mỗi cạnh thuộc tối đa một chu trình (`cactus graph`) | DFS cactus decomposition / block tree | Bridge/BCC decomposition tổng quát |
| Nhiều query connectivity theo thời gian | DSU rollback + segment tree time | Rebuild theo block |

### 2) Directed graph

| Tính chất | High | Medium |
|---|---|---|
| dependency / prerequisite / ordering | Topological sort (Kahn/DFS) | SCC + condensation (nếu có cycle) |
| SCC / mutually reachable | Tarjan SCC / Kosaraju + condensation graph | DFS reachability trên DAG nén |
| cycle directed | DFS cycle detection, topo fail-check | SCC |
| DP trên phụ thuộc | Topo + DP DAG | Memo DFS |
| Mệnh đề logic dạng `a OR b` | 2-SAT (implication graph + SCC) | Backtracking với cắt tỉa nhỏ |

### 3) Path optimization

| Tính chất | High | Medium |
|---|---|---|
| Unweighted shortest path | BFS, multisource BFS, flood fill | Bidirectional BFS |
| Đồ thị ẩn, hỏi \"ít phép biến đổi/ít thao tác nhất\" | BFS trên implicit graph (sinh hàng xóm theo phép biến đổi) | Bidirectional BFS (khi source-target rõ) |
| Lan truyền theo lớp thời gian (`t = 0,1,2,...`) | Level BFS, multisource BFS | DFS + mô phỏng (n nhỏ) |
| Gần nhất tới tập đỉnh đặc biệt | Multisource BFS (đưa toàn bộ special vào queue từ đầu) | BFS lặp từ từng nguồn (n nhỏ) |
| Ràng buộc phụ theo ngữ cảnh (`chẵn/lẻ`, `mod`, `key/door`) | BFS trạng thái `(u, state)` | Dijkstra trạng thái (khi có trọng số) |
| Trọng số chỉ 0/1 | 0-1 BFS | Dijkstra |
| Non-negative weighted | Dijkstra | Dial (trọng số nhỏ), A* (heuristic tốt) |
| Có cạnh âm (không âm chu trình) | Bellman-Ford, Johnson (all-pairs) | SPFA (chỉ khi dữ liệu phù hợp) |
| K-best state / ràng buộc trạng thái | State-space search + Dijkstra/BFS + heap | DP trạng thái |

### 4) Tree problems

| Tính chất | High | Medium |
|---|---|---|
| subtree query/update | Euler flatten + BIT/Segment tree | DSU on tree (nếu có) |
| path query/update online | HLD + segment tree, LCA | Euler + segment trick |
| đường kính cây (unweighted) | 2 BFS (hoặc 2 DFS) | Tree DP O(`n^2`) khi n nhỏ |
| answer cho mọi root | DP rerooting | 2 DFS custom |
| ancestor/k-th ancestor/query nhị phân | Binary lifting | Euler tour + RMQ LCA |

---

## VIII. Greedy / DP / Search on Answer (xếp hạng tiềm năng)

### 1) Greedy + DS

| Tính chất | High | Medium |
|---|---|---|
| Chọn cục bộ + luôn đúng toàn cục | Dominant-choice greedy | DP để kiểm chứng |
| Có thể hối tiếc / thay cái tệ nhất | Greedy with rollback + priority queue/multiset | Set + local repair |
| Có cửa sổ đủ điều kiện theo thời gian | Greedy with eligibility window + heap | Sweep line + set |
| Ứng viên mới làm nhiều ứng viên cũ bị dominated | Greedy + monotonic stack/deque | Segment tree/BST |
| Cân bằng 2 nhóm động | Two-heap greedy (+ rollback/exchange) | Multiset 2 phía |
| Chọn theo trục sort đúng (`key ordering`) rồi mới tham lam | Sort + greedy + exchange/invariant proof | DP hoặc brute-force kiểm chứng |
| Chọn interval không giao nhau / deadline scheduling | Sort + greedy by endpoint/deadline + heap | DP interval |

### 2) Dynamic Programming

| Tính chất | High | Medium |
|---|---|---|
| Mỗi state có nhiều transition cạnh tranh | DP có lựa chọn (`min/max/sum/or`) | Greedy (nếu chứng minh collapse được) |
| State theo tập con nhỏ | DP bitmask | Backtracking + pruning |
| Bài trên số với ràng buộc chữ số (`[L, R]`, tổng chữ số, mod, pattern) | Digit DP (`pos, tight, started, state`) | Memo DFS theo tiền tố không đầy đủ |
| Truy hồi deterministic một hướng | Prefix/suffix recurrence, linear DP | Full DP state lớn |
| Trên cây / DAG | Tree DP, Topo + DP, rerooting | DFS memo |
| Transition tuyến tính theo slope/intercept | Convex Hull Trick / Li Chao Tree | Divide and conquer DP optimization |
| Quadrangle inequality / monotone opt | Knuth optimization, Divide & Conquer DP | O(n^2) DP baseline |

### 3) Search on Answer / Optimization

| Tính chất | High | Medium |
|---|---|---|
| Có `check(x)` đơn điệu (`first true/last true`) | Binary Search on Answer | Ternary (nếu gần unimodal) |
| Nhiều query cùng check theo mốc (`first true/last true` theo từng query) | Parallel Binary Search | BS từng query |
| Tìm `k-th element` trên miền giá trị lớn (không merge/sort full được) | Binary search trên value + counting `count(<= x)` | Heap merge / partial sort (k nhỏ) |
| Hàm unimodal (không phải predicate đơn điệu) | Ternary search on answer | BS theo đạo hàm rời rạc |
| Tradeoff block/impact | Sqrt decomposition, sqrt heavy-light by impact | Segment tree |

---

## IX. Chiến lược chuyển mức (nâng/giáng tiềm năng)

### Nâng từ Medium -> High khi có thêm bằng chứng

- Chứng minh được invariant/monotonic/exchange.
- Biến đổi thành đúng cấu trúc chuẩn (range, DAG, state graph, subtree segment).
- Complexity khớp chắc với `n, q`.

### Giáng từ High -> Medium hoặc loại khỏi shortlist khi có cảnh báo

- Vi phạm hard filter.
- Complexity không qua cận.
- Cần quá nhiều giả định không có trong đề.
- Thuật toán đúng mô hình nhưng overkill, khó implement đúng trong contest.

---

## X. Phân loại theo time constraint (lọc nhanh theo độ lớn dữ liệu)

| Quy mô dữ liệu điển hình | Mục tiêu độ phức tạp | Shortlist nhanh nên nghĩ trước |
|---|---|---|
| `n <= 20` | `O(2^n * n)` hoặc `O(n!)` có prune | Backtracking, DP bitmask, brute force thông minh |
| `20 < n <= 45` | `O(2^(n/2))` | Meet-in-the-middle, chia đôi tập |
| `n <= 200` | `O(n^3)` còn chấp nhận được | Floyd-Warshall, interval DP, cubic DP |
| `n <= 2000` | `O(n^2)` hoặc `O(n^2 log n)` | DP 2 chiều, graph dày vừa, prefix 2D |
| `n, m <= 2e5`, `q <= 2e5` | `O((n+q) log n)` hoặc tốt hơn | Segment tree, Fenwick, DSU, HLD, Dijkstra |
| `n ~ 1e6` (ít query, dữ liệu tĩnh) | `O(n)` hoặc `O(n log log n)` | Prefix/sieve/linear scan/two pointers |
| Nhiều query tĩnh (`q` rất lớn, update ít/không) | Tiền xử lý `O(n log n)` + query `O(1)`/`O(log n)` | Sparse table, prefix, binary lifting |
| Update + query cùng lớn | Mỗi thao tác `O(log n)` | Segment tree lazy, Fenwick, balanced BST |
| Đồ thị dày (`m ~ n^2`, `n` nhỏ-vừa) | `O(n^3)` có thể hợp lý | Floyd-Warshall, bitset optimization |

Quy tắc đọc nhanh:
- Nếu `T` test lớn, nhân complexity theo `T` trước khi chốt thuật toán.
- Với `n` cỡ `2e5`, mặc định ưu tiên `O(n log n)` trở xuống.
- Nếu thao tác online bắt buộc, ưu tiên DS online; nếu offline được, xét Mo/PBS/sort event để giảm chi phí.

---

## XI. Checklist thực chiến 30s

1. Sau biến đổi, bài toán là `number`, `linear`, hay `graph/state`?
2. Truy vấn là `single`, `many queries`, hay `dynamic updates`?
3. Có từ khóa cứng: `range query/update`, `leftmost/rightmost`, `k-th/find any`, `check(x)`, `subarray/path/component/ordering/palindrome`?
4. Có điều kiện đơn điệu, kết hợp, one-shot, hoặc offline độc lập không?
5. Theo `n, m, q`, complexity mục tiêu là gì và shortlist nào còn sống?
6. Với ràng buộc hiện tại, thuật toán nào đạt `High` theo điểm 10?

Nếu không trả lời được >= 4 câu thì quay lại bước biến đổi, chưa nên chốt thuật toán.

---

## XII. Liên kết trực tiếp theo nhóm note (đồng bộ full từ `Kiến thức đã học`)

- Algorithm core:
    [Backtracking](<Kiến thức đã học/Algorithm/Backtracking.md>), [Bit manipulation and bitmask](<Kiến thức đã học/Algorithm/Bit manipulation and bitmask.md>), [Divide and Conquer](<Kiến thức đã học/Algorithm/Divide and Conquer.md>), [Sweep line](<Kiến thức đã học/Algorithm/Sweep line.md>), [Two Pointers](<Kiến thức đã học/Algorithm/Two Pointers.md>), [String Processing](<Kiến thức đã học/Algorithm/String Processing.md>), [Kĩ thuật traceback](<Kiến thức đã học/Kĩ thuật traceback.md>)
- Searching:
    [Binary search](<Kiến thức đã học/Algorithm/Searching/Binary search.md>), [Binary search on answer](<Kiến thức đã học/Algorithm/Searching/Binary_search/Binary search on answer.md>), [Binary search on array or set](<Kiến thức đã học/Algorithm/Searching/Binary_search/Binary search on array or set.md>), [Parallel Binary Search](<Kiến thức đã học/Algorithm/Searching/Binary_search/Parallel Binary Search.md>), [Ternary search](<Kiến thức đã học/Algorithm/Searching/Ternary search.md>), [Ternary search on answer](<Kiến thức đã học/Algorithm/Searching/Ternary search/Ternary search on answer.md>)
- String processing:
    [KMP](<Kiến thức đã học/Algorithm/String processing/KMP.md>), [Manacher](<Kiến thức đã học/Algorithm/String processing/Manacher.md>), [rolling hash](<Kiến thức đã học/Algorithm/String processing/rolling hash.md>), [Trie](<Kiến thức đã học/Algorithm/String processing/Trie.md>), [Z algorithm](<Kiến thức đã học/Algorithm/String processing/Z algorithm.md>)
- STL structures:
    [Stack](<Kiến thức đã học/Data_structure/STL/Stack.md>), [Queue](<Kiến thức đã học/Data_structure/STL/Queue.md>), [Deque](<Kiến thức đã học/Data_structure/STL/Deque.md>), [Priority Queue](<Kiến thức đã học/Data_structure/STL/Priority Queue.md>), [Map cơ bản](<Kiến thức đã học/Data_structure/STL/Map/Map cơ bản.md>), [Set cơ bản](<Kiến thức đã học/Data_structure/STL/Set/Set cơ bản.md>), [Set interval nâng cao](<Kiến thức đã học/Data_structure/STL/Set/Set interval nâng cao.md>), [Neighbor-linked array ~ DSU](<Kiến thức đã học/Data_structure/STL/Neighbor-linked array ~ DSU.md>), [Prefix or suffix Arrays](<Kiến thức đã học/Data_structure/STL/Prefix or suffix Arrays.md>)
- Prefix / Difference:
    [Prefix sum 1D](<Kiến thức đã học/Data_structure/STL/Prefix structures and Difference Array/Prefix sum 1D.md>), [Prefix sum 2D](<Kiến thức đã học/Data_structure/STL/Prefix structures and Difference Array/Prefix sum 2D.md>), [Prefix min](<Kiến thức đã học/Data_structure/STL/Prefix structures and Difference Array/Prefix min.md>), [Prefix max](<Kiến thức đã học/Data_structure/STL/Prefix structures and Difference Array/Prefix max.md>), [Difference Array](<Kiến thức đã học/Data_structure/STL/Prefix structures and Difference Array/Difference Array.md>)
- Range / query DS:
    [Segment Tree](<Kiến thức đã học/Data_structure/Non-STL/Segment Tree.md>), [Lazy Segment Tree](<Kiến thức đã học/Data_structure/Non-STL/Lazy Segment Tree.md>), [Query Problem - Relative topics](<Kiến thức đã học/Query Problem/Relative topics.md>), [Mo](<Kiến thức đã học/Sqrt Decomposition/Mo.md>), [Range Query Sqrt decomposition](<Kiến thức đã học/Sqrt Decomposition/Range Query Sqrt decomposition.md>), [Sqrt chung](<Kiến thức đã học/Sqrt Decomposition/Sqrt chung.md>), [Sqrt chia case](<Kiến thức đã học/Sqrt Decomposition/Sqrt chia case.md>)
- DSU và ứng dụng:
    [DSU lý thuyết](<Kiến thức đã học/Data_structure/Non-STL/DSU và các ứng dụng/DSU lý thuyết.md>), [Giá trị đại diện cho tập hợp](<Kiến thức đã học/Data_structure/Non-STL/DSU và các ứng dụng/Giá trị đại diện cho tập hợp.md>), [DSU jump pointer](<Kiến thức đã học/Data_structure/Non-STL/DSU và các ứng dụng/DSU jump pointer.md>), [DSU bipartite](<Kiến thức đã học/Data_structure/Non-STL/DSU và các ứng dụng/DSU bipartite.md>), [Dynamic Connectivity](<Kiến thức đã học/Data_structure/Non-STL/DSU và các ứng dụng/Dynamic Connectivity.md>), [Connected Component Graph](<Kiến thức đã học/Data_structure/Non-STL/DSU và các ứng dụng/Connected Component Graph.md>), [MST Kruskal](<Kiến thức đã học/Data_structure/Non-STL/DSU và các ứng dụng/MST Kruskal.md>)
- Graph:
    [Mô hình hóa bài toán thành các dạng graph](<Kiến thức đã học/Data_structure/Non-STL/Graph/Mô hình hóa bài toán thành các dạng graph.md>), [BFS](<Kiến thức đã học/Data_structure/Non-STL/Graph/BFS.md>), [Topological sort](<Kiến thức đã học/Data_structure/Non-STL/Graph/Topological sort.md>), [bridge and ap](<Kiến thức đã học/Data_structure/Non-STL/Graph/bridge and ap.md>), [basic_spanning_tree_forest](<Kiến thức đã học/Data_structure/Non-STL/Graph/basic_spanning_tree_forest.md>), [Positive or Negative cycle](<Kiến thức đã học/Data_structure/Non-STL/Graph/Positive or Negative cycle.md>)
- Graph decomposition:
    [condensation graph](<Kiến thức đã học/Data_structure/Non-STL/Graph/Graph decomposition/condensation graph.md>), [bet_bct](<Kiến thức đã học/Data_structure/Non-STL/Graph/Graph decomposition/bet_bct.md>), [advance_span_tree_forest](<Kiến thức đã học/Data_structure/Non-STL/Graph/Graph decomposition/advance_span_tree_forest.md>), [dfs_cactus](<Kiến thức đã học/Data_structure/Non-STL/Graph/Graph decomposition/dfs_cactus.md>)
- Graph state-space / DP on graph:
    [State space search - Khái niệm](<Kiến thức đã học/Data_structure/Non-STL/Graph/State space search/Khái niệm.md>), [Single source one best state](<Kiến thức đã học/Data_structure/Non-STL/Graph/State space search/Single source one best state.md>), [Single source k best state](<Kiến thức đã học/Data_structure/Non-STL/Graph/State space search/Single source k best state.md>), [Multisource](<Kiến thức đã học/Data_structure/Non-STL/Graph/State space search/Multisource.md>), [All pair search](<Kiến thức đã học/Data_structure/Non-STL/Graph/State space search/All pair search.md>), [Topo + DP](<Kiến thức đã học/Data_structure/Non-STL/Graph/DP Graph/Topo + DP.md>)
- Tree:
    [1 số mảng thường có trong các bài tree](<Kiến thức đã học/Data_structure/Non-STL/Tree/1 số mảng thường có trong các bài tree.md>), [Euler tour flatten](<Kiến thức đã học/Data_structure/Non-STL/Tree/Euler tour flatten.md>), [Binary lifting và DP](<Kiến thức đã học/Data_structure/Non-STL/Tree/Binary lifting và DP.md>), [Dynamic programming on tree](<Kiến thức đã học/Data_structure/Non-STL/Tree/Dynamic programming on tree.md>), [DP rerooting](<Kiến thức đã học/Data_structure/Non-STL/Tree/DP rerooting.md>)
- Dynamic Programming:
    [Các dạng DP chính](<Kiến thức đã học/Dynamic Programming/Các dạng DP chính.md>), [DP how to solve it G.Polya](<Kiến thức đã học/Dynamic Programming/DP how to solve it G.Polya.md>), [dp_bitmask](<Kiến thức đã học/Dynamic Programming/dp_bitmask.md>), [dp_digit](<Kiến thức đã học/Dynamic Programming/dp_digit.md>), [DP_optimization](<Kiến thức đã học/Dynamic Programming/DP_optimization.md>), [Slope trick](<Kiến thức đã học/Dynamic Programming/Slope trick.md>)
- Greedy:
    [Greedy + Priority Queue](<Kiến thức đã học/Greedy Technique/Greedy + Priority Queue.md>), [Greedy - Relative Topics](<Kiến thức đã học/Greedy Technique/Relative Topics.md>)
- Math:
    [Basic Number Theory](<Kiến thức đã học/Math/Basic Number Theory.md>), [Combinatorics and Probability](<Kiến thức đã học/Math/Combinatorics and Probability.md>), [Harmonic Number](<Kiến thức đã học/Math/Harmonic Number.md>), [Matrix multiplication](<Kiến thức đã học/Math/Matrix multiplication.md>)
