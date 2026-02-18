# Single Source - K Best States

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Graph/Shortest_paths/dijkstra.cpp)

## Mục tiêu
- Với mỗi node, lưu tối đa `k` trạng thái tốt nhất.

## Cấu trúc dữ liệu
- `heap_global`: để lan truyền trạng thái toàn cục.
- `best[u]`: container giữ tối đa `k` đáp án tại node `u`.

## Quy tắc cập nhật
- Nếu `best[v].size() < k`: thêm trạng thái mới.
- Nếu đã đủ `k`: chỉ thay khi trạng thái mới tốt hơn trạng thái tệ nhất hiện có.
- Chỉ lan truyền trạng thái được pop từ `heap_global` (không lan truyền bừa mọi state đang lưu).

## Lưu ý
- Bài simple path thường khó/hiếm trong contest chuẩn.
- Đảm bảo comparator của heap đúng chiều tối ưu.

