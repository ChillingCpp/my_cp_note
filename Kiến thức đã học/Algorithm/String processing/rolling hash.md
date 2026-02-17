# Rolling Hash

## 1) Mục tiêu
- So sánh nhanh hai đoạn con của chuỗi trong `O(1)` sau tiền xử lý.
- Dùng cho matching, palindrome check, binary search theo độ dài chuỗi con.

## 2) Ý tưởng
- Hash prefix: `H[i] = (H[i-1] * base + val(s[i])) mod M`.
- Hash đoạn `[l..r]`:
  - `hash(l,r) = H[r] - H[l-1] * powBase[r-l+1]`.

## 3) Mẫu cài đặt 2 mod
[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Algorithms/String/rolling_hash.cpp)

## 4) Collision
- Hash có xác suất trùng giả.

## 5) Độ phức tạp
- Build: `O(n)`
- Mỗi truy vấn hash đoạn: `O(log n)` do map

## 6) Khi nào dùng
- So sánh substring nhiều lần.
- Longest common substring/prefix với binary search + hash.
- Kiểm tra palindrome kết hợp hash thuận + hash ngược.
