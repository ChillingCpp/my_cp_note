[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Dsu/Dsu.cpp)



# Kĩ thuật này có tư duy tương tự như DSU nhưng không phải là DSU
## Kĩ thuật này dùng để xử lí các truy vấn động trên mảng có các dạng : 
- thêm/ xóa phần tử
- thay đổi/hoán đổi vị trí phần tử
- in ra phần tử kề bên trái/bên phải của phần tử thứ i
- bỏ qua phần tử đã xóa
- có thể ứng dụng đối với mảng tròn ( circular array )
-  Duy trì nhiều dãy độc lập
	- Mỗi phần tử chỉ thuộc **1 dãy**
	- Có thể có nhiều hàng / nhiều chuỗi cùng tồn tại
	- 📌 Có thể dùng:
		- nhiều head
		- hoặc đánh dấu root
 - Cắt – nối đoạn (segment cut & splice)
	- Nếu biết **đầu và cuối đoạn**, ta có thể:
		- cắt cả đoạn
		- nối sang vị trí khác

## Những điều link vị trí KHÔNG làm được (cực kỳ cần nhớ)

Để tránh dùng sai cấu trúc:
❌ **Không truy cập theo thứ tự k**
- Không hỏi: “phần tử thứ k hiện tại là ai?”

❌ **Không query đoạn**
- Không sum / min / max trên đoạn
    
❌ **Không sort / reorder toàn cục**
📌 Nếu đề có những thứ này → **cần Fenwick / Segment Tree / BST**

## Code mẫu
```
#include <bits/stdc++.h>
using namespace std;

/*
====================================================
 POSITION LINKED STRUCTURE (ARRAY-BASED)
----------------------------------------------------
 Hỗ trợ:
 - Thêm / xóa phần tử
 - Đổi / hoán đổi vị trí
 - Truy vấn phần tử trái / phải
 - Bỏ qua phần tử đã xóa
 - Mảng thường / mảng tròn
 - Duy trì nhiều dãy độc lập
 - Cắt – nối đoạn (segment cut & splice)
====================================================
*/

static const int MAXN = 1'000'000 + 5;

int L[MAXN], R[MAXN];   // trái / phải
int root[MAXN];         // đại diện dãy
bool alive[MAXN];       // còn tồn tại hay không

bool circular = false;  // mảng circular

void init(int n) {
    for (int i = 1; i <= n; i++) {
        L[i] = R[i] = 0;
        root[i] = i;
        alive[i] = false;
    }
}
void make_single(int x) {
    L[x] = R[x] = 0;
    root[x] = x;
    alive[x] = true;
}

// Insert i to the LEFT of j
void insert_left(int i, int j) {
    int x = L[j];

    L[i] = x;
    R[i] = j;

    if (x) R[x] = i;
    L[j] = i;

    root[i] = root[j];
    alive[i] = true;
}

// Insert i to the RIGHT of j
void insert_right(int i, int j) {
    int x = R[j];

    R[i] = x;
    L[i] = j;

    if (x) L[x] = i;
    R[j] = i;

    root[i] = root[j];
    alive[i] = true;
}

void erase_node(int i) {
    if (!alive[i]) return;

    int x = L[i], y = R[i];

    if (x) R[x] = y;
    if (y) L[y] = x;

    L[i] = R[i] = 0;
    alive[i] = false;
}

int left_of(int i) {
    return (alive[i] ? L[i] : 0);
}

int right_of(int i) {
    return (alive[i] ? R[i] : 0);
}

void swap_pos(int a, int b) {
    if (!alive[a] || !alive[b] || a == b) return;

    int la = L[a], ra = R[a];
    int lb = L[b], rb = R[b];

    // detach a
    if (la) R[la] = ra;
    if (ra) L[ra] = la;

    // detach b
    if (lb) R[lb] = rb;
    if (rb) L[rb] = lb;

    // place b at a
    if (la) R[la] = b;
    if (ra) L[ra] = b;
    L[b] = la;
    R[b] = ra;

    // place a at b
    if (lb) R[lb] = a;
    if (rb) L[rb] = a;
    L[a] = lb;
    R[a] = rb;

    swap(root[a], root[b]);
}

void make_circular(int head, int tail) {
    R[tail] = head;
    L[head] = tail;
    circular = true;
}

// Cut segment [l ... r] from its sequence
void cut_segment(int l, int r) {
    int x = L[l], y = R[r];

    if (x) R[x] = y;
    if (y) L[y] = x;

    L[l] = R[r] = 0;
}

// Splice segment [l ... r] after node p
void splice_after(int p, int l, int r) {
    int x = R[p];

    R[p] = l;
    L[l] = p;

    R[r] = x;
    if (x) L[x] = r;

    int rt = root[p];
    for (int i = l; i; i = R[i]) {
        root[i] = rt;
        if (i == r) break;
    }
}

void print_chain(int head) {
    for (int i = head; i; i = R[i]) {
        cout << i << " ";
        if (circular && R[i] == head) break;
    }
    cout << "\n";
}
```
