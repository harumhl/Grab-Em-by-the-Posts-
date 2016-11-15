import re
#import pandas as pd
#import json
#from ast import literal_eval

#with open('Utitled.json') as json_data:
#	data = literal_eval(json_data.read())

#df = pd.Dataframe(data)
#print df


text = "A protest at Ohio State was interrupted after an anti-Trump protester was tackled while making a speech... https://t.co/ViTvHWvMGh"
text2 = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

print(text)
print(text2)

# need to make sure this "https" is the format for all tweets

# need to make sure that images dont show up as a img url in the "content"

# unicode to ascii
text = "CNN's new book \"Unprecedented\" reveals Clinton was worried about striking balances in debates with Trump… https://t.co/x1CosKJEHA"
#text.encode("utf8")
#text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

print (text)
