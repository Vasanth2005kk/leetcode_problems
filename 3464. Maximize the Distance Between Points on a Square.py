def maxDistance(side, points, k):
    def to_1d(x, y):
        if y == 0:    return x
        if x == side: return side + y
        if y == side: return 2 * side + (side - x)
        return 3 * side + (side - y)

    pos = sorted(to_1d(x, y) for x, y in points)
    n = len(pos)
    total = 4 * side

    def bisect_left_custom(lo, hi, target, arr, mod):
        # Find leftmost index in [lo, hi) where arr[idx%n] - base >= target (circular)
        result = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if (arr[mid % n] - arr[lo % n] + mod) % mod >= target:  # rough
                hi = mid
            else:
                lo = mid + 1
        return lo

    def find_next(start_idx, cur_val, d):
        # Binary search: first index >= start_idx where (pos[idx%n] - cur_val) % total >= d
        lo, hi = start_idx, start_idx + n
        while lo < hi:
            mid = (lo + hi) // 2
            gap = (pos[mid % n] - cur_val) % total
            if gap >= d:
                hi = mid
            else:
                lo = mid + 1
        return lo  # returns start_idx + n if not found

    def check(d):
        for start in range(n):
            count = 1
            cur = pos[start]
            first_val = cur
            i = start + 1
            valid = True
            while count < k:
                i = find_next(i, cur, d)
                if i >= start + n:
                    valid = False
                    break
                cur = pos[i % n]
                count += 1
                i += 1
            if valid and count == k:
                if (first_val - cur) % total >= d:
                    return True
        return False

    lo, hi, ans = 1, 2 * side, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans