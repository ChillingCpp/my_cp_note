
# HỆ THỐNG CÂU HỎI GIẢI BÀI CP

---
## I. BÀI TOÁN THỰC SỰ LÀ GÌ? (Problem Clarification)

### 1. Câu hỏi cốt lõi

- Chính xác **đề đang hỏi điều gì**?
- Output cuối cùng là:
    - một giá trị?
    - một cấu hình?
    - một chuỗi thao tác?
- Có bao nhiêu output hợp lệ? hay chỉ một?
⚠️ Nếu **không thể phát biểu lại bài toán trong 1–2 câu**, bạn **chưa hiểu đề**.
---
### 2. Những gì được cho là gì?

- Dữ kiện:
    - Số lượng?
    - Kiểu dữ liệu? 
- Điều kiện:
    - Bắt buộc?
    - Có thể vi phạm không?
- Có dữ kiện nào **không ảnh hưởng tới output** không?
---

### 3. Điều kiện có nhất quán không?

- Có tồn tại nghiệm không?
- Có trường hợp **vô nghiệm** không?
- Đề có yêu cầu xử lý trường hợp đó không?

👉 Nhiều bài ad-hoc/constructive **chết** ở đây.

---
## II. MỐI QUAN HỆ GIỮA DỮ KIỆN & ẨN SỐ (Structure Discovery)

### 4. Ẩn số phụ thuộc vào dữ kiện theo cách nào?

- Trực tiếp?
- Gián tiếp qua trung gian?
- Phụ thuộc cục bộ hay toàn cục?
---

### 5. Điều gì _thực sự_ quyết định đáp án?

- Có dữ kiện nào **thay đổi nhưng output không đổi**?
- Có dữ kiện nào **chỉ dùng để đánh lạc hướng**?

> Câu hỏi này rất quan trọng với bài CF rating cao.
---

### 6. Có bất biến (invariant) không?

- Thứ gì **không đổi** sau các thao tác?
- Thứ gì chỉ tăng / giảm?
- Thứ gì bị chặn trên / dưới? Nghiệm, giá trị, điều kiện....?

⚠️ Tôi **không chắc chắn 100%**, nhưng theo kinh nghiệm CP,  
#### **70–80% bài khó có ít nhất 1 invariant**.

---
## III. BIẾN ĐỔI BÀI TOÁN (Reformulation)

### 7. Có thể phát biểu lại bài toán không?

- Bằng:
    - cách khác?
    - ngôn ngữ khác?
    - đại lượng khác?
    - đi ngược lại thứ tự của bài toán?
    - Biết trước kết quả thì có tìm được cấu hình/quá trình thỏa mãn?
Ví dụ:
- Tối ưu → kiểm tra tồn tại
- Đếm trực tiếp → đếm bù
- Điều kiện phức tạp → điều kiện tương đương
---

### 8. Nếu bỏ bớt điều kiện thì sao?

- Bỏ 1 điều kiện:
    - nghiệm có nhiều không?
    - cấu trúc có lộ ra không?
- Thêm điều kiện mạnh:
    - bài có trở nên tầm thường không?
---

### 9. Bài toán đặc biệt

- Trường hợp:
    - nhỏ nhất?
    - lớn nhất?
    - biên?
- Có hành vi khác thường ở biên không?
---
## IV. PHÂN RÃ & TÁI KẾT HỢP (Decomposition)

### 10. Có thể tách bài toán không?

- Theo:
    - phần tử?
    - đoạn?
    - bước?
- Các phần độc lập hay phụ thuộc?
---
### 11. Có thể giải từng phần không?

- Nếu biết kết quả của một phần:
    - phần còn lại có dễ không?
- Có thứ tự tự nhiên để xử lý không?
---
## V. KIỂM SOÁT GIẢ ĐỊNH (Assumption Control)

> Phần này **Polya không viết rõ**, nhưng CP thì **bắt buộc**.

### 12. Tôi đang ngầm giả định điều gì?

- Input có luôn hợp lệ không?
- Thứ tự có quan trọng không?
- Có trùng lặp không?

⚠️ Rất nhiều WA đến từ **giả định vô thức**.

---
### 13. Có phản ví dụ không?

- Với mỗi “ý tưởng”, tự hỏi:
    - có test phá không?
- Nếu không tìm được phản ví dụ:
    - lý do là gì?
---

## VI. CHỌN CÁCH GIẢI (Solution Commitment)

### 13.5. Chọn cách giải dựa trên phân tích đề bài [[Nhận diện thuật toán]]

### 14. Cách giải này dựa trên điều gì?

- Invariant?
- Quy luật?
- Lập luận logic?
- Tính đơn điệu?
---
### 15. Cách giải có bao phủ mọi trường hợp không?

- Trường hợp thường
- Trường hợp biên
- Trường hợp xấu nhất
---

## VII. NHÌN LẠI (Reflection)

### 16. Kết quả có hợp lý không?

- Có vượt giới hạn không?
- Có trường hợp cực đoan không tự nhiên không?
---
### 17. Bài này thuộc “họ” nào?

- Có thể gắn nhãn:
    - invariant-based
    - constructive
    - monotonicity
    - symmetry
- Có dùng lại tư duy này được không?
---