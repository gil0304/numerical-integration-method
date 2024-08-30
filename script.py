import numpy as np
from scipy.integrate import quad, simpson, trapezoid

# 被積分関数の定義
def f(x):
    return np.exp(-x**2) * np.cos(2 * np.pi * x)

# 積分区間
a, b = 0, 5

# 台形法
x = np.linspace(a, b, 100)
y = f(x)
trapz_result = trapezoid(y, x)

# シンプソン法
simps_result = simpson(y, x=x)

# ガウス求積法
quad_result, _ = quad(f, a, b)

# 結果の表示
print("台形法による積分値:", trapz_result)
print("シンプソン法による積分値:", simps_result)
print("ガウス求積法による積分値:", quad_result)

# 結果の差を計算
trapz_diff = abs(trapz_result - quad_result)
simps_diff = abs(simps_result - quad_result)

# 結果の差の表示
print("台形法とガウス求積法の結果の差:", trapz_diff)
print("シンプソン法とガウス求積法の結果の差:", simps_diff)
