
# Mô hình hóa bài toán thành các dạng graph

## 1) Câu hỏi mở đầu trước khi model
- Node là gì: đối tượng hay trạng thái?
- Cạnh nghĩa là gì: liên thông, phụ thuộc, hay chuyển trạng thái?
- Trọng số nằm ở đâu: trên cạnh hay trên node?
- Mục tiêu: tìm đường đi, đếm cách, kiểm tra tồn tại, hay tách thành phần?

## 2) Chọn loại đồ thị

### Đồ thị vô hướng
- Quan hệ đối xứng: `u liên quan v` thì `v liên quan u`.
- Dùng khi bài nói về nhóm, kết nối, thành phần liên thông, cầu/khớp.
- Từ khóa: "cùng nhóm", "kết nối qua lại", "cắt cạnh/node làm tách mạng".

### Đồ thị có hướng
- Quan hệ một chiều: phụ thuộc, thứ tự, điều kiện trước-sau.
- Dùng khi có operation chuyển trạng thái hoặc quan hệ `u -> v`.
- Từ khóa: "phải làm trước", "sau khi", "nếu chọn u thì ảnh hưởng v".

## 3) Pattern model thường gặp

### 3.1 Object graph (mỗi thực thể là 1 node)
- Node: thành phố, người, task, đỉnh lưới...
- Cạnh: quan hệ trực tiếp giữa 2 thực thể.
- Bài thường ra: shortest path, connectivity, MST, bridge/AP.

### 3.2 Dependency graph
- Node: công việc/module/môn học.
- Cạnh `u -> v`: phải xong `u` mới làm `v`.
- Nếu không chu trình: DAG, dùng topo, topo + DP.
- Nếu có chu trình: co SCC rồi làm trên DAG co rút.

### 3.3 State-space graph
- Node: trạng thái `(u, extra_state...)` thay vì chỉ `u`.
- Cạnh: một phép chuyển hợp lệ giữa 2 trạng thái.
- Dùng khi có ràng buộc như số lần dùng phép, parity, mask, số bước còn lại...

## 6) Liên kết note liên quan
- [[Topological sort]]
- [[Topo + DP]]
- [[condensation graph]]
- [[Positive or Negative cycle]]
- [[bridge and ap]]
- [[Khái niệm]]
