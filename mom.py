ray=[]
yu=[]
money=int(input("얼마 넣을래"))
for x in range(26):
        kim = money+1000*x
        konan = {
            x:kim
        }
        yu.append(kim)
        ray.append(konan)
sum_yu=sum(yu)
ray.append(f"합:{sum_yu}")
print(ray) 




#카카오 저금통 각 주마다 얼마 내야 하는지 만들기



    