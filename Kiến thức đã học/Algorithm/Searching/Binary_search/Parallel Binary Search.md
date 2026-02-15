# Parallel Binary Search

## Mục tiêu
- Giải nhiều truy vấn binary search cùng lúc khi check có thể xử lý theo lô.

## Ý tưởng
- Mỗi query giữ `[lo, hi]`, gom theo `mid` từng vòng.
- Xử lý batch check theo timeline/sự kiện.

## Khi dùng
- Nhiều query độc lập, check(mid) cập nhật dần được.
