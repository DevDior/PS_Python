# Clear
# 오늘의 날짜

from datetime import datetime, timedelta

print((datetime.today() + timedelta(hours=9)).strftime("%Y-%m-%d"))