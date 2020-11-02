### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
import pprint
# 検索ソース
with open('source.csv', newline='') as f:
    char_name = csv.reader(f)
    for i in char_name:
        source = i

### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    for i in range(len(source)):
        if word in source:
            return print("{}が見つかりました".format(word))
        else:
            print("{}は見つかりませんでした".format(word))
            add_list_flag = input("新しく追加しますか？Y/N >>> ")
            if add_list_flag == "Y":
                source.append(word)
                return print(source)
            else:
                return print(source)

if __name__ == "__main__":
    search()