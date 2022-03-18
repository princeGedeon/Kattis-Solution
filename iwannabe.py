n,k=input().split()

stat_attack={}
stat_defense={}
stat_health={}

for i in range(int(n)):
    s=input().split()
    stat_attack[str(i)]=int(s[0])
    stat_defense[str(i)] = int(s[1])
    stat_health[str(i)] = int(s[2])
stat_attack=list((dict(sorted(stat_attack.items(), key=lambda x: x[1], reverse=True)).keys()))[0:int(k)]
stat_defense=list((dict(sorted(stat_defense.items(), key=lambda x: x[1], reverse=True)).keys()))[0:int(k)]
stat_health= list((dict(sorted(stat_health.items(), key=lambda x: x[1], reverse=True)).keys()))[0:int(k)]
print(len(set(stat_attack+stat_health+stat_defense)))
