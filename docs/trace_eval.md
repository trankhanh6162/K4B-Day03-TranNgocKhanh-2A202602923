# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Trần Ngọc Khánh 
> **Mã Sinh Viên / Mã Học viên:** 2A202602923  
> **Chủ đề Lựa chọn:** Trợ lý Đơn hàng & Kho vận (Supply Chain Agent)

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Agent có thể phải tra cứu đơn hàng, đọc trạng thái và thực hiện cập nhật tiếp theo. |
| **2. Tool Interaction** | 5 / 5 | Bài toán cần dùng Tool tra cứu và Tool cập nhật dữ liệu đơn hàng qua MCP Server. |
| **3. Dynamic Decision** | 5 / 5 | Hành động cập nhật phụ thuộc vào trạng thái và vị trí nhận được từ bước tra cứu. |
| **4. Long Horizon Goal** | 4 / 5 | Agent cần giữ mục tiêu xử lý đơn hàng qua nhiều bước, dù phạm vi mô phỏng chưa có quy trình dài. |
| **TỔNG ĐIỂM AGENTIC FIT** | **19 / 20** | *Điểm số cao cho thấy Supply Chain Agent phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json`:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "shipment_query",
    "arguments": {
      "order_id": "ORD2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "order_id": "ORD2026001",
      "data": {
        "tracking_code": "VN123456789",
        "order_status": "Đang vận chuyển",
        "warehouse": "Kho Hà Nội",
        "location": "Kệ A-12"
      }
    },
    "latency_ms": 1672.05
  }
]
```

> **Trạng thái lần chạy hiện tại:** Bộ test đã chạy thành công bằng `OpenAIProvider`, không xuất hiện lỗi API hoặc fallback về Mock. Trace thể hiện đầy đủ luồng Supply Chain và ReAct nhiều bước.

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases trên OpenAI API.
- **Số lượt gọi Tool qua MCP Server chính xác:** 5 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
