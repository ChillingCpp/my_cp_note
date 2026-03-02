# BFS: biến thể và các dạng bài

## 1. Các biến thể BFS thường gặp

1. BFS chuẩn (single-source)
- Dùng khi đồ thị không trọng số (hoặc mọi cạnh có cùng trọng số).
- Mục tiêu: tìm khoảng cách ngắn nhất theo số cạnh từ 1 đỉnh nguồn.
- Độ phức tạp: O(V + E).

2. Multi-source BFS
- Đưa nhiều đỉnh nguồn vào queue ngay từ đầu với dist = 0.
- Dùng cho bài lan truyền đồng thời, tìm đỉnh gần nhất tới "tập nguồn".
- Độ phức tạp: O(V + E).

3. 0-1 BFS
- Áp dụng khi trọng số cạnh chỉ là 0 hoặc 1.
- Dùng deque: cạnh 0 thì push_front, cạnh 1 thì push_back.
- Thay cho Dijkstra trong trường hợp đặc biệt, nhanh hơn thực tế.
- Độ phức tạp: O(V + E).

4. Bidirectional BFS (BFS hai đầu)
- Chạy BFS từ nguồn và đích cùng lúc.
- Hữu ích khi không gian trạng thái lớn, branching factor cao.
- Thường giảm rất mạnh số trạng thái phải duyệt.

5. BFS trên đồ thị ẩn (implicit graph)
- Đỉnh không cho sẵn, sinh hàng xóm bằng phép biến đổi trạng thái.
- Ví dụ: đổi số, đổi chuỗi, puzzle, trạng thái game.

6. BFS trạng thái (state-space BFS)
- Mỗi đỉnh mở rộng thành (u, state).
- state có thể là: parity, modulo, bitmask chìa khóa, số bước theo chu kỳ, ...
- Dùng khi bài có ràng buộc phụ thuộc ngữ cảnh chứ không chỉ vị trí u.

7. BFS theo lớp mức (level BFS)
- Duyệt theo từng layer để xử lý "sau k bước", "ít bước nhất", "lan truyền theo ngày".
- Hay dùng trong lưới, mô phỏng theo thời gian rời rạc.

## 2. Các dạng bài chính dùng BFS trực tiếp

1. Đường đi ngắn nhất trên đồ thị không trọng số
- Tìm dist từ s tới mọi đỉnh hoặc tới t.
- Truy vết đường đi bằng mảng parent.

2. Duyệt thành phần liên thông
- BFS từ các đỉnh chưa thăm để đếm số component.

3. Kiểm tra đồ thị hai phía (bipartite)
- Tô màu 2 màu theo BFS; nếu gặp cạnh nối 2 đỉnh cùng màu thì không hợp lệ.

4. Bài toán trên lưới (grid)
- Mê cung, flood fill, khoảng cách Manhattan theo bước đi hợp lệ.

5. Bài toán cây
- Level theo gốc.
- Đường kính cây: 2 lần BFS.

6. Mô phỏng lan truyền
- Cháy rừng, lây nhiễm, nước dâng, thối rữa, ... theo từng đơn vị thời gian.

## 3. Dạng bài ẩn có thể quy về BFS

1. "Ít phép biến đổi nhất" hoặc "ít thao tác nhất"
- Dù đề không nói đồ thị, thường mỗi trạng thái là 1 đỉnh, mỗi thao tác là 1 cạnh.

2. "Trọng số nhỏ đặc biệt" (chỉ 0/1)
- Nhìn giống weighted graph nhưng thực ra dùng 0-1 BFS.

3. "Nhiều điểm bắt đầu cùng lúc"
- Có thể quy về multi-source BFS thay vì chạy BFS nhiều lần.

4. Ràng buộc theo thời điểm/chẵn lẻ/modulo, tìm multiple của ( hay là số chia hết cho ) K thỏa predicate
- Mở rộng đỉnh thành (u, time mod k) hoặc (u, parity).
- multiple của K : (u, (10*u + d) % mod, state...) với d ∈ {0,1,…,9}.
5. Bài có chìa khóa/cửa/công tắc
- Trạng thái phải kèm bitmask tài nguyên đã thu thập.

6. Bài truy vấn gần nhất tới tập đặc biệt
- Gộp toàn bộ đỉnh đặc biệt làm nguồn và chạy 1 lần BFS.

7. Bài tìm chu trình ngắn nhất trên đồ thị không trọng số
- Có thể BFS từ từng đỉnh (hoặc tối ưu theo cấu trúc đề).

8. Bài "mức phụ thuộc" trong DAG
- Kahn (topo bằng queue) là tư duy BFS theo indegree.

## 4. Checklist nhận diện BFS nhanh

- Mục tiêu là số bước ít nhất, không phải tổng trọng số bất kỳ.
- Chuyển trạng thái có chi phí đều nhau (hoặc 0/1).
- Cần xử lý theo lớp thời gian.
- Có thể mô hình hóa trạng thái + phép chuyển.
- Cần khoảng cách từ một hoặc nhiều nguồn đến toàn bộ đỉnh.

## 5. Gợi ý chọn biến thể

- Cạnh đồng trọng số -> BFS chuẩn.
- Nhiều nguồn -> Multi-source BFS.
- Cạnh 0/1 -> 0-1 BFS.
- Không gian trạng thái lớn, có nguồn và đích rõ -> Bidirectional BFS.
- Có ràng buộc phụ -> BFS trạng thái (u, state).
