[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dsu/Dsu.cpp)

# Neighbor-linked array (tư duy gần DSU)

## Ý tưởng
- Mỗi phần tử `i` lưu hàng xóm trái/phải: `L[i]`, `R[i]`.
- Xóa phần tử bằng cách nối trực tiếp 2 hàng xóm.
- Phù hợp cho truy vấn động kiểu "xóa/chèn/trái/phải" trên dãy.

## Hỗ trợ
 - Thêm / xóa phần tử
 - Đổi / hoán đổi vị trí
 - Truy vấn phần tử trái / phải
 - Bỏ qua phần tử đã xóa
 - Mảng thường / mảng tròn
 - Duy trì nhiều dãy độc lập
 - Cắt – nối đoạn (segment cut & splice)
## Khi nào dùng
- Thêm/xóa phần tử theo vị trí tham chiếu đã biết.
- Truy vấn phần tử kề trái/phải của một node.
- Bỏ qua phần tử đã xóa mà không dịch chuyển cả mảng.

## Độ phức tạp
- `insert_left`, `insert_right`, `erase`, `left_of`, `right_of`: `O(1)`.

## Khung thao tác cốt lõi
```cpp
// Xóa node i khỏi chuỗi hiện tại
void erase_node(int i) {
    int l = L[i], r = R[i];
    if (l) R[l] = r;
    if (r) L[r] = l;
    L[i] = R[i] = 0;
}
```

## Không phù hợp khi
- Cần truy vấn phần tử thứ `k` hiện tại.
- Cần sum/min/max theo đoạn.
- Cần sort/reorder toàn cục thường xuyên.

## Gợi ý thay thế
- Query đoạn: Fenwick/Segment Tree.
- Truy vấn thứ tự động mạnh: balanced BST/order statistic tree.
