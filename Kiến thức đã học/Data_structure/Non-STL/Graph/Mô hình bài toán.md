[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Data_Structures/Graph)


# Mô hình hóa bài toán thành các dạng graph

## 1) Câu hỏi mở đầu trước khi model
- Node là gì: đối tượng hay trạng thái?
    - Cách xác định: lấy "đơn vị thay đổi độc lập" nhỏ nhất, bị phép toán của đề bài tác động; nếu kết quả phụ thuộc thêm lịch sử/tài nguyên thì node phải là `(vị trí, trạng thái phụ)`.
- Cạnh nghĩa là gì: liên thông, phụ thuộc, hay chuyển trạng thái?
    - Cách xác định: mỗi thao tác hợp lệ hoặc quan hệ trực tiếp tạo đúng 1 cạnh, chiều cạnh bám theo thứ tự tác động.
- Trọng số nằm ở đâu: trên cạnh hay trên node?
    - Cách xác định: chi phí phát sinh khi di chuyển thì đặt trên cạnh; chi phí phát sinh khi đi vào/chọn node thì đặt trên node (hoặc đổi tương đương sang cạnh).
- Mục tiêu: tìm đường đi, đếm cách, kiểm tra tồn tại, hay tách thành phần?
    - Cách xác định: đọc output cần tối ưu hay chỉ cần đúng/sai, rồi map về dạng chuẩn tương ứng (shortest path, counting, reachability, connectivity/components).

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

## 4) Chọn thuật toán dựa trên mô hình

### 4.1 Object graph
- Cần đường đi ngắn nhất theo số cạnh (không trọng số / đồng trọng số): [BFS](BFS.md).
- Cần shortest path với trọng số không âm: Dijkstra (xem [Shortest path](<State space search/Shortest path.md>)).
- Có cạnh âm: Bellman-Ford/SPFA; nếu cần phát hiện chu trình âm: [Positive or Negative cycle](<Positive or Negative cycle.md>).
- Cần kiểm tra liên thông / đếm thành phần: DFS/BFS.
- Cần tìm cầu / khớp: [bridge and ap](<bridge and ap.md>).
- Cần truy vấn tìm cầu khớp nhanh : [BCT/BET](<Graph decomposition/bet_bct.md>)
- Cần chọn cạnh để nối toàn bộ đỉnh với tổng trọng số tối ưu: [MST](basic_spanning_tree_forest.md).

### 4.2 Dependency graph
- Cần kiểm tra có thứ tự hợp lệ hay không: [Topological sort](<Topological sort.md>).
- Là DAG và cần tối ưu/đếm trên thứ tự phụ thuộc: [Topo + DP](<DP Graph/Topo + DP.md>).
- Có chu trình: tách SCC rồi co về DAG: [condensation graph](<Graph decomposition/condensation graph.md>), sau đó topo/DP trên DAG co rút.

### 4.3 State-space graph
- Mỗi bước có cùng cost: BFS trạng thái.
- Cost cạnh chỉ thuộc `{0,1}`: 0-1 BFS.
- Cost cạnh không âm tổng quát: Dijkstra.
- Có cạnh âm: Bellman-Ford/SPFA và kiểm tra negative cycle khi cần.
- Nhiều nguồn: multi-source (hoặc thêm super source trọng số 0).

## 6) Liên kết note liên quan
- [Topological sort](<Topological sort.md>)
- [Topo + DP](<DP Graph/Topo + DP.md>)
- [condensation graph](<Graph decomposition/condensation graph.md>)
- [Positive or Negative cycle](<Positive or Negative cycle.md>)
- [bridge and ap](<bridge and ap.md>)
- [Khái niệm](<State space search/Khái niệm.md>)

