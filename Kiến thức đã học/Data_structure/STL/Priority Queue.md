[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/monotonic_queue(deque).cpp)

# Priority Queue (`std::priority_queue`)

## Khi nào dùng
- Cần lấy phần tử tốt nhất hiện tại (max/min) nhiều lần.
- Mỗi bước cần `push` và lấy cực trị nhanh.
- Rất hay gặp trong greedy, Dijkstra, và tối ưu DP.

## Độ phức tạp
- `top`: `O(1)`.
- `push/pop`: `O(log n)`.

## Mẫu bài quan trọng
- Dijkstra (chọn node có dist nhỏ nhất).
- Merge `k` dãy đã sort.
- Chọn top-k phần tử.
- Sweep line với active events có ưu tiên.
- Greedy + Priority Queue

## Lưu ý
- Không hỗ trợ xóa phần tử bất kỳ hiệu quả như `set`.
- Nếu cần xóa "lười" (lazy deletion), dùng thêm map đếm số lần cần loại.
