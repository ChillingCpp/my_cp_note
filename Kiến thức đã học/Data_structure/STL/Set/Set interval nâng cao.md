[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Data_Structures)

# Set interval nâng cao

## Ý tưởng
- Lưu các đoạn rời nhau dạng `[l, r]` (kèm trạng thái/giá trị) trong `set`.
- Khi update/query, tách đoạn tại biên (`split`), xử lý đoạn giữa, rồi merge nếu cần.

## Khi nên dùng
- Trạng thái đồng nhất trên từng đoạn liên tiếp.
- Cần split + merge động nhiều lần.
- Thứ tự miền chỉ số ổn định (thường là 1D).

## Độ phức tạp điển hình
- `split`: `O(log n)`.
- Một lần cập nhật chạm `k` đoạn: `O((k + 1) log n)`.
- tổng độp phức tạp cho các truy vấn thường là `O(n log n)`

## Mẫu bài
- Tô màu đoạn, gán trạng thái đoạn.
- Đếm số đoạn đang bật/tắt sau mỗi truy vấn.
- Quản lý tập interval active trong sweep line.

## Không nên dùng khi
- One-shot xử lý rồi bỏ (DSU next có thể nhanh và đơn giản hơn).
- Dữ liệu không gom được thành các đoạn đồng nhất.
- Cần query đoạn kiểu sum/min/max nặng (ưu tiên Segment Tree/Fenwick).

## Gợi ý mở rộng
- Kết hợp Segment Tree khi cần vừa quản lý interval vừa truy vấn giá trị số học phức tạp.
