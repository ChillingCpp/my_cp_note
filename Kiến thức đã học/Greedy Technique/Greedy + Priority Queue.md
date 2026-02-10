
## Các biến thể Greedy + Priority Queue

- **Greedy with rollback** :
	- chọn phương án hiện tại và loại bỏ các lựa chọn xấu trong quá khứ để thỏa mãn rằng buộc
- **Greedy with eligibility window** :
	- Chỉ các lựa chọn **đã đủ điều kiện** tại thời điểm hiện tại mới được đưa vào heap
	- Greedy **chỉ được phép chọn trong cửa sổ hợp lệ này**.
	- **Lazy greedy ( biến thể sử dụng eligibility window )** : 
		- Sử dụng eligibility window
		- Chỉ ra quyết định khi vi phạm rằng buộc; rằng buộc hợp lệ thì chưa lựa chọn vội
-  **Dominant-choice / Irrevocable Greedy** :
	- Có quan hệ **dominance tuyệt đối**: lựa chọn tốt nhất hiện tại **không bao giờ bị hối tiếc**, nên có thể chọn ngay và không rollback.
- **Two-Heap Greedy**
	- Dùng **hai heap** để duy trì cân bằng trạng thái; quyết định greedy dựa trên **so sánh giữa hai miền giá trị**.
	- **Two-Heap Greedy with rollback**
		- Một kỹ thuật greedy duy trì **hai tập động** (`include`, `exclude`) bằng heap
		- Mọi quyết định rollback không chỉ loại bỏ phần tử khỏi nghiệm, mà còn **cho phép exchange (hoán đổi) giữa hai tập** để duy trì một bất biến thứ tự toàn cục.