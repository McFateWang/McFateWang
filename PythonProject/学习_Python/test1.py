

import matplotlib.pyplot as plt


date=['2016-01-01', '2016-01-02', '2016-01-03']
money=[100000, 110000, 105000]
plt.plot(date,money)
plt.xlabel("date")
plt.ylabel("money")
plt.xticks(date, rotation=20)
plt.title("holding money")
plt.show()