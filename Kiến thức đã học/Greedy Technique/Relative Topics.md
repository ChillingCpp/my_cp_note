[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/Greedy)



[[Binary search]]
[[Two Pointers]]
[[Prefix or suffix Arrays]]
[[Priority Queue]]


# Các dạng Greedy **khó nhận diện** & **lối tư duy đặc biệt** (tóm tắt)

> Mục tiêu: **nhìn ra greedy khi lựa chọn cục bộ _không hiển nhiên_** nhưng vẫn dẫn tới **global optimal** nhờ cấu trúc toán học / bất biến.

---
## 1. Greedy with Regret (Tham lam có hối tiếc)

**Ý tưởng**: Chọn cục bộ, _cho phép sửa sai quá khứ_ khi gặp lựa chọn tốt hơn.

- Công cụ đi kèm: **priority queue / multiset / sorting**
- Dấu hiệu:
    - Lựa chọn trước đó _có thể bị thay thế_
    - Có khái niệm "bỏ cái tệ nhất đã chọn"    
- Bản chất:
    - Duy trì tập nghiệm tốt nhất ở mỗi prefix    

> Thực chất là greedy **trên prefix tối ưu**, không commit sớm.
---
## 2. Greedy + Sorting by Key (Key Ordering Greedy)

**Ý tưởng**: Không greedy trực tiếp trên quyết định, mà greedy **sau khi sắp xếp theo một trục đúng**.

- Dấu hiệu:
    - Có nhiều tiêu chí, nhưng chỉ **1 tiêu chí đúng** để sort
    - Sort xong → greedy đơn giản
- Sai lầm phổ biến:
    - Sort theo tiêu chí “trông có vẻ hợp lý” 

> Nếu sort sai → greedy sập hoàn toàn.
---
## 3. Greedy trên Bất biến (Invariant-driven Greedy)

**Ý tưởng**: Không tối ưu giá trị, mà giữ **một bất biến** khiến nghiệm cuối là tối ưu:
- Dấu hiệu:
    - Không có hàm mục tiêu rõ ràng tại từng bước
    - Mỗi bước chỉ cần _không phá vỡ bất biến_
- Ví dụ:
    - Two pointers giữ window hợp lệ
    - Huffman coding (luôn ghép 2 nhỏ nhất)
> Greedy đúng vì **không có lựa chọn nào phá invariant mà tốt hơn**.

---

## 4. Exchange Argument Greedy

**Ý tưởng**: Chứng minh greedy bằng cách **hoán đổi** với nghiệm tối ưu bất kỳ.

- Dấu hiệu:
    - Bài toán cho phép tráo thứ tự phần tử
    - Có thể chứng minh: nếu nghiệm tối ưu khác greedy ở bước i → đổi được
- Ví dụ:
    - Interval scheduling
    - MST (Kruskal, Prim)
> Nếu đổi không làm tệ đi → greedy hợp lệ.
---
## 5. Greedy nhìn như DP nhưng không phải DP

**Ý tưởng**: Bài có vẻ là DP, nhưng state collapse → greedy.
- Dấu hiệu:
    - DP chỉ phụ thuộc **giá trị tốt nhất hiện tại**, không cần nhớ toàn bộ state
    - Transition mang tính đơn điệu
> DP bị "nén" thành greedy + DS.
---
## 6. Greedy + Monotonic Structure

**Ý tưởng**: Chỉ giữ các lựa chọn _không bị dominated_.
- Công cụ:
    - Monotonic stack / deque
- Dấu hiệu:
    - Khi một phần tử mới đến, loại bỏ hàng loạt phần tử cũ
> Greedy dựa trên quan hệ **domination**.
---
## 7. Greedy trên Prefix / Suffix tối ưu

**Ý tưởng**: Tại mọi prefix, nghiệm đang giữ là tốt nhất có thể.
- Dấu hiệu:
    - Bài xử lý theo thứ tự thời gian / index
    - Không cần nhìn tương lai sâu
- Ví dụ:
    - Max subsequence with constraints
    - Online scheduling
> Gần với greedy with regret, nhưng nhấn mạnh tính online.
---
## 8. Greedy nhờ Tính đơn điệu (Monotonicity Greedy)

**Ý tưởng**: Khi đã chọn A thay vì B, thì về sau **A luôn tốt hơn B**.

- Dấu hiệu:
    - Hàm lợi ích / chi phí đơn điệu theo thời gian
- Ví dụ:
    - Gas station
    - Jump game    
> Một khi bỏ B, không cần hối tiếc.

---
## Bản đồ tư duy nhanh

- ❓ Có cần sửa quyết định cũ? → **Greedy with Regret**
    
- ❓ Phải sort đúng trục trước? → **Key Ordering Greedy**
    
- ❓ Dựa trên invariant? → **Invariant Greedy**
    
- ❓ Chứng minh bằng hoán đổi? → **Exchange Argument**
    
- ❓ Nhìn như DP nhưng state nhỏ? → **DP → Greedy**
    
- ❓ Loại phần tử bị dominated? → **Monotonic Greedy**
    

---
### Kết luận thẳng thắn

> **Greedy khó không nằm ở code, mà ở việc phát hiện _cấu trúc cho phép greedy tồn tại_.**

Nếu bạn muốn: tôi có thể **map từng dạng này với bài CF/LC cụ thể** hoặc **chỉ ra dấu hiệu nhận diện khi đọc đề trong 30s**.
