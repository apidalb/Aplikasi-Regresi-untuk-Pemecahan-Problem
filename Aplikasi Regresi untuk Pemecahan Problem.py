# Data diambil secara manual dari file CSV
data = [
    [1, 10],
    [2, 12],
    [3, 15],
    [4, 20],
    [5, 22],
    [6, 24],
    [7, 25],
    [8, 28],
    [9, 30],
    [10, 35]
]

# Pisahkan kolom menjadi dua daftar: X dan y
X = [row[0] for row in data]
y = [row[1] for row in data]

# Fungsi untuk menghitung regresi linear
def linear_regression(X, y):
    n = len(X)
    sum_x = sum(X)
    sum_y = sum(y)
    sum_x_squared = sum(x**2 for x in X)
    sum_xy = sum(X[i] * y[i] for i in range(n))
    
    b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b0 = (sum_y - b1 * sum_x) / n
    
    y_pred = [b0 + b1 * x for x in X]
    return y_pred, b0, b1

# Fungsi untuk menghitung eksponensial secara manual
def exponential_regression(X, y):
    # Logarithmic transformation of y values
    log_y = [log(yi) for yi in y]
    
    n = len(X)
    sum_x = sum(X)
    sum_log_y = sum(log_y)
    sum_x_squared = sum(x**2 for x in X)
    sum_x_log_y = sum(X[i] * log_y[i] for i in range(n))
    
    b1 = (n * sum_x_log_y - sum_x * sum_log_y) / (n * sum_x_squared - sum_x**2)
    log_b0 = (sum_log_y - b1 * sum_x) / n
    b0 = exp(log_b0)
    
    y_pred = [b0 * exp(b1 * x) for x in X]
    return y_pred, b0, b1

# Fungsi untuk menghitung log tanpa pustaka math
def log(x, base=2.718281828459045):
    result = 0
    current = x
    while current > 1:
        current /= base
        result += 1
    return result

# Fungsi untuk menghitung eksponen tanpa pustaka math
def exp(x):
    n = 10  # Precision level
    result = 1
    term = 1
    for i in range(1, n+1):
        term *= x / i
        result += term
    return result

# Fungsi untuk menghitung RMS secara manual
def calculate_rms(y_true, y_pred):
    n = len(y_true)
    mse = sum((y_true[i] - y_pred[i]) ** 2 for i in range(n)) / n
    rms = mse ** 0.5
    return rms

# Fungsi untuk membuat plot ASCII sederhana
def plot_data(X, y, y_pred_linear, y_pred_exp):
    max_y = max(max(y), max(y_pred_linear), max(y_pred_exp))
    min_y = min(min(y), min(y_pred_linear), min(y_pred_exp))
    scale = 50 / (max_y - min_y)
    
    print("\nOriginal data (blue) and model predictions:\n")
    for i in range(len(X)):
        print(f"X={X[i]:2d} | y={y[i]:5.1f} | Linear={y_pred_linear[i]:5.1f} | Exp={y_pred_exp[i]:5.1f}")

# Main function to run everything
def main():
    y_pred_linear, b0_linear, b1_linear = linear_regression(X, y)
    y_pred_exp, b0_exp, b1_exp = exponential_regression(X, y)

    rms_linear = calculate_rms(y, y_pred_linear)
    rms_exp = calculate_rms(y, y_pred_exp)

    print(f'Linear Model: b0 = {b0_linear}, b1 = {b1_linear}, RMS Error = {rms_linear}')
    print(f'Exponential Model: b0 = {b0_exp}, b1 = {b1_exp}, RMS Error = {rms_exp}')

    plot_data(X, y, y_pred_linear, y_pred_exp)

if __name__ == "__main__":
    main()