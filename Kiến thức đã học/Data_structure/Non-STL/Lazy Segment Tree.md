# Lazy Segment Tree

## Bài toán mẫu trong template này
- Cập nhật cộng đoạn: cộng `x` cho mọi phần tử trong đoạn `[l, r]`.
- Truy vấn min đoạn: lấy `min` trên đoạn `[l, r]`.

## Ý tưởng
- `Segment Tree` lưu thông tin theo đoạn.
- `Lazy` lưu cập nhật chưa đẩy xuống con để không phải update từng phần tử.
- Khi truy vấn/cập nhật đi qua một node, nếu cần thì `push` lazy từ node đó xuống 2 con.

## Mapping theo code
- `Node`: dữ liệu node của segment tree.
  - `sum`: ở template này thực chất đang giữ **giá trị min** của đoạn.
  - `sz`: chưa dùng (có thể bỏ hoặc dùng cho các bài range sum).
- `Lazy`: dữ liệu lazy.
  - `val`: giá trị cần cộng dồn cho cả đoạn.
- `idn()`: phần tử trung tính của `Node`.
- `idl()`: phần tử trung tính của `Lazy`.
- `op(a, b)`: gộp 2 node con.
  - Đang là `min(a.sum, b.sum)`.
- `tf(a, b)`: áp lazy `b` vào node `a`.
  - Vì là cộng đoạn nên min đoạn tăng thêm `b.val`.
- `opl(a, b)`: gộp 2 lazy.
  - Cả hai đều là phép cộng nên cộng dồn `a.val + b.val`.

## Khung code (range add + range min)
```cpp
struct Node
{
    ll sum = 0, sz = 0;
};
struct Lazy
{
    ll val = 0;
};
Node idn()
{
    return Node();
}
Lazy idl()
{
    return Lazy();
}
Node op(Node a, Node b)
{
    return { min(a.sum, b.sum) };
}
Node tf(Node a, Lazy b)
{
    return { a.sum + b.val };
}
Lazy opl(Lazy a, Lazy b)
{
    return { a.val + b.val };
}
struct lazyseg
{
    int          n = 1, h = 0;
    vector<Node> st;
    vector<Lazy> lz;
    lazyseg(vector<Node>& a)
    {
        int n1 = a.size();
        while (n < n1)
            n <<= 1, h++;
        st.resize(2 * n);
        lz.resize(n);
        copy(a.begin(), a.end(), st.begin() + n);
        for (int i = n - 1; i > 0; --i)
            update(i);
    }
    Node query(int l, int r)
    {
        l += n, r += n + 1;
        push(l, r);
        Node n1;
        n1.sum = 1e18;
        for (; l < r; l >>= 1, r >>= 1)
        {
            if (l & 1)
                n1 = op(n1, st[l++]);
            if (r & 1)
                n1 = op(n1, st[--r]);
        }
        return n1;
    }
    void apply(int l, int r, Lazy la)
    {
        l += n, r += n + 1;
        push(l, r);
        int l1 = l, r1 = r;
        for (; l < r; l >>= 1, r >>= 1)
        {
            if (l & 1)
                apply_l(l++, la);
            if (r & 1)
                apply_l(--r, la);
        }
        update(l1, r1);
    }
    void apply_l(int p, Lazy l)
    {
        st[p] = tf(st[p], l);
        if (p < n)
            lz[p] = opl(lz[p], l);
    }
    void update(int p)
    {
        st[p] = op(st[p << 1], st[p << 1 | 1]);
    }
    void update(int l, int r)
    {
        for (int i = 1; i <= h; ++i)
        {
            if (((l >> i) << i) != l)
                update(l >> i);
            if (((r >> i) << i) != r)
                update((r - 1) >> i);
        }
    }
    void push(int p)
    {
        apply_l(p << 1, lz[p]);
        apply_l(p << 1 | 1, lz[p]);
        lz[p] = idl();
    }
    void push(int l, int r)
    {
        for (int i = h; i >= 1; --i)
        {
            if (((l >> i) << i) != l)
                push(l >> i);
            if (((r >> i) << i) != r)
                push((r - 1) >> i);
        }
    }
};
```

## Cách dùng nhanh
```cpp
int n; cin >> n;
vector<Node> a(n);
for (int i = 0; i < n; ++i) {
    ll x; cin >> x;
    a[i].sum = x;
}
lazyseg st(a);

// cong +v cho [l, r]
st.apply(l, r, Lazy{v});

// min tren [l, r]
ll ans = st.query(l, r).sum;
```

## Độ phức tạp
- Build: `O(n)`
- Mỗi lần update đoạn: `O(log n)`
- Mỗi lần query đoạn: `O(log n)`

## Lỗi hay gặp
- Quên `push(l, r)` trước query/update nên kết quả sai.
- Nhầm đoạn đóng/mở: code này dùng `[l, r]` (đóng cả hai đầu).
- Giá trị vô cực cho min (`1e18`) phải phù hợp kiểu `ll`.
- Dùng template này cho bài khác thì phải sửa đồng bộ `Node/Lazy/op/tf/opl`.
