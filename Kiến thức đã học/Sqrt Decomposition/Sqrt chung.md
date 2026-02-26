# Sqrt Decomposition

## Tư tưởng
- Sqrt decomposition là tư tưởng "chia theo ngưỡng `sqrt(n)`" để đổi một thao tác đắt thành:
	- phần nhỏ xử lý trực tiếp,
	- phần lớn xử lý theo block/nhóm.
- Từ tư tưởng này sinh ra nhiều dạng bài:
	- `Dạng 1: Chia block theo chỉ số mảng`
		- Query/update đoạn bằng cách tách `[l, r]` thành đầu lẻ + block đầy đủ + cuối lẻ.
			- "range query"
			- "point update range query"
			- "range update range query"
	- `Dạng 2: Offline query (Mo's algorithm)`
		- Sắp xếp query theo block của `L` (và `R`) để giảm số lần add/remove.
	- `Dạng 3: Chia theo case nặng/nhẹ`
		- Tìm dạng dữ liệu có thể chia case thành "nhẹ/nặng", hoặc chia theo tần suất/độ lớn/độ dài để tối ưu thuật toán hiện có

- Mẫu nhận diện:
	- Có tradeoff tự nhiên giữa 2 phía (ví dụ: số block và kích thước block).
	- Chọn ngưỡng `B ~ sqrt(n)` để cân bằng 2 phần chi phí.

## Khi nào dùng
- Cần code nhanh, dễ debug hơn segment tree.
- Có thể chấp nhận mỗi thao tác khoảng `O(sqrt(n))`.
- Bài có update/query online nhưng không quá nặng.

## Chi tiết về các dạng sqrt
- [Range Query Sqrt decomposition](<Range Query Sqrt decomposition.md>)
- [Mo](Mo.md)
## Đường dẫn
- [Segment Tree](<../Data_structure/Non-STL/Segment Tree.md>)
- [Lazy Segment Tree](<../Data_structure/Non-STL/Lazy Segment Tree.md>)
- [Prefix sum 1D](<../Data_structure/STL/Prefix structures and Difference Array/Prefix sum 1D.md>)

