# Bridge Tree

## Mục tiêu
- Co mỗi 2-edge-connected component thành 1 node.
- Mỗi bridge trở thành cạnh giữa 2 component.

## Cách dựng
1. Tìm bridge bằng low-link.
2. Bỏ bridge, flood-fill component còn lại.
3. Dựng cây trên các component.
