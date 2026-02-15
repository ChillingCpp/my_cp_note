# Sweep Line

## Mục tiêu
- Biến bài toán thành danh sách sự kiện theo trục thời gian/toạ độ rồi quét tuần tự.

## Khi dùng
- Có thể mô hình bằng event `add/remove/query`.
- Cần biết tập active tại mỗi thời điểm.

## Khung chuẩn
1. Tạo event.
2. Sort theo key và tie-break.
3. Duyệt từ trái sang phải, cập nhật cấu trúc active.
4. Trả lời query tại thời điểm tương ứng.

## Cấu trúc hay đi kèm
- `set/multiset`, Fenwick, Segment Tree, Priority Queue.
