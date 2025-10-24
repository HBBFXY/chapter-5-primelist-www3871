def PrimeList(N):
    if N <= 2:
        return ""
    primes = []
    # 遍历2到N-1的所有数
    for num in range(2, N):
        is_prime = True
        # 判断num是否为质数，只需检查到num的平方根即可
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 以空格分隔输出
    return " ".join(primes)

# 测试示例
n = int(input("请输入整数N："))
print(PrimeList(n))