"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "shipment_query",
        "description": "Tra cứu thông tin đơn hàng, mã vận đơn, trạng thái và vị trí lưu kho.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Mã đơn hàng cần tra cứu (ví dụ: 'ORD2026001')"
                }
            },
            "required": ["order_id"]
        }
    },
    {
        "name": "update_order_status",
        "description": "Cập nhật trạng thái xử lý của một đơn hàng.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Mã đơn hàng cần cập nhật (ví dụ: 'ORD2026001')"
                },
                "new_status": {
                    "type": "string",
                    "description": "Trạng thái mới của đơn hàng, ví dụ: 'Đang vận chuyển' hoặc 'Đã giao'"
                }
            },
            "required": ["order_id", "new_status"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "ORD2026001": {
        "tracking_code": "VN123456789",
        "order_status": "Đang vận chuyển",
        "warehouse": "Kho Hà Nội",
        "location": "Kệ A-12",
        "customer": "Nguyễn Văn An",
        "updated_at": "13/09/2026 09:30"
    },
    "ORD2026002": {
        "tracking_code": "VN987654321",
        "order_status": "Đang đóng gói",
        "warehouse": "Kho Hồ Chí Minh",
        "location": "Kệ C-05",
        "customer": "Trần Thị Bình",
        "updated_at": "13/09/2026 10:15"
    }
}

VALID_ORDER_STATUSES = {
    "Đã tạo",
    "Đang xử lý",
    "Đang đóng gói",
    "Đang vận chuyển",
    "Đã giao",
    "Đã hủy"
}


def execute_shipment_query(order_id: str) -> str:
    """Tra cứu thông tin đơn hàng theo mã đơn."""
    normalized_order_id = order_id.strip().upper()
    order = MOCK_DATABASE.get(normalized_order_id)
    if order:
        return json.dumps({
            "status": "SUCCESS",
            "order_id": normalized_order_id,
            "data": order
        }, ensure_ascii=False)
    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy đơn hàng có mã '{order_id}'"
    }, ensure_ascii=False)


def execute_update_order_status(order_id: str, new_status: str) -> str:
    """Cập nhật trạng thái đơn hàng trong cơ sở dữ liệu mô phỏng."""
    normalized_order_id = order_id.strip().upper()
    normalized_status = new_status.strip()
    order = MOCK_DATABASE.get(normalized_order_id)

    if not order:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy đơn hàng có mã '{order_id}'"
        }, ensure_ascii=False)

    if normalized_status not in VALID_ORDER_STATUSES:
        return json.dumps({
            "status": "INVALID_STATUS",
            "message": f"Trạng thái '{new_status}' không hợp lệ.",
            "valid_statuses": sorted(VALID_ORDER_STATUSES)
        }, ensure_ascii=False)

    order["order_status"] = normalized_status
    return json.dumps({
        "status": "SUCCESS",
        "order_id": normalized_order_id,
        "new_status": normalized_status,
        "message": f"Đã cập nhật đơn hàng {normalized_order_id} sang trạng thái '{normalized_status}'."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "shipment_query": execute_shipment_query,
    "update_order_status": execute_update_order_status
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
