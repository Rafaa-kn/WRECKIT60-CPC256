import re

def extract_and_compute(text):
    try:
        s1 = int(re.search(r"s1=([0-9]+)", text).group(1))
        s2 = int(re.search(r"s2=([0-9]+)", text).group(1))
        sigma1 = int(re.search(r"sigma1=([0-9]+)", text).group(1))
        sigma2 = int(re.search(r"sigma2=([0-9]+)", text).group(1))
    except Exception as e:
        print("Gagal mengekstrak integer dari teks. Pastikan kamu menempel seluruh blok signature.")
        print("Error:", e)
        return

    diff_s = s1 - s2
    diff_sigma = sigma1 - sigma2
    q, r = divmod(diff_s, diff_sigma)
    print("floor quotient q =", q)
    print("remainder r =", r)
    # search small neighborhood
    for t in range(-1000, 1001):
        lam = q + t
        a1 = s1 - sigma1 * lam
        a2 = s2 - sigma2 * lam
        if 1 <= a1 < 2**256 and 1 <= a2 < 2**256:
            print("\nFound candidate: t =", t)
            print("lambda (decimal) =", lam)
            print("lambda (hex)     =", hex(lam))
            print("alpha1 =", a1)
            print("alpha2 =", a2)
            return
    print("Tidak ditemukan kandidat dalam rentang pencarian. Coba pastikan teks yang kamu paste benar.")

if __name__ == "__main__":
    print("Tempel output sesi nc di bawah ini. Akhiri dengan baris kosong lalu Enter.")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            break
        lines.append(line)
    banner = "\n".join(lines)
    extract_and_compute(banner)
