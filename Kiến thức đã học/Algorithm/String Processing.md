[source code](https://github.com/ChillingCpp/DSA_CP/tree/main/Algorithms/String)

## Tính chất ứng dụng giải bài

- `Exact pattern matching` một pattern: ưu tiên [[KMP]] hoặc [[Z algorithm]].
- So sánh substring nhiều lần / LCP nhanh: ưu tiên [[rolling hash]].
- Palindrome substring: ưu tiên [[Manacher]]; nếu nhiều query palindrome thì dùng hash thuận-ngược.
- Prefix dictionary/autocomplete/XOR theo bit: ưu tiên [[Trie]].
- Nhận diện nhanh keyword: `pattern`, `prefix-suffix`, `border`, `periodic`, `palindrome`, `dictionary`, `substring compare`.

## Đường dẫn
