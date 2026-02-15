
- chủ đề này sẽ hướng đến việc xây dựng MST từ đồ thị, sử dụng thuật toán trên cây để hỗ trợ các bài toán đặc biệt
## Cách build chung
- Sau khi build được cây thì ta sẽ xây dựng thuật toán cho truy vấn : 
    - Binary lifting
    - min/max cho dp sparse table
- tính chất : 
    - query(u, v) >= hoặc <= w(u, v)
- 1 vài bài có thể hỗ trợ :
    - tìm second span tree : 
        - best(combine($W_st$, subtract(w(u, v), query(u, v)))) với w(u, v) != query(u, v);
    - tìm simple cycle tối ưu trọng số : 
        - best(combine(w(u, v), query(u, v)))
    - kiểm tra 1 cạnh có thể có trong span tree :
        - query(u, v) == w(u, v)

## Forest


## Đường dẫn :
- [[Binary lifting và DP]]