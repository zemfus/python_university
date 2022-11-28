def parse_email(l: list[str]):
    dict = {}
    for i in l:
        dict[i.split("@")[0]] = i.split("@")[1]
    return dict

def main():
    emails = ["alex@42", "ver@mfua"]
    print(parse_email(emails))

if __name__ == "__main__":
    main()