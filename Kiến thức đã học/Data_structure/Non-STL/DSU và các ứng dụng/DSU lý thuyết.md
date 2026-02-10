
## 6️⃣ DSU dùng cho merge giá trị

> **DSU có thể duy trì và gộp thông tin của mỗi tập nếu phép toán gộp là kết hợp (associative), và tốt nhất là giao hoán (commutative).**
---
### 🔹 Kết hợp (bắt buộc)
$(a⊗b)⊗c=a⊗(b⊗c)(a ⊗ b) ⊗ c = a ⊗ (b ⊗ c)(a⊗b)⊗c=a⊗(b⊗c)$
### 🔹 Giao hoán (rất nên)
$a ⊗ b = b ⊗ a$
---
## 7️⃣ Các phép toán CÓ THỂ dùng trong DSU

✅ Hợp lệ:
- `sum`    
- `min`, `max`
- `gcd`
- `xor`
- `and`, `or`
- đếm số phần tử
❌ Không hợp lệ:
- trừ
- chia
- trung bình trực tiếp (phải lưu sum + count)
- đếm tần số
---
## 🔟 DSU dùng được khi phép toán KHÔNG giao hoán
➡️ Nếu bạn **lưu thêm thông tin theo hướng**
Ví dụ:
- DSU parity
- DSU weighted
- DSU xor-distance
📌 Khi đó:
- Không cần commutative
- Nhưng **phải thiết kế logic cẩn thận**
---

# Các dạng bài DSU:



---

---
## 1️⃣6️⃣ DSU + Parity = kiểm tra bipartite

- Lưu **parity đường đi tới root**
- get trả về: `(root, parity)`
- union tính parity giữa hai root
- 
📌 Đây là dạng DSU:
- **toán tử KHÔNG giao hoán**
- nhưng vẫn đúng vì ta lưu **thông tin theo hướng**
---
## 1️⃣6️⃣  DSU lưu danh sách phần tử trong component, có trỏ tới root 

```
vector<int> lst[MAXN];
int parent[MAXN];

void make_set(int v) {
    lst[v] = vector<int>(1, v);
    parent[v] = v;
}

int find_set(int v) {
    return parent[v];
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (lst[a].size() < lst[b].size())
            swap(a, b);
        while (!lst[b].empty()) {
            int v = lst[b].back();
            lst[b].pop_back();
            parent[v] = a;
            lst[a].push_back (v);
        }
    }
}
```

- Lưu **parity đường đi tới root**
- get trả về: `(root, parity)`
- union tính parity giữa hai root
- 
📌 Đây là dạng DSU:
- **toán tử KHÔNG giao hoán**
- nhưng vẫn đúng vì ta lưu **thông tin theo hướng**
---



## 1️⃣6️⃣ Tìm cầu online : lưu trữ cây nén/ không nén
- DSU hoạt động với cả dynamic, changing graph : add/remove edge




# 1️⃣9️⃣ Nhận diện nhanh DSU

---
## 1. Từ khóa trước khi biến đổi

Các từ này **chỉ là tín hiệu yếu**, dùng để nghi ngờ chứ **không được quyết định**:

- connect / disconnect
- same group / same component
- related / reachable
- merge / join
- friend / enemy
- cluster
- road / network / cable
- equivalence / equality
- consistent / contradiction
    
👉 **Sai lầm phổ biến**: thấy các từ này là nhảy vào DSU ngay.

---
## 2. Bản chất thật sự sau khi biến đổi (QUYẾT ĐỊNH)

Sau khi phát biểu lại bài toán một cách toán học, bài DSU **luôn rơi vào một trong các dạng sau**.

---
### Dạng 1: **Partition / Equivalence Relation**

#### Mô tả sau biến đổi

> Ta cần duy trì một **phân hoạch** các phần tử, chỉ có:
- gộp hai tập
- hỏi hai phần tử có cùng tập hay không
#### Dấu hiệu cứng

- Quan hệ có tính:
    - phản xạ   
    - đối xứng
    - bắc cầu 
- Không cần thứ tự, không cần đường đi
#### Từ khóa sau biến đổi

- “thuộc cùng nhóm”
- “tương đương”
- “đồng nhất”
- “cùng loại”
👉 **DSU thuần**.

---
### Dạng 2: **Constraint giữa các phần tử (DSU + aux)**

#### Mô tả sau biến đổi

> Mỗi cạnh không chỉ nối, mà còn mang **ràng buộc đại số**.

Ví dụ:
- `a - b = c`
- `color[a] XOR color[b] = 1`
- `parity[a] != parity[b]`
#### Dấu hiệu quyết định

- Quan hệ **không tuyệt đối**, mà là **tương đối**
- Câu hỏi: _“mối quan hệ giữa u và v là gì?”_
- Chỉ cần kiểm tra mâu thuẫn, không cần đường đi

#### Từ khóa sau biến đổi

- difference
- parity
- relative
- constraint
- consistency
- contradiction

👉 **Weighted / Parity / XOR DSU**.

---

### Dạng 3: **Offline connectivity (DSU không thời gian)**

#### Mô tả sau biến đổi

> Kết nối **thay đổi theo thời gian**, nhưng ta **được phép offline**.
#### Dấu hiệu rất mạnh

- add edge
- remove edge
- query connectivity
- offline / batch
- time interval
#### Sau biến đổi
- mỗi cạnh tồn tại trên 1 đoạn thời gian
- dùng:    
    - segment tree on time
    - DSU rollback   

👉 **DSU rollback**.

---

### Dạng 4: **Graph nhưng chỉ cần component, không cần đường**

#### Mô tả

> Bài nói về graph, nhưng câu hỏi **không bao giờ hỏi đường đi**.
#### Dấu hiệu lừa đảo

- Có graph
- Có edge  
- Nhưng:
    - không hỏi path    
    - không hỏi distance    
    - không hỏi sequence

👉 Thực chất là DSU, không phải BFS/DFS.

---

### Dạng 5: **Kruskal trá hình**

#### Mô tả sau biến đổi
> Chọn các cạnh sao cho:
- không tạo chu trình
- tối ưu theo trọng số
#### Từ khóa sau biến đổi

- minimum / maximum
- spanning
- threshold
- at least / at most
    
👉 **DSU là công cụ kiểm tra chu trình**, không phải trọng tâm.

---
## 3. Đặc điểm nhận diện SAU khi bạn biến đổi đúng

Sau khi biến đổi bài toán, nếu bạn thấy **≥ 2 dấu hiệu sau**, rất nhiều khả năng là DSU:
### Checklist cứng

-  Không cần lưu đường đi
-  Mỗi phần tử cùng chung tính chất nằm trong 1 nhóm
-  Quan hệ có tính bắc cầu
-  Thao tác chính là merge
-  Không có undo (hoặc undo rõ ràng → rollback)
-  Không cần thứ tự
    