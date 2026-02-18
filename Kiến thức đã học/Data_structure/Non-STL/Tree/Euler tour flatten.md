# Euler Tour + Flatten Tree

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/GraphTree/3typesEulerTour.cpp)

## Mảng thường dùng
- `in[u]`: thời điểm vào node `u`.
- $out[u]$ : 
	- Euler tour loại 1 và 2 : thời điểm cuối cùng mà node u được process
	- Euler tour loại 3 : thời điểm mà node cuối cùng của cây con gốc u 
- `depth[u]`: độ sâu.
- `flat[t]`: node/giá trị tại thời điểm `t`.

## 3 biến thể Euler tour
### 1. Euler đầy đủ `2n-1`
- Dùng cho RMQ/LCA theo chuỗi Euler depth.

### 2. Euler `2n` (mỗi node xuất hiện 2 lần)
- [[Mo]]`
- Query path `u-v` được đổi về đoạn trên mảng Euler + xử lý riêng LCA.
- cách xử lí truy vấn : 
	- gặp lần 1 : on
	- gặp lần 2 : off

### 3. Euler `n` (mỗi node 1 lần)
- Subtree `u` thành đoạn liên tiếp `[in[u], out[u]]`.
- Rất hợp cho subtree query/update bằng Fenwick/Segment Tree.

## Ứng dụng
- Subtree sum/min/max.
- Path root -> u bằng kỹ thuật prefix/difference trên mảng flatten.

## Lưu ý
- Chốt rõ loại Euler trước khi viết công thức `in/out`.
- Với path query bất kỳ `u-v`, thường cần LCA + tách đoạn đúng cách.

