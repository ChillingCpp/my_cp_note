# Range Query Sqrt decomposition

[Sqrt + Sqrt lazy](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/DS_decomposition/array_decomposition.cpp)

## Tư tưởng
- Chia mảng thành các block có độ dài `B ~ sqrt(n)`.
- Mỗi block lưu thông tin gộp (thường là `sum/min/max`).
    - phép gộp thông tin phải có tính chất kết hợp
- Query đoạn `[l, r]` tách thành 2 trường hợp:
    - `bl == br`:
        duyệt từ `l -> r` để lấy giá trị
    - `bl != br` : duyệt theo 3 phần 
        - phần lẻ đầu (duyệt tay),
        - các block đầy đủ (lấy nhanh từ mảng block),
        - phần lẻ cuối (duyệt tay).

## Công thức cốt lõi
- `B = floor(sqrt(n)) + 1`
- `block_id(i) = i / B`
- `num_block = (n + B - 1) / B`
- `bid(int i) = i / B`;
- `iid(int b) = b * B`;
- Với query `[l, r]`:
    - `bl = bid(l)`, `br = bid(r)`
- Block `b` có biên:
    - `L = b * B`
    - `R = min(n - 1, iid(b+1) - 1)`
- Duyệt lẻ đầu:
    - `[l, iid(bl + 1) - 1]`
    - for (int i = l; i < iid(bl+ 1); ++i)
- Duyệt lẻ cuối:
    - `[iid(br), r]`
    - for (int i = iid(br); i <= r; ++i)
- Các block đầy đủ ở giữa:
    - `[bl + 1, br - 1]`
    - for (int i = bl + 1; i < br; ++i)



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
- [Sqrt chung](<Sqrt chung.md>)
- [Mo](Mo.md)
- [Segment Tree](<../Data_structure/Non-STL/Segment Tree.md>)
- [Lazy Segment Tree](<../Data_structure/Non-STL/Lazy Segment Tree.md>)
- [Prefix sum 1D](<../Data_structure/STL/Prefix structures and Difference Array/Prefix sum 1D.md>)
