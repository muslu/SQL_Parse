import sys, sqlparse
sql = "select a, b, c from table where a = 3;"

print sqlparse.format(sql,  reindent=True, keyword_case='upper')
