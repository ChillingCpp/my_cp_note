# Binary Search on Array or Set

## 1) Điều kiện áp dụng
- Dữ liệu phải có thứ tự:
    - mảng đã sort theo giá trị, hoặc
    - cấu trúc ordered set/map (BST, tree-based container).
- Mục tiêu thường là tìm vị trí biên (`first/last`) thỏa điều kiện.

## 2) Khái niệm cốt lõi
- `lower_bound(x)`:
    - phần tử đầu tiên `>= x`
- `upper_bound(x)`:
    - phần tử đầu tiên `> x`
- Số lần xuất hiện của `x` trong mảng sort:
    - `upper_bound(x) - lower_bound(x)`

## 3) Mẫu tự cài đặt (first >= x)
```cpp
int first_geq(const vector<int>& a, int x) {
    int l = 0, r = (int)a.size() - 1, ans = (int)a.size();
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (a[m] >= x) ans = m, r = m - 1;
        else l = m + 1;
    }
    return ans; // = n nếu không có
}
```

## 4) Dùng STL nhanh
```cpp
auto it1 = lower_bound(a.begin(), a.end(), x);
auto it2 = upper_bound(a.begin(), a.end(), x);
int cnt = (int)(it2 - it1);
```

Với `set`/`multiset`:
```cpp
auto it = s.lower_bound(x); // iterator đầu tiên >= x
```

## 5) Bài toán điển hình
- Tìm vị trí chèn để vẫn giữ sort.
- Đếm phần tử trong đoạn giá trị `[L, R]`.
- Tìm phần tử gần nhất thỏa điều kiện trong ordered set.

## 6) Độ phức tạp
- Mảng + binary search: `O(log n)`.
- `set`/`multiset` lower_bound/upper_bound: `O(log n)`.

## 7) Lỗi hay gặp
- Dùng binary search trên dữ liệu chưa sort.
- Nhầm `lower_bound` và `upper_bound`.
- Tràn số khi tính `mid` (`l + (r - l)/2` là an toàn hơn).
- Không kiểm tra iterator `end()` trước khi dereference.
