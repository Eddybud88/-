import statistics


def compute_stats(*args):
    if not args:
        raise ValueError("至少需要一个数值参数")

    min_val = min(args)

    max_val = max(args)

    median_val = statistics.median(args)

    mean_val = statistics.mean(args)

    variance_val = statistics.variance(args)

    return {
        'min': min_val,
        'max': max_val,
        'median': median_val,
        'mean': mean_val,
        'variance': variance_val
    }


result = compute_stats(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)