
- dùng để tính tổng 1 hình chữ nhật giới hạn bởi (x1, y1) và (x2, y2)
- code mẫu xây dựng :
	- ```
	  for (int i = 1; i <= n; ++i)
		  for (int j = 1; j <= n; ++j)
			  pref[i][j] = pref[i][j-1] + pref[i-1][j] - pref[i-1][j-1] + a[i][j];
	  ```
- truy vấn khoảng (x1, y1), (x2, y2) :
	- ```
	  // condition : x1 <= x2, y1 <= y2
	  auto query = [&](int x1, int x2, int y1, int y2){
		  return pref[x1][y1] - pref[x2][y1-1] - pref[x1-1][y2] + pref[x1-1][y1-1];
	  }
	  ``` 
- Dạng nhận biết prefix sum 2d :
	- mảng 2 chiều
	- có 2 rằng buộc cần thiết cho tính toán tổng lượng thỏa mãn