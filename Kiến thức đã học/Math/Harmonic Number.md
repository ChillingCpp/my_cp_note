

- Harmonic Number is a set of algorithms run in
$$\sum_{i=1}^{n} \frac{1}{i} \approx O(n \log n)$$
- We can prove this using integral formula

- C++ codes :
	- ```
	  for (int i = 1; i <= n; ++i)
            for (int j = i; j <= n; j += i)
	   ```
- When to use it :
	- Dealing with Dynamic programming subproblems involves divisibility or multiplication
	- Prime sieve and Number theory technique
	- Problems that require calculate f(n) using f(2n), f(3n), f(4n),.... and vice versa
	- The algorithm using this technique must not overcount subproblems neither miss count
