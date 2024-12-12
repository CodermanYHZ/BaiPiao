import uuid

def update_machine_id():
    try:
        print(f"成功更新 macMachineId 为: {uuid.uuid4().hex}{uuid.uuid4().hex}")
        print(f"成功更新 sqmId 为: {str(uuid.uuid4()).upper()}")
        print(f"成功更新 machineId 为: {uuid.uuid4().hex}{uuid.uuid4().hex}")
        print(f"成功更新 devDeviceId 为: {uuid.uuid4()}")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    update_machine_id()
    input("\n按回车键退出...")
