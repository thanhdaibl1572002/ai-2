# Thuật toán Di truyền cho bài toán Người bán hàng (TSP)

Dự án này triển khai thuật toán **Di truyền (Genetic Algorithm - GA)** để giải bài toán **Người bán hàng (Traveling Salesman Problem - TSP)** bằng Python. Thuật toán sử dụng nhiều phương pháp lai ghép khác nhau để tạo ra các hành trình mới và tối ưu qua các thế hệ nhằm tìm ra hành trình ngắn nhất.

## Tính năng

- **Hỗ trợ nhiều phương pháp lai ghép**:
  - PMX (Partially Mapped Crossover - Lai ghép ánh xạ một phần)
  - CX (Cycle Crossover - Lai ghép chu trình)
  - OX (Order Crossover - Lai ghép theo thứ tự)
- Khởi tạo quần thể ban đầu ngẫu nhiên.
- Lựa chọn cha mẹ dựa trên **Phương pháp Vòng quay Roulette**.
- Đột biến để duy trì sự đa dạng di truyền.
- Dễ dàng tùy chỉnh các tham số như kích thước quần thể, số thế hệ,...

## Cách sử dụng

1. **Cài đặt Python**: 
   - Đảm bảo Python (phiên bản >= 3.7) đã được cài đặt trên máy tính.
   - Cài đặt các thư viện cần thiết nếu có yêu cầu (ví dụ: `numpy`).
2. **Chạy chương trình**:
   - Tải tệp mã nguồn `main.py` và chạy bằng lệnh:
     ```bash
     python main.py
     ```
3. **Chọn phương pháp lai ghép**:
   - Sửa biến `method` trong file `main.py` để thay đổi phương pháp lai ghép:
     ```python
     method = "pmx"  # Hoặc "cx", "ox"
     ```

## Ví dụ đầu ra

### Ma trận khoảng cách
```plaintext
[[ 0 72 51 64 79]
 [72  0  5 72 24]
 [51  5  0 82 74]
 [64 72 82  0 34]
 [79 24 74 34  0]]
```

## Hành trình tốt nhất

Sau **100 thế hệ** với kích thước quần thể là **10**:

```plaintext
Best route using PMX: [0, 2, 4, 1, 3]
Best distance: 203
```

## Cấu trúc chương trình

- **main.py**: Tệp chính chứa toàn bộ thuật toán di truyền và các hàm hỗ trợ.

### Hàm chính:

- `initialize_population`: Khởi tạo quần thể ban đầu.
- `calculate_fitness`: Tính toán độ thích nghi của từng cá thể.
- `select_parents`: Lựa chọn cha mẹ bằng vòng quay roulette.
- `pmx`, `cx`, `ox`: Các phương pháp lai ghép (crossover).
- `mutate`: Hàm đột biến.
- `genetic_algorithm`: Triển khai thuật toán di truyền.

## Tùy chỉnh

Bạn có thể thay đổi các tham số trong hàm `genetic_algorithm` để phù hợp với bài toán:

- **Kích thước quần thể**: Điều chỉnh tham số `population_size`.
- **Số thế hệ**: Điều chỉnh tham số `generations`.
- **Tỷ lệ đột biến**: Có thể thay đổi trong hàm `mutate`.

## Yêu cầu

- **Python**: Phiên bản >= 3.7
- **Thư viện Python**:
  - `random`
  - `numpy`

## Ghi chú

- Các phương pháp lai ghép PMX, CX, và OX đảm bảo tính hợp lệ của hành trình (không lặp lại thành phố).
- Nếu có lỗi trong quá trình thực thi, vui lòng kiểm tra:
  - **Ma trận khoảng cách** (`distance_matrix`) có hợp lệ không.
  - **Kích thước và giá trị đầu vào** của danh sách thành phố (`cities`).
