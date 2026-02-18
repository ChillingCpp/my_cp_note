# Divide and Conquer

[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/divide_and_conquer.cpp)

## 1) Khái niệm
- Chia bài toán lớn thành các bài toán con độc lập cùng dạng, giải đệ quy, rồi gộp kết quả.
- Mẫu chuẩn: `solve(A) = combine(solve(B1), solve(B2), ..., solve(Bk))`.

## 2) Điều kiện nhận biết
- Có thể tách bài toán thành nhiều phần nhỏ hơn mà vẫn giữ bản chất bài toán.
- Các bài toán con gần như độc lập (ít hoặc không phụ thuộc lẫn nhau).
- Có bước `combine` rõ ràng để ghép nghiệm con thành nghiệm lớn.

## 3) Ví dụ điển hình
- Merge Sort
- Count Inversion (qua merge)
- Binary Search (một dạng divide-and-conquer 1 nhánh)
- Closest Pair of Points
- FFT/Karatsuba (mức nâng cao)

## 4) Khung triển khai
1. Base case đủ nhỏ để trả lời trực tiếp.
2. Chia input thành các phần con.
3. Giải đệ quy từng phần.
4. Gộp kết quả bằng `combine`.

```cpp
Result solve(int l, int r) {
    if (l == r) return base(l);
    int m = (l + r) >> 1;
    auto L = solve(l, m);
    auto R = solve(m + 1, r);
    return combine(L, R);
}
```

## 5) Phân tích độ phức tạp
- Thường đưa về truy hồi: `T(n) = aT(n/b) + f(n)`.
- Dùng Master Theorem hoặc cây đệ quy.
- Ví dụ Merge Sort: `T(n)=2T(n/2)+O(n)=O(n log n)`.

## 6) Lưu ý quan trọng
- Tối ưu bộ nhớ ở bước combine (tránh copy thừa).
- Cẩn thận stack recursion khi `n` lớn.
- `combine` phải đúng bất biến, vì sai combine thường sai toàn bộ.

## 7) Lỗi hay gặp
- Thiếu/đặt sai base case.
- Chia đoạn sai lệch biên (`mid`, `[l,m]`, `[m+1,r]`).
- Gộp kết quả không bảo toàn thứ tự/tính chất cần thiết.

