# Backtracking

## 1) Khái niệm
- Backtracking là duyệt không gian nghiệm bằng DFS, thử lựa chọn, kiểm tra điều kiện, rồi quay lui.
- Mục tiêu: tìm một nghiệm, tất cả nghiệm, hoặc nghiệm tối ưu (kết hợp pruning).

## 2) Khung chuẩn
1. Chọn biến/quyết định tiếp theo.
2. Thử từng giá trị hợp lệ.
3. Đánh dấu trạng thái (choose).
4. Gọi đệ quy.
5. Hoàn tác trạng thái (un-choose).

```cpp
void dfs(int pos) {
    if (done_condition) {
        record_answer();
        return;
    }
    for (auto choice : candidates(pos)) {
        if (!valid(choice)) continue;
        apply(choice);
        dfs(pos + 1);
        rollback(choice);
    }
}
```

## 3) Khi nào dùng
- Bài toán tổ hợp/tạo cấu hình: permutation, combination, n-queens, sudoku.
- Không gian lời giải lớn nhưng có nhiều điều kiện để cắt nhánh.
- Cần liệt kê nghiệm hoặc tìm nghiệm đầu tiên thỏa điều kiện.

## 4) Pruning (cắt nhánh) quan trọng
- Feasibility pruning: vi phạm ràng buộc thì dừng ngay.
- Bound pruning: ước lượng tốt nhất còn lại cũng không thắng đáp án hiện tại.
- Symmetry breaking: bỏ các nhánh đối xứng tương đương.
- Ordering heuristic: thử lựa chọn "khó" trước để fail sớm.

## 5) Độ phức tạp
- Tệ nhất thường là exponential (`O(b^d)`), phụ thuộc mạnh vào pruning.

## 6) Lỗi hay gặp
- Quên rollback làm nhiễm trạng thái giữa các nhánh.
- Base case sai khiến thiếu hoặc thừa nghiệm.
- Pruning sai làm mất nghiệm đúng.
- Dùng global state nhưng không reset giữa test.

## 7) So sánh nhanh
- Backtracking: chủ yếu để tìm kiếm có điều kiện và liệt kê nghiệm.
- DP: tận dụng chồng lặp trạng thái để tối ưu tính toán.
- Branch and Bound: backtracking + cận trên/cận dưới chặt để tối ưu.
