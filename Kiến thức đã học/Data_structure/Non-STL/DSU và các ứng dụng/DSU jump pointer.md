# DSU Jump Pointer (Next Pointer)

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dsu/Dsu.cpp)

## Mục tiêu
- Bỏ qua nhanh các phần tử đã xử lý theo thứ tự tuyến tính.

## Chỉ dùng khi đủ 3 điều kiện
1. Có thứ tự tuyến tính cố định (total order).
2. Mỗi phần tử chỉ bị xử lý đúng 1 lần (one-shot).
3. Không có rollback/undo.

## Không phù hợp nếu
- Phần tử có thể active lại.
- Có rollback/split-merge.
- Trạng thái không đơn điệu.
- Không xác định được `next` duy nhất.

## Mẫu bài điển hình
- Xóa/chọn phần tử 1 lần trên mảng 1D.
- Euler tour loại 3 + xử lý one-shot trên tree.
- DAG topo-order + one-shot.

## Bảng áp dụng nhanh
| Cấu trúc | Dùng được không | Ghi chú |
|---|---|---|
| Mảng 1D | Có | Dễ nhất |
| Tree | Có | Thường ép về dãy Euler |
| DAG | Có | Theo topo + one-shot |
| Graph tổng quát | Có điều kiện | Chỉ khi node không quay lại |
| Mảng 2D | Có điều kiện | Ép 2D -> 1D, đảm bảo đơn điệu |

## Liên kết
- [Neighbor-linked array ~ DSU](<../../STL/Neighbor-linked array ~ DSU.md>)

