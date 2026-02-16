# Trie

## 1) Mục tiêu
- Lưu tập chuỗi để query prefix nhanh.
- Hỗ trợ insert, search, startsWith theo độ dài chuỗi.

## 2) Ý tưởng
- Mỗi node biểu diễn một prefix.
- Cạnh theo ký tự kế tiếp.
- Node có cờ `end` nếu kết thúc một từ.

## 3) Mẫu cài đặt (alphabet a-z)
[[https://github.com/ChillingCpp/DSA_CP/blob/main/Data_Structures/trie.cpp]](Source code)

## 4) Độ phức tạp
- Insert/search/prefix: `O(|s|)`.
- Bộ nhớ: `O(tổng độ dài các chuỗi đã lưu)`.

## 5) Biến thể thường gặp
- Trie đếm tần suất prefix/word.
- Binary trie cho XOR tối ưu.
- Aho-Corasick: trie + failure links cho multi-pattern matching.

## 6) Khi nào dùng
- Nhiều truy vấn theo prefix.
- Dictionary word, autocomplete, filter từ cấm.
- Bài XOR max/min theo bit.

## 7) Lỗi hay gặp
- Không chuẩn hóa alphabet (hoa/thường/ký tự ngoài a-z).
- Lãng phí bộ nhớ khi alphabet lớn mà vẫn dùng mảng cố định.
- Quên phân biệt `findWord` và `startsWith`.
