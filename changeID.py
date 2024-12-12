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

    # "telemetry.macMachineId": "15c57a0a03d1d48a6e2bdf5bb4f0dbebf5248d7dda7856299c811ea32ccb7cbc",
    # "telemetry.sqmId": "{D0D29866-7FFC-4A6B-BF5D-9DC8A6A2E3A0}",
    # "telemetry.machineId": "ebc9de64e435a280c15da39201877947b96170b940af1a00a3b572412ff141d9",
    # "telemetry.devDeviceId": "c069dc3a-39fe-4091-ad1d-5801341e449f",