# Prefix Min

## Định nghĩa
- `prefMin[i] = min(a[1..i])`.

## Build
```cpp
prefMin[1] = a[1];
for (int i = 2; i <= n; ++i) prefMin[i] = min(prefMin[i-1], a[i]);
```
