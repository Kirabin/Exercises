// https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4

extension Int {
    func isSimple() -> Bool {
        var i = 2
        while i*i <= self {
            if self % i == 0 {
                return false
            }
            i += 1
        }
        return true
    }
}

func gap(_ g: Int, _ m: Int, _ n: Int) -> (Int, Int)? {
    var previousSimple:Int? = nil

    for i in m...n {
        if i.isSimple() {
            if let prev = previousSimple {
                if i - prev == g {
                    return (prev, i)
                }
            }
            previousSimple = i
        }
    }
    return nil
}

assert(gap(2, 100, 110)! == (101, 103))
assert(gap(4, 100, 110)! == (103, 107))
assert(gap(6, 100, 110) == nil)
assert(gap(2,10000000,11000000)! == (10000139, 10000141))
