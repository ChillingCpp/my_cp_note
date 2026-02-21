# Pattern Recognize + Potential Ranking

## Yêu cầu về file chọn thuật toán tối nhnah :
- Cách giải 1 bài toán dựa vào [[how_to_solve_it]]
- chọn thuật toán là 1 bước trong file đó, đọc file đó và sau đó đọc file này

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

## 0) Flow mapping nhanh 30s (dùng trước mọi thứ)

1. Chuẩn hóa đề trong 1 câu: `object + thao tác + mục tiêu`...
2. Xác định lớp bài: `number` hoặc `linear` hoặc `graph/tree/state`...
3. Xác định kiểu thao tác: `single` / `many queries` / `dynamic updates`...
4. Xác định kiểu mục tiêu: `optimize` / `count` / `exist` / `k-th`...
5. Gắn keyword cứng: `subarray`, `nearest`, `component`, `dependency`, `cycle`, `palindrome`, `check(x)`, `one-shot`...
6. Chạy hard filter 
7. Chấm điểm tiềm năng (0-10): `fit cấu trúc` + `fit thao tác` + `fit complexity` + `fit tính chất đặc biệt`...
8. Xếp hạng:
    - `High`: 8-10
    - `Medium`: 5-7
    - `Low`: 0-4
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
- `Low`:

### Mục tiêu: **không đoán thuật toán trực tiếp từ đề**, mà **biến đổi bài toán -> trích xuất từ khóa -> xếp hạng tiềm năng thuật toán (Thấp/Trung bình/Cao)**.
### Đầu ra cuối cùng phải là **một shortlist có thứ tự ưu tiên**, không phải một thuật toán duy nhất.

---

## I. Đầu ra chuẩn của framework

Sau khi nhận diện, luôn xuất theo mẫu:

- `High`: 1-3 hướng mạnh nhất, đáng thử trước.
- `Medium`: 2-4 hướng dự phòng, có thể đúng nếu biến đổi thêm.
- `Low`: các hướng ít tiềm năng hoặc mâu thuẫn với tính chất bài.
- `Lý do`: nêu ngắn gọn vì sao một hướng bị đẩy xuống `Medium/Low`.

---

## II. Quy tắc bắt buộc trước khi tra từ khóa

### 1) Chuẩn hóa đối tượng

- Tree -> Euler tour/flatten -> array/range.
- Subtree -> đoạn `[tin, tout]`.
- Path query on tree -> LCA + tách đoạn.
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

- `n, q` cỡ nào (`1e5`, `2e5`, `1e6`...).
- Cần `O(n)`, `O(n log n)`, hay chấp nhận `O(n sqrt n)`.
- Giá trị có âm/không âm, có thể có cycle âm không.

### 5) Nếu chưa chuẩn hóa xong 4 bước này thì chưa xếp hạng tiềm năng.

---

## III. Cơ chế chấm tiềm năng (Low / Medium / High)

### 1) Hard filter (lọc cứng)

Nếu vi phạm điều kiện cứng thì thuật toán đó mặc định `Low`:

| Thuật toán | Điều kiện cứng | Nếu thiếu điều kiện |
|---|---|---|
| Prefix sum / Prefix min-max | Dữ liệu tĩnh hoặc truy vấn không update phá prefix | `Low` |
| Difference Array | Nhiều range update + tổng hợp cuối/offline | `Low` |
| Segment Tree | Phép gộp có tính kết hợp, cần query/update online | `Low` |
| Lazy Segment Tree | Range update tổng quát, không prune one-shot | `Low` |
| Mo | Offline query + add/remove cục bộ hiệu quả | `Low` |
| Binary Search on Answer | Có `check(x)` đơn điệu | `Low` |
| Parallel Binary Search | Nhiều query cùng kiểu check đơn điệu theo mốc | `Low` |
| DSU Jump Pointer | One-shot + thứ tự tuyến tính + không rollback | `Low` |
| Topological Sort | Directed graph + lý do thứ tự phụ thuộc | `Low` |
| Dijkstra | Trọng số không âm | `Low` |
| Manacher | Bài lõi palindrome substring | `Low` |

### 2) Điểm tiềm năng mềm

Chấm mỗi thuật toán theo 4 tiêu chí:

- `Fit cấu trúc dữ liệu`: 0-3.
- `Fit loại thao tác (query/update/path/substring...)`: 0-3.
- `Fit độ phức tạp theo ràng buộc`: 0-2.
- `Mức tận dụng tính chất đặc biệt (monotonic/invariant/offline...)`: 0-2.

`Total = 0..10`.

- `High`: 8-10.
- `Medium`: 5-7.
- `Low`: 0-4.

### Quy tắc thực chiến: thuật toán có keyword khớp mạnh nhưng sai độ phức tạp vẫn phải hạ xuống `Medium/Low`.

---

## IV. Hệ từ khóa cấp 0 (phân loại gốc)

### 1) Number / Value / Single answer

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Chủ yếu là số học, modulo, gcd/lcm, prime | Number theory (`gcd/lcm`, mod, fast power, ext-euclid, sieve) | Binary search on answer (nếu có monotonic) | Segment tree, Mo, graph/tree nặng |
| N nhỏ (`<= 20..22`), xét tập con | Bitmask, DP bitmask, backtracking | Meet-in-the-middle, branch and bound | Cấu trúc query nặng |
| Truy hồi tuyến tính dài, bước rất lớn | Matrix exponentiation | DP thường | Brute force |
| Đếm cấu hình có tách block độc lập | Combinatorics + multinomial + DP count | Backtracking (n nhỏ) | Dijkstra/DSU |
| Tối đa số ước trong miền `<= N` (siêu hợp số / highly composite) | Backtracking đệ quy theo prime + số mũ không tăng, kèm prune theo giới hạn `N` | Sinh ứng viên bằng DFS + log bound | Segment tree, graph, Mo |

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

| Tính chất | High | Medium | Low |
|---|---|---|---|
| `sum/xor` trên đoạn tĩnh | Prefix sum/xor, prefix frequency, hashing | Sqrt decomposition | Segment tree lazy, graph |
| `max/min` trên cửa sổ | Monotonic deque/stack, sliding window | Segment tree, divide and conquer | DSU |
| `exactly/at most/at least k` với cửa sổ hợp lệ đơn điệu | Two pointers, sliding window, prefix + binary search | Mo (offline) | Floyd/graph decomposition |
| `next/previous/nearest` | Monotonic stack, neighbor-linked array/DSU next-pointer | Balanced BST / set | Prefix thuần |

### 2) Range query/update trên mảng

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Static query nhiều lần | Prefix/suffix, sparse table | Sqrt decomposition | Lazy segment tree |
| Point update + range query online | Segment tree, Fenwick/sqrt block | Set/map tùy bài | Prefix thuần |
| Range update tổng quát + range query | Lazy segment tree | Sqrt lazy | Prefix thuần |
| Range update one-shot/co dần | Segment tree không lazy + prune | Difference array (offline) | Mo thuần |

### 3) Set interval (split-merge động)

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Trạng thái đồng nhất trên các đoạn liên tiếp, cần split/merge nhiều lần | Set interval (`std::set` lưu đoạn) | Lazy segment tree | Prefix thuần |
| Update/query interval động, thứ tự chỉ số ổn định | Set interval + lower_bound + merge lân cận | Segment tree + custom node | DSU thường |
| Chỉ xử lý one-shot, xóa 1 lần và không kích hoạt lại | DSU next pointer / Neighbor-linked array | Set interval | Cấu trúc nặng không cần thiết |
| Không gom được thành đoạn, hoặc thứ tự không ổn định | Segment tree/Fenwick/graph DS phù hợp bài | Sqrt decomposition | Set interval |

### 4) Frequency / Distinct / Offline queries

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Offline queries độc lập, add/remove O(1) | Mo / Hilbert order | Prefix offline trick, sqrt decomposition | Segment tree online nặng |
| Query theo thời gian mốc đầu tiên thỏa | Parallel Binary Search + DS check | Binary search từng query | Online brute force |

### 5) String processing

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Exact pattern matching 1 pattern | KMP, Z algorithm | Rolling hash (chấp nhận collision) | Trie |
| So sánh nhiều substring | Rolling hash (2 mod), prefix hash | Suffix structures (nếu có) | KMP thuần |
| Palindrome substring | Manacher | Hash thuận-ngược + binary search | KMP/Z |
| Prefix dictionary / autocomplete / XOR trie | Trie | Hash map prefix | Manacher |

### 6) Keyword đặc thù khác trong nhánh tuyến tính

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Event theo trục thời gian/toạ độ | Sweep line + set/heap/segment tree | Sorting + prefix | DFS/DSU thuần |
| Chia bài thành 2 nửa độc lập | Divide and Conquer / Meet-in-the-middle | Backtracking có pruning | Segment tree |
| Truy vết chu trình hàm lặp | Floyd cycle finding | Hash visited | Dijkstra |

---

## VII. Cấp 2B: Non-linear Problem (graph/tree/state)

### 1) Undirected graph

| Tính chất | High | Medium | Low |
|---|---|---|---|
| connected/component | DFS/BFS, DSU | Dynamic connectivity offline (rollback) | Topo sort |
| bridge / articulation | Tarjan low-link | BET/BCT (nhiều query path) | Dijkstra |
| bipartite / odd cycle | BFS/DFS coloring, DSU bipartite | SCC | Prefix sum |
| MST | Kruskal + DSU, Prim | Boruvka (nếu có) | Mo |

### 2) Directed graph

| Tính chất | High | Medium | Low |
|---|---|---|---|
| dependency / prerequisite / ordering | Topological sort (Kahn/DFS) | SCC + condensation (nếu có cycle) | DSU thuần |
| SCC / mutually reachable | Tarjan SCC / Kosaraju + condensation graph | DFS reachability | Dijkstra |
| cycle directed | DFS cycle detection, topo fail-check | SCC | Prefix |
| DP trên phụ thuộc | Topo + DP DAG | Memo DFS | DSU |

### 3) Path optimization

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Unweighted shortest path | BFS, multisource BFS, flood fill | 0-1 BFS (nếu 0/1) | Dijkstra nặng |
| Non-negative weighted | Dijkstra | A* (nếu heuristic tốt) | SPFA cho mọi bài |
| Có cạnh âm | Bellman-Ford / SPFA, Floyd (all-pairs nhỏ) | Johnson (all-pairs lớn) | Dijkstra thuần |
| K-best state / ràng buộc trạng thái | State-space search + Dijkstra/BFS + heap | DP trạng thái | DFS thường |

### 4) Tree problems

| Tính chất | High | Medium | Low |
|---|---|---|---|
| subtree query/update | Euler flatten + BIT/Segment tree | DSU on tree (nếu có) | DSU thuần |
| path query | LCA, Binary lifting, tree DP | Euler + segment trick | Prefix thuần |
| answer cho mọi root | DP rerooting | 2 DFS custom | Brute force root |

---

## VIII. Greedy / DP / Search on Answer (xếp hạng tiềm năng)

### 1) Greedy + DS

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Chọn cục bộ + luôn đúng toàn cục | Dominant-choice greedy | DP để kiểm chứng | Backtracking |
| Có thể hối tiếc / thay cái tệ nhất | Greedy with rollback + priority queue/multiset | Set + local repair | Prefix |
| Có cửa sổ đủ điều kiện theo thời gian | Greedy with eligibility window + heap | Sweep line + set | DSU |
| Cân bằng 2 nhóm động | Two-heap greedy (+ rollback/exchange) | Multiset 2 phía | Stack |

### 2) Dynamic Programming

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Mỗi state có nhiều transition cạnh tranh | DP có lựa chọn (`min/max/sum/or`) | Greedy (nếu chứng minh collapse được) | Prefix |
| State theo tập con nhỏ | DP bitmask | Backtracking + pruning | Segment tree |
| Truy hồi deterministic một hướng | Prefix/suffix recurrence, linear DP | Full DP state lớn | Graph decomposition |
| Trên cây / DAG | Tree DP, Topo + DP, rerooting | DFS memo | DSU thuần |

### 3) Search on Answer / Optimization

| Tính chất | High | Medium | Low |
|---|---|---|---|
| Có `check(x)` đơn điệu | Binary Search on Answer | Ternary (nếu gần unimodal) | Random search |
| Nhiều query cùng check theo mốc | Parallel Binary Search | BS từng query | Mo |
| Hàm unimodal | Ternary search on answer | BS theo đạo hàm rời rạc | Dijkstra |
| Tradeoff block/impact | Sqrt decomposition, sqrt heavy-light by impact | Segment tree | Prefix |

---

## IX. Chiến lược chuyển mức (nâng/giáng tiềm năng)

### Nâng từ Medium -> High khi có thêm bằng chứng

- Chứng minh được invariant/monotonic/exchange.
- Biến đổi thành đúng cấu trúc chuẩn (range, DAG, state graph, subtree segment).
- Complexity khớp chắc với `n, q`.

### Giáng từ High -> Medium/Low khi có cảnh báo

- Vi phạm hard filter.
- Complexity không qua cận.
- Cần quá nhiều giả định không có trong đề.
- Thuật toán đúng mô hình nhưng overkill, khó implement đúng trong contest.

---

## X. Checklist thực chiến 30s

1. Sau biến đổi, bài toán là `number`, `linear`, hay `graph/state`?
2. Truy vấn là `single`, `many queries`, hay `dynamic updates`?
3. Có từ khóa cứng: `subarray/path/component/ordering/palindrome/k-th/check(x)`?
4. Có điều kiện đơn điệu, kết hợp, one-shot, hoặc offline độc lập không?
5. Với ràng buộc hiện tại, thuật toán nào đạt `High` theo điểm 10?

Nếu không trả lời được >= 3 câu thì quay lại bước biến đổi, chưa nên chốt thuật toán.

---

## XI. Liên kết trực tiếp theo nhóm note

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
