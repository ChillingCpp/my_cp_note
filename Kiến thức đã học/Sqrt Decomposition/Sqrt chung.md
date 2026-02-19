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
	- `Dạng 2: Block + lazy theo block`
		- Update đoạn và query đoạn với nhãn lazy cho từng block.
			- "range update range query"
	- `Dạng 3: Offline query (Mo's algorithm)`
		- Sắp xếp query theo block của `L` (và `R`) để giảm số lần add/remove.
	- `Dạng 4: Chia theo giá trị/ngưỡng`
		- Tách phần tử thành "nhẹ/nặng", hoặc chia theo tần suất/độ lớn/độ dài để tối ưu.
	- `Dạng 5: Harmonic grouping`
		- Với biểu thức kiểu `floor(n / i)`:
			- `i <= sqrt(n)`
			- `i > sqrt(n)` 
- Mẫu nhận diện:
	- Có tradeoff tự nhiên giữa 2 phía (ví dụ: số block và kích thước block).
	- Chọn ngưỡng `B ~ sqrt(n)` để cân bằng 2 phần chi phí.

## Khi nào dùng
- Cần code nhanh, dễ debug hơn segment tree.
- Có thể chấp nhận mỗi thao tác khoảng `O(sqrt(n))`.
- Bài có update/query online nhưng không quá nặng.

## Công thức thường dùng
- `block_id(i) = i / len` (0-index).
- Số block: `num_block = (n + len - 1) / len`.
- Mỗi query/update:
	- brute force phần block bị intersect với biên l và r
	- block đầy đủ: dữ liệu block

## Code mẫu
[Sqrt + Sqrt lazy](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/DS_decomposition/array_decomposition.cpp)

## Đường dẫn
- [[Segment Tree]]
- [[Lazy Segment Tree]]
- [[Harmonic Number]]
- [[Prefix sum 1D]]
- [[Range Query Sqrt decomposition]]

