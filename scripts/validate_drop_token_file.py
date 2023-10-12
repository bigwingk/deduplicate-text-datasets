import argparse


def main():
    parser = argparse.ArgumentParser(description="drop_token_fileと元のテキストを用いて削除箇所をチェックする")

    parser.add_argument("-d", "--drop", type=str, required=True, help="元のテキストから削除する箇所を記載したファイル")
    parser.add_argument("-t", "--text", type=str, required=True, help="元のテキストファイル")
    parser.add_argument("-o", "--output", type=str, required=True, help="チェック後新たに作成するdrop_token_file")

    args = parser.parse_args()

    f = open(args.text, "rb")
    original_text = f.read()

    with open(args.output, "w") as out:
        with open(args.drop, "r") as file:
            for line in file:
                out.write(line)
                if "out" in line:
                    break
            for line in file:
                parts = line.strip().split()
                start = int(parts[0])
                end = int(parts[1])

                try:
                    target = original_text[start:end].decode()
                    out.write(line)
                except:
                    continue

    f.close()


if __name__ == "__main__":
    main()
