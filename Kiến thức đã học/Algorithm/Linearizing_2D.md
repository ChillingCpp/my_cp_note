# Linearizing 2D matrix -> 1D

## 1) Ý tưởng tổng quát
- Đây là kỹ thuật **linearizing matrix**: nén một lát cắt 2D thành mảng 1D để dùng thuật toán 1D.
- Chọn một chiều để cố định 2 biên (ví dụ `top/bottom` theo hàng).
- Duy trì mảng nén `compressed[]` trên chiều còn lại:
    - `compressed[c] = g(a[top..bottom][c])`
    - `g` thường là phép cộng, nhưng có thể là phép gộp khác tùy bài.
- Sau khi nén, bài toán còn lại là một bài 1D trên `compressed[]`.
- Lặp mọi cặp biên và lấy kết quả tốt nhất toàn cục.

## 2) Khung áp dụng
1. Chọn chiều có kích thước nhỏ hơn làm chiều cố định biên.
2. Duyệt biên 1 (`L1`).
3. Reset `compressed[]`.
4. Duyệt biên 2 (`L2 >= L1`):
    - Cập nhật `compressed[]` bằng cách "thêm" lớp mới vào lát cắt.
    - Chạy thuật toán 1D phù hợp trên `compressed[]`.
    - Cập nhật đáp án.

## 3) Độ phức tạp tổng quát
- Gọi `K = min(n, m)`, `L = max(n, m)`.
- Nếu thuật toán 1D trên mảng dài `L` có độ phức tạp `F(L)`, thì:
    - Tổng: `O(K^2 * F(L))`
    - Bộ nhớ phụ: `O(L)`

## 4) Ví dụ điển hình
- **Maximum Sum Submatrix**:
    - `g = sum`
    - Thuật toán 1D: Kadane
    - Độ phức tạp: `O(K^2 * L)`
- **Đếm số submatrix có tổng = k**:
    - `g = sum`
    - Thuật toán 1D: đếm subarray sum = `k` bằng prefix sum + hash map
    - Độ phức tạp: `O(K^2 * L)`

## 5) Case cụ thể: Kadane 2D (fixed top-bottom)
- Cố định `top/bottom`, nén từng cột thành `colSum[]`.
- Chạy Kadane trái -> phải trên `colSum[]`.
- Lưu ý xử lý đúng trường hợp toàn số âm khi viết Kadane.

## 6) C++ khung cơ bản (Kadane 2D)
```cpp
#include <bits/stdc++.h>
using namespace std;

struct KadaneResult {
    long long sum;
    int l, r;
};

KadaneResult kadane1D(const vector<long long>& a) {
    long long best = a[0], cur = a[0];
    int bestL = 0, bestR = 0, start = 0;

    for (int i = 1; i < (int)a.size(); i++) {
        if (cur < 0) {
            cur = a[i];
            start = i;
        } else {
            cur += a[i];
        }

        if (cur > best) {
            best = cur;
            bestL = start;
            bestR = i;
        }
    }
    return {best, bestL, bestR};
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cin >> a[i][j];
    }

    long long ans = LLONG_MIN;
    int topAns = 0, bottomAns = 0, leftAns = 0, rightAns = 0;

    vector<long long> colSum(m, 0);
    for (int top = 0; top < n; top++) {
        fill(colSum.begin(), colSum.end(), 0);

        for (int bottom = top; bottom < n; bottom++) {
            for (int c = 0; c < m; c++) colSum[c] += a[bottom][c];

            auto cur = kadane1D(colSum);
            if (cur.sum > ans) {
                ans = cur.sum;
                topAns = top;
                bottomAns = bottom;
                leftAns = cur.l;
                rightAns = cur.r;
            }
        }
    }

    cout << ans << "\n";
    // Rectangle: [topAns..bottomAns] x [leftAns..rightAns]
    return 0;
}
```
