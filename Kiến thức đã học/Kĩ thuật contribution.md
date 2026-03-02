

## Tư tưởng
- Khi gặp các dạng toán yêu cầu tính giá trị gì đó với mọi cấu hình có thể, thay vì brute force thì có thể tính xem ta có thể tách cấu hình đó thành các phần cấu hình nhỏ hơn và dựa vào đó có thể tính bằng số lượng đóng góp
- giảm độ phức tạp từ O(n^2) -> O(n log n) hoặc O(n)
### Dạng bài
- trên mảng : sử dụng [monotonic stack](Data_structure/Stack.md)
- trên cây : sử dụng [DSU](<Data_structure/Non-STL/DSU và các ứng dụng/Value contribution trên cây.md>)
- trên bit : sử dụng [bit](Algorithm/bit_contribution.md)