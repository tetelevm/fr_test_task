export default {
    getMonthCodeFromDate(date) {
        return date.getMonth() + 1
    },
    formatDate(date) {
        let day = "0" + date.getDay()
        day = day.slice(day.length - 2)
        let month = "0" + this.getMonthCodeFromDate(date)
        month = month.slice(month.length - 2)
        return `${day}.${month}.${date.getFullYear()}`
    },

    arrayRange(start, end) {
        if (end === undefined) {
            end = start
            start = 0
        }
        const array = Array.apply(null, Array(end - start))
        return array.map((v, index) => (start + index))
    },

    max(f, s) {
        return f > s ? f : s
    },
    min(f, s) {
        return f < s ? f : s
    },

    crop(string, len, endSym = "") {
        if (string.length < len) {
            return string
        }
        len = len - endSym.length
        return string.slice(0, len) + endSym
    },
}
