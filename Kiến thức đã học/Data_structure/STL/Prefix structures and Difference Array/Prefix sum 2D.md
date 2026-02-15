# Prefix Sum 2D

## Build
```cpp
for (int i = 1; i <= n; ++i)
  for (int j = 1; j <= m; ++j)
    pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + a[i][j];
```

## Query hình chữ nhật `(x1,y1) -> (x2,y2)`
```cpp
sum = pref[x2][y2] - pref[x1-1][y2] - pref[x2][y1-1] + pref[x1-1][y1-1];
```
