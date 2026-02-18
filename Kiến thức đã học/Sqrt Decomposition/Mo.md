# Mo's Algorithm

## Tư tưởng
- Mo là kỹ thuật xử lý truy vấn đoạn `query(l, r)` theo kiểu offline.
- Không trả lời theo thứ tự input, mà sort truy vấn để cửa sổ hiện tại `[curL, curR]` di chuyển ít nhất.
- Duy trì cấu trúc trạng thái cho cửa sổ hiện tại bằng 3 thao tác:
    - `add(pos)`
    - `remove(pos)`
    - `get_answer()`

## Khi nào dùng
- Chỉ có query, không có update online theo thời gian.
- Đáp án query có thể cập nhật gia tăng khi thêm/bớt 1 phần tử.
- Cần xử lý nhiều query trên cùng mảng.

## Ý tưởng chia block
- Thay vì sort theo block `sqrt(n)` truyền thống, gán mỗi query một khóa Hilbert:
    - `ord = hilbertOrder(l, r, pow, 0)`.
- Sort tăng dần theo `ord`.
- Mục tiêu: giảm quãng đường di chuyển tổng của `[curL, curR]` thực tế, thường nhanh hơn trên data lớn.

## Hilbert order
(https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/sqrt_decomposition/MO_algorithm/hilbert_order.cpp)[Source code]

## Độ phức tạp
- Sort query: `O(q log q)`.
- Lý thuyết thường vẫn phân tích gần `O((n + q) * sqrt(n))` cho Mo.
- Hilbert order chủ yếu tối ưu hằng số nhờ locality tốt hơn.

## Mẹo tối ưu
- Nén giá trị (`coordinate compression`) nếu miền giá trị lớn.
- Dùng mảng tĩnh thay `unordered_map` nếu có thể.
- Hilbert thường thắng block sort khi `q` lớn hoặc test random mạnh.
- Với `n` nhỏ, block sort thường đủ và code ngắn hơn.

## Lỗi hay gặp
- Nhầm `0-index` và `1-index` khi đọc query.
- Sai thứ tự update con trỏ trước/sau gọi `add/remove`.
- Quên lưu `id` để trả đáp án theo thứ tự ban đầu.
- Hàm `remove` làm vỡ invariant (đặc biệt bài distinct/frequency).

## Biến thể
- Mo with modifications (có update thời gian): thêm chiều `t`.
- Mo on tree: kết hợp Euler Tour để đưa về đoạn mảng.

## Đường dẫn
- [[Tư tưởng]]
- [[Harmonic Number]]
- [[Euler tour flatten]]
