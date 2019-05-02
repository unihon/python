import requests
from colorama import init, Fore, Style

URL = "https://translate.googleapis.com/translate_a/single"

def requests_data(query_s):
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": "zh-CN",
        "hl": "zh-CN",
        "dt": ["t", "bd"],
        "dj": "1",
        "source": "icon",
        "tk": "",
        "q": query_s
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        'Cache-Control': "no-cache",
        'Host': "translate.googleapis.com",
    }

    try:
        response = requests.get(url=URL, headers=headers, params=params)
    except:
        print("ConnectionError...")
        return None

    if response.status_code == 429:
        print("Too Many Requests.")
        return None
    return response.json()

# 字典处理
# n为词性单词列举最多个数
def dict_process(dict_d, n):
    tmp_dict = []
    for i in dict_d:
        tmp_dict.append("[{pos}] {terms}".format(
            pos=i["pos"], terms=",".join(i["terms"][:n])))
    return "\n".join(tmp_dict)

# 单词、句子处理
def raw_process(raw):
    try:
        data_st = raw["sentences"]
    except KeyError:
        pass

    # 如果长度>1，则只需要处理sentences
    if len(data_st) > 1:
        tmp_trans = []
        tmp_orig = []

        # 句子拼接
        for i in data_st:
            tmp_trans.append(i["trans"])
            tmp_orig.append(i["orig"])

        trans_s = "".join(tmp_trans)
        orig_s = "".join(tmp_orig).replace(".", ". ")

        return {"trans": trans_s, "orig": orig_s, "dict_s": None}
    else:
        trans_s = raw["sentences"][0]["trans"]
        orig_s = raw["sentences"][0]["orig"]
        try:
            return {"trans": trans_s, "orig": orig_s, "dict_s": dict_process(raw["dict"], 5)}
        except KeyError:
            return {"trans": trans_s, "orig": orig_s, "dict_s": None}


def data_show(data_s):
    init()
    data_s = raw_process(data_s)
    process_s = """
{orig}

{trans}

{dict_s}
""".format(orig = Fore.YELLOW + data_s["orig"] + Style.RESET_ALL, trans = data_s["trans"], dict_s = data_s["dict_s"]).replace("\nNone\n", "")
    return process_s

if __name__ == '__main__':
    query_s = "since"
    print("Loading...")
    res = requests_data(query_s)
    if res:
        print(data_show(res))
