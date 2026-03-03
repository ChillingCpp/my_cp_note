# Greedy + Priority Queue

[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/Greedy)

## Các kỹ thuật chính
- **Dominant-choice / Irrevocable Greedy**: Nếu lựa chọn tốt nhất hiện tại luôn an toàn toàn cục thì chốt ngay, không cần rollback.
- **Greedy with rollback**: Chọn phương án hiện tại rồi loại bỏ phần tử tệ nhất đã chọn khi vi phạm ràng buộc.
- **Greedy with eligibility window**: Chỉ đưa vào heap những lựa chọn đã "mở khóa" tại thời điểm hiện tại.
- **Lazy greedy**: Tạm chưa chốt quyết định, chỉ pop/chỉnh heap khi phát hiện vi phạm điều kiện.
- **Two-Heap Greedy**: Dùng hai heap để quản lý hai miền giá trị và cân bằng trạng thái theo bất biến, hoặc exchange giữa 2 heap để giữ nghiệm tối ưu hợp lệ.
- **Two-Heap Greedy with rollback**: Cho phép rollback và exchange

## Dấu hiệu nhận biết nên dùng heap trong greedy
- Cần truy cập nhanh phần tử nhỏ nhất/lớn nhất trong tập phương án động.
- Bài toán có luồng sự kiện theo thời gian/index và tập ứng viên thay đổi liên tục.
- Mỗi bước chỉ cần quyết định cục bộ nhưng phải duy trì một bất biến toàn cục.

## Mẫu khung tư duy
1. Sắp thứ tự xử lý (theo thời gian, deadline, vị trí, trọng số...).
2. Đưa các ứng viên hợp lệ vào `priority_queue`.
3. Chọn/loại bằng `top()` để giữ bất biến bài toán.
4. Trích đáp án từ tập còn lại trong heap.


