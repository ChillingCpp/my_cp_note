

- code mẫu dùng hàm có sẵn
	- ```
	  vector<ll> a(n+1), pref(n+1);
	  std::partial_sum(a.begin(), a.end(), pref.begin());  
	  ```
- code mẫu implement
	- ```
	  vector<ll> a(n+1), pref(n+1);
	  for (int i = 1; i <=n; ++i)
		   pref[i]= pref[i-1] + a[i];
	  ```

- prefix sum dạng alternating  $a[i] + a[i+1] - a[i+2] + a[i+3]... \ hoặc \ a[i] - a[i+1] + a[i+2] - a[i-3]...$
	- ```
	  vector<ll> a(n+1), pref(n+1);
	  for (int i = 1; i <=n; ++i)
		   pref[i] = pref[i-1] + (i % 2 == 1 ? a[i] : -a[i]);
	  ```
- tính chất
	- Prefix sum dạng bình thường  $$ \sum_{i = l}^{r} a[i] = pref[r] - pref[l-1]$$
	- Prefix sum dạng alternating $$ \sum_{i = l}^{r} a[i] = 
	  \begin{cases}
		pref[r] - pref[l-1], & if & (r-l+1) \mod 2 == 0 \\\\
		pref[l-1] - pref[r], & if & (r-l+1) \mod 2 == 1
	 \end{cases}
	 $$
- Dấu hiệu nhận biết:
	- dạng bài phải có tính chất subarray
	- dạng bài static range sum query không có point update
	- dạng bài range update add/subtract : $a[l] \ += val, a[r+1] \ -= val$
	- dạng bài kết hợp với map
		- dạng bài liên quan tới subarray sum/sum modulo
		- dạng bài khi các operation  sau khi thực hiện thì mảng không bị đứt thành các đoạn rời và vẫn còn tính chất subarray
	- prefix sum dạng alternating  $a[i] + a[i+1] - a[i+2] + a[i+3]... \ hoặc \ a[i] - a[i+1] + a[i+2] - a[i-3]...$
	- prefix sum với mảng tần số nhỏ ( nfreq <= 100 )
	- Kadane maximum subarray sum.
	- Cyclic Prefix sum
- Có thể kết hợp cùng với các kĩ thuật khác 