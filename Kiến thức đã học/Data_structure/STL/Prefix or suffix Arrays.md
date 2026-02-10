

- Cấu trúc tổng thể :
	- ```
	  vector<ll> a(n+1), pref(n+1);
	  for (int i = 1; i <= n; ++i)
		  pref[i] = op(pref[i-1], a[i]);  
	  ```

[[Prefix sum 1D]]
[[Prefix sum 2D]]
[[Prefix min]]
[[Prefix max]]
[[Difference Array]]
