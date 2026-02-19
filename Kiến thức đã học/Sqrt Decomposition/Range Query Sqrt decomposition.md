# Range Query Sqrt decomposition

[Sqrt + Sqrt lazy](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/DS_decomposition/array_decomposition.cpp)

## Tư tưởng
- Chia mảng thành các block có độ dài `B ~ sqrt(n)`.
- Mỗi block lưu thông tin gộp (thường là `sum/min/max`).
    - phép gộp thông tin phải có tính chất kết hợp
- Query đoạn `[l, r]` tách thành 3 phần:
    - phần lẻ đầu (duyệt tay),
    - các block đầy đủ (lấy nhanh từ mảng block),
    - phần lẻ cuối (duyệt tay).

## Công thức cốt lõi
- `B = floor(sqrt(n)) + 1`
- `block_id(i) = i / B`
- `num_block = (n + B - 1) / B`
- Block `b` có biên:
    - `L = b * B`
    - `R = min(n - 1, (b + 1) * B - 1)`

## Dạng kinh điển: Range Sum + Point Update
- Dữ liệu:
    - `a[i]`: mảng gốc
    - `block_sum[b]`: tổng block `b`
- Query `[l, r]`: `O(sqrt(n))`
- Point update `a[pos] = val`: `O(1)` (cập nhật trực tiếp `block_sum`)

## Biến thể: Range Add + Range Sum (Sqrt lazy theo block)
- Thêm `lazy[b]`: giá trị cộng dồn cho toàn block.
- Khi update full block:
    - `lazy[b] += x`
    - `block_sum[b] += x * block_size(b)`
- Khi chạm block biên (không full):
    - cập nhật từng phần tử,
    - đồng thời sửa lại `block_sum`.
- Query phần tử/block nhớ tính cả `lazy`.

Độ phức tạp thường là `O(sqrt(n))` cho mỗi query/update.

## Khi nào dùng
- Muốn code nhanh hơn Segment Tree nhưng vẫn cần online query/update.
- `n, q` vừa phải (thường tới cỡ `2e5` vẫn ổn trong nhiều bài).
- Phép gộp đơn giản (`sum/min/max`) và không cần nhiều custom phức tạp.

## Đường dẫn
- [[Sqrt chung]]
- [[Mo]]
- [[Segment Tree]]
- [[Lazy Segment Tree]]
- [[Prefix sum 1D]]
