[source code](https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/Graph/Topological_lexicographically_sort.cpp)


- Chỉ áp dụng cho đồ thị có hướng
- Dùng để kiểm tra cycle trong đồ thị có hướng
- Bản chất của Topological sort :
    - Mọi thứ tự topo hợp lệ nếu và chỉ nếu với mọi cạnh u -> v thì u đứng trước v
        - Nếu không tồn tại cạnh u -> v thì v có thể đứng trước u trong thứ tự topo
- 2 thuật toán cơ bản :
    - DFS
    - thuật toán Kahn
        - Một DAG có topo duy nhất khi và chỉ khi: ở mọi bước của Kahn, luôn chỉ có **duy nhất 1 node có indegree = 0**
- nếu như yêu cầu lexicographically order : 
    - sử dụng thuật toán Kahn nhưng thay vì dùng queue thì dùng min-heap0000
