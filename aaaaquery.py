import urllib
import hashlib
import urllib.parse
import requests
import json
import tqdm
import os


def baidumapquery(addr):
    AK = ""
    SK = ""

    if not AK or not SK:
        raise RuntimeError("Please get AK and SK from baidu")

    queryStr = "/geocoding/v3/?address=" + addr + "&output=json&ak=" + AK
    encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    rawStr = encodedStr + SK
    sn = hashlib.md5(urllib.parse.quote_plus(rawStr).encode("utf-8")).hexdigest()
    url = "http://api.map.baidu.com" + queryStr + "&sn=" + sn
    response = requests.get(url)
    result = response.json()

    return result


def processandsave(addr, i):
    result = baidumapquery(addr)
    result["addr"] = addr
    outputfile = f"output/{i:04d}.json"
    outputfile = open(outputfile, "w")
    json.dump(result, outputfile)


def main():
    os.makedirs('output', exist_ok=True)
    for i, line in enumerate(tqdm.tqdm(open("allaaaa.txt").readlines())):
        line = line.strip()
        if not line:
            continue
        processandsave(line, i)


if __name__ == "__main__":
    main()
