
## 1. Understand the problem - hiểu vấn đề


### _What is the unknown? What are the data? What are the conditions?_

Trong DP, điều này tương đương:

- **Unknown** → giá trị cần tối ưu (max / min / count / exist)
- **Data** → input + constraints + đề bài
	- Có thể phát biểu lại đề bài để dễ hiểu hơn không
	- Có thể dự đoán độ phức tạp từ dữ liệu không 
- **Conditions** → ràng buộc ảnh hưởng đến quyết định
	- Hãy viết lại các điều kiện thành 1 danh sách
	- Phát biểu lại các điều kiện theo toán học
## 2. Devising a plan - lập kế hoạch

### _Liên hệ giữa dữ liệu và ấn số_ 

- Biến đổi dữ liệu đã có thành 1 hướng xác định để dễ tiếp cận
	- sort, map, compress, prefix, suffix, block, subsequence, tree....
- Tìm các tính chất đặc biệt của bài toán sau khi đã phát biểu lại đề bài
	- brute force
	- Dựa vào các định lý, dạng bài đã gặp
- Có thể chia nhỏ bài toán thành bài toán con không
	- Nếu ta giải được các bài toán con a, b, c,... Liệu các bài toán đó có đóng góp vào bài toán lớn hơn là A chứa các bài toán con a, b, c...
	- Nếu ta cố định 1 phần rằng buộc/dữ liệu/yêu cầu thì có thể tách bài toán thành các bài toán con không.
	- Tạo mối liên kết giữa rằng buộc, yêu cầu, dữ liệu, tính chất với các bài toán con
	
- Phân tích quá trình ra quyết định (RẤT QUAN TRỌNG)
    - Quyết định diễn ra ở đâu ?
	    - theo index?
	    - theo thời gian?
	    - theo số lượng đã chọn?

	- Mỗi quyết định ảnh hưởng **tương lai** như thế nào?
	- Để quyết định tiếp, **cần nhớ tối thiểu thông tin gì?**
    
👉 **Thông tin cần nhớ = mầm mống của state**

### _Nếu chưa có tiến triển_

-  Tìm một hướng khác dễ tiếp cận hơn
	- Suy nghĩ ngược lại
	- Tư duy theo 1 hướng khác
	- Nếu biết đáp án, thì có thể làm gì để suy ra điều đó không
-  Tim được các bài toán có liên quan, tương đồng, tổng quát, đặc biệt ? 
	 - Knapsack, LCS, LIS, LCIS, edit distance, matrix multiplication, palindrome subsequence/array
	 - 
	 -  Có thể lấy 1 phần trong đó để giải không, cần thêm ẩn phụ không
- Giải 1 phần bài toán 
	- Giải bài toán nếu không có rằng buộc A hoặc B hoặc C...
		- Quan sát sự thay đổi của bài toán
	
## 3. Carry out the plan

### Chú ý : đây có thể là vòng lặp

- Xác định hướng đi của bài toán :
	- Chiều thuận
	- Chiều ngược
	- Ưu tiên chiều thuận nếu cả 2 hướng có thể giải

- Cách 1 :
	- Định nghĩa state của DP dựa trên những điều trên
		- độ dài, tổng, số lượng, prefix, mex,....
	- Dựa trên các rằng buộc, yêu cầu để chuyển state A sang state B
		- rằng buộc, yêu cầu cho ta biết ở state A có thể thực hiện các bước nào để sang state B
		- Nếu ta cố định 1 phần rằng buộc/dữ liệu/yêu cầu, có thể chuyển state không
		- khi sang state B cần những dữ kiện gì ở state A	
			- phát biểu lại state
			- thêm/bớt dữ kiện
	- Lập công thức truy hồi khi đã xác định rõ ràng 3 điều trên
- Cách 2 :
	- Vẽ sơ đồ cây quyết định lựa chọn
		- đối với bài min/max/optimal : đáp án sẽ là nhánh tốt nhất trong sơ đồ cây đó
		- đối với bài valid/count... : đáp án sẽ bao gồm toàn bộ node con
	- Mỗi 1 node đại diện cho 1 tình huống cụ thể chứa thông tin gì đó,  thử xem node đó chuyển trạng thái cần những dữ liệu gì, rằng buộc gì, thử xem có tính chất đặc biệt gì của chuyển trạng thái. 
	- Xác định được những dữ liệu cần thiết cho chuyển trạng thái thì định nghĩa đầy đủ trạng thái và xác định rõ công thức chuyển trạng thái.
- Kiểm tra lại công thức
	- Chứng minh mỗi bước không trùng/thiếu state
	- Nếu định nghĩa trạng thái mà bị cycle dependency thì phải định nghĩa lại
### Nếu 1 trong 5 bước bị fail, quay về bước đầu tiên

## 4. Look back - nhìn lại bài toán

### _Can you derive the result differently? Can you improve it?_

Trong DP:

- State có dư không?
- Có thể giảm chiều?
- Có thể rolling array?
	- rolling array là kĩ thuật chỉ lưu trữ những state cần thiết cho bước tiếp theo, để tối ưu bộ nhớ
- Có thể đổi hướng duyệt?
- Có thể áp dụng phương pháp cho các dạng bài toán khác không?

➡️ Đây là lúc từ **DP 3D → 2D → 1D**, hoặc từ O(N²) → O(N log N)
