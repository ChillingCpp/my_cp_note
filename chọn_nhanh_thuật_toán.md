# Pattern Recognize + Potential Ranking

## Yêu cầu về file chọn thuật toán tối nhanh
- Cách giải 1 bài toán dựa vào [[how_to_solve_it]]
- Chọn thuật toán là 1 bước trong file đó, đọc file đó và sau đó đọc file này

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

## 0) Flow mapping nhanh 30s (dùng trước mọi thứ)

1. Chuẩn hóa đề trong 1 câu: `object + thao tác + mục tiêu`.
2. Xác định lớp bài: `number` hoặc `linear` hoặc `graph/tree/state`.
3. Xác định kiểu thao tác: `single` / `many queries` / `dynamic updates`.
4. Xác định kiểu mục tiêu: `optimize` / `count` / `exist` / `k-th`.
5. Gắn keyword cứng: `subarray`, `nearest`, `component`, `dependency`, `cycle`, `palindrome`, `check(x)`, `one-shot`.
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

---

## I. Đầu ra chuẩn của framework

Sau khi nhận diện, luôn xuất theo mẫu:

- `High`: 1-3 hướng mạnh nhất, đáng thử trước.
- `Medium`: 2-4 hướng dự phòng, có thể đúng nếu biến đổi thêm.
- `Rejected`: hướng không phù hợp bản chất bài hoặc fail hard filter (không coi là một mức xếp hạng).
- `Lý do`: nêu ngắn gọn vì sao bị giữ ở `Medium` hoặc bị loại.

---

## II. Quy tắc bắt buộc trước khi tra từ khóa

### 1) Chuẩn hóa đối tượng

- Tree -> Euler tour/flatten -> array/range.
- Subtree -> đoạn `[tin, tout]`.
- Path query on tree -> LCA + tách đoạn hoặc HLD.
- Grid 2D -> graph/component hoặc prefix 2D.
- Quan hệ phụ thuộc/trạng thái -> directed graph hoặc state-space graph.

### 2) Chuẩn hóa yêu cầu

- Tối ưu -> `min/max` hoặc chuyển sang feasibility.
- Đếm -> frequency/prefix/combinatorics/DP count.
- Tồn tại -> boolean check.
- `k-th` -> order statistic hoặc binary search on answer + counting.

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

## III. Cơ chế chấm tiềm năng (High / Medium + loại bỏ)

### 1) Hard filter (lọc cứng)

Nếu vi phạm điều kiện cứng thì thuật toán đó bị **loại khỏi shortlist**:

| Thuật toán | Điều kiện cứng | Nếu thiếu điều kiện |
|---|---|---|
| Prefix sum / Prefix min-max | Dữ liệu tĩnh hoặc truy vấn không update phá prefix | Loại khỏi shortlist |
| Difference Array | Nhiều range update + tổng hợp cuối/offline | Loại khỏi shortlist |
| Segment Tree | Phép gộp có tính kết hợp, cần query/update online | Loại khỏi shortlist |
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

## IV. Hệ từ khóa cấp 0 (phân loại gốc)

### 1) Number / Value / Single answer

| Tính chất | High | Medium |
|---|---|---|
| Chủ yếu là số học, modulo, gcd/lcm, prime | Number theory (`gcd/lcm`, mod, fast power, ext-euclid, sieve, SPF) | Binary search on answer (nếu có monotonic) |
| Hệ đồng dư / phương trình Diophantine | CRT, ext-euclid, modular inverse | Brute force kiểm chứng mẫu nhỏ |
| N nhỏ (`<= 20..22`), xét tập con | Bitmask, DP bitmask, backtracking | Meet-in-the-middle, branch and bound |
| N tầm `30..45`, tách đôi độc lập | Meet-in-the-middle | Backtracking có pruning mạnh |
| Truy hồi tuyến tính dài, bước rất lớn | Matrix exponentiation | DP thường |
| Đếm cấu hình có tách block độc lập | Combinatorics + multinomial + DP count | Backtracking (n nhỏ) |
| Tối đa số ước trong miền `<= N` (siêu hợp số / highly composite) | Backtracking đệ quy theo prime + số mũ không tăng, prune theo `N` | Sinh ứng viên bằng DFS + log bound |

### 2) Array / String / Sequence / Grid / Tree / Graph

- Chuyển sang cấp 1: `Linearizable` hoặc `Non-linear`.

---

## V. Cấp 1: Linearizable vs Non-linear

### A) Linearizable

Keyword mạnh:

- `subarray`, `substring`, `prefix`, `suffix`, `left-right`, `window`, `nearest`, `flatten tree`.

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
| Point update + range query online | Segment tree, Fenwick | Set/map tùy bài |
| Range update tổng quát + range query | Lazy segment tree | Sqrt lazy |
| Range update one-shot/co dần | Segment tree không lazy + prune | Difference array (offline) |
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
| Event theo trục thời gian/toạ độ | Sweep line + set/heap/segment tree | Sorting + prefix |
| Chia bài thành 2 nửa độc lập | Divide and conquer / Meet-in-the-middle | Backtracking có pruning |
| Truy vết chu trình hàm lặp | Floyd cycle finding | Hash visited |
| Truy vấn median/percentile chạy động | Two-heaps + lazy delete | Multiset đôi |

---

## VII. Cấp 2B: Non-linear Problem (graph/tree/state)

### 1) Undirected graph

| Tính chất | High | Medium |
|---|---|---|
| connected/component | DFS/BFS, DSU | Dynamic connectivity offline (rollback) |
| bridge / articulation | Tarjan low-link | BET/BCT (nhiều query path) |
| bipartite / odd cycle | BFS/DFS coloring, DSU bipartite | BFS theo lớp + parity state |
| MST | Kruskal + DSU, Prim | Boruvka (nếu có) |
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
| Trọng số chỉ 0/1 | 0-1 BFS | Dijkstra |
| Non-negative weighted | Dijkstra | Dial (trọng số nhỏ), A* (heuristic tốt) |
| Có cạnh âm (không âm chu trình) | Bellman-Ford, Johnson (all-pairs) | SPFA (chỉ khi dữ liệu phù hợp) |
| K-best state / ràng buộc trạng thái | State-space search + Dijkstra/BFS + heap | DP trạng thái |

### 4) Tree problems

| Tính chất | High | Medium |
|---|---|---|
| subtree query/update | Euler flatten + BIT/Segment tree | DSU on tree (nếu có) |
| path query/update online | HLD + segment tree, LCA | Euler + segment trick |
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
| Cân bằng 2 nhóm động | Two-heap greedy (+ rollback/exchange) | Multiset 2 phía |
| Chọn interval không giao nhau / deadline scheduling | Sort + greedy by endpoint/deadline + heap | DP interval |

### 2) Dynamic Programming

| Tính chất | High | Medium |
|---|---|---|
| Mỗi state có nhiều transition cạnh tranh | DP có lựa chọn (`min/max/sum/or`) | Greedy (nếu chứng minh collapse được) |
| State theo tập con nhỏ | DP bitmask | Backtracking + pruning |
| Truy hồi deterministic một hướng | Prefix/suffix recurrence, linear DP | Full DP state lớn |
| Trên cây / DAG | Tree DP, Topo + DP, rerooting | DFS memo |
| Transition tuyến tính theo slope/intercept | Convex Hull Trick / Li Chao Tree | Divide and conquer DP optimization |
| Quadrangle inequality / monotone opt | Knuth optimization, Divide & Conquer DP | O(n^2) DP baseline |

### 3) Search on Answer / Optimization

| Tính chất | High | Medium |
|---|---|---|
| Có `check(x)` đơn điệu | Binary Search on Answer | Ternary (nếu gần unimodal) |
| Nhiều query cùng check theo mốc | Parallel Binary Search | BS từng query |
| Hàm unimodal | Ternary search on answer | BS theo đạo hàm rời rạc |
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
3. Có từ khóa cứng: `subarray/path/component/ordering/palindrome/k-th/check(x)`?
4. Có điều kiện đơn điệu, kết hợp, one-shot, hoặc offline độc lập không?
5. Theo `n, m, q`, complexity mục tiêu là gì và shortlist nào còn sống?
6. Với ràng buộc hiện tại, thuật toán nào đạt `High` theo điểm 10?

Nếu không trả lời được >= 4 câu thì quay lại bước biến đổi, chưa nên chốt thuật toán.

---

## XII. Liên kết trực tiếp theo nhóm note

- Query/Range:
    [[Segment Tree]], [[Lazy Segment Tree]], [[Mo]], [[Range Query Sqrt decomposition]],
    [[Prefix sum 1D]], [[Prefix sum 2D]], [[Difference Array]], [[Prefix or suffix Arrays]]
- STL DS:
    [[Stack]], [[Queue]], [[Deque]], [[Priority Queue]], [[Set cơ bản]],
    [[Set interval nâng cao]], [[Map cơ bản]], [[Neighbor-linked array ~ DSU]]
- Graph/Tree:
    [[Topological sort]], [[bridge and ap]], [[condensation graph]], [[Euler tour flatten]],
    [[Binary lifting và DP]], [[Dynamic programming on tree]], [[DP rerooting]]
- Searching:
    [[Binary search on answer]], [[Parallel Binary Search]], [[Ternary search on answer]],
    [[Binary search on array or set]]
- String:
    [[KMP]], [[Z algorithm]], [[rolling hash]], [[Manacher]], [[Trie]]
- Math/Bit/DP/Greedy:
    [[Basic Number Theory]], [[Combinatorics and Probability]], [[Bit manipulation and bitmask]],
    [[Các dạng DP chính]], [[Greedy + Priority Queue]], [[Sqrt chung]], [[Sqrt chia case]]
