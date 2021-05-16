# design1

- [] 並び替える
- [] 等差数列かを判定する
    - [] 


# 【採用】design2

a,b,cの並び替えかたは

+ a,b,c
    + a-b = b-c
+ a,c,b
    + a-c = c-b
+ b,a,c
    + b-a = a-c
+ b,c,a
    + b-c = c-a
+ c,a,b
    + c-a = a-b
+ c,b,a
    + c-b = b-a


このうち以下だけ試して、どれか一つでもTrueならTrue

+ a,b,c
    + a-b = b-c
+ a,c,b
    + a-c = c-b
+ b,a,c
    + b-a = a-c

- [] 入力をa,b,cに格納する。
- [] 3つの等差判定を行う。
