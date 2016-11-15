import re
	 #= "A protest at Ohio State was interrupted after an anti-trump protestor was tackeld while making a speech..."
text = "A protest at Ohio State was interrupted after an anti-Trump protester was tackled while making a speech... https://t.co/ViTvHWvMGh"
text2 = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

print(text)
print(text2)