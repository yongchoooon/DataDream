import torch

# GPU가 사용 가능한지 확인
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if device.type != "cuda":
    raise RuntimeError("CUDA가 가능한 GPU가 필요합니다.")

# 의미 없는 텐서 계산을 반복적으로 실행
def waste_gpu():
    print("GPU를 의미 없이 무한으로 사용 중...")
    size = 10000  # 텐서 크기
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)
    while True:
        # GPU를 사용하는 무의미한 계산
        c = torch.mm(a, b)
        c = c * torch.sin(c)

# 실행
if __name__ == "__main__":
    waste_gpu()
