[source code](https://github.com/ChillingCpp/DSA_CP/tree/main)

## Tính chất ứng dụng giải bài

- Query tĩnh, không update: ưu tiên `Prefix/Suffix`, `Sparse Table`.
- Point update + range query online: ưu tiên `Segment Tree` hoặc `Fenwick`.
- Range update tổng quát + range query: ưu tiên `Lazy Segment Tree`.
- Offline query nhiều, add/remove cục bộ tốt: ưu tiên `Mo`.
- Offline tìm mốc đầu tiên thỏa điều kiện cho nhiều query: ưu tiên `Parallel Binary Search`.
- Muốn code nhanh, chấp nhận `O(sqrt n)` mỗi thao tác: dùng `Sqrt decomposition`.
- One-shot range update rồi tổng hợp cuối: dùng `Difference Array`.

## Đường dẫn :
- [[Segment Tree]]
- [[Lazy Segment Tree]]
- [[Parallel Binary Search]]
- [[Mo]]
- [[Sqrt chung]]
- [[Range Query Sqrt decomposition]]
- [[Prefix sum 1D]]
- [[Prefix sum 2D]]
- [[Prefix min]]
- [[Prefix max]]
- [[Difference Array]]
- [[Prefix or suffix Arrays]]
- [[Stack]]
