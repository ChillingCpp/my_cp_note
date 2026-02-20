[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/monotonic_queue(deque).cpp)

# Deque (`std::deque<T>`)

## Khi nào dùng
- Cần thêm/xóa ở cả hai đầu trong `O(1)`.
- Cần duy trì cửa sổ trượt (sliding window).
- Cần cấu trúc cho `0-1 BFS`.

## Mẫu bài quan trọng
- Monotonic queue: giữ max/min trên cửa sổ trượt.
- Sliding window fixed size và variable size.
- DP cửa sổ: tối ưu trạng thái trong đoạn `i-k ... i-1`.
- `0-1 BFS`: cạnh trọng số `0` đẩy đầu, trọng số `1` đẩy cuối.

## Lưu ý
- Không truy cập ngẫu nhiên nhanh như `vector` trong mọi tình huống cache.
- Với monotonic queue, xác định rõ điều kiện pop (`<`, `<=`, `>`, `>=`) để tránh đếm trùng.
