[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/merge2set.cpp)

# Set cơ bản (`std::set` / `std::multiset`)

## Khi nào dùng
- Cần tập phần tử có thứ tự và truy vấn cực trị/lân cận nhanh.
- Cần thêm/xóa/tìm kiếm online trong `O(log n)`.
- Cần binary search động bằng `lower_bound`/`upper_bound`.

## Độ phức tạp
- Thêm/xóa/tìm kiếm: `O(log n)`.

## `set` vs `multiset`
- `set`: không trùng.
- `multiset`: cho phép trùng.

## Mẫu bài quan trọng
- Greedy cần lấy phần tử gần nhất thỏa điều kiện.
- Duy trì active values trong sweep line.
- Tối ưu online cần chèn/xóa liên tục.
