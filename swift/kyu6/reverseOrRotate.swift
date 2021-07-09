// https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/swift
// Doesn't pass tests for some reason


extension StringProtocol {
    func slice(start: Int, end: Int) -> SubSequence {
        let startIndex = index(self.startIndex, offsetBy: start)
        let endIndex = index(self.startIndex, offsetBy: end)
        return self[startIndex...endIndex]
    }
    func slice(start: Int) -> SubSequence {
        let startIndex = index(self.startIndex, offsetBy: start)
        let endIndex = index(before: self.endIndex)
        return self[startIndex...endIndex]
    }
}

func sumOfCubes(_ n: Int) -> Int {
    var sum:Int = 0
    var number = n

    while number != 0 {
        sum += (number % 10)*(number % 10)*(number % 10)
        number /= 10
    }
    return sum
}


func revRot(_ s: String, _ c: Int) -> String {
    guard !s.isEmpty    else { return "" }
    guard c > 0         else { return "" }
    guard c <= s.count   else { return "" }

    var result: String = ""
    for i in stride(from: 0, to: s.count - c + 1, by: c) {
        let slice = s.slice(start: i, end: i + c - 1)
        if sumOfCubes(Int(slice) ?? 0) % 2 == 0 {
            result += slice.reversed()
        } else {
            result += slice.slice(start: 1) + slice.slice(start: 0, end: 0)
        }
    }

    return result
}


assert(revRot("123456987654", 6) == "234561876549")
assert(revRot("123456987653", 6) == "234561356789")
assert(revRot("66443875", 4) == "44668753")
assert(revRot("66443875", 8) == "64438756")
assert(revRot("664438769", 8) == "67834466")
assert(revRot("123456779", 8) == "23456771")
assert(revRot("", 8) == "")
assert(revRot("123456779", 0) == "")
assert(revRot("563000655734469485", 4) == "0365065073456944")

print("OK")
