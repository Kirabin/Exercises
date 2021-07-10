// https://www.codewars.com/kata/55aa075506463dac6600010d/swift

extension Int {
    func squareRoot() -> Int {
        return Int(Double(self).squareRoot())
    }

    func divisors() -> [Int] {
        var divisors:[Int] = []

        for i in 1...self.squareRoot() {
            if i * i == self {
                divisors.append(i)
            }
            else if self % i == 0 {
                divisors.append(i)
                divisors.append(self / i)
            }
        }
        return divisors
    }

    func isSquared() -> Bool {
        let root = Double(self).squareRoot()
        if Int(exactly: root) != nil {
            return true
        }
        return false
    }
}

extension Array where Element == Int {
    func summed() -> Int {
        var sum:Int = 0

        for i in self {
            sum += i
        }
        return sum
    }

    func squared() -> [Int] {
        var squared:[Int] = []

        for i in self {
            squared.append(i * i)
        }
        return squared
    }
}

func listSquared(_ m: Int, _ n: Int) -> [(Int, Int)] {
    var result:[(Int, Int)] = []

    for i in m...n {
        let divSum = i.divisors().squared().summed()
        if divSum.isSquared() {
            result.append((i, divSum))
        }
    }
    return result
}
