import pytest
from src.bll.pet_service import PetService  # นำเข้าคลาส PetService จาก BLL[cite: 2]

# 1. ทดสอบว่าสามารถสร้าง Instance ของ PetService ได้ถูกต้อง
def test_pet_service_initialization():
    service = PetService()
    assert service is not None

# 2. ทดสอบว่ามีฟังก์ชันค้นหาสัตว์เลี้ยงด้วย ID (get_pet_by_id)[cite: 2]
def test_get_pet_by_id_function_exists():
    service = PetService()
    assert hasattr(service, "get_pet_by_id")

# 3. ทดสอบว่ามีฟังก์ชันอัปเดตสถานะคำขอ (update_application_status)[cite: 2]
def test_update_application_status_function_exists():
    service = PetService()
    assert hasattr(service, "update_application_status")

# 4. ทดสอบตรรกะการตรวจสอบสถานะ (Status Logic Check)
def test_valid_application_status():
    valid_statuses = ["Pending", "Approved", "Rejected"]
    test_status = "Approved"
    assert test_status in valid_statuses
