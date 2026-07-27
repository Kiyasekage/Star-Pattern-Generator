def pattern(max_num):
    limit = 1
    for i in range(max_num):
        print("*"*limit)
        limit+=1
        if limit>max_num:
            limit-=2
            for j in range(limit):
                print("*"*limit)
                limit-=1
stars = int(input("What is the maximum length of stars you wished for? "))
pattern(stars)
