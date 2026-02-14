# DSU Problemset

## Gợi ý lộ trình
1. DSU cơ bản (`merge/same`).
2. DSU có kích thước/tổng thành phần.
3. DSU có ràng buộc (parity/weighted/xor).
4. DSU offline (rollback, dynamic connectivity).
5. DSU trong MST/Kruskal và bài đồ thị nâng cao.

## Nguồn bài luyện
- http://www.spoj.com/problems/ADABRANC/
- https://www.spoj.com/problems/CONSEC/
- https://codeforces.com/gym/102006/problem/C
- http://codeforces.com/gym/101962/problem/J
- http://codeforces.com/contest/915/problem/F
- http://codeforces.com/contest/141/problem/E
- 7903 — Pandaria
- http://codeforces.com/contest/110/problem/E
- http://codeforces.com/contest/90/problem/E
- http://codeforces.com/contest/87/problem/D
- http://codeforces.com/contest/884/problem/E
- http://codeforces.com/contest/60/problem/D
- UVA 10947
- UVA 12363
- LA 3833
- http://codeforces.com/problemset/problem/742/D
- UVA 10178
- http://codeforces.com/contest/723/problem/F
- UVA 13153
- UVA 13169
- UVA 11987
- UVA 11474
- http://www.spoj.com/problems/BTCODE_G/
- http://codeforces.com/problemset/problem/691/D
- Gym 101174K
- UVA 10583
- LightOJ 1003
- http://codeforces.com/problemset/problem/731/C
- UVA 793
- UVA 11966
- https://www.codechef.com/problems/COZIC
- 3939
- UVA 11503
- http://codeforces.com/problemset/problem/755/C
- UVA 1395
- http://codeforces.com/contest/687/problem/D
- http://codeforces.com/contest/680/problem/E
- http://codeforces.com/contest/766/problem/D
- http://www.spoj.com/problems/LEXSTR/
- http://codeforces.com/contest/805/problem/C
- http://www.spoj.com/problems/IITKWPCI/
- http://www.spoj.com/problems/FRNDCIRC
- http://www.spoj.com/problems/FOXLINGS/
- http://www.spoj.com/problems/NITTROAD/
- http://www.spoj.com/problems/SHAHBG/
- http://codeforces.com/contest/598/problem/D
- http://codeforces.com/contest/9/problem/E
- http://codeforces.com/contest/25/problem/D
- http://codeforces.com/contest/28/problem/B
- http://codeforces.com/contest/876/problem/D
- http://codeforces.com/contest/875/problem/F


## Entry Level: 
- Kattis - unionfind * (basic UFDS; similar to UVa 00793) 2.
- UVa 01197 - The Suspects * (LA 2817 - Kaohsiung03; CCs) 3.
- UVa 01329 - Corporative Network * (LA 3027 - SouthEasternEurope04; interesting UFDS variant; modify the union and find routine) 4. 
- UVa 10685 - Nature * (find the set with the largest item) 5. 
- Kattis - control * (LA 7480 - Singapore15; simulation of UFDS; size of set; number of disjoint sets) 6. 
- Kattis - ladice * (size of set; decrement one per usage) 7. 
- Kattis - almostunionfind * (new operation: move; idea: do not destroy the parent array structure; also available at UVa 11987 - Almost Union-Find) 
- Extra UVa: 00793, 10158, 10507, 10583, 10608, 11690. 
- Extra Kattis: chatter, forests, more10, swaptosort, tildes, virtualfriends.


## Ghi chú
- Truy vấn có thể là strictly online hoặc offline.
- Nếu đề cho phép gom truy vấn xử lý sau, luôn nghĩ tới offline + DSU rollback.
