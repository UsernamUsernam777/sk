def sk(text, copy=False):
        import pyperclip
        """تحويل الحروف من انجليزي لعربي هكذا
lpl]
sk('lpl]') ➡ 'محمد'"""
        s = ''
        eng_ara = {'`': 'ذ', 'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'د', 'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل', 'h': 'ا',
                   'j': 'ت', 'k': 'ن', 'l': 'م', ';': 'ك', "'": 'ط', 'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا', 'n': 'ى', 'm': 'ة', ',': 'و', '.': 'ز', '/': 'ظ'}
        eng_ara_shift = {'~': 'ّ', 'Q': 'َ', 'W': 'ً', 'E': 'ُ', 'R': 'ٌ', 'T': 'لإ', 'Y': 'إ', 'U': '‘', 'I': '÷', 'O': '×', 'P': '؛', '{': '<', '}': '>', 'A': 'ِ', 'S': 'ٍ',
                         'D': ']', 'F': '[', 'G': 'لأ', 'H': 'أ', 'J': 'ـ', 'K': '،', 'L': '/', ':': ':', '"': '"', 'Z': '~', 'X': 'ْ', 'C': '}', 'V': '{', 'B': 'لآ', 'N': 'آ', 'M': '’', '<': ',', '>': '.', '?': '؟'}
        swap_eng_ara = {v: k for k, v in eng_ara.items()}
        swap_eng_ara_shift = {v: k for k, v in eng_ara_shift.items()}
        for i in text:
            if i in eng_ara:س
                s += eng_ara[i]
            elif i in swap_eng_ara:
                s += swap_eng_ara[i]
        #shift
            elif i in eng_ara_shift:
                s += eng_ara_shift[i]
            elif i in swap_eng_ara_shift:
                s += swap_eng_ara_shift[i]
            else:
                s += i
        if s and copy:
            pyperclip.copy(s)
        return s
