//regular expression
import re
s="An apple asday keeps doctor away!!!"
ans=re.match('a',s)
if ans!=none:
    print(ans.group())
else:
    print("no match found!!!")
//search
ans=re.search('a',s)
if ans!=none:
    print(ans.group())
else:
    print("no match found!!!")
ans=re.findall('a',s)
print(ans)
