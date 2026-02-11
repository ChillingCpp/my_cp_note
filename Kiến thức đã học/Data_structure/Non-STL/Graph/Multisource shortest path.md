
- Multi-source không phải thuật toán mới.
	- Khởi tạo nhiều node có `dist = 0`, sau đó chạy BFS / Dijkstra như bình thường.
- Tương đương về mặt lý thuyết với:
	- Thêm một **super source S**
	- Nối `S → s_i` với trọng số 0
	- Chạy single-source từ S

- Độ phức tạp : O(n) hoặc O(n log n)
## 3️⃣ Khi nào sử dụng?

### (1) Khoảng cách đến nguồn gần nhất

- dist[u] = khoảng cách từ u đến source gần nhất
    
- Ứng dụng: nearest facility, nearest special node
    

---

### (2) Lan truyền đồng thời

- Fire spread
    
- Zombie spread
    
- Infection model
    
- Flood fill nhiều điểm
    

---

### (3) Kiểm tra khả thi

- Có tồn tại đường đi từ **bất kỳ nguồn nào** đến t?
    
- Kiểm tra `dist[t] != INF`
    

---

### (4) Reverse graph trick

Nếu cần biết:

> Node nào có thể đi tới một node đặc biệt

Ta:

1. Đảo chiều tất cả cạnh
    
2. Multi-source từ các node đặc biệt
    
3. Chạy BFS / Dijkstra
    

Khi đó:

`dist[u] = khoảng cách từ u đến special node gần nhất`

Rất hay dùng trong CP.

---

# 4️⃣ Kết hợp nâng cao

Đây là phần bạn chưa ghi nhưng rất quan trọng.

---

## 🔹 A. Multi-source + 0-1 BFS

Khi cạnh có trọng số 0 hoặc 1.

Ví dụ:

- Có nhiều checkpoint miễn phí
    
- Di chuyển bình thường tốn 1
    

Ta:

- Push tất cả checkpoint vào deque với dist = 0
    
- Chạy 0-1 BFS
    

Độ phức tạp: `O(n + m)`

---

## 🔹 B. Multi-source trên DAG

Nếu graph là DAG:

- Có thể topo sort
    
- Khởi tạo nhiều node có dist = 0
    
- Relax theo topo order
    

Độ phức tạp: `O(n + m)`

Áp dụng khi:

- Tối ưu hóa trên dependency graph
    
- DP nhiều trạng thái khởi đầu
    

---

## 🔹 C. Multi-layer graph (Graph trạng thái)

Rất mạnh trong CP.

Ví dụ:

Node dạng `(u, state)`

Ta có nhiều trạng thái ban đầu hợp lệ.

Ví dụ:

- Có k loại năng lượng
    
- Có nhiều điểm bắt đầu hợp lệ
    

Ta push tất cả `(s_i, state_i)` vào PQ.

Multi-source khi:

- Có nhiều cấu hình khởi tạo hợp lệ
    

---

## 🔹 D. Multi-source + Meet-in-the-middle trên graph

Một kỹ thuật thường gặp:

- Chạy multi-source từ tập A
    
- Chạy multi-source từ tập B
    
- Kết hợp dist
    

Ví dụ:

Tìm đường ngắn nhất giữa 2 tập node.

---

## 🔹 E. Tách bài toán về nearest special node

Rất nhiều bài CP thực chất là:

> Tính dist_to_nearest_special

Sau đó dùng dist đó để:

- So sánh
    
- DP
    
- Binary search
    
- Greedy
    

Multi-source là bước tiền xử lý.