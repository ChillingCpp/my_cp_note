
# Sqrt chia case (Heavy-Light theo mức độ ảnh hưởng)

## Tư tưởng
- Không chia theo chỉ số mảng, mà chia theo `object`.
- Mỗi `object` có một độ ảnh hưởng `impact(object)`:
    - số lần xuất hiện,
    - số đỉnh kề (degree),
    - số phần tử bị tác động khi object thay đổi.
- Chọn ngưỡng  `B ~ sqrt(N)` để tối ưu:
- Chia thành 2 nhóm
    - 1 nhóm brute force, 1 nhóm thuật toán tốt:  
    - `light`: `impact < B`
    - `heavy`: `impact >= B`

## Quy trình áp dụng
1. Xác định `object` và định nghĩa đúng `impact(object)`.
2. Chọn ngưỡng `B` (thường `sqrt(N)` hoặc tinh chỉnh theo `Q`).
3. Gán nhãn heavy/light cho từng object.
4. Thiết kế dữ liệu phụ cho heavy để query/update nhanh.
5. Khi xử lý thao tác, luôn tách 2 case heavy/light.


## Các mẫu bài hay gặp
- Chia theo tần suất giá trị:
    - Object là giá trị `x`.
    - `impact(x)` là `freq[x]`.
    - Heavy value giữ sẵn đáp án/cấu trúc phụ, light value duyệt list vị trí.
- Chia theo bậc đỉnh trong graph:
    - Object là đỉnh `u`.
    - `impact(u)` là `deg(u)`.
    - Heavy node giữ tổng đóng góp từ neighbors; light node duyệt adjacency list.
- Chia theo kích thước tập con:
    - Object là một set/list.
    - `impact(i)` là size(set_i/list_i)
    - Heavy set tiền xử lý intersection hoặc contribution.
    - lazy update 1 set : lazy chỉ là 1 phần tử thay vì nguyên set
        - giá trị thực của set k là : $lazy[heavy] * intersect[h][k]$

## Nhận diện nhanh
- Có 1 loại object mà “động vào nó” gây ảnh hưởng không đều.
- Có object rất nhỏ và object rất lớn.
- Nếu brute force theo object lớn thì TLE, nhưng số object lớn lại ít.
- Có thể chấp nhận tiền xử lý/caching cho nhóm lớn.

## Độ phức tạp thường thấy
- Tiền xử lý: từ `O(N)` đến `O(N * sqrt(N))` tùy bài.
- Mỗi query/update: thường quanh `O(sqrt(N))` sau khi cân bằng ngưỡng.

