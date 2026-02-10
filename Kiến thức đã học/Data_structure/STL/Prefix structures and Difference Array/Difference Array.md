

- Các dạng bài : thực hiện n operations, mỗi operations tăng giá trị khoảng $[L, R]$ lên 1 giá trị K nào đó ( range update )
- Kĩ thuật như sau :
	- ```
	  for (int i = 0; i < n; ++i){
		  int l, r, k;
		  cin >> l >> r >> k;
		  a[l] += k;
		  a[r+1] -= k;
	  }
	  partial_sum(a.begin(), a.end(), a.begin()); // prefix sum cuối cùng
	  ```