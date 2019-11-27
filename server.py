{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('train.csv') #load train csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>...</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>842</td>\n",
       "      <td>0</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>0.6</td>\n",
       "      <td>188</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>20</td>\n",
       "      <td>756</td>\n",
       "      <td>2549</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1021</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>53</td>\n",
       "      <td>0.7</td>\n",
       "      <td>136</td>\n",
       "      <td>3</td>\n",
       "      <td>...</td>\n",
       "      <td>905</td>\n",
       "      <td>1988</td>\n",
       "      <td>2631</td>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>563</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>41</td>\n",
       "      <td>0.9</td>\n",
       "      <td>145</td>\n",
       "      <td>5</td>\n",
       "      <td>...</td>\n",
       "      <td>1263</td>\n",
       "      <td>1716</td>\n",
       "      <td>2603</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>615</td>\n",
       "      <td>1</td>\n",
       "      <td>2.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>0.8</td>\n",
       "      <td>131</td>\n",
       "      <td>6</td>\n",
       "      <td>...</td>\n",
       "      <td>1216</td>\n",
       "      <td>1786</td>\n",
       "      <td>2769</td>\n",
       "      <td>16</td>\n",
       "      <td>8</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1821</td>\n",
       "      <td>1</td>\n",
       "      <td>1.2</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>44</td>\n",
       "      <td>0.6</td>\n",
       "      <td>141</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>1208</td>\n",
       "      <td>1212</td>\n",
       "      <td>1411</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  m_dep  \\\n",
       "0            842     0          2.2         0   1       0           7    0.6   \n",
       "1           1021     1          0.5         1   0       1          53    0.7   \n",
       "2            563     1          0.5         1   2       1          41    0.9   \n",
       "3            615     1          2.5         0   0       0          10    0.8   \n",
       "4           1821     1          1.2         0  13       1          44    0.6   \n",
       "\n",
       "   mobile_wt  n_cores  ...  px_height  px_width   ram  sc_h  sc_w  talk_time  \\\n",
       "0        188        2  ...         20       756  2549     9     7         19   \n",
       "1        136        3  ...        905      1988  2631    17     3          7   \n",
       "2        145        5  ...       1263      1716  2603    11     2          9   \n",
       "3        131        6  ...       1216      1786  2769    16     8         11   \n",
       "4        141        2  ...       1208      1212  1411     8     2         15   \n",
       "\n",
       "   three_g  touch_screen  wifi  price_range  \n",
       "0        0             0     1            1  \n",
       "1        1             1     0            2  \n",
       "2        1             1     0            2  \n",
       "3        1             0     0            2  \n",
       "4        1             1     0            1  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',\n",
       "       'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',\n",
       "       'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',\n",
       "       'touch_screen', 'wifi', 'price_range'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns #feature yang digunakan untuk mencari rentang harga"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "battery_power   [ 842 1021  563 ... 1139 1467  858]\n",
      "blue   [0 1]\n",
      "clock_speed   [2.2 0.5 2.5 1.2 1.7 0.6 2.9 2.8 2.1 1.  0.9 1.1 2.6 1.4 1.6 2.7 1.3 2.3\n",
      " 2.  1.8 3.  1.5 1.9 2.4 0.8 0.7]\n",
      "dual_sim   [0 1]\n",
      "fc   [ 1  0  2 13  3  4  5  7 11 12 16  6 15  8  9 10 18 17 14 19]\n",
      "four_g   [0 1]\n",
      "int_memory   [ 7 53 41 10 44 22 24  9 33 17 52 46 13 23 49 19 39 47 38  8 57 51 21  5\n",
      " 60 61  6 11 50 34 20 27 42 40 64 14 63 43 16 48 12 55 36 30 45 29 58 25\n",
      "  3 54 15 37 31 32  4 18  2 56 26 35 59 28 62]\n",
      "m_dep   [0.6 0.7 0.9 0.8 0.1 0.5 1.  0.3 0.4 0.2]\n",
      "mobile_wt   [188 136 145 131 141 164 139 187 174  93 182 177 159 198 185 196 121 101\n",
      "  81 156 199 114 111 132 143  96 200  88 150 107 100 157 160 119  87 152\n",
      " 166 110 118 162 127 109 102 104 148 180 128 134 144 168 155 165  80 138\n",
      " 142  90 197 172 116  85 163 178 171 103  83 140 194 146 192 106 135 153\n",
      "  89  82 130 189 181  99 184 195 108 133 179 147 137 190 176  84  97 124\n",
      " 183 113  92  95 151 117  94 173 105 115  91 112 123 129 154 191 175  86\n",
      "  98 125 126 158 170 161 193 169 120 149 186 122 167]\n",
      "n_cores   [2 3 5 6 1 8 4 7]\n",
      "pc   [ 2  6  9 14  7 10  0 15  1 18 17 11 16  4 20 13  3 19  8  5 12]\n",
      "px_height   [  20  905 1263 ...  528  915  483]\n",
      "px_width   [ 756 1988 1716 ...  743 1890 1632]\n",
      "ram   [2549 2631 2603 ... 2032 3057 3919]\n",
      "sc_h   [ 9 17 11 16  8 13 19  5 14 18  7 10 12  6 15]\n",
      "sc_w   [ 7  3  2  8  1 10  9  0 15 13  5 11  4 12  6 17 14 16 18]\n",
      "talk_time   [19  7  9 11 15 10 18  5 20 12 13  2  4  3 16  6 14 17  8]\n",
      "three_g   [0 1]\n",
      "touch_screen   [0 1]\n",
      "wifi   [1 0]\n",
      "price_range   [1 2 3 0]\n"
     ]
    }
   ],
   "source": [
    "for col in df.columns:\n",
    "    print(col, ' ', df[col].unique()) #mengetahui nilai unik dari masing-masing feature\n",
    "    #dari sini dapat diketahui bahwa masing-masing feature tidak memiliki nilai aneh atau sesuatu yang terindikasi null atau null itu sendiri"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Business Understanding\n",
    "#arti dari masing-masing feature dalam domain knowledge mobile pricing\n",
    "#battery_power : total energy a battery can store in one time measured in mAh\n",
    "#blue : has bluetooth or not, 0 is none, 1 is has\n",
    "#clock_speed : speed at which microprossor executes instructions\n",
    "#dual_sim : has dual sim support or not, 0 is hasnt, 1 is has\n",
    "#fc : front camera mega pixels\n",
    "#int_memory : internal memory in Gigabytes\n",
    "#m_dep : mobile depth in cm\n",
    "#n_cores : number of cores of processor\n",
    "#pc : primary camera mega pixels\n",
    "#px_height : pixel resolution height\n",
    "#px_width : pixel resolution width\n",
    "#ram : random access memory in megabytes\n",
    "#sc_h : screen height of mobile in cm\n",
    "#sc_w : screen width of mobile in cm\n",
    "#talk_time : longest time that a single battery charge will last when you are\n",
    "#three_g : has 3G or not, 0 is hasnt, 1 is has\n",
    "#touch_screen : has touch screen or not, 0 is hasnt, 1 is has\n",
    "#wifi : has wifi or not, 0 is hasnt, 1 is has\n",
    "#price_range : target value with value of 0 (low cost), 1 (medium cost), 2 (high cost), 3 (very high cost)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    2000.000000\n",
       "mean       11.011000\n",
       "std         5.463955\n",
       "min         2.000000\n",
       "25%         6.000000\n",
       "50%        11.000000\n",
       "75%        16.000000\n",
       "max        20.000000\n",
       "Name: talk_time, dtype: float64"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['talk_time'].describe() #mengetahui lebih detail mengenai nilai yang terdapat dalam masing-masing feature untuk mengetahui outlier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x199868e6dd8>"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lmplot(x = 'ram', y='price_range', data = df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x19986aa1828>"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x432 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(x = 'ram', y='price_range', data = df, color = 'red', kind = 'kde')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x199fde89e48>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pointplot(y = 'm_dep', x = 'price_range', data= df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x199fde65da0>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pointplot(df['price_range'], df['int_memory'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "labels = ['3G-supported', 'Not supported']\n",
    "values = df['three_g'].value_counts().values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(values, labels = labels, autopct = '%1.1f%%', shadow=True, startangle=90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels4g = ['4G-supported', 'Not supported']\n",
    "values4g = df['four_g'].value_counts().values\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(values4g, labels = labels4g, autopct = '%1.1f%%', shadow = True, startangle = 90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x199fd7af358>"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x = 'price_range', y='battery_power', data = df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 0, 'MegaPixels')"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "df['fc'].hist(alpha = 0.5, color ='blue', label = 'Front camera')\n",
    "df['pc'].hist(alpha = 0.5, color = 'red', label = 'Primary camera')\n",
    "plt.legend(loc ='upper right')\n",
    "plt.xlabel('MegaPixels')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x199ff443c18>"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x432 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(df['mobile_wt'], df['price_range'], kind='kde')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x199ffa71a90>"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pointplot(df['price_range'], df['talk_time'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.drop('price_range', axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df['price_range']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state=101)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "lm = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lm.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9132801488185275"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lm.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
       "                     metric_params=None, n_jobs=None, n_neighbors=10, p=2,\n",
       "                     weights='uniform')"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "knn = KNeighborsClassifier(n_neighbors = 10)\n",
    "knn.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9212121212121213"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "error_rate = []\n",
    "for i in range(1,20):\n",
    "    \n",
    "    knn = KNeighborsClassifier(n_neighbors=i)\n",
    "    knn.fit(X_train, y_train)\n",
    "    pred_i = knn.predict(X_test)\n",
    "    error_rate.append(np.mean(pred_i != y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Error Rate')"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAm0AAAGDCAYAAAB5rSfRAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzdeXxU1f3/8deHsBpEQcCFQMAqIhILGgG1LlUBUxdQwX2rW13rvu/YutSFVktdgWrdgUJxQaAuWEAoUHBBQPgiSwAFBZREgSSc3x9n8iOESTKTzJ07M3k/H495TObOved+hhDy4SyfY845RERERCS1NQg7ABERERGpmZI2ERERkTSgpE1EREQkDShpExEREUkDStpERERE0oCSNhEREZE0oKRNRKQeMzNnZvuEHYeI1ExJm4jUipktNbOfzayowuOvSY7haDPbGrn3RjNbaGa/jeP6+8zs5SBjjJeZXWhmUyq8bmFmU81stJk1qnTus2b2UpQ2DjSzzWbWKhkxi0hyKGkTkbo4yTnXvMLj6mgnmVnDWI5Vp5rzVznnmgMtgOuB581sv3jaTlVm1hL4N7AMOMM5V1LplL8Dp5pZdqXj5wNvO+fWBR+liCSLkjYRSbhIb9FUMxtiZuuA+6o41sDM7jKzZWa2xsxeMrNdIm10jAzdXWxmy4EPqrun894F1gEHVojlL2a2wsx+NLPZZnZE5PjxwB3AGZGeuk8jx3cxs2FmttrMVprZH8wsK8pn3CvS09iqwrEeZvadmTUys33MbLKZ/RA59kacf4atI595HnCuc640ymf+BFgJnFbhuizgbODFyOueZvaJmW2IfKa/mlnjKu75kZldUuF15V6/LmY2yczWRXo1T4/nM4lI3ShpE5Gg9AKWAG2BP1Zx7MLI49fA3kBzoPIQ61HA/kC/6m4WSQBPBloDiyu8NRPoDrQCXgVGmllT59x7wIPAG5Fewl9Gzn8RKAX2AXoAfYFLqMQ5twr4hAoJEz5ZGhXpEXsAmAi0BHKAp6qLv5JWwGRgBnCRc25rNee+hO9ZK3cc0AgYH3ldhu+BbA0cChwLXBlHLABEevMm4f8M2wJnAX8zswPibUtEakdJm4jUxdhID07549IK761yzj3lnCt1zv1cxbFzgCecc0ucc0XA7cCZlYZC73POFVdoo7K9zGwD8DMwBrjBOTen/E3n3MvOue8j93wcaAJEHT41s92BAuC6yD3XAEOAM6u496v45AUzs8h5r0beKwFygb2cc5ucc1OiNxFVe6AzMMLVvEH0P4CjzCwn8vp84NXyoVTn3Gzn3PTI518KPItPhON1IrDUOTci0tb/gNHAwFq0JSK1oKRNROpigHNu1wqP5yu8tyLK+ZWP7YWfr1VuGdAQ2L2Gdipa5ZzbFT+n7UngmIpvmtmNZjY/Mky5AdgF3+sUTS6+l2p1eSKKT3LaVnH+KOBQM9sLOBJwwH8i790CGPBfM5tnZhfV8Dkq+hS4CRhvZj2qO9E5txz4GDjXzJoDA4gMjQKYWWcze9vMvjGzH/G9i1V9/urkAr0qJun4pHuPWrQlIrUQ10RgEZE4ROshqnxsFT4ZKNcBPzT5LX5Isap2dmzYuc1mdiuw0MwGOOfGRuav3YofEpznnNtqZuvxyVS0tlcAm4HW0eaQRbnnBjObCJyOH8J9rbxnzDn3DXApgJn9Cvi3mX3snFtcZYPbt/0XM2sCTDKzo51zX1Rz+ovAbcBq4OtIL1i5p4E5wFnOuY1mdh1V944VAztVeF0xIVsBTHbO9YklfhFJPPW0iUiYXgOuN7NOkV6i8jlmNSZM0TjntgCPA/dEDu2MTwLXAg3N7B58j1y5b4GOZtYgcv1q/Dy0xyOlNhqY2S/MrLrhxFfxQ5KnsW1oFDMbVGHIcj0+QSyL8/P8CfgLPuGrbkXsaPyQ6v1U6GWL2Bn4ESgysy7AFdW0Mxe/GnUn87XbLq7w3ttAZzM7L7LQopGZHWJm+8fzmUSk9pS0iUhdvGXb12kbE+f1w/Fzsj4GvgY2AdfUMabhQAczOwmYgJ+Q/xV+6HUT2w+3jow8f29m5b1T5wONgS/xydYoYM9q7jcO2Bf41jn3aYXjhwAzzKwocs61zrmvASLDpefE8mGccw8ALwDvm9kvqjinmG2J2yuV3r4Jv0BiI/A8UN0q1iHAFnwy+2LFtpxzG/GLMs7E95B+AzyCnyMoIklgNc9xFREREZGwqadNREREJA0oaRMRERFJA0raRERERNKAkjYRERGRNKCkTURERCQN1Iviuq1bt3YdO3YMOwwRERGRGs2ePfs751ybysfrRdLWsWNHZs2aFXYYIiIiIjUys2XRjmt4VERERCQNKGkTERERSQNK2kRERETSgJI2ERERkTSgpE1EREQkDShpExEREUkDStpERERE0oCSNhEREZE0oKRNREREJA3Uix0RMklZGYwfD3PmQI8eUFAAWVlhRyUiIiJBU9KWRsrK4JR+xaycUUjf4rHcmz2A53rlMGZCthI3ERGRDKfh0TQyfjysnFHI9KJuPORuY3pRNwpnrGT8+LAjExERkaApaUsjc+ZA3+KxNKIUgEaU0q94DHPnhhyYiIiIBE5JWxrp0QPebjSAksiodgkNmZB9Ct27hxyYiIiIBE5z2tJIkyawZEsO3ZhHf8Ywodkp5PZqR0FB2JGJiIhI0NTTliZWr4Zzz4UOXbK5YkhnHuVWjr28sxYhiIiI1BNK2tJAaSmceSYUFcHo0fC73/njrVqp3IeIiEh9oeHRNDBrFkyfDsOGQdeu/ljbtrBsWbhxiYiISPIoaUsDvXvDV19Bbu62Y7m5StpERETqEyVtKWzZMpg5EwYO3D5hAz9Muuuu4cQlIiIiyaekLUVt2QKnnw4LF8Kvfw277bb9++3bhxOXiIiIhEMLEVLUTTfBf/8Lw4fvmLABfP453HorrF+f/NhEREQk+ZS0paCRI+Gpp+D66+HUU6Ofs2QJ/OlPsHhxcmMTERGRcChpSzFr1sDFF8Ohh8Ijj1R9Xvkct+XLkxOXiIiIhEtz2lJM27bwzDNwxBHQqFHV55UnbVpBKiIiUj+opy2FrFjhn88+u+aFBrvuCs2bK2kTERGpL5S0pYgXX4TOnX2Jj1iY+d62NWuCjUtERERSg4ZHU8Dnn8MVV/h5bAcdFPt1M2dCs2bBxSUiIiKpQz1tIdu4EQYNgl12gVdfjW8vUSVsIiIi9YeSthA5B5ddBosWwWuvwR57xHf95Ml+/ltxcTDxiYiISOoINGkzs+PNbKGZLTaz26K8f6SZ/c/MSs1sYKX3LjCzRZHHBRWOfxRpc27k0TbIzxCkrVshJwf+8Ac4+uj4r1+1yid7WowgIiKS+QKb02ZmWcBQoA9QCMw0s3HOuS8rnLYcuBC4qdK1rYB7gXzAAbMj15bX/z/HOTcrqNiTJSsLHn209tdXLPvRtWtiYhIREZHUFGRPW09gsXNuiXNuC/A60L/iCc65pc65z4Ctla7tB0xyzq2LJGqTgOMDjDWp1q+Ho46CGTPq1k6HDv5ZPW0iIiKZL8ikrR2wosLrwsixRFw7IjI0ereZWbQGzOwyM5tlZrPWrl0bT9yBcg4uvBA++cR/XRd77gkNGyppExERqQ+CTNqiJVOxpinVXXuOcy4POCLyOC9aA86555xz+c65/DZt2sR42+A9/jiMG+eHRXv3rltbWVlwwAFQVpaY2ERERCR1BVmnrRCoWNc/B1gVx7VHV7r2IwDn3MrI80YzexU/DPtSHWNNiilT4Lbb4LTT4Pe/T0ybc+cmph0RERFJbUH2tM0E9jWzTmbWGDgTGBfjtROAvmbW0sxaAn2BCWbW0MxaA5hZI+BE4IsAYg/ECy9Ap04wbJjf0UBEREQkVoElbc65UuBqfAI2H3jTOTfPzAab2ckAZnaImRUCg4BnzWxe5Np1wAP4xG8mMDhyrAk+efsMmAusBJ4P6jMk2rBh8NFHvpBuoowe7Rc1lJQkrk0RERFJPebqOhs+DeTn57tZs8KrEPLSS3DssdAu1mUYcRg2DC65BL7+Gjp2THz7IiIiklxmNts5l1/5uHZECNikSX616MMPB9N+xVptIiIikrmUtAVo5Uo45xzYf//gkrbyWm3LlwfTvoiIiKQGJW0BKSmBM8+En36CUaMgOzuY+6jAroiISP0QZMmPeu2xx3yJj1de8T1tQWnaFI44AnbeObh7iIiISPiUtAXkyiuhTRs4++zg7/Xxx8HfQ0RERMKl4dEE++Yb2LTJl/W45JKwoxEREZFMoaQtgTZvhpNOghNOqPu+ovEYOhS6dEnuPUVERCS5NDyaQDfcALNmwZgxyd3xoKwMFi6EtWuhbdvk3VdERESSRz1tdVRWBm+/DaefDn/7G1x/PQwYkNwYVKtNREQk86mnrQ7KyuCUfsWs+KSQPj+NpUuDAXw1N4eysmyyspIXR8Wk7ZBDkndfERERSR71tNXB+PGwckYh//2pG3/iNj7b2o1VM1cyfnxy4yhP2lRgV0REJHMpaauDOXOgb/FYGlEKQCNK6Vc8hrlzkxvHrrtC//7B7G0qIiIiqUFJWx306AETswdQEhllLqEhE7JPoXv35MZhBmPHwhlnJPe+IiIikjxK2uqgoADa9cqhV/N53G4P06v5PHJ6taOgIJx4VPJDREQkc2khQh1kZcGYCdmMH9+ZuXNvZXB3n8glcxFCubvugmHDYPXq5N9bREREgqekrY6ysuDEE/0jTM2b+90Yior81yIiIpJZNDyaIVSrTUREJLMpacsQStpEREQym5K2DNGhg39W0iYiIpKZlLRliD33hEsugf32CzsSERERCYIWImSIrCx4/vmwoxAREZGgqKctg2zdCuvWhR2FiIiIBEFJWwa59FL45S/DjkJERESCoKQtg+TkwKpVUFISdiQiIiKSaEraMkiHDn6ItLAw7EhEREQk0ZS0ZZDyWm3Ll4cbh4iIiCSekrYMogK7IiIimUtJWwZp3x7uv1+LEURERDKR6rRlkKZN4Z57wo5CREREgqCetgyzdi0sXBh2FCIiIpJoStoyzJVXwsknhx2FiIiIJJqStgyTm+tXjzoXdiQiIiKSSIEmbWZ2vJktNLPFZnZblPePNLP/mVmpmQ2s9N4FZrYo8rigwvGDzezzSJtPmpkF+RnSTW4ubNrkh0lFREQkcwSWtJlZFjAUKAC6AmeZWddKpy0HLgRerXRtK+BeoBfQE7jXzFpG3n4auAzYN/I4PqCPkJZU9kNERCQzBdnT1hNY7Jxb4pzbArwO9K94gnNuqXPuM2BrpWv7AZOcc+ucc+uBScDxZrYn0MI594lzzgEvAQMC/AxpR0mbiIhIZgoyaWsHrKjwujByrC7Xtot8XWObZnaZmc0ys1lr69FY4T77wPDhcMghYUciIiIiiRRk0hZtrlms0+OrujbmNp1zzznn8p1z+W3atInxtukvOxt++9ttPW4iIiKSGYJM2gqB9hVe5wCr6nhtYeTr2rRZb8ybB9OmhR2FiIiIJFKQSdtMYF8z62RmjYEzgXExXjsB6GtmLSMLEPoCE5xzq4GNZtY7smr0fOBfQQSfzm69Fa66KuwoREREJJECS9qcc6XA1fgEbD7wpnNunpkNNrOTAczsEDMrBAYBz5rZvMi164AH8InfTGBw5BjAFcALwGLg/4DxQX2GdNWhg6/VJiIiIpkj0L1HnXPvAu9WOnZPha9nsv1wZ8XzhgPDoxyfBXRLbKSZJTcX1q2DoiJo3jzsaERERCQRtCNCBlLZDxERkcyjpC0DdejgnzVEKiIikjkCHR6VcOTlwcSJkJ8fdiQiIiKSKEraMtDOO0OfPmFHISIiIomk4dEMNWkSjNe6WhERkYyhnrYM9eCDsGULFBSEHYmIiIgkgnraMlRurlaPioiIZBIlbRkqNxdWrYKSkrAjERERkURQ0pahcnPBOSgsDDsSERERSQQlbRmqvFabhkhFREQygxYiZKhDD4UFC6Bjx7AjERERkURQ0pahsrNhv/3CjkJEREQSRcOjGWzECHjzzbCjEBERkURQT1sGe+YZaNECTj897EhERESkrtTTlsFyc7VpvIiISKZQ0pbBypM258KOREREROpKSVsG69ABNm2CNWvCjkRERETqSklbBsvN9c8rVoQbh4iIiNSdFiJksH79oKjIl/8QERGR9KakLYM1aeIfIiIikv40PJrh7rvP12sTERGR9KakLcONHg1jx4YdhYiIiNSVkrYMp1ptIiIimUFJW4bLzYVly8KOQkREROpKSVuG69AB1q+HjRvDjkRERETqQklbhsvNhZYt4dtvw45ERERE6kJJW4Y74wxYtw722SfsSERERKQulLRlOLOwIxAREZFEUNJWD1xwATzzTNhRiIiISF0oaasHpkyBjz8OOwoRERGpCyVt9YDKfoiIiKQ/JW31gJI2ERGR9Bdo0mZmx5vZQjNbbGa3RXm/iZm9EXl/hpl1jBxvbGYjzOxzM/vUzI6ucM1HkTbnRh5tg/wMmaBDB1i1CrZsCTsSERERqa3AkjYzywKGAgVAV+AsM+ta6bSLgfXOuX2AIcAjkeOXAjjn8oA+wONmVjHWc5xz3SOPNUF9hkzRpQvk5fkiuyIiIpKeguxp6wksds4tcc5tAV4H+lc6pz/wYuTrUcCxZmb4JO99gEhStgHIDzDWjHbWWfDpp7D77mFHIiIiIrUVZNLWDlhR4XVh5FjUc5xzpcAPwG7Ap0B/M2toZp2Ag4H2Fa4bERkavTuS5O3AzC4zs1lmNmvt2rWJ+UQiIiIiIQkyaYuWTLkYzxmOT/JmAX8GpgGlkffPiQybHhF5nBft5s6555xz+c65/DZt2tQi/MxRVgZHHAFPPRV2JCIiIlJbQSZthWzfO5YDrKrqHDNrCOwCrHPOlTrnro/MWesP7AosAnDOrYw8bwRexQ/DSjWysmDxYj9EKiIiIukpyKRtJrCvmXUys8bAmcC4SueMAy6IfD0Q+MA558xsJzPLBjCzPkCpc+7LyHBp68jxRsCJwBcBfoaMobIfIiIi6a1hUA0750rN7GpgApAFDHfOzTOzwcAs59w4YBjwDzNbDKzDJ3YAbYEJZrYVWMm2IdAmkeONIm3+G3g+qM+QSTp0gLlzw45CREREaiuwpA3AOfcu8G6lY/dU+HoTMCjKdUuB/aIcL8YvSpA45ebCuHHgnDaRFxERSUeBJm2SOg4+GI47Dn76CbKzw46memVlMH48zJkDPXpAQYGflyciIlKfmXOVF3Rmnvz8fDdr1qyww5AYlJXBKf2KWTmjkL7FY5mYPYB2vXIYMyFbiZuIiNQLZjbbObdDfVrtPSopZfx4KPykkOlF3XjI3cb0om4UzljJ+PFhRyYiIhIuJW31RHGxX4wwZEjYkVRvzhzo+/NYGkXK8jWilH7FY7SIQkRE6j0lbfXETjvBhg3w9ddhR1K9Hj3g7YYDKIlMtyyhIROyT6F795ADExERCZmStnrCLD1qtRUUwNomORyYNY/b7WF6NZ9HTq92FBSEHZmIiEi4tHq0HkmHpA1gvx7ZtG/fmden3cpRR8GwYVo9KiIioqStHsnNhWnTwo6iellZ8PHH/utDDoFFi5SwiYiIgIZH65VjjoEzzoDS0rAjqVrFCjQFBTB9OqxbF148IiIiqUJJWz1y2mnw9NPQMIX7V/v3hwsv9F8XFMDWrTBpUqghiYiIpAQlbfVMaSls3hx2FNGVlcFHH/mVrgA9e0KrVqhGm4iICEra6pVvv4WmTWH48LAjiW7ePNi4EQ47zL/OyoKbboJf/SrcuERERFJBCg+USaK1aQMNGqTuCtKpU/3z4YdvO3b77eHEIiIikmrU01aPNGgA7dunbtI2bRrssQd07Lj98XXrYP78UEISERFJGeppq2dSuVbb0UdDt26+EHBFxx8PjRvDlCmhhCUiIpIS1NNWz6Ry0nbxxXDrrTse79cPPvkE1q9PfkwiIiKpIqakzcyamdl+QQcjwTv1VLjmmu3roaWC1ath7dro76n0h4iISAxJm5mdBMwF3ou87m5m44IOTIJx0klw2207DkGG7bHH/Hy7LVt2fK9XL2jZUqU/RESkfoulp+0+oCewAcA5NxfoGFxIEqStW6GwEH74IexItjdtGuTn+7lrlWVlQd++8N57Pn4REZH6KJakrdQ5l2K/4qW2lizxPVpjx4YdyTY//wyzZ29f6qOye+/1e5I20CxMERGpp2JZPfqFmZ0NZJnZvsDvgRTfdlyq0r69f06lxQizZ0NJybaiutHsv3/y4hEREUlFsfRbXAMcAGwGXgV+AK4NMigJTpMmvhZaKiVt5UV1q0vawM9pu//+4OMRERFJRbEkbSc45+50zh0SedwFnBx0YBKc3FxYvjzsKLY54wx47TW/Y0N1pk6FBx6ADRuSE5eIiEgqiSVpi7aRkDYXSmOpVqutY0c488yazyso8JvKq/SHiIjUR1XOaTOzAuA3QDsze7LCWy2A0qADk+BcdlnVNdGSbdUqvyp0wABo1ar6c3v1gl139cOkgwYlJz6JX1mZ/x7NmQM9evhkOysr7KhERNJfdQsRVgGz8EOhsysc3whcH2RQEqxjjw07gm0mTfI7IfTuXXPS1rDhttIfzqVerTnxCdsp/YpZOaOQvsVjuTd7AM/1ymHMhGwlbiIidVRl0uac+xT41Mxedc6VJDEmCdhPP8Gnn8K++0Lr1uHGMnWq7z3r0iW28wsKfOzffusXVEhqGT8eVs4oZHpRNxpRyuCiu+g1Yx7jx3fmxBPDjk5EJL3FMqeto5mNMrMvzWxJ+SPwyCQwixb5lZoffhh2JL6o7qGHxl5/7fzzYcECJWypas4c6Fs8lkaRGRSNKKVf8Rjmzg05MBGRDBDLr8oRwNP4eWy/Bl4C/hFkUBKs3Fz/HPZihPXrYd686ovqVlae3GlnhNTUowdMzB5ASaQTv4SGTMg+he7dQw5MRCQDxJK0NXPOvQ+Yc26Zc+4+4Jhgw5Ig7bortGgRftI2Z45/rqk+W2WvvQa7767SH6mooABadsvhAOZxKw/Tq/k8cnq1o6Ag7MhERNJfLEnbJjNrACwys6vN7BSgbcBxScA6dAi/Vtsxx8A338SftLVvD999B//+dzBxSe1lZcHRJ2SziM7MPvZWDrugsxYhiIgkSCxJ23XATvjtqw4GzgMuiKVxMzvezBaa2WIzuy3K+03M7I3I+zPMrGPkeGMzG2Fmn5vZp2Z2dIVrDo4cX2xmT5ppDWFtpEqttt1397s0xKN3722lPyT1/N//+XmKTZvC5Mkq9yEikig1Jm3OuZnOuSLnXKFz7rfOuVOB1TVdZ2ZZwFCgAOgKnGVmXSuddjGw3jm3DzAEeCRy/NLIvfOAPsDjkd4+8PPrLgP2jTyOrykW2dHdd8PQoeHdv6QETj8d3n8//msbNoQ+fbaV/pDUMmKE/77m5flFI1u2hB2RiEhmqDZpM7NDzWygmbWNvD7QzF4FpsTQdk9gsXNuiXNuC/A60L/SOf2BFyNfjwKOjfScdQXeB3DOrQE2APlmtifQwjn3iXPO4RdFDIjlg8r2evWKbwFAon32GYwcWfsivwUFvjDvZ58lNi6pm/Ikulkzn7SVlsJXX4Ubk4hIpqgyaTOzR4HhwGnAO2Z2LzAJmIHv4apJO2BFhdeFkWNRz3HOleI3o98N+BTob2YNzawTfli2feT8whralBh8/z28+SasWRPO/adN88/xzmcrV1AAN9/sF1RI6jjmGLjlFv91Xp5//vzz8OIREckk1e2IcALQwzm3ycxa4ndIONA5tyjGtqPNNas8mFXVOcOB/fE7MiwDpuFLjsTSpm/Y7DL8MCodOnSILeJ6ZNEiv1H722/DCSck//5Tp0JOjl8QURt77AF/+lNiY5K6WbECPvrID10D7Lefn6+4cmWoYYmIZIzqkrafnXObAJxz681sYRwJG/hesPYVXufgE79o5xSaWUNgF2BdZOjz/2+VZWbTgEXA+kg71bVJJObngOcA8vPzNfOpkvJkKazFCNOm1b6XrdyWLT75y8+HnXdOTFxSe//8p38eONA/N24MP/wQ/0ITERGJrro5bb8ws3HlD/zOCBVf12QmsK+ZdTKzxsCZQOXrxrFtJepA4APnnDOzncwsG8DM+gClzrkvnXOrgY1m1jsy9+184F+xf1wpt8ce/pdqGGU/iopgzz3h6KPr1s6MGX44btKkhIQldTR6NHTrBp07bzumhE1EJHGq62mrvGjg8Xgads6VmtnVwAQgCxjunJtnZoOBWc65ccAw4B9mthhYh0/swNeBm2BmW4GV+DIj5a4A/g40A8ZHHhKnBg18vbMwetqaN/cJV10deijssgu8+y6cemrd25Pa++YbmDIF7r13++MffOCHsd94w3+vRESk9qrbMH5yXRt3zr0LvFvp2D0Vvt4EDIpy3VJgvyranAV0q2ts4odIw0janINEVNerXPpDFfvCk5XlE7Yzz9z+eHExTJjgtyur63C4iEh9F+M23ZKJhg6FV19N/n2POgquv77m82JRUOAnumuFYrjatPFJ236V/qulFaQiIomjpK0e239/6NgxufcsLvaLELKzE9Pe8ZHSyhMmJKY9id+6dfCvf8GmTTu+l5vrF4koaRMRqbuaiutmReq1SQZauhSeeCK5tdpmzoSyssQNle21F8yalbieO4nfmDEwYADMn7/je2Z+cYKSNhGRuqs2aXPOlQEHa3/PzPR//wc33ujnGyVLeVHd3r0T1+bBB/v5bRKOUaOgUyfo3j36+0ceCa1bJzcmEZFMFMuvujnAv8xsJFBcftA598/AopKkyM31z8lcjDB1KnTtCq1aJa7NDRvg/vvhxBPh2GMT167UbMMGv8/odddVvRDk4YeTG5OISKaKJWlrBXwPHFPhmAOUtKW59pHSx8ms1davX+JXeWZnw/Dhfr6ckrbkeustKCmB004LOxIRkcxXY9LmnPttMgKR5GvSxBe5TWZP2+9/n/g2GzXypT/efVelP5Lto4/8dmSHHFL1OT//DD17wiWXwLXXJi00EZGMU+PqUTPLMbMxZrbGzL41s9FmllPTdZIeklmrrbAQ1q8Ppu3y0tEJh9kAACAASURBVB9ffBFM+xLdCy/AJ5/4Ys1VadbMrzD93/+SF5eISCaKpeTHCPx2U3sB7YC3IsckA/zrX37T+GS4+27o0sX3hiVaeemP8dofI6nMfE9bTfLytIJURKSuYkna2jjnRjjnSiOPvwNtAo5LkmT33aFp0+Tca9o0v2o0iOHLdu38PqRlZYlvO9HKynyi/MAD/jkdYo7myivhzjtjOzcvD778EkpLg41JRCSTxZK0fWdm50ZqtmWZ2bn4hQmSAT791Nc4+z7g7+h338FXX8Hhhwd3j/ffh9tvD679RCgrg1P6FXPvWQv56d5HuPeshZzSrzjtEreffoIXX4x9uDsvDzZvhsWLg41LRCSTxZK0XQScDnwDrAYGRo5JBli+HP785+B/mZbXZwt6/0nnolfmTxXjx8PKGYVML+rGQ+42phd1o3DGyrQb1n3vPZ+4xbpq9JBD4JxztEhERKQuatwRATjNOXeyc66Nc66tc26Acy6EbcYlCMmq1TZtml/lefDBwd3DOd9+ECtUE2XOHOhTPJZG+HHCRpTSr3gMc+eGHFicRo+G3Xbz+8jGYv/94eWXd9ybVEREYhfLjgj9kxSLhKA8aQu6VtvFF/vN6Zs1C+4eZn4v1fHjg1nskAg9esC4BgMoiVTbKaEhE7JPqXI3gVS0ebOvz3bKKfHtROGcL8YrIiK1E8vw6FQz+6uZHWFmB5U/Ao9MkmKXXaBFi+B72vbdFwYODPYe4Et/FBYmd2uueJjBsrIcDmo8j9vsYfKbzmOvQ9pRUBB2ZLHbuNEPdZ5zTnzX/fa3kJ8fTEwiIvVBLEnbYcABwGDg8cjjsSCDkuTq2DG4+mng9zh9+WX48cfg7lGuPPlJxTlipaVwyy2w5y+yGfx6Z7694FY+29SZ0y/MJisr7Ohi17o1PP00HH10fNftvTcsWeJ3rhARkfiZq2YcycwaAAOdc28mL6TEy8/Pd7NmzQo7jJRVUuLnmwXliSf8xvSrVvkdGIJ24IE+sfjgg+DvFQ/n4J//hJ13hr59YetWv6qyYUOYOzc9JumXlPgiuT17xh/vmDFw6qkwY4a/XkREojOz2c65HcYmaprTthW4OrCoJCUEmbCB3yS+U6fkJGwAd90FV12VnHvFw8yvtuzb179u0ABuugk++wwmTQo3tlh9+KGvtffuu/Ffm5fnn1VkV0SkdmIZHp1kZjeZWXsza1X+CDwySZoPP/TJRBDDl875laNBl/qo6PTTU28D87vuggcf3PH42Wf7ZPbRR5MfU22MGgXNm8Oxx8Z/7d57+4UoStpERGon1jptVwEfA7MjD401ZpC1a/2wXRCLEZYuhW++CbaobjTz56dO79XChfDII9H/fJs08SVKvvoq2HmFiVBaCmPHwokn1m4XjQYN4OGH/fUiIhK/GhfsO+c6JSMQCU+HDv55+fJtQ1iJUj6VMJk9bQB33AGzZ/tEKey5Yjfd5HuYBg+O/v611/o5f0EPU9fVf/7jE/y69GKmcg09EZFUV2VPm5ndUuHrQZXeizLQI+kqyAK7gwbBihXQrVvi265OQYG/75dfJve+lU2c6PcXvesuv89rNM2a+YRt82b44YfkxhePf/3Lx1qX8iSbNsHMmVBUlLi4RETqi+qGR8+s8HXlHR2PDyAWCcnuu0PjxsHVasvJIeklLVKh9Idzvpdt7719b1p1Nm2Czp3h/vuTE1ttPPwwTJ4M2dm1b2PqVL9ydMaMxMUlIlJfVJe0WRVfR3staaxBA+je3T8n0o8/whlnwPTpiW03Fu3bwwEHhJu0mcHw4TBsmJ+7Vp2mTeFXv4Lnn0/dXQOaNvV7iNaFVpCKiNRedb+mXRVfR3staW7GDHjoocS3+eabvoJ+GH7zG58whrGBfHn5w/z82IvQ3nyzHzZ89tnAwqq1J56Ivvo1Xm3b+oeSNhGR+FWXtP3SzH40s43AgZGvy18neLq6ZKJp03zvXa9e4dz/ppt8Qd/arHSsq1tugUsv9QV0Y9W9Oxx3HPzlL35+W6pwDv7858T1mHbrpqRNRKQ2qkzanHNZzrkWzrmdnXMNI1+Xv07xdW4Sr5EjfdHULVsS1+bUqX44rEWLxLUZj7Zt/d6qyfbVVz7JcS7+Ieebb4bVq/2G7Kli5ky/qCNRte/y8vzesPEktCIiEludNqkHior8cGZhYWLaKyvzPTPJLvVR2ZgxvthuNbu1JdzNN/vevT/8If5r+/SBjz9OreLAo0f7rbZOPjkx7V16qV9Rm8zviYhIJlDSJsC2Wm2JWkG6Zg3ssw8ccURi2qtLHCNH+mK7yfDvf8O4cXDnnbDHHvFfb+b/zMxSI6lxzidtxx4LLVsmps0DDoBf/zr5K4pFRNKdkjYBEl+rbc89/cbiZ52VmPZqK9mlP+6+Gzp2hOuuq1s7jzwCAwYkJKQ6KSryw5lnn53Ydt96yxfrFRGR2ClpE8CXyIDEJW2p0EsEvgexa9fkJW0jR8Jrr9V98UPDhr7HblbIG8btvLMfYj7//MS2e/318OSTiW1TRCTTKWkTwNcR69MHWrVKTHu//GXqFIotKPC9OkFW4S8p8YlqTo5f0FFXl17qF3A89ljd26qLFSuCaTcvTytIRUTiFWjSZmbHm9lCM1tsZrdFeb+Jmb0ReX+GmXWMHG9kZi+a2edmNt/Mbq9wzdLI8blmpo3rE2jiRLjmmrq3s3q1/4W88851bysRTjrJF65dsya4e9x5py/XUVKSmPZatIDLL/c9d19/nZg24/Xll76n8rXXEt92Xh4sWgQ//5z4tkVEMlVgSZuZZQFDgQKgK3CWmXWtdNrFwHrn3D7AEOCRyPFBQBPnXB5wMPC78oQu4tfOue7Oufyg4pfamzbNPx9+eLhxlDvqKHj/fb+dVBAWL/YlPnJzE7vp++9/7yfrDxmSuDbjMXq0XxBx1FGJbzsvz5f8WLAg8W2LiGSqIHvaegKLnXNLnHNbgNeB/pXO6Q+8GPl6FHCsmRl+x4VsM2sINAO2AD8GGKsAf/2rn0Rf1/pZ06b5OV09eiQkrIRZvz6YuXa33OL3bv3jHxPbbrt2MHQoXHxxYtuN1ejRvmTLXnslvm1tZyUiEr8gk7Z2QMUZMYWRY1HPcc6VAj8Au+ETuGJgNbAceMw5ty5yjQMmmtlsM7ssuPDrHzO/EKGuw4jTpvk9Khs3TkxcifDPf0Lr1onv2fnwQz9R/447/IrZRLv0Uj8/MNkWL4ZPPw2uXty++8LChXDOOcG0LyKSiYJM2qJtKl+5n6Oqc3oCZcBeQCfgRjMrH9w63Dl3EH7Y9SozOzLqzc0uM7NZZjZr7dq1tfoA9U2iyn6ceCJceGGdw0mogw/2PYiJXkX6pz/5P7frr09suxUtXAhXXJHcPVRHj/bPQSVtWVnQubNqtYmIxCPIpK0QaF/hdQ6wqqpzIkOhuwDrgLOB95xzJc65NcBUIB/AObcq8rwGGINP8HbgnHvOOZfvnMtv06ZNwj5UJktUgd0774SLLqp7PImUmwv775/4pG3UKF9zrFmzxLZb0apV8Mwz8I9/BHePyi66yH+28r8TQXj/fT+0LCIisQkyaZsJ7GtmncysMXAmMK7SOeOACyJfDwQ+cM45/JDoMeZlA72BBWaWbWY7A0SO9wW+CPAz1CvlPW3Ll9e+jeXLYePGxMSTaAUFfouo4uK6t/XTT36f1uzsbfOzgnL00b6n8PHHk7dfZ5s2wW+l9b//waOPwrp1NZ8rIiIBJm2ROWpXAxOA+cCbzrl5ZjbYzMp3MRwG7GZmi4EbgPKyIEOB5viEbCYwwjn3GbA7MMXMPgX+C7zjnHsvqM9Q3+yyC5xxhl+MUFvXXAM9o/Z9hq+gwCdaH35Y97YGD4YDD/TJW9DM4Kab/DBpMjaS/+c/4emngy+QrMUIIiLxMZcqpesDlJ+f72aFXVq+HnAO2rb1c9pGjAg7mh1t3gzPPut7kNpVXhIThyVL/FDr2Wcn73OWlvrJ++3awZQpwd7r8MN9MjpnTrD3WbnSFyN+6im4+upg7yUikk7MbHa0smbaEUF2UFpau+sWLYLvvvNlIlJRkya+9lldEjbw87AaNUp8iY/qNGzo5wr26pW4Ar7RrFzpV/8GPTQKvpRIy5bqaRMRiZWSNtnOHXf43rLamDrVP6dKUd1oNm6El1+u/by9yZP9ysrbbw+mfll1LrnEz2tLZAHfysaM8c8DBwZ3j3Jmfoj5u++Cv5eISCZQ0ibb2XVXX4T2hx/iv3baNH99ly6JjytR1q2D887bVtIiXiNG+BWVN9yQ2Lhi5RxMmhTc1lajRkHXrsn7Hk6aVPvvhYhIfaOkTbZTlxWk114Lf/87NEjhv1V1Lf0xfDh89FGwJT6q8913fs7gn/6U+LZLSvzQ+KBBiW+7KkH2GoqIZJoU/vUqYahLgd1u3aB/5Y3KUlBBgR/mjKf0R1ERfP+9T0g7dQoutpq0aQPnn++T47ruXFFZo0Z+kcO99ya23eqsWAEnn5yYFb0iIplOSZtsp7Y9bfPmwRtvwM8/Jz6mRCsv/fHRR7Ff8+CDvoJ/KtQUu/FGvzvC0KGJbbf8e2fR9ikJyC67+DIm06cn754iIulKSZtsZ/fdffmFAw6I77rXXvP7SCar+GtdHHEE7LQTzJwZ2/lffw1PPAEnnACtWgUbWyy6dPG9U0OHJq5O3Lp1vhfv739PTHuxatHC/0dBK0hFRGrWMOwAJLU0aODrZsVr2jTo0cPvEJDqmjSBpUt9khKLW2/1e2Q++GCgYcXlppt80rlgARx0UN3bGzfODxd361b3tuLVrZuSNhGRWKinTXZQUgLffBPf+TNmpG59tmhiTdj+8x8YOdInbjk5wcYUj1/9yieeiUjYwK8azc3122UlW16eTz63bEn+vUVE0omSNtnB5ZfH98v7s8/8MF06JW2bN8Ppp8MLL1R/3nvvQfv2vmcrlZhB48Y+Ya7LXrHgy7tMnOgL6iZzPlu5nj190eDvv0/+vUVE0omSNtlBhw6wenXsPR/lO4SlclHdypo08UNyI0dWf94f/whz5/o5cKmoXz9foqMuu9G9/bZP/pKxC0I0p5ziV63uuWc49xcRSRdK2mQHHTr4JGDFitjOv+wyP1SXSsOHsSgv/RFtMn9Rkd+gHVJj8UFVBg6E//63bvuRHnaYr/vWu3fi4hIRkcRT0iY7iLdWm9m2a9LJ8cf7YdJopT8eftjPtYo1cQ3LhRdC69bw6KO1b6NTJ7j55nCLIp99th+uFhGRqilpkx3Ek7QVFvpSH599FmxMQTjySD/sWXl3hGXL4LHHfBLRvn04scVqp53gqqt8rbMFC+K/fvp0+Oc//U4IYZsxI+wIRERSm5I22UFOju9pys+v+dwpU+DVV/2cqHTTtKnfhL1jx+2P33KL73V66KFQworbVVf5z/Lyy/FfO2QIXHFFOAsQKsrL8wsqarPnrYhIfaE6bbKDJk18iYtYTJvme3sOPDDYmILyl79s/3rKFHjzTb+VU6r3spVr08YvBtl///iu+/lneOcdOPdcX4cuTHl5/nnevPRahSwikkzqaZOoVq+OreDptGm+ZEM6b/y9ZQusWuW//vTTbXO80skBB/jewbKy2K+ZONEX1A1r1WhF5UmbiuyKiFRNSZtEdf31cOqp1Z9TVOTLYaRTqY9oDjsMTjwRHnjAz+f74ov02NmhsldfhX339d+XWIwaBS1bwtFHBxpWTDp08D1+6bigRdJPWZkvdfPAA/45nv/sSGqor99DDY9KVLm5MGaM30u0qlWFq1b5Ibl0TtrKyqBoTTFuRSHFc8dyb/YAnuuVw5gJ2aEPGcZr7739PqnDh8Pvf1/9uc75ocgBA1Kjl9QM/vGPsKOQ+qCsDE7pV8zKGYX0LU7vn/n6qj5/D9XTJlHl5vphw2+/rfqczp39cFZBQfLiSrTx46Hp2kK+oBsPu9uYXtSNwhkrd1hRmg569/bbWw0ZUvNqUDOYPRuefDI5scXqu+/qVihYpCbjx8PKGYVML+rGQ2n+M19f1efvoZI2iapDB/9c3RZJmfDLdc4cOH7zWBrhs5xGlNKveAxz54YcWC3dfLMvdDxqVPXnOecTt+bNkxJWTJ5/3i+qKJ9fKBKEOXOgb3Hm/MzXR/X5e6ikTaKqqVbb1q3wi1/suPoy3fToAZOyB1ASmSlQQkMmZJ9C9+4hB1ZLJ54I++3ni+1WlVSXlPhh7Zr2XU22zp39sxYjSJB69IAJO2XOz3x91KMHTGhWP7+HStokql/8wtf9OvTQ6O8vWODnT+2yS3LjSrSCAmjXK4dezedxuz1Mr+bzyOnVLm2HfBs0gKFD4Zlnqq69Nnmy36Jrt92SG1tNtIJUkqGgAIp2zeEA5nFb5Gd+z4PT92e+PioogKKW/nt4Cw/Tzeax1yH143uohQgS1U47+Z0OqjJ1qn9O50UI4OuTjZmQzfjxnZk791YGd/f/IKTzZNZjj63+/dGj/erY449PTjyxatUK9tpLSZsEa/58WLwqm9+c0JnmvW/lsG/gjTdgw4bU+4+MRLduHSz/Lpuj+nZmVZtb+eoVuPui9P53O1bqaZMqzZnje2WimTbN73m5zz7JjSkIWVl+WPGuu/xzJvzgr14NF120YwJUVua3rTrhBGjWLJzYqpOXp6RNgvX1136l9Ysv+p/5K67wScB994UdmcRq6FC/b/Sf/wwvvQRdusDjj2fGPOuaKGmTKt1zT9WlI6ZN8/XNwt7+SKJr0sTv7PD449sfnzoV1qxJjYK60Vx5JdxwQ9hRSCY76aTtpwcccABcfjk8/TR8+WW4sUnNfvoJ/vpX/33cf38/JeTGG33N0PffDzu64Clpkyrl5kZfiLB1KwwcCGedlfyYJDatWsHFF/uCuytXbjveti1cfTX85jfhxVadk0+G884LOwrJRCUl8Nprvre5cm/6/ff7ldQ33hhObBK7L77wv4Mq7lpz7rl+z+h99w0vrmRR0iZVys31G3hX3sS7QQP44x/hzDPDiUtic/31/hdUxRW+XbrAU0+lVqmPisrK/FZiVa1aFqmtv/0Nzj4bPvpox/dat/b7DX/wAXz1VdJDkzj07AmFhb4mZbmmTeGRR+rHjipK2qRKVdVqW7rUd1FLauvYEQYNgmefhR9/hCVL/LD21q1hR1a1khI4+GAYNizsSCSTfP+9n7PWty8cc0z0c666yi9SKC89I6nnm2/8v1877RR9as6UKX6eWyZT0iZVqqpW23nn+X/8JPXdcgucf77f3eJvf/P7jG7cGHZUVWva1A9xaDGCJNJ99/n/uDzxRNXzcBs39gsUQAWeU5Fzftu9k06q+pyRI/2waWFh8uJKNiVtUqW8PL969Igjth3bvBlmzvRbJknqO+gg/z/PTz7xvVcHHpi6Q6PltIJUEunLL/0ig8sv94sOanL//dCtm19RKqljyhSYMcOvfK/K9df75C7di75XR0mbVCk7G448cvsCunPm+MTtsMPCi0tiV1YGp/Qt5s6BC7l0wyNs+WIhp/Qrpqws7Miqlpfnh3KLi8OORDLBDz9Afr5PxmJx6qn+mljPl+R49FE/9/DCC6s+p+KUkMpzsTNFoEmbmR1vZgvNbLGZ3Rbl/SZm9kbk/Rlm1jFyvJGZvWhmn5vZfDO7PdY2JbHefRfGjdv2eto0/6ykLT2MHw8r/1vI7C3d+BO3MXtz6m+snJfn/7c8b17YkUgmOPRQmD7d/8KPRV4eXHaZrwU2f36wsUls5s+Ht97y8w532qn6c2++2U8Bef755MSWbIElbWaWBQwFCoCuwFlm1rXSaRcD651z+wBDgEcixwcBTZxzecDBwO/MrGOMbUoCPfEEPPTQttdTp/p5H3vsEV5MErt03Fj5iCN8stmlS9iRSDorKfF1CouK4r928GA/0nDTTYmPS+I3fLif73rVVTWfe9BBvrJBTcldugqyp60nsNg5t8Q5twV4Hehf6Zz+wIuRr0cBx5qZAQ7INrOGQDNgC/BjjG1KAnXosP1ChDvv9CUjJD306AETs9NrY+XddvNbbLVoEXYkks6eecYnXdFKfNSkTRtfXPy//9WihFTw0EN+TlubNrGd/9prvlB3JgoyaWsHrKjwujByLOo5zrlS4AdgN3wCVwysBpYDjznn1sXYJgBmdpmZzTKzWWvXrq37p6mncnP9lkibN/vXBx2UuoVZZUcFBdCuVw69ms/j9sjm2Dm9Un9j5U8+gddfDzsKSVfr1vm6a8cdV/3E9epccw0sWuT3w5XwOAcNG/pSQPEoK4N33sm8ra2CTNqiLayu/MdX1Tk9gTJgL6ATcKOZ7R1jm/6gc8855/Kdc/ltYk3PZQflZT8KC2H2bL9vZUlJuDFJ7LKyYMyEbAa/1pnswbcy+LXOjJmQnfL7q77wQtVbqInU5P77/UT06kp81KRxY9h1V//LX9tbhaOoCLp29b934jVypN9LesKExMcVpiCTtkKgfYXXOUDljub/f05kKHQXYB1wNvCec67EObcGmArkx9imJFB5gd1ly/wv0gsv9DsiSPrIyvL/eN11l39O9YQN/GTwtWvh22/DjkTSzfz5fhHBZZf5v0d1ddVVfp7l+vV1b0viM2wYLFhQu97OU0+Fdu3gsccSH1eYgvz1OxPY18w6mVlj4ExgXKVzxgEXRL4eCHzgnHP4IdFjzMsGegMLYmxTEqh3b19+4cgj/crR3r3T45e+pLfyX7aq1ybxatDA/+dk8ODEtHfllbBhQ+Lak9iUlsKQIX67qtrUBW3cGK691m8i/7//JT6+sASWtEXmqF0NTADmA2865+aZ2WAzOzly2jBgNzNbDNwAlJfwGAo0B77AJ2ojnHOfVdVmUJ9B/AqcTp18zazPP4fDDw87IqkPlLRJbe23H4wdG/uk9ZoceCBccgn89a+wcGFi2pSajRzpR3jqsoL3sstg550zq7fNXKbN0osiPz/fzZo1K+ww0tZzz/lSHy+9BBMnQp8+YUck9cHuu/seE+1DKrEoLYU77vALCNq3r/n8eKxZA/vsA0cd5euFSbCc8wsPfvrJzyesy5Scm27yJYT+9z9o0iRxMQbNzGY75/IrH28YRjCSXkaM8MUpGzSAXr3Cjkbqi+nT/ZwUkVg8+6yvmn/44YlP2tq2hbvv9v8Wrl8PLVsmtn3Z0RNP+KoFdZ1Dff/98MgjmTOtRz1tUq2yMvj1r+GLL3wX8wUXZM5ffpHaKivz/3ufM8fXwiso0M9FmNav9z1h3bvDv/9d+xWj1dmyxbfbqFHi2w6C/o5ur7jY9+Cl+t7L5arqadM6QKlSWRmc0q+YddMXcsn6Rxh6bervWymZ46uv4LrrYMWKms9NpvKfi3vPWshP9z7CvWfp5yJsgwf7xQJDhgSTsIGf2N6oEfz4o+8FTmXp/Hf08899uZ9Ellf9/ntfvurJJxPXZliUtEmVxo+HlTMKmVPi962cXpT6+1ZK5tiwAf7yF0i1TvLyn4vpRd14yOnnImwLF/pFApdc4hcNBO2ii/xcyw0bgr9XbaXz39HHH/fzWBNZWmq33SA/3ydt5YXi05WSNqlSOu5bKZnjgAN8r0mqrSCdMwf66OciZbRs6VcJJqskx513+h0XHnggOferjZkz4bii9Ps7unIlvPoqXHyxT7QS6aabfN3Hl19ObLvJpqRNqpSO+1ZK5sjOhr33Tr2krUcPGNdg+5+Ld5vo5yIsbdv6Yrq7756c+/Xo4XvbnnzSD+Gnmu+/9+UyxpJ+/3b/5S9+aPf66xPf9rHH+jmPjz0GW7cmvv1kUdImVUrXfSslc+TlpV7S1q4dLCvLoUdj/3PRo/E8Fm9qx+efZ94+h6mstNQnT2EUTv3DH6BpU7j55uTfuyazZsHSpbBrN/9v921p8m/3jz/6FcCDBvnaoIlm5r9fCxbAf/6T+PaTRUmbVCld962UzJGX52s1lZaGHck2Q4YAO2Vz14v+5+KB1ztz4unZ3HGH3/IolWLNZC+84EtwLFuW/HvvsYcfJt28GX7+Ofn3j6Z8m61+/eDrr2HaXP9vd/PBt3LrC51p2CKbyZPDjbE6P/0Ep50WbCI8aJDf2eeoo4K7R9BU8kNEUlZZWWqVKdi82c+1O/FE+POftx3futUXdn3kEf/e66/74V0JxoYNsO++0K0bfPBBcCtGq7N1q79vGPeu7O234ZxzYNSo6MXPN26EQw7xf25z5sCeeyY/xlTjXGp876qikh8iknZSKWEDX1F9/vwdJ703aAAPP+znVk2dGk7vT33yhz/4uVtBlvioSYMG/t7LlvnacGF55hno3x86d6569ezOO/uE7scf4ayzUq83+OOPk7tK/NZbfc3RdKSkTURS2nnn+TIAYfv5Z9/T1qgRtGgR/Zwrr4T/+z/o2tX/T/7bb5MbY32waJFfBHDxxaTExPrLLoOzz4YffkjufbduhdtugyuugN/8Bj76qPrFGN26wdNPw+TJcM89SQuzRs75rccuvDB5c0IbNIBXXvE/q+lGSZuIpLR582DSpLCj8LXAOnXyPTzVKd/i6G9/g/33hylTgo+tPsnJ8VsTpUrJjYcegu++gz/+Mbn3HTvWD8dffjmMGRPbcPwFF/hkd8SI1KkzN2kSfPaZL8mRrF7Ta67xvfhPPJGc+yWS5rSJSEq74AI//LRyZXgxbNniy4/stx+8/35s13z9tV+BvXQpvPQSnH56oCFKiC6+GP7xD7+5+T77BHuv8rlYzvkiugUF8SU7P//sE7ZUmdfWp4//c/v6a7/rRLJcdJGfe7p8ObRunbz7xkpz2kQkLeXlwapVvqBpWF57zSeN8axs69TJz2875BA44ww/xFsP/o8cmNJSOPlkUrKq/x/+4BOOoEuALF0KRx7pd4Ew88Oi8fZONWvmE7ayMj8fbsuWQEKNyZw5/j9kv/99chM28D17P//s56GmEyVtIpLS8vL8c1j12pzzBTnz8nw5Eo2imgAAF8ZJREFUhXjstpsf/jn9dP8L/bPPgomxPhg2DN56y5eGSDV77gl33+1LgQQ1yX/2bDj0UP9zsGZN3dubPNnPh7vllrq3VVtffeWHu3/3u+Tfu2tXeOopvzAjnWh4VERS2urVvofl4Yd9VfNkmzwZjj4aXnwRzj+/dm1s3errQ/3qV/51qpcbSDU//OCHHbt29RPu69uf3bvv+sR/t9381wcckJh2r73WL+oYORIGDkxMm/EqLYWGDcO5dyrT8KiIpKU99/R7KYaRsIEfjnr/fTjzzNq30aDBtoRtwgTfZiJ6S+qLVCjxEavp032PYKJMmuT/09K5M3zySeISNoBHH4Vevfz8rkWLEtduLBYu9P95CTthmzPHr/ouKws3jlgpaRORtBDWoIAZHHNM4ubcbNrka1Idemhq7l2ZapYt83tS/va3cNBBYUdTPef8cOMll/iaaInwq1/5+VeTJ8NeeyWmzXKNG8Obb/oyNueck7yfsQ0bID/flywJ26JFvhTKv/4VdiSxUdImIinv8cehffvkJ26/+x3ce29i2+zfHz780P9SP+wwP2wqVevQAf7+d9/blurMfG/g2rXw4IO1b2fLFrjrLp/cNGvmpwbsvHPi4qyoQwe/ivKpp5LXi/nMM1BU5Ovbhe3UU/2iocceCzuS2ChpE5GU17y5X72ZzJ0Gli71k9+DmPjeu7cf6mrZ0vfiffll4u+RCcrn/p19duqUqKjJwQf7MjVDhsCSJfFfv2EDHH+8r/v2zjuJjy+aPn38MClAYWGw99q82fec9ukDv/xlsPeKRcOGcMMN/udx6tSwo6mZkjYRSXlhrCD98599wnDttcG0v88+/hfF4MG+CK9sr6zMb+w9bFjYkcTvj3/0Q47xrsxcscIPh06Z4uu+nXNOMPFV5ZlnfC3CL74I7h6vvALffBN8eZR4/Pa30KqVn+OX6pS0iUjK69bNPycraVu/Hl54wZcDyMkJ7j6tW/tf7GZ+fttdd/mVpgLDh8N//hPcsGCQ9trLD+f27Bn7kP4XX/ge2BUr4L334Nxzg40xmv79/Z/3wIF++DIIr7/utx877rhg2q+N7Gy44w4fV6oX1NBCWxFJeS1aQG5u8pK2p5+G4mI/ATxZRo/2PTQLFvhelmbNknfvVPPDD3DnnXD44TBoUNjR1M5118V3fsuW0LEjPPvstv+kJNuee/pC0scd5/dUfeWVxM9ze+cdPwSbaquAb7wx7Ahio6RNRNLCpZdu29czaCed5Oe6HHhgcu4HcPvtPlG74Qa/A8S4cam5vU4yPPign8z/7rup98s9Hs7BG2/4fS6rSj4nTvTlbNq188OiYX/eX//aD9nfdZcvTXP55Ylru6TEDxt36pS4NhNp61b/c3fYYdC2bdjRRKfhURFJC3fe6espJUNeXjiV4q+7zhc6nTPHlwRZsSL5MYRt7Vo/Uf2CC3xZiHT35JN+g/KNG7c/7pxfmdyvn+9dg/ATtnK33+5XVcayCX2sZs70PYmpXOd+yRL/uZ96KuxIqqakTUTSxg8/+GHLoGzd6odE580L7h41Oe00X8x3//3rZ09bmzbwwQd1K5mRKsz8gpZvv4WHHtp2fMsWP/l98GD/fOml4cUYTYMGMGoUnHde4tp89FH/s7vffolrM9H22cfP6/vb34L9d6YuNDwqImlhwQKfyLzySnD1nd55x9eEO+igxFaej9dhh/lhGvCJ6tSpPqGcMwd69ICCAj/kFpSyMr8xe7LvN2uW710L+n7J1LOnT34efxz23tuXknn7bfj0U7jvPrjnntTpYauoPKaXXvILI+oyv23JEj9n8+abU39hyc03w9ixMGIEXH112NHsSHuPikha2LLF12u78cbtey0S6cgjfS24xYv93JtUcO218MKTxfyicSEnlIxlYvYA2vXKYcyE7EASm7IyOKVfMStnFNK3OLn3O65oLO82HkCnI4K7XxiWL4cDOhXTwQo5aetYxrgB7Lx/DjM+T/3POGSIn2f5+OP+uTauvhqee84nrIne1SEIhx/u9zz+6qvwttmqau9RnHMZ/zj44IOdiKS/bt2cO+GEYNqePt05cO6JJ4Jpv7ZGjnRu/6wFbgsNnQO3hYauW+OF7q23nPv+e+e6dNnx8dxz/trly6O//8or/v0FC3Z8LyfHuQObbn+//Wyhy8nZds7Eif76jz+O3v7Uqf798eOjvz9njn9/1Ch/vy62/f16NPefL1O89ZZzeU3S8zNu3ercqac617Dhtu9rPL7/3rlmzZy78MLExxaUMWOc69jRucWLw4sBmOWi5DMaHhWRtJGXF1zV8sceg1128ftGppL58+HkrWP5f+3de5BU5ZnH8e/DcFPwxkXXgGy8gBGYLJeRiZWSIuUGGJxw8cKlqEjULTUrW5sYN6hbuxpMUhjimki2NKJGNEp04w6iJYtsZRO31oXiNgITgxCCOmghSkRuLjPw7B/vQdrm9DBAd58+3b9PVVf39Hn7zHPeOqfnmfe8l060AtCJVq5saaCxcRYjR8aPcO3dOzx37hy/vWfP8Ny169Hbm5qgbttnf98Eb+DlM2cxcGAoc/rp4fm00+L33717eD7jjPjthzu49+gRylzZ/NnfN2ZvOL76+tgqSZ21a+HKA+k8RrMwZ96wYTB5cjiWw+dXe5x1VrjdWKojRuOMHw/19ckvZh8rLpMrt4da2kTKww9/GFrDPvoov/s9dMj9u991//7387vffHjxRfdh3YvXSlPuvy8J5XCMa9a4d+3qPn9+0pEUz/797s3NyfxucrS0qU+biKTG+vVhLqvp04+09pS7w32+mldsY8zeBpZ2m0Tf2j4F72NWrr8vCeVyjG+/HRaYb6+nngoDLn7wA+jSpXBxFYJ7WBu1X78wcKTYcvVpK2jSZmZjgZ8CVcCj7j4na3sX4ElgOPAhMMXdt5rZdCBzZbIvAsPcvdHMfgucC+yPto129/fbikNJm4jk8uGHsHp1WMC6FEfxwZHRlY2NYamdYo3mLNffl4RyOsYVK+CTT8LasLkcOgRf+EL452rlytK9ttpy771hdG9TE592DSiWoidtZlYFvAl8FWgGVgLT3P33GWX+Fviiu99iZlOBSe4+JWs/1cAL7n5B9PNvgdvdvd1ZmJI2kfKxaVNYF3Ho0Pzsb/bsMMnpxo0wYEB+9ilSrg4dguHDw6oda9fmHg26aBFMmhTWGp0yJb5Mqfvgg9DSNnVq6NdXTLmStkJOrjsC2OzuW9z9APArYEJWmQnAguj1r4ErzI7Kx6cBCwsYp4ikyDe+EabByIf9++FnPwudjpWwiRxbhw5hzrY9e2DaNGhtjS83d25YAeHqq4saXl716gU33AC//GVIUktBIZO2PkDmIizN0XuxZdy9FdgF9MwqM4Wjk7ZfmFmjmf1TTJIHgJndZGarzGzVjh07TvQYRKTEVFeHvm35uEmwYEFYNqmYC8OLpN3AgWHetVdfDWuUZnvttfC47bYSHYF5HL797XBr+7nnko4kKGTSFpdMZX/NtlnGzGqBfe6+IWP7dHevBi6PHrELbbj7I+5e4+41vY9nfLKIlLTqavjoI9i27eT2c/BgmDD00kvDpLoi0n7Tp8PNN8N994XBQZl69QpT51x/fTKx5dOFF8K6dflr3T9ZhUzamoHzMn7uC2Q3MH5axsw6AmcAOzO2TyWrlc3dt0XPu4FnCLdhRaRCDB4cnjdsaLvcsfzpT7BvX1i2Jo2dpEWS9pOfhO4Fl1322fcHDID584/M15d2gwaF74iDB5OOpLBJ20qgv5mdb2adCQnY4qwyi4EZ0etrgN9E85NgZh2Aawl94Yje62hmvaLXnYB64CS/ukUkTaqrw/P69Se3n4suConbVVedfEwilahrV7j11jAKdts2aGgI19O8eaWR4OTTvHmhj94994QpQJI6voLdbXb3VjObCSwlTPnxuLs3mdlswqRxi4HHgKfMbDOhhW1qxi5GAs3uviXjvS7A0ihhqwL+E5hfqGMQkdLTowe8/PLJjR7dvj3sp3Pn/MUlUql27IDB5+/lc97Mla2L+PmLE1n2QvmsH3vwICx8dC+nNjfzyexF3N1tIo8UcD3etmhyXRGpOBMnhoXh16zRrVGRk/XSS3DHVRtZ2zKYTrTSQkdquzcxe+GAkl+mqz1eegnunraR5XuKd3xJTPkhIlIQb74Z+tPkmm6gLRs3wuLF8LWvKWETyYe1a6G+NW5t1YQDy5O1a2H03tI4PiVtIpI6y5eHofibNh3/Z++/P9wWnTkz/3GJVKKhQ2FZt4m0RD2uWujI0m6TGDIk4cDyZOhQeKVEjk9Jm4ikzokORti+HZ58EmbMgLPPzn9cIpWorg761PaltnsTd9ocars30be2D3V1SUeWH6V0fCmf9k5EKtEll4QRa+vXw+TJ7f/cM8/AgQPwne8ULjaRSlNVBQ1Lu7FkyQAaG2cxO+Vrq2YrpePTQAQRSaVLLoGLLw5rHLaXexh8MHx44eISETlZGoggImWluhqamtpf3j0MPFDCJiJppaRNRFJp3jx4/fX2lW1thWHDwiztIiJppT5tIpJK55zT/rLPPw+NjaBliEUkzdTSJiKpdHjd0KVL2y7nDnPnQv/+MH58cWITESkEtbSJSCp17QoPPQQtLTBmTO5yv/sdrF4NDz8MHfRvqoikmL7CRCSVOnSAQYOOPVfb3Lnhtuh11xUnLhGRQlFLm4ik1uDB8OKLbZf53vfgnXfglFOKE5OISKGopU1EUqu6GnbsCCsd5FJTA5MmFS8mEZFCUdImIqlVXQ09e4aWtGzvvgs33ghvvVX8uERECkFJm4ik1le+Elraao6aNxwefBCeeAIOHix6WCIiBaE+bSKSWrlGg+7eHUaLXn01XHBBcWMSESkUtbSJSKrNmQPTp3/2vUcfhV274Pbbk4lJRKQQlLSJSKpt3w4NDUdug7a0wAMPwMiRMGJEsrGJiOSTbo+KSKpVV8P+/bBlS1j1YP9+mDgRxo1LOjIRkfxS0iYiqVZdHZ43bAhJ2+mnh0EIIiLlRkmbiKTaoEFgFlZG6NcPPv4YRo0K74mIlBMlbSKSaqeeCvX1cOaZcNddsG4dbN0KXbokHZmISH5pIIKIpF5DQ2hZe+UVGD0aOurfUREpQ0raRCTVDh6ESWP28vBtG/kH7mP98xuZNGavJtUVkbKjpE1EUm3JEnj7f5ppbB3Mj7iDFXsH07xiG0uWJB2ZiEh+KWkTkVRbuxbG/t8iOtEKQCdaGbO3gcbGhAMTEckzJW0ikmpDh8KybhNpicZVtdCRpd0mMWRIwoGJiOSZkjYRSbW6OuhT25fa7k3caXOo7d5E39o+1NUlHZmISH5pjJWIpFpVFTQs7caSJQNobJzF7CEhkauqSjoyEZH8UtImIqlXVRXmaquvTzoSEZHC0e1RERERkRQoaNJmZmPNbKOZbTazO2K2dzGzZ6PtK8zs89H7082sMeNxyMyGRNuGm9n66DMPmmmxGhERESl/BUvazKwK+FegDhgITDOzgVnFbgT+7O4XAQ8A9wG4+9PuPsTdhwBfB7a6++EB/A8BNwH9o8fYQh2DiIiISKkoZEvbCGCzu29x9wPAr4AJWWUmAAui178GrohpOZsGLAQws3OB0939f93dgSeBiYU6ABEREZFSUcikrQ/wTsbPzdF7sWXcvRXYBfTMKjOFKGmLyjcfY58iIiIiZaeQSVtcXzM/njJmVgvsc/cNx7HPw5+9ycxWmdmqHTt2tCdeERERkZJVyKStGTgv4+e+wLu5yphZR+AMYGfG9qkcaWU7XL7vMfYJgLs/4u417l7Tu3fvEzoAERERkVJRyKRtJdDfzM43s86EBGxxVpnFwIzo9TXAb6K+aphZB+BaQl84ANz9PWC3mX0p6vt2HfBCAY9BREREpCQUbHJdd281s5nAUqAKeNzdm8xsNrDK3RcDjwFPmdlmQgvb1IxdjASa3X1L1q6/CTwBnAIsiR4iIiIiZc2ihq2yVlNT46tWrUo6DBEREZFjMrPV7l5z1PuVkLSZ2Q7graTjKBG9gA+SDqJEqW7iqV5yU93EU73kprqJp3r5rL9096M65FdE0iZHmNmquOxdVDe5qF5yU93EU73kprqJp3ppH609KiIiIpICStpEREREUkBJW+V5JOkASpjqJp7qJTfVTTzVS26qm3iql3ZQnzYRERGRFFBLm4iIiEgKKGkrQ2Z2npn9l5m9YWZNZvb3MWVGmdkuM2uMHv+cRKxJMLOtZrY+Ou6jJvCz4EEz22xm68xsWBJxFpOZXZxxLjSa2cdm9q2sMhVzzpjZ42b2vpltyHivh5ktM7NN0fNZOT47IyqzycxmxJVJqxz1MtfM/hBdKw1mdmaOz7Z53aVdjrq5x8y2ZVwz43J8dqyZbYy+c+4oXtSFl6Nens2ok61m1pjjs2V9zpwI3R4tQ2Z2LnCuu68xs9OA1cBEd/99RplRwO3uXp9QmIkxs61AjbvHzgkUfbH+HTAOqAV+6u61xYswWWZWBWwDat39rYz3R1Eh54yZjQT2AE+6++DovR8BO919TvSH9Sx3n5X1uR7AKqAGcMK1N9zd/1zUAyiQHPUymrAEYauZ3QeQXS9Rua20cd2lXY66uQfY4+4/buNzVcCbwFcJ62uvBKZlfl+nWVy9ZG2/H9jl7rNjtm2ljM+ZE6GWtjLk7u+5+5ro9W7gDaBPslGlygTCF4y7+3LgzCgRrhRXAH/MTNgqjbu/SlhaL9MEYEH0egEwMeajY4Bl7r4zStSWAWMLFmiRxdWLu7/i7q3Rj8uBvkUPrATkOGfaYwSw2d23uPsBwnrbE/IaXILaqpdoDfHJwMKiBpViStrKnJl9HhgKrIjZfJmZvW5mS8xsUFEDS5YDr5jZajO7KWZ7H+CdjJ+bqaykdyq5v0Qr9ZwBOMfd34PwjxFwdkyZSj93biD3etDHuu7K1czo1vHjOW6pV/I5czmw3d035dheqedMTkraypiZdQeeB77l7h9nbV5DWCbjr4B5wKJix5egL7v7MKAOuDVqvs9kMZ+piH4EZtYZGA/8W8zmSj5n2quSz51/BFqBp3MUOdZ1V44eAi4EhgDvAffHlKnYcwaYRtutbJV4zrRJSVuZMrNOhITtaXf/9+zt7v6xu++JXr8MdDKzXkUOMxHu/m70/D7QQLg9kakZOC/j577Au8WJLnF1wBp33569oZLPmcj2w7fJo+f3Y8pU5LkTDbioB6Z7jo7S7bjuyo67b3f3g+5+CJhP/DFX6jnTEbgKeDZXmUo8Z45FSVsZivoJPAa84e7/kqPMX0TlMLMRhHPhw+JFmQwz6xYNzsDMugGjgQ1ZxRYD14VBpPYlQifZ94ocalJy/udbqedMhsXA4dGgM4AXYsosBUab2VnRrbDR0Xtly8zGArOA8e6+L0eZ9lx3ZSerL+wk4o95JdDfzM6PWrqnEs61cvfXwB/cvTluY6WeM8fSMekApCC+DHwdWJ8xlPouoB+Auz8MXAN808xagf3A1Fz/IZeZc4CGKPfoCDzj7v9hZrfAp3XzMmHk6GZgH3B9QrEWlZmdShjBdnPGe5n1UjHnjJktBEYBvcysGbgbmAM8Z2Y3Am8D10Zla4Bb3P1v3H2nmd1L+EMMMNvdT6RzeknKUS93Al2AZdF1tdzdbzGzzwGPuvs4clx3CRxCweSom1FmNoRwu3Mr0bWVWTfRqNuZhOS+Cnjc3ZsSOISCiKsXd3+MmL6zlXbOnAhN+SEiIiKSAro9KiIiIpICStpEREREUkBJm4iIiEgKKGkTERERSQElbSIiIiIpoKRNROQ4mNmejNfjzGyTmfVLMiYRqQyap01E5ASY2RWE5bxGu/vbSccjIuVPSZuIyHEys8sJyxKNc/c/Jh2PiFQGTa4rInIczKwF2A2Mcvd1SccjIpVDfdpERI5PC/AacGPSgYhIZVHSJiJyfA4Bk4FLzeyupIMRkcqhPm0iIsfJ3feZWT3w32a2PVoAW0SkoJS0iYicAHffaWZjgVfN7AN3fyHpmESkvGkggoiIiEgKqE+biIiISAooaRMRERFJASVtIiIiIimgpE1EREQkBZS0iYiIiKSAkjYRERGRFFDSJiIiIpICStpEREREUuD/AUDl4/nGZFnxAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "plt.plot(range(1,20), error_rate, color='blue', linestyle = 'dashed', marker = 'o', markerfacecolor='red', markersize =5)\n",
    "plt.title('Error Rate vs. K Value')\n",
    "plt.xlabel('K')\n",
    "plt.ylabel('Error Rate')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "logmodel= LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ASUS\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:432: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n",
      "C:\\Users\\ASUS\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:469: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",
      "  \"this warning.\", FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
       "                   multi_class='warn', n_jobs=None, penalty='l2',\n",
       "                   random_state=None, solver='warn', tol=0.0001, verbose=0,\n",
       "                   warm_start=False)"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "logmodel.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7515151515151515"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "logmodel.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "dtree = DecisionTreeClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,\n",
       "                       max_features=None, max_leaf_nodes=None,\n",
       "                       min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "                       min_samples_leaf=1, min_samples_split=2,\n",
       "                       min_weight_fraction_leaf=0.0, presort=False,\n",
       "                       random_state=None, splitter='best')"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dtree.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8272727272727273"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dtree.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "feature_names = ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',\n",
       "                       max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
       "                       min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "                       min_samples_leaf=1, min_samples_split=2,\n",
       "                       min_weight_fraction_leaf=0.0, n_estimators=200,\n",
       "                       n_jobs=None, oob_score=False, random_state=None,\n",
       "                       verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "rfc = RandomForestClassifier(n_estimators = 200)\n",
    "rfc.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8666666666666667"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rfc.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = lm.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x1998548a278>"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x199854e8128>]"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import classification_report, confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = knn.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.96      0.99      0.97       158\n",
      "           1       0.88      0.95      0.91       152\n",
      "           2       0.93      0.85      0.89       199\n",
      "           3       0.92      0.93      0.93       151\n",
      "\n",
      "    accuracy                           0.93       660\n",
      "   macro avg       0.93      0.93      0.93       660\n",
      "weighted avg       0.93      0.93      0.93       660\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test, pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[156   2   0   0]\n",
      " [  6 144   2   0]\n",
      " [  0  17 170  12]\n",
      " [  0   0  10 141]]\n"
     ]
    }
   ],
   "source": [
    "matrix = confusion_matrix(y_test, pred)\n",
    "print(matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x199854f8748>"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x504 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,7))\n",
    "sns.heatmap(matrix, annot = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_test = pd.read_csv('test.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>...</th>\n",
       "      <th>pc</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1043</td>\n",
       "      <td>1</td>\n",
       "      <td>1.8</td>\n",
       "      <td>1</td>\n",
       "      <td>14</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0.1</td>\n",
       "      <td>193</td>\n",
       "      <td>...</td>\n",
       "      <td>16</td>\n",
       "      <td>226</td>\n",
       "      <td>1412</td>\n",
       "      <td>3476</td>\n",
       "      <td>12</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>841</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>61</td>\n",
       "      <td>0.8</td>\n",
       "      <td>191</td>\n",
       "      <td>...</td>\n",
       "      <td>12</td>\n",
       "      <td>746</td>\n",
       "      <td>857</td>\n",
       "      <td>3895</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1807</td>\n",
       "      <td>1</td>\n",
       "      <td>2.8</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>27</td>\n",
       "      <td>0.9</td>\n",
       "      <td>186</td>\n",
       "      <td>...</td>\n",
       "      <td>4</td>\n",
       "      <td>1270</td>\n",
       "      <td>1366</td>\n",
       "      <td>2396</td>\n",
       "      <td>17</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1546</td>\n",
       "      <td>0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>25</td>\n",
       "      <td>0.5</td>\n",
       "      <td>96</td>\n",
       "      <td>...</td>\n",
       "      <td>20</td>\n",
       "      <td>295</td>\n",
       "      <td>1752</td>\n",
       "      <td>3893</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1434</td>\n",
       "      <td>0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>0.5</td>\n",
       "      <td>108</td>\n",
       "      <td>...</td>\n",
       "      <td>18</td>\n",
       "      <td>749</td>\n",
       "      <td>810</td>\n",
       "      <td>1773</td>\n",
       "      <td>15</td>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  \\\n",
       "0   1           1043     1          1.8         1  14       0           5   \n",
       "1   2            841     1          0.5         1   4       1          61   \n",
       "2   3           1807     1          2.8         0   1       0          27   \n",
       "3   4           1546     0          0.5         1  18       1          25   \n",
       "4   5           1434     0          1.4         0  11       1          49   \n",
       "\n",
       "   m_dep  mobile_wt  ...  pc  px_height  px_width   ram  sc_h  sc_w  \\\n",
       "0    0.1        193  ...  16        226      1412  3476    12     7   \n",
       "1    0.8        191  ...  12        746       857  3895     6     0   \n",
       "2    0.9        186  ...   4       1270      1366  2396    17    10   \n",
       "3    0.5         96  ...  20        295      1752  3893    10     0   \n",
       "4    0.5        108  ...  18        749       810  1773    15     8   \n",
       "\n",
       "   talk_time  three_g  touch_screen  wifi  \n",
       "0          2        0             1     0  \n",
       "1          7        1             0     0  \n",
       "2         10        0             1     1  \n",
       "3          7        1             1     0  \n",
       "4          7        1             0     1  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_test.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_test.drop('id', axis = 1, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>pc</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1043</td>\n",
       "      <td>1</td>\n",
       "      <td>1.8</td>\n",
       "      <td>1</td>\n",
       "      <td>14</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0.1</td>\n",
       "      <td>193</td>\n",
       "      <td>3</td>\n",
       "      <td>16</td>\n",
       "      <td>226</td>\n",
       "      <td>1412</td>\n",
       "      <td>3476</td>\n",
       "      <td>12</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>841</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>61</td>\n",
       "      <td>0.8</td>\n",
       "      <td>191</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>746</td>\n",
       "      <td>857</td>\n",
       "      <td>3895</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1807</td>\n",
       "      <td>1</td>\n",
       "      <td>2.8</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>27</td>\n",
       "      <td>0.9</td>\n",
       "      <td>186</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1270</td>\n",
       "      <td>1366</td>\n",
       "      <td>2396</td>\n",
       "      <td>17</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1546</td>\n",
       "      <td>0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>25</td>\n",
       "      <td>0.5</td>\n",
       "      <td>96</td>\n",
       "      <td>8</td>\n",
       "      <td>20</td>\n",
       "      <td>295</td>\n",
       "      <td>1752</td>\n",
       "      <td>3893</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1434</td>\n",
       "      <td>0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>0.5</td>\n",
       "      <td>108</td>\n",
       "      <td>6</td>\n",
       "      <td>18</td>\n",
       "      <td>749</td>\n",
       "      <td>810</td>\n",
       "      <td>1773</td>\n",
       "      <td>15</td>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  m_dep  \\\n",
       "0           1043     1          1.8         1  14       0           5    0.1   \n",
       "1            841     1          0.5         1   4       1          61    0.8   \n",
       "2           1807     1          2.8         0   1       0          27    0.9   \n",
       "3           1546     0          0.5         1  18       1          25    0.5   \n",
       "4           1434     0          1.4         0  11       1          49    0.5   \n",
       "\n",
       "   mobile_wt  n_cores  pc  px_height  px_width   ram  sc_h  sc_w  talk_time  \\\n",
       "0        193        3  16        226      1412  3476    12     7          2   \n",
       "1        191        5  12        746       857  3895     6     0          7   \n",
       "2        186        3   4       1270      1366  2396    17    10         10   \n",
       "3         96        8  20        295      1752  3893    10     0          7   \n",
       "4        108        6  18        749       810  1773    15     8          7   \n",
       "\n",
       "   three_g  touch_screen  wifi  \n",
       "0        0             1     0  \n",
       "1        1             0     0  \n",
       "2        0             1     1  \n",
       "3        1             1     0  \n",
       "4        1             0     1  "
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_test.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "predicted_price = knn.predict(df_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 3, 2, 3, 1, 3, 3, 1, 3, 0, 3, 3, 0, 0, 2, 0, 2, 1, 3, 2, 1, 3,\n",
       "       1, 1, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 0, 1, 3, 1, 2, 1, 1, 2, 0, 0,\n",
       "       0, 1, 0, 3, 1, 2, 1, 0, 3, 0, 3, 1, 3, 1, 1, 3, 3, 2, 0, 1, 1, 1,\n",
       "       2, 3, 1, 2, 1, 2, 2, 3, 3, 0, 2, 0, 2, 3, 0, 3, 3, 0, 3, 0, 3, 1,\n",
       "       3, 0, 1, 2, 2, 1, 2, 1, 0, 2, 1, 2, 1, 0, 0, 3, 0, 2, 0, 1, 2, 3,\n",
       "       3, 3, 1, 3, 3, 3, 3, 1, 3, 0, 0, 3, 2, 1, 2, 0, 3, 2, 3, 1, 0, 2,\n",
       "       1, 1, 3, 1, 1, 0, 3, 2, 1, 3, 1, 3, 2, 3, 3, 3, 2, 3, 2, 3, 1, 0,\n",
       "       3, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 1, 0, 3, 0, 0, 0, 2, 1, 0, 1,\n",
       "       0, 0, 1, 2, 1, 0, 0, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 3, 1, 0, 2, 2,\n",
       "       3, 3, 1, 1, 3, 3, 3, 2, 2, 1, 1, 0, 1, 2, 0, 2, 3, 3, 0, 2, 0, 3,\n",
       "       2, 3, 3, 1, 0, 1, 0, 3, 0, 1, 0, 2, 2, 1, 2, 0, 3, 0, 3, 1, 2, 0,\n",
       "       0, 2, 1, 3, 3, 3, 1, 1, 3, 0, 0, 2, 3, 3, 1, 3, 1, 1, 3, 2, 1, 2,\n",
       "       3, 3, 3, 1, 0, 1, 2, 3, 1, 1, 3, 2, 0, 3, 0, 0, 2, 0, 0, 3, 2, 3,\n",
       "       3, 2, 1, 3, 3, 2, 3, 1, 2, 1, 2, 0, 2, 3, 1, 0, 0, 3, 0, 3, 0, 1,\n",
       "       2, 0, 2, 3, 1, 3, 2, 2, 1, 2, 0, 0, 0, 1, 3, 2, 0, 0, 0, 3, 2, 0,\n",
       "       2, 3, 1, 2, 2, 2, 3, 1, 3, 3, 1, 2, 3, 3, 3, 0, 3, 0, 3, 1, 3, 1,\n",
       "       2, 3, 0, 1, 0, 3, 1, 3, 1, 3, 0, 0, 0, 0, 2, 0, 0, 2, 1, 1, 2, 2,\n",
       "       2, 0, 1, 0, 0, 3, 2, 0, 3, 1, 2, 2, 1, 2, 3, 1, 1, 2, 2, 1, 2, 0,\n",
       "       1, 1, 0, 3, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 2, 2, 3, 2, 3, 0, 3,\n",
       "       0, 3, 0, 1, 1, 1, 2, 0, 3, 2, 3, 3, 1, 3, 1, 3, 1, 3, 2, 0, 1, 2,\n",
       "       1, 1, 0, 0, 0, 1, 2, 1, 0, 3, 2, 0, 2, 2, 0, 0, 3, 1, 1, 0, 3, 2,\n",
       "       3, 0, 3, 0, 2, 3, 3, 3, 0, 2, 0, 2, 3, 0, 1, 1, 0, 0, 1, 1, 1, 3,\n",
       "       3, 3, 2, 3, 1, 1, 2, 3, 3, 3, 2, 0, 2, 1, 2, 2, 1, 0, 2, 2, 0, 0,\n",
       "       0, 3, 1, 0, 2, 2, 2, 0, 3, 0, 2, 2, 0, 3, 0, 2, 3, 0, 1, 1, 3, 3,\n",
       "       1, 1, 1, 3, 2, 0, 3, 1, 2, 0, 3, 3, 1, 2, 2, 2, 3, 0, 1, 2, 3, 1,\n",
       "       3, 2, 3, 1, 1, 1, 0, 3, 1, 0, 3, 2, 3, 2, 0, 3, 3, 3, 2, 3, 3, 1,\n",
       "       2, 0, 2, 3, 3, 1, 0, 1, 1, 2, 2, 2, 0, 0, 2, 2, 3, 2, 0, 2, 1, 3,\n",
       "       3, 0, 1, 3, 0, 2, 1, 1, 0, 0, 2, 1, 0, 1, 1, 2, 2, 0, 2, 2, 1, 0,\n",
       "       3, 0, 0, 3, 2, 0, 0, 0, 0, 0, 3, 0, 3, 1, 3, 1, 1, 3, 3, 0, 1, 1,\n",
       "       3, 2, 3, 2, 0, 3, 0, 2, 0, 2, 0, 0, 1, 1, 1, 2, 1, 3, 1, 3, 2, 2,\n",
       "       1, 3, 2, 0, 1, 2, 0, 3, 3, 0, 2, 1, 1, 2, 0, 3, 2, 0, 3, 2, 3, 0,\n",
       "       0, 3, 0, 2, 2, 3, 2, 2, 2, 2, 1, 1, 3, 0, 1, 0, 1, 2, 1, 0, 0, 1,\n",
       "       0, 0, 3, 0, 1, 2, 0, 0, 1, 1, 3, 0, 3, 2, 3, 0, 0, 1, 2, 2, 1, 0,\n",
       "       1, 2, 0, 1, 1, 0, 0, 3, 3, 0, 3, 1, 2, 3, 0, 1, 0, 2, 2, 0, 3, 1,\n",
       "       0, 3, 0, 1, 0, 3, 3, 3, 2, 3, 0, 3, 2, 0, 0, 0, 2, 3, 2, 0, 1, 1,\n",
       "       2, 1, 0, 3, 2, 0, 3, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 0, 1, 2, 0,\n",
       "       3, 0, 0, 0, 0, 2, 3, 3, 3, 0, 1, 2, 1, 1, 0, 0, 2, 1, 0, 2, 0, 3,\n",
       "       2, 2, 1, 2, 0, 2, 1, 3, 0, 0, 3, 2, 3, 0, 0, 2, 3, 3, 1, 2, 2, 1,\n",
       "       0, 0, 2, 3, 0, 3, 0, 0, 0, 2, 2, 1, 2, 0, 3, 2, 1, 2, 3, 3, 0, 1,\n",
       "       1, 2, 1, 2, 2, 0, 1, 3, 1, 1, 3, 1, 2, 3, 1, 1, 1, 1, 3, 2, 0, 2,\n",
       "       3, 0, 2, 3, 2, 2, 2, 3, 2, 0, 1, 2, 0, 2, 1, 1, 2, 2, 2, 1, 2, 1,\n",
       "       0, 1, 3, 1, 0, 1, 2, 3, 1, 0, 0, 3, 2, 2, 3, 0, 3, 3, 2, 1, 3, 0,\n",
       "       1, 3, 1, 1, 1, 1, 3, 2, 0, 3, 0, 2, 3, 0, 3, 2, 2, 3, 1, 0, 2, 3,\n",
       "       1, 0, 2, 1, 2, 1, 2, 0, 2, 2, 0, 2, 3, 2, 3, 0, 2, 1, 1, 2, 2, 3,\n",
       "       3, 0, 2, 1, 2, 1, 3, 0, 1, 3, 0, 1, 0, 0, 3, 3, 2, 0, 0, 0, 0, 3,\n",
       "       2, 3, 3, 0, 0, 2, 1, 0, 2, 2], dtype=int64)"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predicted_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_test['price_range'] = predicted_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>...</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1043</td>\n",
       "      <td>1</td>\n",
       "      <td>1.8</td>\n",
       "      <td>1</td>\n",
       "      <td>14</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0.1</td>\n",
       "      <td>193</td>\n",
       "      <td>3</td>\n",
       "      <td>...</td>\n",
       "      <td>226</td>\n",
       "      <td>1412</td>\n",
       "      <td>3476</td>\n",
       "      <td>12</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>841</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>61</td>\n",
       "      <td>0.8</td>\n",
       "      <td>191</td>\n",
       "      <td>5</td>\n",
       "      <td>...</td>\n",
       "      <td>746</td>\n",
       "      <td>857</td>\n",
       "      <td>3895</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1807</td>\n",
       "      <td>1</td>\n",
       "      <td>2.8</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>27</td>\n",
       "      <td>0.9</td>\n",
       "      <td>186</td>\n",
       "      <td>3</td>\n",
       "      <td>...</td>\n",
       "      <td>1270</td>\n",
       "      <td>1366</td>\n",
       "      <td>2396</td>\n",
       "      <td>17</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1546</td>\n",
       "      <td>0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>25</td>\n",
       "      <td>0.5</td>\n",
       "      <td>96</td>\n",
       "      <td>8</td>\n",
       "      <td>...</td>\n",
       "      <td>295</td>\n",
       "      <td>1752</td>\n",
       "      <td>3893</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1434</td>\n",
       "      <td>0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>0.5</td>\n",
       "      <td>108</td>\n",
       "      <td>6</td>\n",
       "      <td>...</td>\n",
       "      <td>749</td>\n",
       "      <td>810</td>\n",
       "      <td>1773</td>\n",
       "      <td>15</td>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  m_dep  \\\n",
       "0           1043     1          1.8         1  14       0           5    0.1   \n",
       "1            841     1          0.5         1   4       1          61    0.8   \n",
       "2           1807     1          2.8         0   1       0          27    0.9   \n",
       "3           1546     0          0.5         1  18       1          25    0.5   \n",
       "4           1434     0          1.4         0  11       1          49    0.5   \n",
       "\n",
       "   mobile_wt  n_cores  ...  px_height  px_width   ram  sc_h  sc_w  talk_time  \\\n",
       "0        193        3  ...        226      1412  3476    12     7          2   \n",
       "1        191        5  ...        746       857  3895     6     0          7   \n",
       "2        186        3  ...       1270      1366  2396    17    10         10   \n",
       "3         96        8  ...        295      1752  3893    10     0          7   \n",
       "4        108        6  ...        749       810  1773    15     8          7   \n",
       "\n",
       "   three_g  touch_screen  wifi  price_range  \n",
       "0        0             1     0            3  \n",
       "1        1             0     0            3  \n",
       "2        0             1     1            2  \n",
       "3        1             1     0            3  \n",
       "4        1             0     1            1  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_test.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
