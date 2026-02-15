# Kĩ thuật Traceback

## Mục tiêu
- Truy vết lại lời giải từ trạng thái đích.

## Nguyên tắc
- Lưu `parent[next_state] = current_state` khi cập nhật tối ưu.
- Đi ngược parent để dựng đáp án.
