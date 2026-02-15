# Prefix Max

## Định nghĩa
- `prefMax[i] = max(a[1..i])`.

## Build
```cpp
prefMax[1] = a[1];
for (int i = 2; i <= n; ++i) prefMax[i] = max(prefMax[i-1], a[i]);
```
