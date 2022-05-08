import re

# content = r'hellow python, 123,end'
content = r'2011-07-20'

# .*でなるべく多い文字をマッチするため、12は.*に含まれる
pattern1 = '2011-07-..'
# .*?でなるべく少ない文字をマッチするため、123は\dにの残る
pattern2 = '.*?(\d+)'

result1 = re.match(pattern1, content)
result2 = re.match(pattern2, content)

if result1:
  print(result1.group())
  # output:3

if result2:
  print(result2.group(1))
   # output:123