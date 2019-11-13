import json
import os
import csv


def main():
    outputfile = open("aaaaresult.csv", "w", newline="")
    outputfile.write("\ufeff")
    writer = csv.writer(outputfile)
    for f in os.listdir("output"):
        if not f.endswith(".json"):
            continue
        f = open(os.path.join("output", f))
        f = json.load(f)
        if f["status"] == 0:
            writer.writerow(
                (
                    f["addr"],
                    "Yes",
                    f["result"]["location"]["lat"],
                    f["result"]["location"]["lng"],
                    f["result"]["confidence"],
                )
            )
        else:
            writer.writerow((f["addr"], "No"))
        outputfile.flush()


if __name__ == "__main__":
    main()
