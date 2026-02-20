[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Data_Structures)

# Map cơ bản (`std::map`)

## Khi nào dùng
- Cần key có thứ tự và thao tác ổn định `O(log n)`.
- Muốn tránh rủi ro worst-case của `unordered_map` trong contest.
- Cần `lower_bound`, `upper_bound` theo key.

## Thao tác chính
- `mp[key]`, `mp.at(key)`.
- `insert`, `erase`, `find`, `count`.
- `lower_bound(key)`, `upper_bound(key)`.

## Độ phức tạp
- Thêm/xóa/tìm kiếm: `O(log n)`.

## Mẫu bài quan trọng
- Mảng tần số động với key lớn.
- Coordinate compression (gom key, đánh chỉ số).
- Đếm số lượng phần tử unique.
- Prefix operation có tính chất loại trừ theo key đã sắp.

## Lưu ý
- `map` không cho key trùng; cần trùng thì dùng `multimap` hoặc `map<key, int>`.
- Dùng `long long` cho key/value khi tổng lớn.
