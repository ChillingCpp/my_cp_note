[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/dp)

## Tính chất ứng dụng giải bài

- Dùng cho DP tối ưu khi hàm chi phí theo biến quyết định có tính lồi từng đoạn (piecewise-linear convex).
- Mẫu thường gặp: transition thêm các hạng `|x-a|`, `max(0, x-a)`, `max(0, a-x)` lặp nhiều bước.
- Mục tiêu: duy trì hàm chi phí tối ưu và lấy giá trị min nhanh sau mỗi bước.
- Keyword nhận diện: `convex DP`, `piecewise linear`, `add abs`, `penalty lệch khỏi mốc`.
- Không phù hợp khi hàm mục tiêu không lồi hoặc cần toàn bộ bảng trạng thái rời rạc.
