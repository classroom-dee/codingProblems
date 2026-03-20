impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        // x = N
        // for _ in range(10):
        //     x = 0.5 * (x + N / x)
        let mut left = 0;
        let mut right = x;

        while left <= right {
            let mid = left + (right - left) / 2;
            let sq = mid as i64 * mid as i64;
            // b
            if sq == x as i64 {
                return mid;
            } else if sq < x as i64 {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        right
    }
}