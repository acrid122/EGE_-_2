s = open('24_19254 (3).txt').readline().strip()

parts = s.split('FSRQ')
# parts[i] — фрагменты между вхождениями FSRQ
# окно с ровно 80 вхождениями: parts[i] + FSRQ*80 + parts[i+80]
# можно расширить влево на 3 символа (SRQ из предыдущего FSRQ)
# и вправо на 3 символа (FSR из следующего FSRQ)
max_len = 0
for i in range(len(parts) - 80):
    window_len = len('FSRQ'.join(parts[i:i+81]))
    left_extra = 3 if i > 0 else 0
    right_extra = 3 if i + 81 < len(parts) else 0
    max_len = max(max_len, window_len + left_extra + right_extra)

print(max_len)