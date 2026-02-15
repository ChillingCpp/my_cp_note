# Rolling Hash

## Mục tiêu
- So sánh substring nhanh bằng hash prefix.

## Công thức
- `H[i] = H[i-1] * base + s[i]`.
- `hash(l,r) = H[r] - H[l-1] * powBase[r-l+1]`.

## Lưu ý
- Có collision, nên dùng double hash.
