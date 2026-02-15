# DP how to solve it (G.Polya)

## 1. Understand
- Unknown: cần tối ưu gì (max/min/count/exist).
- Data: input + constraints.
- Conditions: ràng buộc ảnh hưởng quyết định.

## 2. Devising a plan
- Biến đổi dữ liệu để nhìn ra cấu trúc (sort/compress/prefix/tree...).
- Tìm bài toán con và quyết định cần nhớ gì.
- Thông tin cần nhớ chính là state.

## 3. Carry out
- Định nghĩa state.
- Xây transition.
- Kiểm tra không trùng/không thiếu state.
- Nếu cycle dependency, đổi state.

## 4. Look back
- Giảm chiều state, rolling array, đổi hướng duyệt, tối ưu độ phức tạp.
