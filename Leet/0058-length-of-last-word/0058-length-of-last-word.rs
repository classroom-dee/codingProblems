impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        match s.split_whitespace().last() {
            Some(w) => {
                w.len() as i32
            }
            // but i want safety
            None => {
                0
            }
        }
    }
}