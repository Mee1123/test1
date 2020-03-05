PATH = "input.txt"

def read(path):  # リストの読み出し
    dividen = 1
    num_date = {}
    with open(path, 'r') as f:
        line = f.readline()
        while line is not "":
            # print("1.最初に取得"+line)
            if ":" in line:
                # print(":を確認"+line)
                single = date_entry(line)
                num_date[single[0]] = single[1].strip()
                # print("num_dateを更新")
                # print(num_date)
            else:
                dividen = int(line)
            line = f.readline()

    # print("必要データ")
    # print(num_date)
    # print(dividen)
    return num_date, dividen


def date_entry(line):  # データの辞書化
    word_list = "error"
    numer = -1
    try:
        char_list = list(line)
        is_number = True  # どこ:が出現するか
        numer = 0  # 整数i
        word_list: str = ""  # 文字列s
        for word in char_list:
            if word == ':':
                is_number = False
            elif is_number:
                numer = int(word) + numer * 10
            else:
                word_list = word_list + str(word)
    except:
        print("エラー:date_entry")
    return numer, word_list


def FizzBuzz(datas, m):
    out_text = ""
    out_text = {number: valu for number, valu in datas.items() if m % number == 0}
    out_text = sorted(out_text.items(), key=lambda x: x[0])
    if not out_text:
        out_text = m
    else:
        out_text = out_print(out_text)
    return out_text


def out_print(out_test):
    data_created = ""
    for text in out_test:
        data_created += text[1]
    return data_created


def main():
    num_date, dividen = read(PATH)
    out_put = FizzBuzz(num_date, dividen)
    print("答え:")
    print((out_put))


if __name__ == '__main__':
    main()
