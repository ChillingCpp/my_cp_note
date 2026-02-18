# Pattern Recognize (Keyword‑driven, sau khi biến đổi bài toán)

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

> Mục tiêu: **không đoán thuật toán trực tiếp từ đề**, mà **biến đổi bài toán → trích xuất từ khóa đặc biệt → suy ra tập thuật toán khả thi**.
> Không loại bỏ bất kỳ thuật toán nào bạn đã liệt kê; chỉ **tổ chức lại theo hệ từ khóa phân cấp**.

---

## I. Quy tắc tổng quát (bắt buộc trước khi đọc từ khóa)

Trước khi tra từ khóa, **bắt buộc thực hiện biến đổi**:

1. **Chuẩn hóa đối tượng**

   * Tree → Euler tour → array
   * Subtree → segment [tin, tout]
   * Path query → LCA + 2–3 segment
   * 2D grid → graph / component / prefix 2D

2. **Chuẩn hóa yêu cầu**

   * "tối ưu / cực trị" → min / max / earliest / latest
   * "đếm" → frequency / prefix / invariant
   * "tồn tại" → boolean / feasibility / matching

3. **Chuẩn hóa thời gian**

   * 1 lần → Normal
   * Nhiều query → Query
   * Có update? → Dynamic

Chỉ sau bước này mới dùng bảng từ khóa bên dưới.

---

## II. Hệ từ khóa cấp 0 – Phân loại gốc

### 1. Từ khóa: **number / value / single answer**

→ Nhánh **Number Problem**

**Gợi ý thuật toán**:

* Bit manipulation, bitmask
* GCD / LCM / modulo / fast power
* Combinatorics nhỏ, invariant, symmetry

**Loại bỏ ngay**:

* Segment tree, Mo
* DP mảng lớn
* Graph / Tree

---

### 2. Từ khóa: **array / string / sequence / grid / tree / graph**

→ Nhánh **Normal / Query** (chưa quyết định)

Chuyển sang cấp 1.

---

## III. Hệ từ khóa cấp 1 – Tuyến tính vs Phi tuyến

### A. Nhóm từ khóa **Linearizable**

> Điều kiện: sau biến đổi, **duyệt được theo một trục cố định**.

**Từ khóa chính**:

* array, string, sequence
* subarray, substring
* prefix, suffix
* two ends, left–right
* monotonic
* frequency, count
* flatten tree (Euler tour)

→ **Linear Problem**

Chuyển sang cấp 2A.

---

### B. Nhóm từ khóa **Non‑linear**

**Từ khóa gốc (bắt buộc gom):**

* **graph**
* tree (chưa flatten)
* state (u, v), mask, multiple parameters
* dependency nhiều chiều
* 2D interaction (không tách hàng/cột)

> Quy ước: **mọi bài có tính chất đồ thị đều quy về từ khóa `graph`**.
> Sau đó **chỉ phân nhánh theo hướng cạnh**.

#### graph → **undirected / directed**

* **Undirected graph** (không hướng)

  * connected / component
  * bridge / articulation
  * tree (special case của undirected graph)
  * bipartite

* **Directed graph** (có hướng)

  * cycle / dependency
  * ordering
  * reachability
  * SCC / condensation

→ **Non‑linear Problem**

Chuyển sang cấp 2B.

---

## IV. Hệ từ khóa cấp 2A – Linear Problem (chi tiết)

### 1. Từ khóa: **subarray / substring**

#### 1.1 + **sum / xor / modulo**

* Prefix sum / prefix xor
* Hashing
* Frequency map

#### 1.2 + **max / min**

* Monotonic stack / deque
* Sliding window (nếu window co giãn)
* Divide & conquer (ít gặp, nhưng hợp lệ)

#### 1.3 + **exactly / at most / at least k**

* Two pointers
* Sliding window
* Prefix + binary search

---

### 2. Từ khóa: **palindrome / symmetry**

* Two pointers
* Manacher
* DP 1D/2D nhỏ

---

### 3. Từ khóa: **frequency / count distinct**

#### 3.1 Single pass

* Prefix frequency
* Sliding window

#### 3.2 Nhiều query (sau biến đổi)

* Mo algorithm
* Offline prefix trick

---

### 4. Từ khóa: **range [l, r] (sau flatten)**

#### 4.1 Static (không update)

* Prefix / suffix
* Sparse table

#### 4.2 Dynamic (có update)

* Segment tree
* Fenwick tree

---

### 5. Từ khóa: **next / previous / nearest**

* Monotonic stack
* DSU next‑pointer (neighbor‑linked array)

---
## IV-bis. Hệ từ khóa riêng – **Greedy + Priority Queue**

> Greedy + Heap **không phải Linear thuần**, cũng **không phải DP**.
> Đây là nhóm bài có **quyết định cục bộ + cấu trúc dữ liệu duy trì lựa chọn tốt nhất**.

### Nhóm keyword nhận diện chung

* "chọn dần"
* "tối ưu tức thời"
* "giữ tập tốt nhất hiện tại"
* "có thể loại bỏ / thay thế lựa chọn cũ"
* "mỗi bước chọn 1 phần tử"

---

### 1. **Greedy with Rollback**

**Keyword đặc trưng**:

* "loại bỏ hoàn toàn quyết định cũ"
* "hối tiếc / thay thế"
* "vi phạm ràng buộc thì sửa"
* Quyết định hiện tại phụ thuộc vào tương lai
* Không thể nhìn trước “đỉnh” / “max”
* Tài nguyên khan hiếm nhưng chưa rõ nên dùng vào đâu

---

### 2. **Greedy with Eligibility Window**

**Keyword đặc trưng**:

* "chỉ chọn khi đủ điều kiện"
* "theo thời gian / deadline"
* "chưa đến lượt thì chưa xét"

---

### 3. **Lazy Greedy (Deferred Decision)**

**Keyword đặc trưng**:

* "chưa cần quyết định ngay"
* "chỉ xử lý khi bắt buộc"
* "để đó nếu chưa vi phạm"

---

### 4. **Dominant-choice / Irrevocable Greedy**

**Keyword đặc trưng**:

* "lựa chọn tốt nhất chắc chắn"
* "không bao giờ hối tiếc"
* "quyết định không đảo ngược"

- **Two-Heap Greedy with rollback = exchange**

- median / split
- balance / balanced
- two groups / split into two sets
- boundary / threshold
- exchange / swap = rollback
- rebalance
- lower half / upper half
- compare extremes
   - So sánh kiểu:
      -worst(include) vs best(exclude)
- maintain invariant across two sets

### Chiến lược tư duy
- Greedy Dominant-choice -> greedy with rollback -> Dynamic Programming

## V. Hệ từ khóa cấp 2B – Non‑linear Problem

> Mục tiêu của mục này: **chỉ cần nhìn thấy một từ khóa là bật ngay 1–2 thuật toán chủ lực**.
> Mọi bài non‑linear liên quan quan hệ đỉnh–cạnh **bắt buộc gom về `graph` trước**.

---

### Từ khóa gốc: **graph**

Sau biến đổi, nếu tồn tại quan hệ *entity → entity* (ràng buộc, phụ thuộc, đi lại được) ⇒ **graph**.

Bước quyết định cấp 1 (không được bỏ qua):

```
GRAPH → UNDIRECTED | DIRECTED
```

---

### 1. **Undirected graph** (vô hướng)

> Bao gồm: graph vô hướng, **tree**, grid (4/8 directions).

#### 1.1 Từ khóa: **connected / component**

→ Thuật toán bật ngay:

* DFS / BFS
* DSU

#### 1.2 Từ khóa: **bridge / articulation**

→ Thuật toán bật ngay:

* Tarjan (low-link)

#### 1.3 Từ khóa: **tree**

→ Thuật toán bật ngay:

* DFS tree
* DP on tree
* LCA (binary lifting, Euler tour)

#### 1.4 Từ khóa: **bipartite / odd cycle**

→ Thuật toán bật ngay:

* BFS / DFS + coloring

---

### 2. **Directed graph** (có hướng)

> Bao gồm: dependency, quan hệ trước–sau, flow logic một chiều.

#### 2.1 Từ khóa: **ordering / dependency / prerequisite**

→ Thuật toán bật ngay:

* Topological sort

#### 2.2 Từ khóa: **cycle (directed)**

→ Thuật toán bật ngay:

* DFS cycle detection
* Topo sort (fail ⇒ cycle)

#### 2.3 Từ khóa: **SCC / mutually reachable**

→ Thuật toán bật ngay:

* Tarjan SCC
* Kosaraju
* Condensation graph

#### 2.4 Từ khóa: **reachability**

→ Thuật toán bật ngay:

* DFS / BFS
* DP on DAG (nếu acyclic)

---

### 3. **Graph + path optimization**

> Chỉ xét sau khi đã xác định loại graph.

#### 3.1 Từ khóa: **shortest path**

→ Thuật toán bật ngay:

* BFS (unweighted)
* Dijkstra (non‑negative weight)
* Bellman‑Ford / SPFA (có negative)

#### 3.2 Từ khóa: **longest path**

→ Thuật toán bật ngay:

* DP on DAG
* Tree DP (nếu là tree)

---

### 4. **Graph sau khi biến đổi cấu trúc**

#### 4.1 Từ khóa: **subtree**

→ Thuật toán bật ngay:

* Euler tour → range
* Segment tree / BIT

#### 4.2 Từ khóa: **tree path**

→ Thuật toán bật ngay:

* LCA
* Binary lifting
* DP on tree

#### 4.3 Từ khóa: **2D grid / island**

→ Thuật toán bật ngay:

* Flood fill
* BFS / DFS
* Prefix sum 2D

---

## VI. Hệ từ khóa cấp 3 – Query Problem

### 1. Từ khóa: **many queries**

→ Query Problem

#### 1.1 + **online / interactive / adaptive**

* Segment tree
* BIT
* Balanced BST
* Persistent segment tree

**Loại bỏ**: Mo, offline D&C

#### 1.2 + **offline / independent queries**

* Mo algorithm
* Offline divide & conquer
* DSU rollback

---

## VII. Hệ từ khóa đặc biệt – Search on Answer & Optimization


### 1. **Binary Search on Answer (BSOA)**

**Từ khóa nhận diện**:

* "maximize / minimize" + ràng buộc
* "smallest / largest value such that"
* Có thể viết hàm `check(x)` dạng **monotonic (true → true)** hoặc **false → false**

**Lưu ý quan trọng**:

* Bài toán có thể xuất phát từ **linear hoặc non‑linear**; nếu mô hình được `check(x)` thì **đều áp dụng được**.

---

### 2. **Parallel Binary Search (PBS)**

**Từ khóa đặc điểm (nhận diện nhanh):**

* Binary search on answer
* Có **nhiều query**, mỗi query cần tìm đáp án riêng
* Có thể viết `check(x)` **giống nhau cho mọi query**
* Hàm `check` **(≈ 10^5)** nếu chạy từng query 
* Có thể **gom nhiều query** để xử lý chung trong một lần `check`

### 3. **Ternary Search**

**Từ khóa nhận diện**:

* Hàm **unimodal** (tăng rồi giảm / giảm rồi tăng)
* Không yêu cầu tính nguyên

### 4. **Sqrt‑Decomposition / Sqrt‑Optimization**

- **Từ khóa cốt lõi:**
	* **chia block theo √N** (block size ≈ √N)

- **Từ khóa nhận diện (mạnh → yếu):**
	1. **N ≈ 10^5, Q ≈ 10^5**

	   * O(NQ) quá chậm
	   * O((N+Q) log N) có thể không cần thiết

	2. **Query + update xen kẽ**, nhưng:
	   * Update **tác động cục bộ** (một phần tử / một block)
	   * Query có thể trả lời bằng cách **gộp kết quả từ các block**

	3. Có thể tách xử lý thành:
	   * **Trong block** → brute force / rebuild
	   * **Giữa các block** → dùng thông tin tổng hợp (sum, max, freq, lazy tag)

	4. Thấy các cụm từ:
	   * "block"
	   * "bucket"
	   * "rebuild after k operations"
	   * "offline by blocks"

## VIII. Checklist nhận diện nhanh (thực chiến)

1. Sau biến đổi, có thành **range [l, r]** không?
2. Có **nhiều query** không?
3. Query có **update** không?
4. Có thể **viết hàm check(x)** không?
5. Quan hệ chính là **subarray / path / component / feasibility**?

Nếu không trả lời được **≥ 3 câu** → bạn **chưa biến đổi xong bài toán**.



