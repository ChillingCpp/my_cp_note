
# I. DP **CÓ LỰA CHỌN**

_(Explicit choice hoặc implicit / hidden choice đều tính)_

👉 **Định nghĩa**

> Tồn tại ≥ 2 cách hợp lệ để chuyển từ một trạng thái hiện tại.

Hay nói ngắn gọn:

`dp[state] = aggregate over multiple next states`

---
## 1. Lựa chọn hiện trong đề

Quyết định được mô tả rõ.

**Ví dụ**

- Chọn / không chọn
    
- Chọn 1 trong nhiều thao tác
    
- Chọn điểm chia đoạn
    

**Dạng bài**

- Knapsack
    
- Coin Change
    
- Interval DP
    
- Edit Distance
    
- Game DP
    

---

## 2. Lựa chọn ẩn trong đề

Không nói “chọn”, nhưng **bản chất là chọn**.

### a. Chọn cấu hình

- Bitmask DP
    
- Assignment
    
- TSP
    

### b. Chọn trạng thái

- Tree DP (chọn trạng thái node)
    
- Coloring DP
    
- DP với constraint
    

### c. Chọn chuyển tiếp

- Automaton DP
    
- String DP
    
- Digit DP (chọn chữ số)
    

---

## 3. Lựa chọn đối kháng

- Game / Minimax
    
- Grundy DP
    

---

## 4. Lựa chọn để tối ưu

- Scheduling DP
    
- DP + Greedy
    
- DP + Binary Search
    
- Advanced DP Optimization  
    (Knuth, D&C, CHT)
    

---

### ✔ Nhận diện DP có lựa chọn

- Có `min / max / sum over transitions`
    
- Có nhánh
    
- Có cạnh tranh giữa các phương án
    
- Có câu hỏi ngầm: _“nên đi hướng nào?”_
    

---

# II. DP **KHÔNG DỰA VÀO LỰA CHỌN**

_(State-evolution DP – không nhánh)_

👉 **Định nghĩa**

> Với mỗi trạng thái, trạng thái kế tiếp được xác định duy nhất.

Hay:

`dp[next_state] = f(dp[state])`

không có “hoặc”.

---

## 1. DP lan truyền tuyến tính

- Prefix / Suffix DP
    
- Rolling DP
    
- Fibonacci dạng chuẩn
    

---

## 2. DP đếm không nhánh

- Đếm cấu hình có công thức cố định
    
- DP tổ hợp (Catalan, Bell, Stirling…)
    

---

## 3. DP mô phỏng hệ xác định

- DP mô phỏng quá trình xác định
    
- Không có quyết định
    

**Ví dụ**

- Automaton _không nhánh_
    
- DP trạng thái máy với chuyển duy nhất
    

---

## 4. DP theo thời gian (deterministic)

- Hệ tiến hóa theo bước
    
- Không lựa chọn
    

---

## 5. DP toán học / công thức truy hồi

- Công thức truy hồi duy nhất
    
- Không tối ưu
    

---

### ✔ Nhận diện DP không lựa chọn

- Không có vòng `for transition`
    
- Không có cạnh tranh
    
- Trạng thái sau là tất yếu
    
- Chỉ “tính tiếp”, không “chọn”
    

---

# III. Bảng ranh giới chuẩn (quan trọng)

|Bài|Có lựa chọn?|Vì sao|
|---|---|---|
|Fibonacci|❌|Trạng thái duy nhất|
|Prefix sum|❌|Chuyển tiếp xác định|
|Digit DP|✅|Chọn chữ số|
|Tree DP|✅|Chọn trạng thái|
|Interval DP|✅|Chọn điểm chia|
|TSP|✅|Chọn tập tiếp theo|
|DP đếm đường đi DAG|❌|Không nhánh|
|Game DP|✅|Đối kháng|

---

# IV. Kết luận cốt lõi (rất mạnh)

✔ **DP có thể chia gọn thành đúng 2 loại**  
✔ Ranh giới nằm ở **số lượng chuyển tiếp hợp lệ từ 1 trạng thái**  
✔ “Lựa chọn” không phụ thuộc vào câu chữ đề bài  
✔ Đây là cách nhìn **đúng bản chất**, dùng được cho mọi DP

---

Nếu bạn muốn đi tiếp:

- 🔥 Chuẩn hóa định nghĩa này thành **1 định lý tư duy DP**
    
- 🔥 Áp dụng phân loại này để **phân tích nhanh đề CF**
    
- 🔥 Phản ví dụ: _khi nào DP tưởng không có lựa chọn nhưng thực ra có_
    
- 🔥 So sánh DP không lựa chọn vs Prefix/Recurrence thuần
    

Bạn muốn tôi đào sâu nhánh nào tiếp?