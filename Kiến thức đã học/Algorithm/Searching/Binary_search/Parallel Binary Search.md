# Parallel Binary Search (Offline)

## 1) Bản chất
- Kỹ thuật offline để trả lời nhiều truy vấn dạng:
    - "thời điểm nhỏ nhất/lớn nhất mà query thỏa điều kiện".
- Mỗi query tự có một binary search, nhưng được xử lý **song song theo mid** để giảm chi phí.

## 2) Khi nào dùng
- Có `q` truy vấn, mỗi truy vấn cần tìm đáp án trong miền `[L, R]`.
- Có thể kiểm tra query tại một `mid` nếu biết trạng thái sau khi áp dụng `mid` update/sự kiện đầu tiên.
- Hàm kiểm tra theo `mid` là đơn điệu cho từng query.

## 3) Ý tưởng vận hành
1. Mỗi query giữ khoảng tìm kiếm `lo[i], hi[i]`.
2. Lặp cho tới khi mọi query hội tụ:
    - gom các query theo `mid = (lo+hi)/2` vào bucket.
    - reset DS (Fenwick/Segment Tree/DSU rollback...).
    - quét các mốc `t` từ trái sang phải, áp dụng update thứ `t`.
    - tại mỗi `t`, xử lý toàn bộ query có `mid = t` để quyết định đi trái/phải.
3. Kết quả là `lo[i]` (hoặc `hi[i]`) theo mẫu `first true` / `last true`.

## 4) Khung pseudo
```cpp
while (true) {
    bool any = false;
    buckets.clear();
    for (int i = 0; i < q; i++) {
        if (lo[i] < hi[i]) {
            any = true;
            int mid = (lo[i] + hi[i]) / 2;
            buckets[mid].push_back(i);
        }
    }
    if (!any) break;

    resetDS();
    for (int t = L; t <= R; t++) {
        apply_update(t);
        for (int id : buckets[t]) {
            if (check_query(id)) hi[id] = t;
            else lo[id] = t + 1;
        }
    }
}
```

## 5) Độ phức tạp
- Thường: `O((cost_apply_all + cost_check_all) * log Range)`.
- So với chạy riêng từng query, tiết kiệm lớn khi `q` nhiều.

## 6) Ứng dụng thường gặp
- Truy vấn "thời điểm đầu tiên đủ điều kiện".
- Bài dynamic connectivity/offline updates.
- Bài có update theo thời gian + điều kiện prefix.
