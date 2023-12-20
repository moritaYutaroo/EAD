import subprocess

def get_connected_devices():
    try:
        # ルーターなどから接続デバイスの情報を取得
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        # 接続デバイスの情報を表示
        for line in output_lines:
            print(line)

    except Exception as e:
        print(f"Error: {e}")

# ネットワーク内の接続デバイスを取得
get_connected_devices()