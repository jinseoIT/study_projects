const str = `
010-1234-5678
thelion@gmail.com
https://www.omdbapi.com/?apikey=7035c60c&s=forzen
The quick brown fox jumps over the lazy dog
abcccccc`

const regexp = /fox/gi
console.log(regexp.test(str))
console.log(str.replace(regexp, 'AAA'))

// 이스케이프 문자(Escape Character) 란 \(백슬래시) 기호를 통해 본래의 기능에서 벗어난 상태가 바뀌는 문자
console.log(str.match(/\.$/gi))

